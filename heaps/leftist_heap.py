"""
Leftist Heap Implementation

A leftist heap is a binary tree that maintains the "leftist property":
the null path length (npl) of the left child is at least as large as
the npl of the right child for every node.

Time Complexities:
- Insert: O(log n)
- Find-Min: O(1)
- Delete-Min: O(log n)
- Merge: O(log n)

Key Properties:
1. Min-heap ordered binary tree
2. Leftist property: npl(left) >= npl(right)
3. Right path is always short (at most log(n+1) nodes)
4. Efficient merging due to short right path

Null Path Length (NPL):
- NPL of a node is the length of the shortest path to a null child
- NPL of null node is -1
- NPL of leaf is 0

Applications:
- When merge is a frequent operation
- Priority queues in distributed systems
- Event-driven simulation
- Graph algorithms requiring heap merging
"""

from typing import Optional, Any


class LeftistNode:
    """Node in a leftist heap"""
    
    def __init__(self, key: Any):
        self.key = key
        self.npl = 0  # Null path length
        self.left: Optional['LeftistNode'] = None
        self.right: Optional['LeftistNode'] = None
    
    def __repr__(self):
        return f"LeftistNode(key={self.key}, npl={self.npl})"


class LeftistHeap:
    """
    Leftist Heap implementation
    
    Maintains the leftist property to ensure efficient merging.
    The right path is always short, making merge O(log n).
    """
    
    def __init__(self):
        self.root: Optional[LeftistNode] = None
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
    
    def _get_npl(self, node: Optional[LeftistNode]) -> int:
        """Get null path length of a node"""
        return node.npl if node else -1
    
    def _update_npl(self, node: LeftistNode):
        """Update the null path length of a node"""
        left_npl = self._get_npl(node.left)
        right_npl = self._get_npl(node.right)
        node.npl = min(left_npl, right_npl) + 1
    
    def _merge_nodes(self, h1: Optional[LeftistNode], h2: Optional[LeftistNode]) -> Optional[LeftistNode]:
        """
        Merge two leftist heap nodes
        Time Complexity: O(log n)
        
        Algorithm:
        1. If either heap is empty, return the other
        2. Make the heap with smaller root the result
        3. Recursively merge the right subtree with the other heap
        4. Swap left and right children if leftist property violated
        5. Update NPL
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
        
        # Maintain leftist property: swap if necessary
        if self._get_npl(h1.left) < self._get_npl(h1.right):
            h1.left, h1.right = h1.right, h1.left
        
        # Update NPL
        self._update_npl(h1)
        
        return h1
    
    def insert(self, key: Any) -> LeftistNode:
        """
        Insert a new key into the heap
        Time Complexity: O(log n)
        """
        new_node = LeftistNode(key)
        self.root = self._merge_nodes(self.root, new_node)
        self.size += 1
        return new_node
    
    def merge(self, other: 'LeftistHeap'):
        """
        Merge another leftist heap into this one
        Time Complexity: O(log n)
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
        Time Complexity: O(log n)
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        
        min_key = self.root.key
        
        # Merge left and right subtrees
        self.root = self._merge_nodes(self.root.left, self.root.right)
        self.size -= 1
        
        return min_key
    
    def _get_right_path_length(self, node: Optional[LeftistNode]) -> int:
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
    
    def _height(self, node: Optional[LeftistNode]) -> int:
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
            return "LeftistHeap(empty)"
        return f"LeftistHeap(size={self.size}, min={self.root.key}, right_path={self.get_right_path_length()})"


# Example usage and testing
if __name__ == "__main__":
    print("=== Leftist Heap Demo ===\n")
    
    # Create heap and insert elements
    heap = LeftistHeap()
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
    heap1 = LeftistHeap()
    heap2 = LeftistHeap()
    
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
    
    # Demonstrate efficiency of merge
    print("\n=== Merge Efficiency Demo ===")
    import time
    
    # Create two large heaps
    h1 = LeftistHeap()
    h2 = LeftistHeap()
    
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
    
    # Verify right path is logarithmic
    import math
    expected_path = math.log2(len(h1) + 1)
    print(f"Expected right path (log₂(n+1)): {expected_path:.2f}")
    print(f"Actual right path: {h1.get_right_path_length()}")
    print(f"Leftist property maintained: {h1.get_right_path_length() <= expected_path + 1}")


