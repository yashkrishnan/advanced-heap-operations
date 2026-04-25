"""
Basic Operations Examples for Advanced Heap Structures

This module demonstrates basic usage of all heap implementations
with simple examples and explanations.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from heaps.binomial_heap import BinomialHeap
from heaps.fibonacci_heap import FibonacciHeap
from heaps.min_max_heap import MinMaxHeap
from heaps.pairing_heap import PairingHeap
from heaps.leftist_heap import LeftistHeap
from heaps.skew_heap import SkewHeap


def binomial_heap_example():
    """Demonstrate Binomial Heap operations"""
    print("\n=== Binomial Heap Example ===")
    heap = BinomialHeap()
    
    # Insert elements
    print("Inserting: 10, 5, 20, 3, 15")
    heap.insert(10)
    heap.insert(5)
    heap.insert(20)
    heap.insert(3)
    heap.insert(15)
    
    # Find minimum
    print(f"Minimum element: {heap.find_min()}")
    
    # Delete minimum
    print(f"Deleting minimum: {heap.delete_min()}")
    print(f"New minimum: {heap.find_min()}")
    
    # Merge with another heap
    heap2 = BinomialHeap()
    heap2.insert(1)
    heap2.insert(25)
    print("Merging with heap containing [1, 25]")
    heap.merge(heap2)
    print(f"Minimum after merge: {heap.find_min()}")


def fibonacci_heap_example():
    """Demonstrate Fibonacci Heap operations"""
    print("\n=== Fibonacci Heap Example ===")
    heap = FibonacciHeap()
    
    # Insert elements
    print("Inserting: 10, 5, 20, 3, 15")
    node1 = heap.insert(10)
    node2 = heap.insert(5)
    node3 = heap.insert(20)
    node4 = heap.insert(3)
    node5 = heap.insert(15)
    
    # Find minimum
    print(f"Minimum element: {heap.find_min()}")
    
    # Decrease key
    print(f"Decreasing key of node with value 20 to 2")
    heap.decrease_key(node3, 2)
    print(f"New minimum: {heap.find_min()}")
    
    # Delete minimum
    print(f"Deleting minimum: {heap.delete_min()}")
    print(f"New minimum: {heap.find_min()}")


def min_max_heap_example():
    """Demonstrate Min-Max Heap operations"""
    print("\n=== Min-Max Heap Example ===")
    heap = MinMaxHeap()
    
    # Insert elements
    print("Inserting: 10, 5, 20, 3, 15, 25, 1")
    for val in [10, 5, 20, 3, 15, 25, 1]:
        heap.insert(val)
    
    # Find minimum and maximum
    print(f"Minimum element: {heap.find_min()}")
    print(f"Maximum element: {heap.find_max()}")
    
    # Delete minimum
    print(f"Deleting minimum: {heap.delete_min()}")
    print(f"New minimum: {heap.find_min()}")
    
    # Delete maximum
    print(f"Deleting maximum: {heap.delete_max()}")
    print(f"New maximum: {heap.find_max()}")


def pairing_heap_example():
    """Demonstrate Pairing Heap operations"""
    print("\n=== Pairing Heap Example ===")
    heap = PairingHeap()
    
    # Insert elements
    print("Inserting: 10, 5, 20, 3, 15")
    heap.insert(10)
    heap.insert(5)
    heap.insert(20)
    heap.insert(3)
    heap.insert(15)
    
    # Find minimum
    print(f"Minimum element: {heap.find_min()}")
    
    # Delete minimum
    print(f"Deleting minimum: {heap.delete_min()}")
    print(f"New minimum: {heap.find_min()}")
    
    # Merge with another heap
    heap2 = PairingHeap()
    heap2.insert(1)
    heap2.insert(25)
    print("Merging with heap containing [1, 25]")
    heap.merge(heap2)
    print(f"Minimum after merge: {heap.find_min()}")


def leftist_heap_example():
    """Demonstrate Leftist Heap operations"""
    print("\n=== Leftist Heap Example ===")
    heap = LeftistHeap()
    
    # Insert elements
    print("Inserting: 10, 5, 20, 3, 15")
    heap.insert(10)
    heap.insert(5)
    heap.insert(20)
    heap.insert(3)
    heap.insert(15)
    
    # Find minimum
    print(f"Minimum element: {heap.find_min()}")
    
    # Delete minimum
    print(f"Deleting minimum: {heap.delete_min()}")
    print(f"New minimum: {heap.find_min()}")
    
    # Merge with another heap
    heap2 = LeftistHeap()
    heap2.insert(1)
    heap2.insert(25)
    print("Merging with heap containing [1, 25]")
    heap.merge(heap2)
    print(f"Minimum after merge: {heap.find_min()}")


def skew_heap_example():
    """Demonstrate Skew Heap operations"""
    print("\n=== Skew Heap Example ===")
    heap = SkewHeap()
    
    # Insert elements
    print("Inserting: 10, 5, 20, 3, 15")
    heap.insert(10)
    heap.insert(5)
    heap.insert(20)
    heap.insert(3)
    heap.insert(15)
    
    # Find minimum
    print(f"Minimum element: {heap.find_min()}")
    
    # Delete minimum
    print(f"Deleting minimum: {heap.delete_min()}")
    print(f"New minimum: {heap.find_min()}")
    
    # Merge with another heap
    heap2 = SkewHeap()
    heap2.insert(1)
    heap2.insert(25)
    print("Merging with heap containing [1, 25]")
    heap.merge(heap2)
    print(f"Minimum after merge: {heap.find_min()}")


def main():
    """Run all basic operation examples"""
    print("=" * 60)
    print("Advanced Heap Operations - Basic Examples")
    print("=" * 60)
    
    try:
        binomial_heap_example()
    except Exception as e:
        print(f"Error in Binomial Heap: {e}")
    
    try:
        fibonacci_heap_example()
    except Exception as e:
        print(f"Error in Fibonacci Heap: {e}")
    
    try:
        min_max_heap_example()
    except Exception as e:
        print(f"Error in Min-Max Heap: {e}")
    
    try:
        pairing_heap_example()
    except Exception as e:
        print(f"Error in Pairing Heap: {e}")
    
    try:
        leftist_heap_example()
    except Exception as e:
        print(f"Error in Leftist Heap: {e}")
    
    try:
        skew_heap_example()
    except Exception as e:
        print(f"Error in Skew Heap: {e}")
    
    print("\n" + "=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()


