"""
Unit tests for Fibonacci Heap implementation
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from heaps.fibonacci_heap import FibonacciHeap


class TestFibonacciHeap(unittest.TestCase):
    """Test cases for Fibonacci Heap"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.heap = FibonacciHeap()
    
    def test_empty_heap(self):
        """Test empty heap properties"""
        self.assertTrue(self.heap.is_empty())
        self.assertEqual(self.heap.size, 0)
        with self.assertRaises(ValueError):
            self.heap.find_min()
    
    def test_insert_single(self):
        """Test inserting a single element"""
        self.heap.insert(10)
        self.assertFalse(self.heap.is_empty())
        self.assertEqual(self.heap.size, 1)
        self.assertEqual(self.heap.find_min(), 10)
    
    def test_insert_multiple(self):
        """Test inserting multiple elements"""
        values = [10, 5, 20, 3, 15]
        for val in values:
            self.heap.insert(val)
        
        self.assertEqual(self.heap.size, 5)
        self.assertEqual(self.heap.find_min(), 3)
    
    def test_find_min(self):
        """Test finding minimum element"""
        self.heap.insert(10)
        self.heap.insert(5)
        self.heap.insert(20)
        
        self.assertEqual(self.heap.find_min(), 5)
        # Find-min should not remove element
        self.assertEqual(self.heap.size, 3)
    
    def test_delete_min(self):
        """Test deleting minimum element"""
        values = [10, 5, 20, 3, 15]
        for val in values:
            self.heap.insert(val)
        
        min_val = self.heap.delete_min()
        self.assertEqual(min_val, 3)
        self.assertEqual(self.heap.size, 4)
        self.assertEqual(self.heap.find_min(), 5)
    
    def test_delete_min_sequence(self):
        """Test deleting all elements in order"""
        values = [10, 5, 20, 3, 15, 8, 12]
        for val in values:
            self.heap.insert(val)
        
        sorted_values = sorted(values)
        extracted = []
        
        while not self.heap.is_empty():
            extracted.append(self.heap.delete_min())
        
        self.assertEqual(extracted, sorted_values)
    
    def test_decrease_key(self):
        """Test decreasing key operation"""
        node1 = self.heap.insert(10)
        node2 = self.heap.insert(20)
        node3 = self.heap.insert(30)
        
        self.heap.decrease_key(node2, 5)
        self.assertEqual(self.heap.find_min(), 5)
        
        self.heap.decrease_key(node3, 2)
        self.assertEqual(self.heap.find_min(), 2)
    
    def test_merge_empty_heaps(self):
        """Test merging two empty heaps"""
        heap2 = FibonacciHeap()
        self.heap.merge(heap2)
        self.assertTrue(self.heap.is_empty())
    
    def test_merge_with_empty(self):
        """Test merging with an empty heap"""
        self.heap.insert(10)
        self.heap.insert(5)
        
        heap2 = FibonacciHeap()
        self.heap.merge(heap2)
        
        self.assertEqual(self.heap.size, 2)
        self.assertEqual(self.heap.find_min(), 5)
    
    def test_merge_non_empty_heaps(self):
        """Test merging two non-empty heaps"""
        self.heap.insert(10)
        self.heap.insert(20)
        
        heap2 = FibonacciHeap()
        heap2.insert(5)
        heap2.insert(15)
        
        self.heap.merge(heap2)
        
        self.assertEqual(self.heap.size, 4)
        self.assertEqual(self.heap.find_min(), 5)
    
    def test_delete_node(self):
        """Test deleting a specific node"""
        node1 = self.heap.insert(10)
        node2 = self.heap.insert(20)
        node3 = self.heap.insert(30)
        
        self.heap.delete(node2)
        self.assertEqual(self.heap.size, 2)
        
        values = []
        while not self.heap.is_empty():
            values.append(self.heap.delete_min())
        
        self.assertEqual(values, [10, 30])
    
    def test_large_dataset(self):
        """Test with a large number of elements"""
        n = 1000
        for i in range(n, 0, -1):
            self.heap.insert(i)
        
        self.assertEqual(self.heap.size, n)
        self.assertEqual(self.heap.find_min(), 1)
        
        # Extract first 10 elements
        for i in range(1, 11):
            self.assertEqual(self.heap.delete_min(), i)
    
    def test_duplicate_values(self):
        """Test handling duplicate values"""
        values = [5, 10, 5, 20, 10, 5]
        for val in values:
            self.heap.insert(val)
        
        self.assertEqual(self.heap.size, 6)
        
        extracted = []
        while not self.heap.is_empty():
            extracted.append(self.heap.delete_min())
        
        self.assertEqual(extracted, sorted(values))
    
    def test_negative_values(self):
        """Test with negative values"""
        values = [-10, 5, -20, 0, 15, -5]
        for val in values:
            self.heap.insert(val)
        
        self.assertEqual(self.heap.find_min(), -20)
        
        extracted = []
        while not self.heap.is_empty():
            extracted.append(self.heap.delete_min())
        
        self.assertEqual(extracted, sorted(values))
    
    def test_amortized_operations(self):
        """Test sequence of operations for amortized complexity"""
        # Insert many elements
        for i in range(100):
            self.heap.insert(i)
        
        # Perform multiple decrease-key operations
        nodes = []
        for i in range(50, 100):
            node = self.heap.insert(i + 100)
            nodes.append(node)
        
        for i, node in enumerate(nodes):
            self.heap.decrease_key(node, i)
        
        # Verify minimum
        self.assertEqual(self.heap.find_min(), 0)
        
        # Delete some elements
        for _ in range(10):
            self.heap.delete_min()
        
        self.assertEqual(self.heap.size, 140)


class TestFibonacciHeapEdgeCases(unittest.TestCase):
    """Test edge cases for Fibonacci Heap"""
    
    def test_single_element_operations(self):
        """Test operations on heap with single element"""
        heap = FibonacciHeap()
        node = heap.insert(42)
        
        self.assertEqual(heap.find_min(), 42)
        self.assertEqual(heap.delete_min(), 42)
        self.assertTrue(heap.is_empty())
    
    def test_decrease_key_to_minimum(self):
        """Test decreasing key to become new minimum"""
        heap = FibonacciHeap()
        heap.insert(10)
        heap.insert(20)
        node = heap.insert(30)
        
        heap.decrease_key(node, 5)
        self.assertEqual(heap.find_min(), 5)
    
    def test_multiple_merges(self):
        """Test multiple merge operations"""
        heap1 = FibonacciHeap()
        heap2 = FibonacciHeap()
        heap3 = FibonacciHeap()
        
        heap1.insert(10)
        heap2.insert(5)
        heap3.insert(15)
        
        heap1.merge(heap2)
        heap1.merge(heap3)
        
        self.assertEqual(heap1.find_min(), 5)
        self.assertEqual(heap1.size, 3)


def run_tests():
    """Run all tests"""
    unittest.main(argv=[''], exit=False, verbosity=2)


if __name__ == '__main__':
    run_tests()


