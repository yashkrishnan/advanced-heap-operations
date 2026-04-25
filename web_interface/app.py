"""
Flask Web Interface for Advanced Heap Operations
Allows running examples and viewing outputs through a web browser
"""

from flask import Flask, render_template, jsonify, request
import subprocess
import sys
import os
from io import StringIO
import traceback

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)

# Store the project root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


@app.route('/')
def index():
    """Main page with navigation"""
    return render_template('index.html')


@app.route('/run/<example_type>')
def run_example(example_type):
    """Run a specific example and return output"""
    try:
        if example_type == 'basic_operations':
            script_path = os.path.join(PROJECT_ROOT, 'examples', 'basic_operations.py')
        elif example_type == 'graph_algorithms':
            script_path = os.path.join(PROJECT_ROOT, 'examples', 'graph_algorithms.py')
        elif example_type == 'performance_comparison':
            script_path = os.path.join(PROJECT_ROOT, 'examples', 'performance_comparison.py')
        elif example_type == 'tests':
            # Run unit tests
            result = subprocess.run(
                [sys.executable, '-m', 'unittest', 'tests.test_fibonacci_heap', '-v'],
                cwd=PROJECT_ROOT,
                capture_output=True,
                text=True,
                timeout=30
            )
            return jsonify({
                'success': True,
                'output': result.stdout + result.stderr,
                'return_code': result.returncode
            })
        else:
            return jsonify({'success': False, 'error': 'Unknown example type'})
        
        # Run the script
        result = subprocess.run(
            [sys.executable, script_path],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        return jsonify({
            'success': True,
            'output': result.stdout,
            'error': result.stderr if result.stderr else None,
            'return_code': result.returncode
        })
        
    except subprocess.TimeoutExpired:
        return jsonify({'success': False, 'error': 'Script execution timed out'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e), 'traceback': traceback.format_exc()})


@app.route('/run_interactive', methods=['POST'])
def run_interactive():
    """Run custom Python code interactively"""
    try:
        code = request.json.get('code', '')
        
        # Capture stdout
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        # Create a safe execution environment
        exec_globals = {
            '__builtins__': __builtins__,
            'sys': sys,
            'os': os,
        }
        
        # Import heap modules
        from heaps import (BinomialHeap, FibonacciHeap, MinMaxHeap, 
                          PairingHeap, LeftistHeap, SkewHeap)
        exec_globals.update({
            'BinomialHeap': BinomialHeap,
            'FibonacciHeap': FibonacciHeap,
            'MinMaxHeap': MinMaxHeap,
            'PairingHeap': PairingHeap,
            'LeftistHeap': LeftistHeap,
            'SkewHeap': SkewHeap,
        })
        
        # Execute the code
        exec(code, exec_globals)
        
        # Get output
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        return jsonify({'success': True, 'output': output})
        
    except Exception as e:
        sys.stdout = old_stdout
        return jsonify({
            'success': False, 
            'error': str(e),
            'traceback': traceback.format_exc()
        })


@app.route('/heap_info/<heap_type>')
def heap_info(heap_type):
    """Get information about a specific heap type"""
    heap_descriptions = {
        'binomial': {
            'name': 'Binomial Heap',
            'description': 'Collection of binomial trees with efficient merge operations',
            'complexity': {
                'insert': 'O(log n)',
                'find_min': 'O(log n)',
                'delete_min': 'O(log n)',
                'merge': 'O(log n)'
            },
            'use_cases': ['Frequent merge operations', 'Priority queues with merging']
        },
        'fibonacci': {
            'name': 'Fibonacci Heap',
            'description': 'Lazy heap with excellent amortized performance',
            'complexity': {
                'insert': 'O(1) amortized',
                'find_min': 'O(1)',
                'delete_min': 'O(log n) amortized',
                'decrease_key': 'O(1) amortized',
                'merge': 'O(1) amortized'
            },
            'use_cases': ['Dijkstra\'s algorithm', 'Prim\'s algorithm', 'Frequent decrease-key']
        },
        'minmax': {
            'name': 'Min-Max Heap',
            'description': 'Double-ended priority queue with O(1) access to both min and max',
            'complexity': {
                'insert': 'O(log n)',
                'find_min': 'O(1)',
                'find_max': 'O(1)',
                'delete_min': 'O(log n)',
                'delete_max': 'O(log n)'
            },
            'use_cases': ['Double-ended priority queues', 'Range queries', 'Min-max operations']
        },
        'pairing': {
            'name': 'Pairing Heap',
            'description': 'Simple multiway tree with good practical performance',
            'complexity': {
                'insert': 'O(1) amortized',
                'find_min': 'O(1)',
                'delete_min': 'O(log n) amortized',
                'merge': 'O(1) amortized'
            },
            'use_cases': ['Simple implementation', 'Good practical performance', 'Priority queues']
        },
        'leftist': {
            'name': 'Leftist Heap',
            'description': 'Binary tree optimized for efficient merging',
            'complexity': {
                'insert': 'O(log n)',
                'find_min': 'O(1)',
                'delete_min': 'O(log n)',
                'merge': 'O(log n)'
            },
            'use_cases': ['Merge-heavy operations', 'Predictable performance']
        },
        'skew': {
            'name': 'Skew Heap',
            'description': 'Self-adjusting variant of leftist heap',
            'complexity': {
                'insert': 'O(log n) amortized',
                'find_min': 'O(1)',
                'delete_min': 'O(log n) amortized',
                'merge': 'O(log n) amortized'
            },
            'use_cases': ['Self-balancing', 'Simple implementation', 'Good amortized performance']
        }
    }
    
    if heap_type in heap_descriptions:
        return jsonify(heap_descriptions[heap_type])
    else:
        return jsonify({'error': 'Unknown heap type'}), 404


@app.route('/examples/image/<path:filename>')
def serve_example_image(filename):
    """Serve a generated chart image from the examples directory."""
    from flask import send_from_directory
    examples_dir = os.path.join(PROJECT_ROOT, 'examples')
    return send_from_directory(examples_dir, filename)


@app.route('/save_screenshot', methods=['POST'])
def save_screenshot():
    """Save a base64-encoded screenshot to the screenshots folder"""
    import base64, re
    data = request.json
    img_data = re.sub(r'^data:image/[^;]+;base64,', '', data['image'])
    filename = data['filename']
    save_dir = os.path.join(PROJECT_ROOT, 'screenshots')
    os.makedirs(save_dir, exist_ok=True)
    with open(os.path.join(save_dir, filename), 'wb') as f:
        f.write(base64.b64decode(img_data))
    return jsonify({'success': True, 'path': os.path.join(save_dir, filename)})


# Store heap instances in memory (simple session management)
heap_instances = {}

@app.route('/playground_operation', methods=['POST'])
def playground_operation():
    """Execute heap operations in playground"""
    try:
        data = request.json
        heap_type = data.get('heap_type')
        operation = data.get('operation')
        value = data.get('value')
        session_id = data.get('session_id', 'default')
        
        # Import heap classes
        from heaps import (BinomialHeap, FibonacciHeap, MinMaxHeap,
                          PairingHeap, LeftistHeap, SkewHeap)
        
        heap_classes = {
            'binomial': BinomialHeap,
            'fibonacci': FibonacciHeap,
            'minmax': MinMaxHeap,
            'pairing': PairingHeap,
            'leftist': LeftistHeap,
            'skew': SkewHeap
        }
        
        # Get or create heap instance
        key = f"{session_id}_{heap_type}"
        if key not in heap_instances or operation == 'reset':
            heap_instances[key] = heap_classes[heap_type]()
            if operation == 'reset':
                return jsonify({
                    'success': True,
                    'message': f'{heap_type.title()} Heap reset',
                    'heap_state': '[]'
                })
        
        heap = heap_instances[key]
        result_message = ""
        
        # Execute operation
        result = None
        
        if operation == 'insert':
            if value is None:
                return jsonify({'success': False, 'error': 'Value required for insert'})
            heap.insert(int(value))
            result = int(value)
            
        elif operation == 'find_min':
            try:
                result = heap.find_min()
            except:
                result = None
                
        elif operation == 'delete_min':
            try:
                result = heap.delete_min()
            except:
                result = None
                
        elif operation == 'find_max':
            if heap_type == 'minmax':
                try:
                    result = heap.find_max()
                except:
                    result = None
            else:
                return jsonify({'success': False, 'error': 'find_max only available for Min-Max Heap'})
        
        # Get heap state
        heap_state = {
            'size': heap.size if hasattr(heap, 'size') else len(getattr(heap, 'heap', [])),
            'min': None,
            'max': None
        }
        
        # Try to get current min
        try:
            heap_state['min'] = heap.find_min()
        except:
            pass
        
        # Try to get current max (only for MinMaxHeap)
        if heap_type == 'minmax':
            try:
                heap_state['max'] = heap.find_max()
            except:
                pass
        
        return jsonify({
            'success': True,
            'result': result,
            'heap_state': heap_state
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        })


if __name__ == '__main__':
    import socket
    
    # Try to find an available port
    def find_free_port(start_port=5000, max_attempts=10):
        """Return the first available TCP port starting from start_port."""
        for port in range(start_port, start_port + max_attempts):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.bind(('', port))
                sock.close()
                return port
            except OSError:
                continue
        return None
    
    port = find_free_port()
    
    if port is None:
        print("=" * 60)
        print("ERROR: Could not find an available port")
        print("=" * 60)
        print("\nPlease free up ports 5000-5009 or specify a custom port:")
        print("  python3 app.py --port 8080")
        exit(1)
    
    print("=" * 60)
    print("Advanced Heap Operations - Web Interface")
    print("=" * 60)
    print(f"\nStarting server on port {port}...")
    print(f"Open your browser and navigate to: http://localhost:{port}")
    if port != 5000:
        print(f"\nNote: Port 5000 was in use, using port {port} instead")
        print("Tip: On macOS, disable 'AirPlay Receiver' in System Settings")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=port)


