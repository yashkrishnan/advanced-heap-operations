"""
Fibonacci Heap Implementation

A Fibonacci heap is a collection of heap-ordered trees with a "lazy" approach to operations.
It provides exceptional amortized time complexity for priority queue operations.

Time Complexities (Amortized):
- Insert: O(1)
- Find-Min: O(1)
- Delete-Min: O(log n)
- Decrease-Key: O(1)
- Merge: O(1)
- Delete: O(log n)

Key Properties:
1. Collection of min-heap-ordered trees
2. Lazy consolidation (delayed until delete-min)
3. Cascading cuts for decrease-key
4. Marked nodes to track structure changes

Applications:
- Dijkstra's shortest path algorithm
- Prim's minimum spanning tree algorithm
- Any algorithm requiring frequent decrease-key operations
"""

from typing import Optional, Any, List
import math


class FibonacciNode:
    """Node in a Fibonacci heap"""
    
    def __init__(self, key: Any):
        self.key = key
        self.degree = 0  # Number of children
        self.marked = False  # Whether node has lost a child
        self.parent: Optional['FibonacciNode'] = None
        self.child: Optional['FibonacciNode'] = None  # One child (circular list)
        self.left: 'FibonacciNode' = self  # Left sibling (circular)
        self.right: 'FibonacciNode' = self  # Right sibling (circular)
    
    def __repr__(self):
        return f"FibNode(key={self.key}, degree={self.degree}, marked={self.marked})"


class FibonacciHeap:
    """
    Fibonacci Heap implementation
    
    Uses a circular doubly-linked list of trees at the root level.
    Provides excellent amortized performance for priority queue operations.
    """
    
    def __init__(self):
        self.min_node: Optional[FibonacciNode] = None
        self.size = 0
        self.num_trees = 0  # Number of trees in root list
        self.num_marked = 0  # Number of marked nodes
    
    def is_empty(self) -> bool:
        """Check if heap is empty"""
        return self.min_node is None
    
    def find_min(self) -> Any:
        """
        Find the minimum key in the heap
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        return self.min_node.key
    
    def insert(self, key: Any) -> FibonacciNode:
        """
        Insert a new key into the heap
        Time Complexity: O(1) amortized
        """
        node = FibonacciNode(key)
        
        if self.min_node is None:
            # Create a new heap with single node
            self.min_node = node
        else:
            # Add to root list
            self._add_to_root_list(node)
            
            # Update minimum if necessary
            if key < self.min_node.key:
                self.min_node = node
        
        self.size += 1
        self.num_trees += 1
        
        return node
    
    def _add_to_root_list(self, node: FibonacciNode):
        """Add a node to the root list (circular doubly-linked list)"""
        if self.min_node is None:
            self.min_node = node
            node.left = node
            node.right = node
        else:
            # Insert node between min_node and min_node.right
            node.left = self.min_node
            node.right = self.min_node.right
            self.min_node.right.left = node
            self.min_node.right = node
    
    def _remove_from_root_list(self, node: FibonacciNode):
        """Remove a node from the root list"""
        if node.right == node:
            # Only node in list
            return
        
        node.left.right = node.right
        node.right.left = node.left
    
    def _link_trees(self, child: FibonacciNode, parent: FibonacciNode):
        """Make child a child of parent"""
        # Remove child from root list
        self._remove_from_root_list(child)
        
        # Make child a child of parent
        if parent.child is None:
            parent.child = child
            child.left = child
            child.right = child
        else:
            # Add to parent's child list
            child.left = parent.child
            child.right = parent.child.right
            parent.child.right.left = child
            parent.child.right = child
        
        child.parent = parent
        parent.degree += 1
        child.marked = False
        self.num_trees -= 1
    
    def _consolidate(self):
        """
        Consolidate trees to ensure at most one tree of each degree
        Time Complexity: O(log n) amortized
        """
        # Maximum degree is O(log n)
        max_degree = int(math.log(self.size) * 2) + 1
        degree_table: List[Optional[FibonacciNode]] = [None] * max_degree
        
        # Collect all root nodes
        roots = []
        current = self.min_node
        if current:
            while True:
                roots.append(current)
                current = current.right
                if current == self.min_node:
                    break
        
        # Consolidate trees of same degree
        for root in roots:
            degree = root.degree
            
            while degree_table[degree] is not None:
                other = degree_table[degree]
                
                # Make sure root has smaller key
                if root.key > other.key:
                    root, other = other, root
                
                # Link other under root
                self._link_trees(other, root)
                degree_table[degree] = None
                degree += 1
            
            degree_table[degree] = root
        
        # Rebuild root list and find new minimum
        self.min_node = None
        for node in degree_table:
            if node is not None:
                if self.min_node is None:
                    self.min_node = node
                    node.left = node
                    node.right = node
                    self.num_trees = 1
                else:
                    self._add_to_root_list(node)
                    self.num_trees += 1
                    if node.key < self.min_node.key:
                        self.min_node = node
    
    def delete_min(self) -> Any:
        """
        Delete and return the minimum key
        Time Complexity: O(log n) amortized
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        
        min_node = self.min_node
        
        if min_node.child is not None:
            # Add all children to root list
            child = min_node.child
            children = []
            
            # Collect all children
            while True:
                children.append(child)
                child = child.right
                if child == min_node.child:
                    break
            
            # Add children to root list
            for child in children:
                self._add_to_root_list(child)
                child.parent = None
                self.num_trees += 1
        
        # Remove min_node from root list
        self._remove_from_root_list(min_node)
        self.num_trees -= 1
        
        if min_node == min_node.right:
            # Was the only node
            self.min_node = None
        else:
            self.min_node = min_node.right
            self._consolidate()
        
        self.size -= 1
        
        return min_node.key
    
    def merge(self, other: 'FibonacciHeap'):
        """
        Merge another Fibonacci heap into this one
        Time Complexity: O(1)
        """
        if other.is_empty():
            return
        
        if self.is_empty():
            self.min_node = other.min_node
        else:
            # Concatenate root lists
            self.min_node.right.left = other.min_node.left
            other.min_node.left.right = self.min_node.right
            self.min_node.right = other.min_node
            other.min_node.left = self.min_node
            
            # Update minimum
            if other.min_node.key < self.min_node.key:
                self.min_node = other.min_node
        
        self.size += other.size
        self.num_trees += other.num_trees
        self.num_marked += other.num_marked
        
        # Clear other heap
        other.min_node = None
        other.size = 0
        other.num_trees = 0
        other.num_marked = 0
    
    def _cut(self, node: FibonacciNode, parent: FibonacciNode):
        """Cut node from parent and add to root list"""
        # Remove node from parent's child list
        if node.right == node:
            parent.child = None
        else:
            if parent.child == node:
                parent.child = node.right
            node.left.right = node.right
            node.right.left = node.left
        
        parent.degree -= 1
        
        # Add node to root list
        self._add_to_root_list(node)
        node.parent = None
        node.marked = False
        self.num_trees += 1
        
        if node.marked:
            self.num_marked -= 1
    
    def _cascading_cut(self, node: FibonacciNode):
        """Perform cascading cut operation"""
        parent = node.parent
        
        if parent is not None:
            if not node.marked:
                node.marked = True
                self.num_marked += 1
            else:
                self._cut(node, parent)
                self._cascading_cut(parent)
    
    def decrease_key(self, node: FibonacciNode, new_key: Any):
        """
        Decrease the key of a node
        Time Complexity: O(1) amortized
        """
        if new_key > node.key:
            raise ValueError("New key is greater than current key")
        
        node.key = new_key
        parent = node.parent
        
        if parent is not None and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)
        
        if node.key < self.min_node.key:
            self.min_node = node
    
    def delete(self, node: FibonacciNode):
        """
        Delete a specific node
        Time Complexity: O(log n) amortized
        """
        self.decrease_key(node, float('-inf'))
        self.delete_min()
    
    def get_roots(self) -> List[FibonacciNode]:
        """Get list of root nodes"""
        if self.is_empty():
            return []
        
        roots = []
        current = self.min_node
        while True:
            roots.append(current)
            current = current.right
            if current == self.min_node:
                break
        
        return roots
    
    def __len__(self) -> int:
        """Return the number of elements in the heap"""
        return self.size
    
    def __repr__(self) -> str:
        if self.is_empty():
            return "FibonacciHeap(empty)"
        
        roots = self.get_roots()
        root_info = [f"Tree(root={root.key}, deg={root.degree})" for root in roots]
        return f"FibonacciHeap(trees={len(roots)}, size={self.size}, min={self.min_node.key})"


# Example usage and testing
if __name__ == "__main__":
    print("=== Fibonacci Heap Demo ===\n")
    
    # Create heap and insert elements
    heap = FibonacciHeap()
    print("Inserting: 10, 5, 20, 15, 30, 25, 8, 12")
    nodes = {}
    for key in [10, 5, 20, 15, 30, 25, 8, 12]:
        nodes[key] = heap.insert(key)
        print(f"After inserting {key}: {heap}")
    
    print(f"\nMinimum: {heap.find_min()}")
    print(f"Heap size: {len(heap)}")
    print(f"Number of trees: {heap.num_trees}")
    
    # Delete minimum (triggers consolidation)
    print(f"\nDeleting minimum: {heap.delete_min()}")
    print(f"After delete: {heap}")
    print(f"New minimum: {heap.find_min()}")
    print(f"Number of trees after consolidation: {heap.num_trees}")
    
    # Decrease key
    print("\n=== Decrease Key Operation ===")
    print(f"Decreasing key 30 to 3")
    heap.decrease_key(nodes[30], 3)
    print(f"After decrease: {heap}")
    print(f"New minimum: {heap.find_min()}")
    
    # Merge two heaps
    print("\n=== Merge Operation ===")
    heap2 = FibonacciHeap()
    for key in [2, 7, 18]:
        heap2.insert(key)
    print(f"Heap 1: {heap}")
    print(f"Heap 2: {heap2}")
    
    heap.merge(heap2)
    print(f"After merge: {heap}")
    print(f"Minimum: {heap.find_min()}")
    
    # Demonstrate amortized O(1) insert
    print("\n=== Performance Demo: 1000 Inserts ===")
    import time
    
    perf_heap = FibonacciHeap()
    start = time.time()
    for i in range(1000):
        perf_heap.insert(i)
    end = time.time()
    
    print(f"Inserted 1000 elements in {(end-start)*1000:.2f}ms")
    print(f"Average per insert: {(end-start)*1000000/1000:.2f}μs")
    print(f"Final heap: size={len(perf_heap)}, trees={perf_heap.num_trees}")


