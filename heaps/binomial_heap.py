"""
Binomial Heap Implementation

A binomial heap is a collection of binomial trees that satisfies the min-heap property.
Each binomial tree Bk has exactly 2^k nodes and height k.

Time Complexities:
- Insert: O(log n)
- Find-Min: O(log n) or O(1) with min pointer
- Delete-Min: O(log n)
- Merge: O(log n)
- Decrease-Key: O(log n)

Key Properties:
1. Each binomial tree in the heap satisfies the min-heap property
2. There is at most one binomial tree of each degree
3. A binomial tree Bk consists of two Bk-1 trees linked together
"""

from typing import Optional, Any, List


class BinomialNode:
    """Node in a binomial tree"""
    
    def __init__(self, key: Any):
        """Initialize a binomial tree node with the given key."""
        self.key = key
        self.degree = 0  # Number of children
        self.parent: Optional['BinomialNode'] = None
        self.child: Optional['BinomialNode'] = None  # Leftmost child
        self.sibling: Optional['BinomialNode'] = None  # Right sibling

    def __repr__(self):
        """Return a developer-readable string representation of the node."""
        return f"BinomialNode(key={self.key}, degree={self.degree})"


class BinomialHeap:
    """
    Binomial Heap implementation
    
    A binomial heap is a collection of binomial trees stored as a linked list.
    """
    
    def __init__(self):
        """Initialize an empty binomial heap."""
        self.head: Optional[BinomialNode] = None  # Head of the root list
        self.min_node: Optional[BinomialNode] = None  # Pointer to minimum
        self.size = 0
    
    def is_empty(self) -> bool:
        """Check if heap is empty"""
        return self.head is None
    
    def find_min(self) -> Any:
        """
        Find the minimum key in the heap
        Time Complexity: O(1) with min pointer, O(log n) without
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        
        if self.min_node:
            return self.min_node.key
        
        # If min_node not maintained, find it
        min_node = self.head
        current = self.head.sibling
        
        while current:
            if current.key < min_node.key:
                min_node = current
            current = current.sibling
        
        return min_node.key
    
    def insert(self, key: Any) -> BinomialNode:
        """
        Insert a new key into the heap
        Time Complexity: O(log n)
        """
        # Create a new heap with single node
        new_node = BinomialNode(key)
        new_heap = BinomialHeap()
        new_heap.head = new_node
        new_heap.size = 1
        
        # Merge with current heap
        self._merge(new_heap)
        self.size += 1
        
        # Update min pointer
        if self.min_node is None or key < self.min_node.key:
            self.min_node = new_node
        
        return new_node
    
    def _link_trees(self, tree1: BinomialNode, tree2: BinomialNode) -> BinomialNode:
        """
        Link two binomial trees of the same degree
        Makes the tree with larger root a child of the other
        """
        if tree1.key > tree2.key:
            tree1, tree2 = tree2, tree1
        
        # Make tree2 a child of tree1
        tree2.parent = tree1
        tree2.sibling = tree1.child
        tree1.child = tree2
        tree1.degree += 1
        
        return tree1
    
    def _merge_root_lists(self, heap1: 'BinomialHeap', heap2: 'BinomialHeap') -> Optional[BinomialNode]:
        """
        Merge two root lists in increasing order of degree
        Similar to merging two sorted linked lists
        """
        if not heap1.head:
            return heap2.head
        if not heap2.head:
            return heap1.head
        
        # Start with the tree of smaller degree
        if heap1.head.degree <= heap2.head.degree:
            head = heap1.head
            heap1.head = heap1.head.sibling
        else:
            head = heap2.head
            heap2.head = heap2.head.sibling
        
        current = head
        
        # Merge remaining trees
        while heap1.head and heap2.head:
            if heap1.head.degree <= heap2.head.degree:
                current.sibling = heap1.head
                heap1.head = heap1.head.sibling
            else:
                current.sibling = heap2.head
                heap2.head = heap2.head.sibling
            current = current.sibling
        
        # Attach remaining trees
        if heap1.head:
            current.sibling = heap1.head
        else:
            current.sibling = heap2.head
        
        return head
    
    def _merge(self, other: 'BinomialHeap'):
        """
        Merge another binomial heap into this one
        Time Complexity: O(log n)
        """
        if other.is_empty():
            return
        
        # Merge root lists
        merged_head = self._merge_root_lists(self, other)
        
        if not merged_head:
            return
        
        # Consolidate trees of same degree
        prev = None
        current = merged_head
        next_node = merged_head.sibling
        
        while next_node:
            # Case 1 & 2: Current degree != next degree
            if (current.degree != next_node.degree or 
                (next_node.sibling and next_node.sibling.degree == current.degree)):
                prev = current
                current = next_node
            # Case 3: Current degree == next degree, current.key <= next.key
            elif current.key <= next_node.key:
                current.sibling = next_node.sibling
                current = self._link_trees(current, next_node)
            # Case 4: Current degree == next degree, current.key > next.key
            else:
                if prev:
                    prev.sibling = next_node
                else:
                    merged_head = next_node
                current = self._link_trees(next_node, current)
            
            next_node = current.sibling
        
        self.head = merged_head
        
        # Update min pointer
        self._update_min()
    
    def _update_min(self):
        """Update the minimum node pointer"""
        if not self.head:
            self.min_node = None
            return
        
        self.min_node = self.head
        current = self.head.sibling
        
        while current:
            if current.key < self.min_node.key:
                self.min_node = current
            current = current.sibling
    
    def delete_min(self) -> Any:
        """
        Delete and return the minimum key
        Time Complexity: O(log n)
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        
        # Find minimum node and its predecessor
        min_node = self.head
        min_prev = None
        current = self.head
        prev = None
        
        while current.sibling:
            if current.sibling.key < min_node.key:
                min_node = current.sibling
                min_prev = current
            prev = current
            current = current.sibling
        
        # Remove min_node from root list
        if min_prev:
            min_prev.sibling = min_node.sibling
        else:
            self.head = min_node.sibling
        
        # Create new heap from min_node's children
        child_heap = BinomialHeap()
        if min_node.child:
            # Reverse the child list and clear parent pointers
            child = min_node.child
            child_heap.head = None
            
            while child:
                next_child = child.sibling
                child.sibling = child_heap.head
                child.parent = None
                child_heap.head = child
                child = next_child
        
        # Merge with current heap
        self._merge(child_heap)
        self.size -= 1
        
        # Update min pointer
        self._update_min()
        
        return min_node.key
    
    def merge(self, other: 'BinomialHeap'):
        """
        Merge another binomial heap into this one
        Time Complexity: O(log n)
        """
        self._merge(other)
        self.size += other.size
        other.head = None
        other.min_node = None
        other.size = 0
    
    def decrease_key(self, node: BinomialNode, new_key: Any):
        """
        Decrease the key of a node
        Time Complexity: O(log n)
        """
        if new_key > node.key:
            raise ValueError("New key is greater than current key")
        
        node.key = new_key
        current = node
        parent = current.parent
        
        # Bubble up to maintain heap property
        while parent and current.key < parent.key:
            # Swap keys
            current.key, parent.key = parent.key, current.key
            current = parent
            parent = current.parent
        
        # Update min pointer if necessary
        if current.key < self.min_node.key:
            self.min_node = current
    
    def delete(self, node: BinomialNode):
        """
        Delete a specific node
        Time Complexity: O(log n)
        """
        # Decrease key to negative infinity (represented by very small value)
        self.decrease_key(node, float('-inf'))
        # Delete the minimum
        self.delete_min()
    
    def get_trees(self) -> List[BinomialNode]:
        """Get list of root nodes (binomial trees)"""
        trees = []
        current = self.head
        while current:
            trees.append(current)
            current = current.sibling
        return trees
    
    def __len__(self) -> int:
        """Return the number of elements in the heap"""
        return self.size
    
    def __repr__(self) -> str:
        """Return a developer-readable summary of the heap's current state."""
        if self.is_empty():
            return "BinomialHeap(empty)"

        trees = self.get_trees()
        tree_info = [f"B{tree.degree}(root={tree.key})" for tree in trees]
        return f"BinomialHeap(trees=[{', '.join(tree_info)}], size={self.size})"


# Example usage and testing
if __name__ == "__main__":
    print("=== Binomial Heap Demo ===\n")
    
    # Create heap and insert elements
    heap = BinomialHeap()
    print("Inserting: 10, 5, 20, 15, 30, 25")
    for key in [10, 5, 20, 15, 30, 25]:
        heap.insert(key)
        print(f"After inserting {key}: {heap}")
    
    print(f"\nMinimum: {heap.find_min()}")
    print(f"Heap size: {len(heap)}")
    
    # Delete minimum
    print(f"\nDeleting minimum: {heap.delete_min()}")
    print(f"After delete: {heap}")
    print(f"New minimum: {heap.find_min()}")
    
    # Merge two heaps
    print("\n=== Merge Operation ===")
    heap2 = BinomialHeap()
    for key in [3, 7, 12]:
        heap2.insert(key)
    print(f"Heap 1: {heap}")
    print(f"Heap 2: {heap2}")
    
    heap.merge(heap2)
    print(f"After merge: {heap}")
    print(f"Minimum: {heap.find_min()}")


