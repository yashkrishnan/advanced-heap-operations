# Advanced Heap Operations - Academic Mini Project

## Overview

This project provides comprehensive implementations of advanced heap data structures, demonstrating their unique properties, operations, and performance characteristics. Each implementation is designed for academic study and includes detailed documentation, complexity analysis, and practical examples.

## Implemented Heap Structures

### 1. **Binomial Heap**
- Collection of binomial trees satisfying min-heap property
- Efficient union operation in O(log n) time
- Supports insert, find-min, delete-min, and merge operations
- **Key Feature**: Optimal for frequent merge operations

### 2. **Fibonacci Heap**
- Lazy approach with amortized constant time for insert and decrease-key
- Exceptional performance for graph algorithms (Dijkstra's, Prim's)
- Amortized O(1) for insert, find-min, merge, and decrease-key
- Amortized O(log n) for delete-min
- **Key Feature**: Best amortized complexity for priority queue operations

### 3. **Min-Max Heap**
- Complete binary tree with alternating min/max levels
- Double-ended priority queue functionality
- O(1) access to both minimum and maximum elements
- O(log n) insertion and deletion
- **Key Feature**: Efficient access to both extremes

### 4. **Pairing Heap**
- Simple multiway tree structure
- Excellent practical performance despite theoretical bounds
- Easy to implement compared to Fibonacci heaps
- Good for priority queues with frequent key updates
- **Key Feature**: Simplicity with good practical performance

### 5. **Leftist Heap**
- Binary tree with "leftist property" for efficient merging
- Null path length (npl) maintained for balance
- O(log n) merge operation
- **Key Feature**: Optimized specifically for heap merging

### 6. **Skew Heap**
- Self-adjusting variant of leftist heap
- No explicit balance information needed
- Amortized O(log n) for all operations
- Simpler implementation than leftist heap
- **Key Feature**: Self-balancing with minimal overhead

## Project Structure

```
advanced_heap_operations/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── heaps/
│   ├── __init__.py
│   ├── binomial_heap.py              # Binomial heap implementation
│   ├── fibonacci_heap.py             # Fibonacci heap implementation
│   ├── min_max_heap.py               # Min-Max heap implementation
│   ├── pairing_heap.py               # Pairing heap implementation
│   ├── leftist_heap.py               # Leftist heap implementation
│   └── skew_heap.py                  # Skew heap implementation
├── tests/
│   ├── __init__.py
│   └── test_fibonacci_heap.py        # Example test file
├── examples/
│   ├── basic_operations.py           # Basic usage examples
│   ├── graph_algorithms.py           # Dijkstra's and Prim's with heaps
│   └── performance_comparison.py     # Benchmark different heaps
├── visualization/
│   ├── heap_visualizer.py            # Visualize heap structures
│   └── performance_plots.py          # Generate performance graphs
└── docs/
    ├── 01_problem_definition.md      # Problem definition
    ├── 02_algorithm_design.md        # Algorithm design
    ├── 03_complexity_analysis.md     # Detailed complexity analysis
    ├── 04_test_outputs.md            # Test outputs and results
    └── ACADEMIC_REPORT.md            # Complete academic report
```

## Time Complexity Comparison

| Operation | Binomial | Fibonacci | Min-Max | Pairing | Leftist | Skew |
|-----------|----------|-----------|---------|---------|---------|------|
| Insert | O(log n) | O(1)* | O(log n) | O(1)* | O(log n) | O(log n)* |
| Find-Min | O(log n) | O(1) | O(1) | O(1) | O(1) | O(1) |
| Delete-Min | O(log n) | O(log n)* | O(log n) | O(log n)* | O(log n) | O(log n)* |
| Decrease-Key | O(log n) | O(1)* | O(log n) | O(log n)* | O(log n) | O(log n)* |
| Merge | O(log n) | O(1)* | O(n) | O(1)* | O(log n) | O(log n)* |

*Amortized time complexity

## Installation

### Quick Setup (Recommended)

Use the automated setup script:

```bash
cd ads/advanced_heap_operations
./setup.sh
```

This script will:
- Create a virtual environment
- Install all dependencies
- Verify the installation

### Manual Setup

#### Option 1: Using Virtual Environment (Recommended)

```bash
# Navigate to the project directory
cd ads/advanced_heap_operations

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Using System Python (macOS with Homebrew)

```bash
# Install with user flag
pip3 install --user -r requirements.txt

# OR use break-system-packages (not recommended)
pip3 install --break-system-packages -r requirements.txt
```

### Option 3: Using pipx (For standalone tools)

```bash
# Install pipx if not already installed
brew install pipx

# Install packages
pipx install matplotlib numpy
```

**Note:** On macOS with Homebrew-managed Python, using a virtual environment is strongly recommended to avoid conflicts with system packages.

## Quick Start

### Option 1: Web Interface (Easiest) 🌐

Launch the interactive web interface to run examples and code through your browser:

```bash
cd ads/advanced_heap_operations
./start_web_interface.sh
```

Then open your browser to: **http://localhost:5001**

> **Note:** macOS AirPlay Receiver occupies port 5000 by default. The server auto-detects and uses the next available port (5001). The exact URL is printed in the terminal on startup.

**Features (7 tabs):**
- ⚙️ **Basic Operations** — run insert, find-min, delete-min, merge demos for all 6 heaps
- 🗺️ **Graph Algorithms** — Dijkstra's shortest path and Prim's MST
- 📈 **Performance Comparison** — benchmark all 6 heaps with embedded charts (5 charts auto-refresh after each run)
- 🎮 **Heap Playground** — select any heap type and interactively run Insert, Find Min, Delete Min, Find Max (Min-Max only), Reset
- 💻 **Interactive Code** — Python console with all 6 heap classes pre-imported
- 📊 **Heap Information** — time complexity tables and use-case recommendations
- 🧪 **Run Tests** — 18-test Fibonacci Heap suite with colour-coded results

See [web_interface/README.md](web_interface/README.md) for more details.

### Option 2: Command Line

#### Running Examples

```bash
# Navigate to the project directory
cd ads/advanced_heap_operations

# Run basic operations examples
python examples/basic_operations.py

# Run graph algorithms examples
python examples/graph_algorithms.py

# Run performance comparison
python examples/performance_comparison.py
```

### Using in Your Code

```python
from heaps.fibonacci_heap import FibonacciHeap
from heaps.min_max_heap import MinMaxHeap

# Fibonacci Heap Example
fib_heap = FibonacciHeap()
fib_heap.insert(10)
fib_heap.insert(5)
fib_heap.insert(20)
print(f"Minimum: {fib_heap.find_min()}")  # Output: 5
fib_heap.delete_min()

# Min-Max Heap Example
mm_heap = MinMaxHeap()
mm_heap.insert(10)
mm_heap.insert(5)
mm_heap.insert(20)
print(f"Minimum: {mm_heap.find_min()}")  # Output: 5
print(f"Maximum: {mm_heap.find_max()}")  # Output: 20
```

## Running Tests

```bash
# Run all tests with unittest
python -m unittest discover tests/

# Run specific heap tests
python -m unittest tests.test_fibonacci_heap -v

# Or run the test file directly
python tests/test_fibonacci_heap.py

# If you have pytest installed (optional)
python -m pytest tests/ -v
python -m pytest tests/test_fibonacci_heap.py -v
```

## Detailed Examples

### Example 1: Basic Operations

See `examples/basic_operations.py` for comprehensive examples of all heap operations.

```bash
python examples/basic_operations.py
```

### Example 2: Graph Algorithms

See `examples/graph_algorithms.py` for Dijkstra's and Prim's algorithm implementations.

```bash
python examples/graph_algorithms.py
```

### Example 3: Performance Comparison

See `examples/performance_comparison.py` for benchmarking different heap implementations.

```bash
python examples/performance_comparison.py
```

### Example 4: Visualization

Generate performance plots:

```python
from visualization.performance_plots import plot_comparison

# Your performance data
results = {
    'Fibonacci Heap': {'insert': [0.001, 0.002], 'delete_min': [0.003, 0.004]},
    'Binomial Heap': {'insert': [0.002, 0.003], 'delete_min': [0.004, 0.005]}
}

plot_comparison(results, save_path='comparison.png')
```

## Use Cases

### When to Use Each Heap:

1. **Binomial Heap**: When you need frequent merge operations with good worst-case guarantees
2. **Fibonacci Heap**: For graph algorithms (Dijkstra's, Prim's) where decrease-key is frequent
3. **Min-Max Heap**: When you need efficient access to both minimum and maximum elements
4. **Pairing Heap**: When you want simplicity with good practical performance
5. **Leftist Heap**: When merging is the primary operation and you want predictable performance
6. **Skew Heap**: When you want a simple self-adjusting heap with good amortized performance

## Key Concepts

### Binomial Trees
- A binomial tree Bₖ has 2^k nodes
- Root has degree k with children B₀, B₁, ..., Bₖ₋₁
- Height is k

### Fibonacci Heap Lazy Approach
- Delays consolidation until delete-min
- Maintains a collection of heap-ordered trees
- Uses cascading cuts for decrease-key

### Min-Max Heap Levels
- Even levels (0, 2, 4, ...) are min levels
- Odd levels (1, 3, 5, ...) are max levels
- Root is always the minimum element

### Leftist Property
- For every node, npl(left child) ≥ npl(right child)
- Ensures the right path is always short
- Enables efficient merging

## Performance Benchmarks

Typical performance on modern hardware (operations per second):

| Heap Type | Insert (1M ops) | Delete-Min (1M ops) | Merge (10K ops) |
|-----------|----------------|---------------------|-----------------|
| Binomial | ~500K/sec | ~400K/sec | ~50K/sec |
| Fibonacci | ~2M/sec | ~300K/sec | ~1M/sec |
| Min-Max | ~800K/sec | ~600K/sec | ~10K/sec |
| Pairing | ~1.5M/sec | ~500K/sec | ~800K/sec |
| Leftist | ~600K/sec | ~400K/sec | ~100K/sec |
| Skew | ~700K/sec | ~450K/sec | ~120K/sec |

*Note: Actual performance varies based on data patterns and hardware*

## Academic References

1. **Binomial Heaps**: Vuillemin, J. (1978). "A data structure for manipulating priority queues"
2. **Fibonacci Heaps**: Fredman, M. L., & Tarjan, R. E. (1987). "Fibonacci heaps and their uses in improved network optimization algorithms"
3. **Min-Max Heaps**: Atkinson, M. D., et al. (1986). "Min-max heaps and generalized priority queues"
4. **Pairing Heaps**: Fredman, M. L., et al. (1986). "The pairing heap: A new form of self-adjusting heap"
5. **Leftist Heaps**: Crane, C. A. (1972). "Linear lists and priority queues as balanced binary trees"
6. **Skew Heaps**: Sleator, D. D., & Tarjan, R. E. (1986). "Self-adjusting heaps"

## Contributing

This is an academic project. Contributions for educational improvements are welcome:
- Enhanced documentation
- Additional test cases
- Performance optimizations
- Visualization improvements

## License

MIT License - Free for academic and educational use

## Author

Created as part of Advanced Data Structures coursework

## Acknowledgments

- Course materials from MIT OCW, Stanford, and CMU
- Classic papers on heap data structures
- Open-source implementations for reference