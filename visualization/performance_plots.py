"""
Performance Plotting and Visualization

This module provides functions to generate performance comparison plots
for different heap implementations.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List, Any
import time


def plot_comparison(results: Dict[str, Dict[str, List[float]]], save_path: str = None):
    """
    Plot performance comparison of different heap operations
    
    Args:
        results: Dictionary with structure {heap_name: {operation: [times]}}
        save_path: Optional path to save the plot
    """
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Heap Performance Comparison', fontsize=16, fontweight='bold')
    
    operations = ['insert', 'delete_min', 'merge', 'find_min']
    
    for idx, operation in enumerate(operations):
        ax = axes[idx // 2, idx % 2]
        
        for heap_name, heap_results in results.items():
            if operation in heap_results:
                times = heap_results[operation]
                sizes = list(range(len(times)))
                ax.plot(sizes, times, marker='o', label=heap_name, linewidth=2)
        
        ax.set_xlabel('Operation Count', fontsize=12)
        ax.set_ylabel('Time (seconds)', fontsize=12)
        ax.set_title(f'{operation.replace("_", " ").title()} Performance', fontsize=14)
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    else:
        plt.show()


def plot_operation_time_complexity(heap_name: str, operation: str, 
                                   sizes: List[int], times: List[float],
                                   save_path: str = None):
    """
    Plot time complexity for a specific heap operation
    
    Args:
        heap_name: Name of the heap implementation
        operation: Operation name
        sizes: List of input sizes
        times: List of execution times
        save_path: Optional path to save the plot
    """
    plt.figure(figsize=(10, 6))
    
    plt.plot(sizes, times, 'b-o', linewidth=2, markersize=8, label='Actual')
    
    # Add theoretical complexity curves for comparison
    if operation in ['insert', 'delete_min']:
        # O(log n) reference
        log_n = [np.log2(n) * times[-1] / np.log2(sizes[-1]) for n in sizes]
        plt.plot(sizes, log_n, 'r--', linewidth=2, alpha=0.7, label='O(log n)')
    
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Time (seconds)', fontsize=12)
    plt.title(f'{heap_name} - {operation.replace("_", " ").title()} Time Complexity', 
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    else:
        plt.show()


def plot_heap_comparison_bar(results: Dict[str, float], operation: str, 
                             save_path: str = None):
    """
    Create bar chart comparing heap performance for a specific operation
    
    Args:
        results: Dictionary {heap_name: average_time}
        operation: Operation name
        save_path: Optional path to save the plot
    """
    plt.figure(figsize=(12, 6))
    
    heaps = list(results.keys())
    times = list(results.values())
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(heaps)))
    bars = plt.bar(heaps, times, color=colors, edgecolor='black', linewidth=1.5)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.6f}s',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    plt.xlabel('Heap Type', fontsize=12, fontweight='bold')
    plt.ylabel('Average Time (seconds)', fontsize=12, fontweight='bold')
    plt.title(f'Heap Performance Comparison - {operation.replace("_", " ").title()}',
              fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    else:
        plt.show()


def plot_scalability(results: Dict[str, Dict[int, float]], save_path: str = None):
    """
    Plot scalability of different heap implementations
    
    Args:
        results: Dictionary {heap_name: {size: time}}
        save_path: Optional path to save the plot
    """
    plt.figure(figsize=(12, 7))
    
    for heap_name, size_times in results.items():
        sizes = sorted(size_times.keys())
        times = [size_times[s] for s in sizes]
        plt.plot(sizes, times, marker='o', linewidth=2, markersize=8, label=heap_name)
    
    plt.xlabel('Input Size', fontsize=12, fontweight='bold')
    plt.ylabel('Execution Time (seconds)', fontsize=12, fontweight='bold')
    plt.title('Heap Scalability Comparison', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    else:
        plt.show()


def plot_memory_usage(results: Dict[str, List[int]], sizes: List[int],
                     save_path: str = None):
    """
    Plot memory usage comparison
    
    Args:
        results: Dictionary {heap_name: [memory_usage]}
        sizes: List of input sizes
        save_path: Optional path to save the plot
    """
    plt.figure(figsize=(12, 7))
    
    for heap_name, memory in results.items():
        plt.plot(sizes, memory, marker='s', linewidth=2, markersize=8, label=heap_name)
    
    plt.xlabel('Input Size', fontsize=12, fontweight='bold')
    plt.ylabel('Memory Usage (bytes)', fontsize=12, fontweight='bold')
    plt.title('Heap Memory Usage Comparison', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    else:
        plt.show()


def create_comprehensive_report(results: Dict[str, Any], output_dir: str = '.'):
    """
    Create a comprehensive performance report with multiple plots
    
    Args:
        results: Complete results dictionary
        output_dir: Directory to save plots
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    print("Generating comprehensive performance report...")
    
    # Overall comparison
    if 'comparison' in results:
        plot_comparison(results['comparison'], 
                       f'{output_dir}/overall_comparison.png')
    
    # Individual operation comparisons
    operations = ['insert', 'delete_min', 'merge', 'find_min']
    for op in operations:
        if op in results:
            plot_heap_comparison_bar(results[op], op,
                                    f'{output_dir}/{op}_comparison.png')
    
    # Scalability
    if 'scalability' in results:
        plot_scalability(results['scalability'],
                        f'{output_dir}/scalability.png')
    
    # Memory usage
    if 'memory' in results and 'sizes' in results:
        plot_memory_usage(results['memory'], results['sizes'],
                         f'{output_dir}/memory_usage.png')
    
    print(f"Report generated in {output_dir}/")


def main():
    """Example usage of plotting functions"""
    print("=" * 60)
    print("Performance Plotting Examples")
    print("=" * 60)
    
    # Example data
    example_results = {
        'Binomial Heap': {
            'insert': [0.001, 0.002, 0.004, 0.008],
            'delete_min': [0.002, 0.003, 0.005, 0.009],
            'merge': [0.003, 0.005, 0.008, 0.012],
            'find_min': [0.0001, 0.0001, 0.0001, 0.0001]
        },
        'Fibonacci Heap': {
            'insert': [0.0005, 0.0006, 0.0007, 0.0008],
            'delete_min': [0.003, 0.004, 0.006, 0.010],
            'merge': [0.0005, 0.0006, 0.0007, 0.0008],
            'find_min': [0.0001, 0.0001, 0.0001, 0.0001]
        },
        'Min-Max Heap': {
            'insert': [0.0008, 0.0015, 0.003, 0.006],
            'delete_min': [0.0015, 0.0025, 0.004, 0.007],
            'merge': [0.01, 0.02, 0.04, 0.08],
            'find_min': [0.0001, 0.0001, 0.0001, 0.0001]
        }
    }
    
    print("\nGenerating example comparison plot...")
    plot_comparison(example_results, 'example_comparison.png')
    
    print("\nExample plots generated!")
    print("=" * 60)


if __name__ == "__main__":
    main()


