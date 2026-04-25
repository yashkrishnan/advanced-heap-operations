"""
Pairing Heap Implementation

A pairing heap is a type of heap data structure with relatively simple implementation
and excellent practical performance. It is a multiway tree structure.

Time Complexities (Amortized):
- Insert: O(1)
- Find-Min: O(1)
- Delete-Min: O(log n) amortized
- Decrease-Key: O(log n) amortized (O(1) in practice)
- Merge: O(1)

Key Properties:
1. Multiway tree (nodes can have any number of children)
2. Min-heap ordered
3. Simple implementation compared to Fibonacci heaps
4. Excellent practical performance
5. Two-pass pairing strategy for delete-min

Applications:
- Priority queues with frequent updates
- Network optimization algorithms
- Simulation systems
- General-purpose priority queue when simplicity matters
"""

from typing import Optional, Any, List


class PairingNode:
    """Node in a pairing heap"""
    
    def __init__(self, key: Any):
        self.key = key
        self.child: Optional['PairingNode'] = None  # Leftmost child
        self.sibling: Optional['PairingNode'] = None  # Right sibling
        self.parent: Optional['PairingNode'] = None
    
    def __repr__(self):
        return f"PairingNode(key={self.key})"


class PairingHeap:
    """
    Pairing Heap implementation
    
    Uses a multiway tree structure with simple pairing operations.
    Provides excellent practical performance despite theoretical bounds.
    """
    
    def __init__(self):
        self.root: Optional[PairingNode] = None
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
    
    def insert(self, key: Any) -> PairingNode:
        """
        Insert a new key into the heap
        Time Complexity: O(1)
        """
        new_node = PairingNode(key)
        
        if self.is_empty():
            self.root = new_node
        else:
            self.root = self._meld(self.root, new_node)
        
        self.size += 1
        return new_node
    
    def _meld(self, heap1: Optional[PairingNode], heap2: Optional[PairingNode]) -> Optional[PairingNode]:
        """
        Meld (merge) two pairing heaps
        Time Complexity: O(1)
        
        The heap with smaller root becomes the new root,
        and the other heap becomes its leftmost child.
        """
        if heap1 is None:
            return heap2
        if heap2 is None:
            return heap1
        
        # Make the heap with smaller root the parent
        if heap1.key <= heap2.key:
            # heap2 becomes leftmost child of heap1
            heap2.sibling = heap1.child
            if heap1.child:
                heap1.child.parent = None
            heap1.child = heap2
            heap2.parent = heap1
            return heap1
        else:
            # heap1 becomes leftmost child of heap2
            heap1.sibling = heap2.child
            if heap2.child:
                heap2.child.parent = None
            heap2.child = heap1
            heap1.parent = heap2
            return heap2
    
    def merge(self, other: 'PairingHeap'):
        """
        Merge another pairing heap into this one
        Time Complexity: O(1)
        """
        if other.is_empty():
            return
        
        self.root = self._meld(self.root, other.root)
        self.size += other.size
        
        # Clear other heap
        other.root = None
        other.size = 0
    
    def _two_pass_merge(self, node: Optional[PairingNode]) -> Optional[PairingNode]:
        """
        Perform two-pass merge of siblings
        
        First pass: pair up siblings from left to right
        Second pass: merge pairs from right to left
        
        Time Complexity: O(log n) amortized
        """
        if node is None or node.sibling is None:
            return node
        
        # First pass: pair up siblings
        pairs: List[Optional[PairingNode]] = []
        current = node
        
        while current is not None:
            # Take two siblings at a time
            first = current
            second = current.sibling
            
            if second is None:
                # Odd number of siblings, add the last one
                pairs.append(first)
                break
            
            # Move to next pair
            current = second.sibling
            
            # Detach the pair
            first.sibling = None
            second.sibling = None
            
            # Meld the pair
            pairs.append(self._meld(first, second))
        
        # Second pass: merge pairs from right to left
        result = pairs[-1]
        for i in range(len(pairs) - 2, -1, -1):
            result = self._meld(pairs[i], result)
        
        return result
    
    def delete_min(self) -> Any:
        """
        Delete and return the minimum key
        Time Complexity: O(log n) amortized
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        
        min_key = self.root.key
        
        # Merge all children using two-pass strategy
        if self.root.child:
            # Clear parent pointers
            child = self.root.child
            while child:
                child.parent = None
                child = child.sibling
            
            self.root = self._two_pass_merge(self.root.child)
        else:
            self.root = None
        
        self.size -= 1
        return min_key
    
    def decrease_key(self, node: PairingNode, new_key: Any):
        """
        Decrease the key of a node
        Time Complexity: O(log n) amortized, often O(1) in practice
        """
        if new_key > node.key:
            raise ValueError("New key is greater than current key")
        
        node.key = new_key
        
        # If node is root or satisfies heap property, done
        if node.parent is None:
            return
        
        # Cut node from parent
        self._cut(node)
        
        # Meld with root
        self.root = self._meld(self.root, node)
    
    def _cut(self, node: PairingNode):
        """Cut a node from its parent"""
        parent = node.parent
        
        if parent is None:
            return
        
        # Remove node from parent's child list
        if parent.child == node:
            parent.child = node.sibling
        else:
            # Find previous sibling
            prev = parent.child
            while prev and prev.sibling != node:
                prev = prev.sibling
            
            if prev:
                prev.sibling = node.sibling
        
        node.parent = None
        node.sibling = None
    
    def delete(self, node: PairingNode):
        """
        Delete a specific node
        Time Complexity: O(log n) amortized
        """
        self.decrease_key(node, float('-inf'))
        self.delete_min()
    
    def __len__(self) -> int:
        """Return the number of elements in the heap"""
        return self.size
    
    def __repr__(self) -> str:
        if self.is_empty():
            return "PairingHeap(empty)"
        return f"PairingHeap(size={self.size}, min={self.root.key})"


# Example usage and testing
if __name__ == "__main__":
    print("=== Pairing Heap Demo ===\n")
    
    # Create heap and insert elements
    heap = PairingHeap()
    print("Inserting: 10, 5, 20, 15, 30, 25, 8, 12")
    nodes = {}
    for key in [10, 5, 20, 15, 30, 25, 8, 12]:
        nodes[key] = heap.insert(key)
        print(f"After inserting {key}: {heap}")
    
    print(f"\nMinimum: {heap.find_min()}")
    print(f"Heap size: {len(heap)}")
    
    # Delete minimum
    print(f"\nDeleting minimum: {heap.delete_min()}")
    print(f"After delete: {heap}")
    print(f"New minimum: {heap.find_min()}")
    
    # Decrease key
    print("\n=== Decrease Key Operation ===")
    print(f"Decreasing key 30 to 3")
    heap.decrease_key(nodes[30], 3)
    print(f"After decrease: {heap}")
    print(f"New minimum: {heap.find_min()}")
    
    # Merge two heaps
    print("\n=== Merge Operation ===")
    heap2 = PairingHeap()
    for key in [2, 7, 18]:
        heap2.insert(key)
    print(f"Heap 1: {heap}")
    print(f"Heap 2: {heap2}")
    
    heap.merge(heap2)
    print(f"After merge: {heap}")
    print(f"Minimum: {heap.find_min()}")
    
    # Performance demonstration
    print("\n=== Performance Demo ===")
    import time
    
    perf_heap = PairingHeap()
    
    # Test insert performance
    start = time.time()
    for i in range(1000):
        perf_heap.insert(i)
    end = time.time()
    print(f"Inserted 1000 elements in {(end-start)*1000:.2f}ms")
    print(f"Average per insert: {(end-start)*1000000/1000:.2f}μs")
    
    # Test delete-min performance
    start = time.time()
    for i in range(500):
        perf_heap.delete_min()
    end = time.time()
    print(f"Deleted 500 minimums in {(end-start)*1000:.2f}ms")
    print(f"Average per delete: {(end-start)*1000000/500:.2f}μs")
    
    print(f"\nFinal heap size: {len(perf_heap)}")


