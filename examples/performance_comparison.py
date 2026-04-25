"""
Performance Comparison of Advanced Heap Operations

This script performs empirical performance testing and comparison
of all six heap implementations across various operations and data sizes.

Generates:
- Performance metrics CSV files
- Comparison plots
- Statistical analysis
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import random
import statistics
from typing import List, Dict, Callable, Any
import csv

# Import all heap implementations
from heaps.binomial_heap import BinomialHeap
from heaps.fibonacci_heap import FibonacciHeap
from heaps.min_max_heap import MinMaxHeap
from heaps.pairing_heap import PairingHeap
from heaps.leftist_heap import LeftistHeap
from heaps.skew_heap import SkewHeap

try:
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('Agg')  # Use non-interactive backend
    PLOTTING_AVAILABLE = True
except ImportError:
    PLOTTING_AVAILABLE = False
    print("Warning: matplotlib not available. Plots will not be generated.")


class PerformanceTester:
    """Performance testing framework for heap operations"""
    
    def __init__(self):
        """Initialize the tester with an empty results store and all six heap classes registered."""
        self.results = {}
        self.heap_classes = {
            'Binomial': BinomialHeap,
            'Fibonacci': FibonacciHeap,
            'MinMax': MinMaxHeap,
            'Pairing': PairingHeap,
            'Leftist': LeftistHeap,
            'Skew': SkewHeap
        }
    
    def measure_time(self, func: Callable, iterations: int = 1) -> float:
        """Measure execution time of a function"""
        start = time.perf_counter()
        for _ in range(iterations):
            func()
        end = time.perf_counter()
        return (end - start) / iterations
    
    def test_insert(self, heap_class, size: int, iterations: int = 3) -> float:
        """Test insert operation performance"""
        times = []
        for _ in range(iterations):
            heap = heap_class()
            data = list(range(size))
            random.shuffle(data)
            
            start = time.perf_counter()
            for value in data:
                heap.insert(value)
            end = time.perf_counter()
            
            times.append(end - start)
        
        return statistics.mean(times)
    
    def test_delete_min(self, heap_class, size: int, iterations: int = 3) -> float:
        """Test delete-min operation performance"""
        times = []
        for _ in range(iterations):
            # Build heap first
            heap = heap_class()
            data = list(range(size))
            random.shuffle(data)
            for value in data:
                heap.insert(value)
            
            # Measure delete-min
            start = time.perf_counter()
            for _ in range(size // 2):  # Delete half the elements
                heap.delete_min()
            end = time.perf_counter()
            
            times.append(end - start)
        
        return statistics.mean(times)
    
    def test_find_min(self, heap_class, size: int, iterations: int = 3) -> float:
        """Test find-min operation performance"""
        times = []
        for _ in range(iterations):
            # Build heap first
            heap = heap_class()
            data = list(range(size))
            random.shuffle(data)
            for value in data:
                heap.insert(value)
            
            # Measure find-min
            start = time.perf_counter()
            for _ in range(1000):  # Perform 1000 find-min operations
                _ = heap.find_min()
            end = time.perf_counter()
            
            times.append(end - start)
        
        return statistics.mean(times)
    
    def test_merge(self, heap_class, size: int, iterations: int = 3) -> float:
        """Test merge operation performance"""
        times = []
        for _ in range(iterations):
            # Build two heaps
            heap1 = heap_class()
            heap2 = heap_class()
            
            data1 = list(range(0, size, 2))
            data2 = list(range(1, size, 2))
            random.shuffle(data1)
            random.shuffle(data2)
            
            for value in data1:
                heap1.insert(value)
            for value in data2:
                heap2.insert(value)
            
            # Measure merge
            start = time.perf_counter()
            heap1.merge(heap2)
            end = time.perf_counter()
            
            times.append(end - start)
        
        return statistics.mean(times)
    
    def test_decrease_key(self, heap_class, size: int, iterations: int = 3) -> float:
        """Test decrease-key operation performance (for heaps that support it)"""
        if heap_class not in [FibonacciHeap, PairingHeap, BinomialHeap]:
            return -1  # Not supported
        
        times = []
        for _ in range(iterations):
            heap = heap_class()
            nodes = []
            
            # Build heap and save node references
            data = list(range(size))
            random.shuffle(data)
            for value in data:
                node = heap.insert(value)
                nodes.append(node)
            
            # Measure decrease-key
            start = time.perf_counter()
            for i in range(min(100, len(nodes))):  # Decrease 100 keys
                if hasattr(nodes[i], 'key'):
                    try:
                        heap.decrease_key(nodes[i], nodes[i].key - 1000)
                    except:
                        pass
            end = time.perf_counter()
            
            times.append(end - start)
        
        return statistics.mean(times)
    
    def run_comprehensive_test(self, sizes: List[int] = None):
        """Run comprehensive performance tests"""
        if sizes is None:
            sizes = [100, 500, 1000, 2000, 5000]
        
        print("=" * 70)
        print("ADVANCED HEAP OPERATIONS - PERFORMANCE COMPARISON")
        print("=" * 70)
        print()
        
        operations = ['insert', 'delete_min', 'find_min', 'merge']
        
        for op in operations:
            print(f"\n{'=' * 70}")
            print(f"Testing: {op.upper().replace('_', '-')}")
            print(f"{'=' * 70}")
            
            self.results[op] = {}
            
            for heap_name, heap_class in self.heap_classes.items():
                self.results[op][heap_name] = []
                print(f"\n{heap_name} Heap:")
                
                for size in sizes:
                    try:
                        if op == 'insert':
                            time_taken = self.test_insert(heap_class, size)
                        elif op == 'delete_min':
                            time_taken = self.test_delete_min(heap_class, size)
                        elif op == 'find_min':
                            time_taken = self.test_find_min(heap_class, size)
                        elif op == 'merge':
                            time_taken = self.test_merge(heap_class, size)
                        
                        self.results[op][heap_name].append(time_taken)
                        print(f"  Size {size:5d}: {time_taken*1000:8.3f} ms")
                    
                    except Exception as e:
                        print(f"  Size {size:5d}: ERROR - {str(e)}")
                        self.results[op][heap_name].append(None)
        
        print(f"\n{'=' * 70}")
        print("Testing complete!")
        print(f"{'=' * 70}\n")
    
    def save_results_csv(self, filename: str = "performance_results.csv"):
        """Save results to CSV file"""
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            
            # Write header
            writer.writerow(['Operation', 'Heap Type', 'Size', 'Time (ms)'])
            
            # Write data
            sizes = [100, 500, 1000, 2000, 5000]
            for op, heap_data in self.results.items():
                for heap_name, times in heap_data.items():
                    for size, time_val in zip(sizes, times):
                        if time_val is not None:
                            writer.writerow([op, heap_name, size, time_val * 1000])
        
        print(f"Results saved to {filename}")
    
    def generate_plots(self, output_dir: str = "."):
        """Generate performance comparison plots"""
        if not PLOTTING_AVAILABLE:
            print("Matplotlib not available. Skipping plot generation.")
            return
        
        sizes = [100, 500, 1000, 2000, 5000]
        operations = ['insert', 'delete_min', 'find_min', 'merge']
        
        # Create a figure with subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Heap Performance Comparison', fontsize=16, fontweight='bold')
        
        axes = axes.flatten()
        
        for idx, op in enumerate(operations):
            ax = axes[idx]
            
            for heap_name, times in self.results[op].items():
                valid_sizes = []
                valid_times = []
                for size, time_val in zip(sizes, times):
                    if time_val is not None:
                        valid_sizes.append(size)
                        valid_times.append(time_val * 1000)  # Convert to ms
                
                if valid_times:
                    ax.plot(valid_sizes, valid_times, marker='o', label=heap_name, linewidth=2)
            
            ax.set_xlabel('Heap Size (n)', fontsize=11)
            ax.set_ylabel('Time (ms)', fontsize=11)
            ax.set_title(f'{op.replace("_", "-").title()} Operation', fontsize=12, fontweight='bold')
            ax.legend(fontsize=9)
            ax.grid(True, alpha=0.3)
            ax.set_xscale('log')
            ax.set_yscale('log')
        
        plt.tight_layout()
        plot_file = os.path.join(output_dir, 'heap_performance_comparison.png')
        plt.savefig(plot_file, dpi=300, bbox_inches='tight')
        print(f"Performance plot saved to {plot_file}")
        plt.close()
        
        # Generate individual operation plots
        for op in operations:
            fig, ax = plt.subplots(figsize=(10, 6))
            
            for heap_name, times in self.results[op].items():
                valid_sizes = []
                valid_times = []
                for size, time_val in zip(sizes, times):
                    if time_val is not None:
                        valid_sizes.append(size)
                        valid_times.append(time_val * 1000)
                
                if valid_times:
                    ax.plot(valid_sizes, valid_times, marker='o', label=heap_name, 
                           linewidth=2, markersize=8)
            
            ax.set_xlabel('Heap Size (n)', fontsize=12)
            ax.set_ylabel('Time (ms)', fontsize=12)
            ax.set_title(f'{op.replace("_", "-").title()} Operation Performance', 
                        fontsize=14, fontweight='bold')
            ax.legend(fontsize=10)
            ax.grid(True, alpha=0.3)
            ax.set_xscale('log')
            ax.set_yscale('log')
            
            plt.tight_layout()
            plot_file = os.path.join(output_dir, f'heap_{op}_performance.png')
            plt.savefig(plot_file, dpi=300, bbox_inches='tight')
            print(f"Plot saved to {plot_file}")
            plt.close()
    
    def print_summary(self):
        """Print performance summary"""
        print("\n" + "=" * 70)
        print("PERFORMANCE SUMMARY")
        print("=" * 70)
        
        sizes = [100, 500, 1000, 2000, 5000]
        
        for op in ['insert', 'delete_min', 'find_min', 'merge']:
            print(f"\n{op.upper().replace('_', '-')} Operation:")
            print("-" * 70)
            
            # Find fastest for each size
            for i, size in enumerate(sizes):
                times = {}
                for heap_name, time_list in self.results[op].items():
                    if i < len(time_list) and time_list[i] is not None:
                        times[heap_name] = time_list[i]
                
                if times:
                    fastest = min(times, key=times.get)
                    print(f"  Size {size:5d}: Fastest = {fastest:10s} ({times[fastest]*1000:.3f} ms)")


def main():
    """Main execution function"""
    print("\nStarting performance comparison...")
    print("This may take several minutes...\n")
    
    tester = PerformanceTester()
    
    # Run tests with different sizes
    sizes = [100, 500, 1000, 2000, 5000]
    tester.run_comprehensive_test(sizes)
    
    # Save results
    output_dir = os.path.dirname(__file__) or '.'
    csv_file = os.path.join(output_dir, 'performance_results.csv')
    tester.save_results_csv(csv_file)
    
    # Generate plots
    tester.generate_plots(output_dir)
    
    # Print summary
    tester.print_summary()
    
    print("\n" + "=" * 70)
    print("Performance comparison complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()


