"""
Graph Algorithms using Advanced Heap Structures

This module demonstrates the use of Fibonacci and Binomial heaps
in classic graph algorithms like Dijkstra's shortest path and
Prim's minimum spanning tree.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from heaps.fibonacci_heap import FibonacciHeap
from heaps.binomial_heap import BinomialHeap
from typing import Dict, List, Tuple, Any
import time


def dijkstra_fibonacci(graph: Dict[str, List[Tuple[str, int]]], start: str) -> Dict[str, int]:
    """
    Dijkstra's shortest path algorithm using Fibonacci Heap
    
    Args:
        graph: Adjacency list representation {node: [(neighbor, weight), ...]}
        start: Starting node
    
    Returns:
        Dictionary of shortest distances from start to all nodes
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    heap = FibonacciHeap()
    nodes = {}
    
    # Insert all nodes into heap
    for node in graph:
        priority = 0 if node == start else float('inf')
        nodes[node] = heap.insert((priority, node))
    
    visited = set()
    
    while not heap.is_empty():
        min_dist, current = heap.delete_min()
        
        if current in visited:
            continue
        
        visited.add(current)
        
        # Update distances to neighbors
        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                new_dist = distances[current] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    # In a real implementation, we'd use decrease_key here
                    # For simplicity, we insert with new priority
                    heap.insert((new_dist, neighbor))
    
    return distances


def dijkstra_binomial(graph: Dict[str, List[Tuple[str, int]]], start: str) -> Dict[str, int]:
    """
    Dijkstra's shortest path algorithm using Binomial Heap
    
    Args:
        graph: Adjacency list representation {node: [(neighbor, weight), ...]}
        start: Starting node
    
    Returns:
        Dictionary of shortest distances from start to all nodes
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    heap = BinomialHeap()
    heap.insert((0, start))
    
    visited = set()
    
    while not heap.is_empty():
        min_dist, current = heap.delete_min()
        
        if current in visited:
            continue
        
        visited.add(current)
        
        # Update distances to neighbors
        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                new_dist = distances[current] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heap.insert((new_dist, neighbor))
    
    return distances


def prim_fibonacci(graph: Dict[str, List[Tuple[str, int]]]) -> List[Tuple[str, str, int]]:
    """
    Prim's minimum spanning tree algorithm using Fibonacci Heap
    
    Args:
        graph: Adjacency list representation {node: [(neighbor, weight), ...]}
    
    Returns:
        List of edges in MST as (node1, node2, weight)
    """
    if not graph:
        return []
    
    start = next(iter(graph))
    mst = []
    visited = set([start])
    
    heap = FibonacciHeap()
    
    # Add all edges from start node
    for neighbor, weight in graph[start]:
        heap.insert((weight, start, neighbor))
    
    while not heap.is_empty() and len(visited) < len(graph):
        weight, u, v = heap.delete_min()
        
        if v in visited:
            continue
        
        visited.add(v)
        mst.append((u, v, weight))
        
        # Add edges from newly added node
        for neighbor, edge_weight in graph[v]:
            if neighbor not in visited:
                heap.insert((edge_weight, v, neighbor))
    
    return mst


def prim_binomial(graph: Dict[str, List[Tuple[str, int]]]) -> List[Tuple[str, str, int]]:
    """
    Prim's minimum spanning tree algorithm using Binomial Heap
    
    Args:
        graph: Adjacency list representation {node: [(neighbor, weight), ...]}
    
    Returns:
        List of edges in MST as (node1, node2, weight)
    """
    if not graph:
        return []
    
    start = next(iter(graph))
    mst = []
    visited = set([start])
    
    heap = BinomialHeap()
    
    # Add all edges from start node
    for neighbor, weight in graph[start]:
        heap.insert((weight, start, neighbor))
    
    while not heap.is_empty() and len(visited) < len(graph):
        weight, u, v = heap.delete_min()
        
        if v in visited:
            continue
        
        visited.add(v)
        mst.append((u, v, weight))
        
        # Add edges from newly added node
        for neighbor, edge_weight in graph[v]:
            if neighbor not in visited:
                heap.insert((edge_weight, v, neighbor))
    
    return mst


def compare_dijkstra_performance(graph: Dict[str, List[Tuple[str, int]]], start: str):
    """Compare performance of Dijkstra's algorithm with different heaps"""
    print("\n=== Dijkstra's Algorithm Performance Comparison ===")
    
    # Fibonacci Heap
    start_time = time.time()
    distances_fib = dijkstra_fibonacci(graph, start)
    fib_time = time.time() - start_time
    
    # Binomial Heap
    start_time = time.time()
    distances_bin = dijkstra_binomial(graph, start)
    bin_time = time.time() - start_time
    
    print(f"Fibonacci Heap time: {fib_time:.6f} seconds")
    print(f"Binomial Heap time: {bin_time:.6f} seconds")
    print(f"Speedup: {bin_time/fib_time:.2f}x")
    
    return distances_fib


def compare_prim_performance(graph: Dict[str, List[Tuple[str, int]]]):
    """Compare performance of Prim's algorithm with different heaps"""
    print("\n=== Prim's Algorithm Performance Comparison ===")
    
    # Fibonacci Heap
    start_time = time.time()
    mst_fib = prim_fibonacci(graph)
    fib_time = time.time() - start_time
    
    # Binomial Heap
    start_time = time.time()
    mst_bin = prim_binomial(graph)
    bin_time = time.time() - start_time
    
    print(f"Fibonacci Heap time: {fib_time:.6f} seconds")
    print(f"Binomial Heap time: {bin_time:.6f} seconds")
    print(f"Speedup: {bin_time/fib_time:.2f}x")
    
    total_weight = sum(weight for _, _, weight in mst_fib)
    print(f"MST total weight: {total_weight}")
    
    return mst_fib


def main():
    """Run graph algorithm examples"""
    print("=" * 60)
    print("Graph Algorithms with Advanced Heaps")
    print("=" * 60)
    
    # Example graph for Dijkstra's algorithm
    graph_dijkstra = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
        'E': [('C', 10), ('D', 2), ('F', 3)],
        'F': [('D', 6), ('E', 3)]
    }
    
    print("\nGraph for Dijkstra's Algorithm:")
    print("Nodes: A, B, C, D, E, F")
    print("Edges with weights shown in adjacency list above")
    
    # Run Dijkstra's algorithm
    distances = compare_dijkstra_performance(graph_dijkstra, 'A')
    print("\nShortest distances from A:")
    for node, dist in sorted(distances.items()):
        print(f"  {node}: {dist}")
    
    # Example graph for Prim's algorithm
    graph_prim = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 1), ('E', 4)],
        'C': [('A', 3), ('B', 1), ('F', 5)],
        'D': [('B', 1), ('E', 1)],
        'E': [('B', 4), ('D', 1), ('F', 1)],
        'F': [('C', 5), ('E', 1)]
    }
    
    print("\n\nGraph for Prim's Algorithm:")
    print("Nodes: A, B, C, D, E, F")
    print("Edges with weights shown in adjacency list above")
    
    # Run Prim's algorithm
    mst = compare_prim_performance(graph_prim)
    print("\nMinimum Spanning Tree edges:")
    for u, v, weight in mst:
        print(f"  {u} -- {v} (weight: {weight})")
    
    print("\n" + "=" * 60)
    print("Graph algorithm examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()


