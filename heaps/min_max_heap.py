"""
Min-Max Heap Implementation

A min-max heap is a complete binary tree where:
- Even levels (0, 2, 4, ...) are min levels
- Odd levels (1, 3, 5, ...) are max levels
- Root is always the minimum element
- Children of root are in a max level

Time Complexities:
- Insert: O(log n)
- Find-Min: O(1)
- Find-Max: O(1)
- Delete-Min: O(log n)
- Delete-Max: O(log n)

Key Properties:
1. Acts as a double-ended priority queue
2. Efficient access to both minimum and maximum
3. Complete binary tree structure (array-based)
4. Alternating min/max levels

Applications:
- Double-ended priority queues
- Range queries
- Simulation systems requiring both min and max
"""

from typing import Any, List, Optional
import math


class MinMaxHeap:
    """
    Min-Max Heap implementation using array representation
    
    Provides O(1) access to both minimum and maximum elements.
    """
    
    def __init__(self):
        self.heap: List[Any] = []
    
    def is_empty(self) -> bool:
        """Check if heap is empty"""
        return len(self.heap) == 0
    
    def _parent(self, i: int) -> int:
        """Get parent index"""
        return (i - 1) // 2
    
    def _left_child(self, i: int) -> int:
        """Get left child index"""
        return 2 * i + 1
    
    def _right_child(self, i: int) -> int:
        """Get right child index"""
        return 2 * i + 2
    
    def _level(self, i: int) -> int:
        """Get level of node at index i (0-indexed)"""
        return int(math.log2(i + 1)) if i >= 0 else 0
    
    def _is_min_level(self, i: int) -> bool:
        """Check if index i is on a min level"""
        return self._level(i) % 2 == 0
    
    def _is_max_level(self, i: int) -> bool:
        """Check if index i is on a max level"""
        return self._level(i) % 2 == 1
    
    def _has_children(self, i: int) -> bool:
        """Check if node has children"""
        return self._left_child(i) < len(self.heap)
    
    def _get_children_and_grandchildren(self, i: int) -> List[int]:
        """Get indices of all children and grandchildren"""
        indices = []
        left = self._left_child(i)
        right = self._right_child(i)
        
        # Add children
        if left < len(self.heap):
            indices.append(left)
        if right < len(self.heap):
            indices.append(right)
        
        # Add grandchildren
        for child in [left, right]:
            if child < len(self.heap):
                gc_left = self._left_child(child)
                gc_right = self._right_child(child)
                if gc_left < len(self.heap):
                    indices.append(gc_left)
                if gc_right < len(self.heap):
                    indices.append(gc_right)
        
        return indices
    
    def find_min(self) -> Any:
        """
        Find the minimum element (at root)
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        return self.heap[0]
    
    def find_max(self) -> Any:
        """
        Find the maximum element (one of root's children)
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        
        if len(self.heap) == 1:
            return self.heap[0]
        elif len(self.heap) == 2:
            return self.heap[1]
        else:
            return max(self.heap[1], self.heap[2])
    
    def _find_max_index(self) -> int:
        """Find index of maximum element"""
        if len(self.heap) == 1:
            return 0
        elif len(self.heap) == 2:
            return 1
        else:
            return 1 if self.heap[1] > self.heap[2] else 2
    
    def insert(self, key: Any):
        """
        Insert a new key into the heap
        Time Complexity: O(log n)
        """
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)
    
    def _bubble_up(self, i: int):
        """Bubble up element at index i to maintain heap property"""
        if i == 0:
            return
        
        parent = self._parent(i)
        
        if self._is_min_level(i):
            # On min level
            if self.heap[i] > self.heap[parent]:
                # Violates min level property, swap and bubble up on max levels
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                self._bubble_up_max(parent)
            else:
                self._bubble_up_min(i)
        else:
            # On max level
            if self.heap[i] < self.heap[parent]:
                # Violates max level property, swap and bubble up on min levels
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                self._bubble_up_min(parent)
            else:
                self._bubble_up_max(i)
    
    def _bubble_up_min(self, i: int):
        """Bubble up on min levels"""
        while i > 2:  # Has grandparent
            grandparent = self._parent(self._parent(i))
            if self.heap[i] < self.heap[grandparent]:
                self.heap[i], self.heap[grandparent] = self.heap[grandparent], self.heap[i]
                i = grandparent
            else:
                break
    
    def _bubble_up_max(self, i: int):
        """Bubble up on max levels"""
        while i > 2:  # Has grandparent
            grandparent = self._parent(self._parent(i))
            if self.heap[i] > self.heap[grandparent]:
                self.heap[i], self.heap[grandparent] = self.heap[grandparent], self.heap[i]
                i = grandparent
            else:
                break
    
    def delete_min(self) -> Any:
        """
        Delete and return the minimum element
        Time Complexity: O(log n)
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        
        min_val = self.heap[0]
        
        if len(self.heap) == 1:
            self.heap.pop()
            return min_val
        
        # Move last element to root and trickle down
        self.heap[0] = self.heap.pop()
        self._trickle_down(0)
        
        return min_val
    
    def delete_max(self) -> Any:
        """
        Delete and return the maximum element
        Time Complexity: O(log n)
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_idx = self._find_max_index()
        max_val = self.heap[max_idx]
        
        if max_idx == len(self.heap) - 1:
            self.heap.pop()
            return max_val
        
        # Move last element to max position and trickle down
        self.heap[max_idx] = self.heap.pop()
        self._trickle_down(max_idx)
        
        return max_val
    
    def _trickle_down(self, i: int):
        """Trickle down element at index i"""
        if self._is_min_level(i):
            self._trickle_down_min(i)
        else:
            self._trickle_down_max(i)
    
    def _trickle_down_min(self, i: int):
        """Trickle down on min level"""
        while self._has_children(i):
            # Find smallest among children and grandchildren
            indices = self._get_children_and_grandchildren(i)
            m = min(indices, key=lambda idx: self.heap[idx])
            
            if self.heap[m] < self.heap[i]:
                self.heap[i], self.heap[m] = self.heap[m], self.heap[i]
                
                # Check if m is a grandchild
                if m > self._right_child(i):
                    # m is a grandchild
                    parent_m = self._parent(m)
                    if self.heap[m] > self.heap[parent_m]:
                        self.heap[m], self.heap[parent_m] = self.heap[parent_m], self.heap[m]
                    i = m
                else:
                    # m is a child, done
                    break
            else:
                break
    
    def _trickle_down_max(self, i: int):
        """Trickle down on max level"""
        while self._has_children(i):
            # Find largest among children and grandchildren
            indices = self._get_children_and_grandchildren(i)
            m = max(indices, key=lambda idx: self.heap[idx])
            
            if self.heap[m] > self.heap[i]:
                self.heap[i], self.heap[m] = self.heap[m], self.heap[i]
                
                # Check if m is a grandchild
                if m > self._right_child(i):
                    # m is a grandchild
                    parent_m = self._parent(m)
                    if self.heap[m] < self.heap[parent_m]:
                        self.heap[m], self.heap[parent_m] = self.heap[parent_m], self.heap[m]
                    i = m
                else:
                    # m is a child, done
                    break
            else:
                break
    
    def __len__(self) -> int:
        """Return the number of elements in the heap"""
        return len(self.heap)
    
    def __repr__(self) -> str:
        if self.is_empty():
            return "MinMaxHeap(empty)"
        
        min_val = self.find_min()
        max_val = self.find_max()
        return f"MinMaxHeap(size={len(self)}, min={min_val}, max={max_val})"


# Example usage and testing
if __name__ == "__main__":
    print("=== Min-Max Heap Demo ===\n")
    
    # Create heap and insert elements
    heap = MinMaxHeap()
    print("Inserting: 10, 5, 20, 15, 30, 25, 8, 12, 40, 3")
    for key in [10, 5, 20, 15, 30, 25, 8, 12, 40, 3]:
        heap.insert(key)
        print(f"After inserting {key}: min={heap.find_min()}, max={heap.find_max()}")
    
    print(f"\n{heap}")
    print(f"Heap array: {heap.heap}")
    print(f"Heap size: {len(heap)}")
    
    # Access both extremes
    print(f"\nMinimum: {heap.find_min()}")
    print(f"Maximum: {heap.find_max()}")
    
    # Delete minimum
    print(f"\nDeleting minimum: {heap.delete_min()}")
    print(f"After delete min: {heap}")
    print(f"New minimum: {heap.find_min()}")
    
    # Delete maximum
    print(f"\nDeleting maximum: {heap.delete_max()}")
    print(f"After delete max: {heap}")
    print(f"New maximum: {heap.find_max()}")
    
    # Demonstrate double-ended priority queue
    print("\n=== Double-Ended Priority Queue Demo ===")
    deque = MinMaxHeap()
    
    print("Building heap with: 50, 30, 70, 20, 40, 60, 80")
    for val in [50, 30, 70, 20, 40, 60, 80]:
        deque.insert(val)
    
    print(f"Heap: {deque}")
    print(f"Range: [{deque.find_min()}, {deque.find_max()}]")
    
    print("\nExtracting min and max alternately:")
    count = 0
    while len(deque) > 0:
        if len(deque) == 1:
            print(f"  Last element: {deque.delete_min()}")
        else:
            if count % 2 == 0:
                val = deque.delete_min()
                print(f"  Extracted min={val}, remaining: {deque}")
            else:
                val = deque.delete_max()
                print(f"  Extracted max={val}, remaining: {deque}")
            count += 1


