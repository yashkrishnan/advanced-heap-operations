"""
Skew Heap Implementation

A skew heap is a self-adjusting variant of a leftist heap.
It has the advantage of not requiring explicit balance information (NPL).

Time Complexities (Amortized):
- Insert: O(log n)
- Find-Min: O(1)
- Delete-Min: O(log n)
- Merge: O(log n)

Key Properties:
1. Min-heap ordered binary tree
2. Self-adjusting (no explicit balance information)
3. Unconditional swapping during merge
4. Simpler implementation than leftist heap
5. Good amortized performance

Differences from Leftist Heap:
- No NPL maintenance
- Always swaps left and right children during merge
- Simpler code, similar performance

Applications:
- When simplicity is preferred over guaranteed bounds
- Priority queues with frequent merging
- Self-adjusting data structures
- Educational purposes (simpler than leftist heap)
"""

from typing import Optional, Any


class SkewNode:
    """Node in a skew heap"""
    
    def __init__(self, key: Any):
        self.key = key
        self.left: Optional['SkewNode'] = None
        self.right: Optional['SkewNode'] = None
    
    def __repr__(self):
        return f"SkewNode(key={self.key})"


class SkewHeap:
    """
    Skew Heap implementation
    
    A self-adjusting heap that unconditionally swaps children during merge.
    Simpler than leftist heap with similar amortized performance.
    """
    
    def __init__(self):
        self.root: Optional[SkewNode] = None
        self.size = 0
    
    def is_empty(self) -> bool:
        """Check if heap is empty"""
        return self.root is None
    
    def find_min(self) -> Any:
        """
        Find the minimum key in the heap
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        return self.root.key
    
    def _merge_nodes(self, h1: Optional[SkewNode], h2: Optional[SkewNode]) -> Optional[SkewNode]:
        """
        Merge two skew heap nodes
        Time Complexity: O(log n) amortized
        
        Algorithm:
        1. If either heap is empty, return the other
        2. Make the heap with smaller root the result
        3. Recursively merge the right subtree with the other heap
        4. ALWAYS swap left and right children (key difference from leftist heap)
        """
        # Base cases
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        
        # Ensure h1 has smaller root
        if h1.key > h2.key:
            h1, h2 = h2, h1
        
        # Recursively merge h2 with right subtree of h1
        h1.right = self._merge_nodes(h1.right, h2)
        
        # UNCONDITIONALLY swap left and right children
        # This is the key difference from leftist heap
        h1.left, h1.right = h1.right, h1.left
        
        return h1
    
    def insert(self, key: Any) -> SkewNode:
        """
        Insert a new key into the heap
        Time Complexity: O(log n) amortized
        """
        new_node = SkewNode(key)
        self.root = self._merge_nodes(self.root, new_node)
        self.size += 1
        return new_node
    
    def merge(self, other: 'SkewHeap'):
        """
        Merge another skew heap into this one
        Time Complexity: O(log n) amortized
        """
        if other.is_empty():
            return
        
        self.root = self._merge_nodes(self.root, other.root)
        self.size += other.size
        
        # Clear other heap
        other.root = None
        other.size = 0
    
    def delete_min(self) -> Any:
        """
        Delete and return the minimum key
        Time Complexity: O(log n) amortized
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        
        min_key = self.root.key
        
        # Merge left and right subtrees
        self.root = self._merge_nodes(self.root.left, self.root.right)
        self.size -= 1
        
        return min_key
    
    def _get_right_path_length(self, node: Optional[SkewNode]) -> int:
        """Get the length of the right path (for analysis)"""
        length = 0
        current = node
        while current:
            length += 1
            current = current.right
        return length
    
    def get_right_path_length(self) -> int:
        """Get the length of the right path from root"""
        return self._get_right_path_length(self.root)
    
    def _height(self, node: Optional[SkewNode]) -> int:
        """Calculate height of subtree"""
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))
    
    def height(self) -> int:
        """Get height of the heap"""
        return self._height(self.root)
    
    def __len__(self) -> int:
        """Return the number of elements in the heap"""
        return self.size
    
    def __repr__(self) -> str:
        if self.is_empty():
            return "SkewHeap(empty)"
        return f"SkewHeap(size={self.size}, min={self.root.key}, right_path={self.get_right_path_length()})"


# Example usage and testing
if __name__ == "__main__":
    print("=== Skew Heap Demo ===\n")
    
    # Create heap and insert elements
    heap = SkewHeap()
    print("Inserting: 10, 5, 20, 15, 30, 25, 8, 12")
    for key in [10, 5, 20, 15, 30, 25, 8, 12]:
        heap.insert(key)
        print(f"After inserting {key}: {heap}")
    
    print(f"\nMinimum: {heap.find_min()}")
    print(f"Heap size: {len(heap)}")
    print(f"Heap height: {heap.height()}")
    print(f"Right path length: {heap.get_right_path_length()}")
    
    # Delete minimum
    print(f"\nDeleting minimum: {heap.delete_min()}")
    print(f"After delete: {heap}")
    print(f"New minimum: {heap.find_min()}")
    
    # Demonstrate merge operation
    print("\n=== Merge Operation ===")
    heap1 = SkewHeap()
    heap2 = SkewHeap()
    
    print("Building heap1 with: 3, 7, 11")
    for key in [3, 7, 11]:
        heap1.insert(key)
    
    print("Building heap2 with: 2, 9, 13")
    for key in [2, 9, 13]:
        heap2.insert(key)
    
    print(f"\nHeap 1: {heap1}")
    print(f"Heap 2: {heap2}")
    
    heap1.merge(heap2)
    print(f"\nAfter merge: {heap1}")
    print(f"Minimum: {heap1.find_min()}")
    print(f"Right path length: {heap1.get_right_path_length()}")
    
    # Compare with Leftist Heap
    print("\n=== Comparison: Skew vs Leftist Heap ===")
    print("Skew Heap advantages:")
    print("  ✓ Simpler implementation (no NPL maintenance)")
    print("  ✓ Less memory per node")
    print("  ✓ Unconditional swapping is simpler")
    print("\nLeftist Heap advantages:")
    print("  ✓ Guaranteed O(log n) worst-case for merge")
    print("  ✓ More predictable performance")
    print("\nBoth have O(log n) amortized complexity")
    
    # Performance demonstration
    print("\n=== Performance Demo ===")
    import time
    
    # Create two large heaps
    h1 = SkewHeap()
    h2 = SkewHeap()
    
    for i in range(1000):
        h1.insert(i * 2)
        h2.insert(i * 2 + 1)
    
    print(f"Heap 1: size={len(h1)}, right_path={h1.get_right_path_length()}")
    print(f"Heap 2: size={len(h2)}, right_path={h2.get_right_path_length()}")
    
    start = time.time()
    h1.merge(h2)
    end = time.time()
    
    print(f"\nMerged in {(end-start)*1000:.2f}ms")
    print(f"Result: size={len(h1)}, right_path={h1.get_right_path_length()}")
    
    # Test delete-min performance
    print("\n=== Delete-Min Performance ===")
    test_heap = SkewHeap()
    for i in range(1000):
        test_heap.insert(i)
    
    start = time.time()
    for _ in range(500):
        test_heap.delete_min()
    end = time.time()
    
    print(f"Deleted 500 minimums in {(end-start)*1000:.2f}ms")
    print(f"Average per delete: {(end-start)*1000000/500:.2f}μs")
    print(f"Remaining size: {len(test_heap)}")


