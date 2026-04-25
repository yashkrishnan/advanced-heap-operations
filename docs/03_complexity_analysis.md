# Complexity Analysis

## Table of Contents
1. [Overview](#overview)
2. [Time Complexity Analysis](#time-complexity-analysis)
3. [Space Complexity Analysis](#space-complexity-analysis)
4. [Amortized Analysis](#amortized-analysis)
5. [Comparative Analysis](#comparative-analysis)

---

## 1. Overview

This document provides detailed complexity analysis for all six heap implementations:
- Binomial Heap
- Fibonacci Heap
- Min-Max Heap
- Pairing Heap
- Leftist Heap
- Skew Heap

### 1.1 Notation
- **n**: Number of elements in the heap
- **O(f(n))**: Big-O notation (upper bound)
- **Ω(f(n))**: Big-Omega notation (lower bound)
- **Θ(f(n))**: Big-Theta notation (tight bound)
- **Amortized**: Average cost per operation over a sequence

---

## 2. Time Complexity Analysis

### 2.1 Complete Complexity Table

| Operation | Binomial | Fibonacci | Min-Max | Pairing | Leftist | Skew |
|-----------|----------|-----------|---------|---------|---------|------|
| **Insert** | O(log n) | **O(1)*** | O(log n) | **O(1)*** | O(log n) | O(log n)* |
| **Find-Min** | O(log n) or **O(1)** | **O(1)** | **O(1)** | **O(1)** | **O(1)** | **O(1)** |
| **Find-Max** | - | - | **O(1)** | - | - | - |
| **Delete-Min** | O(log n) | O(log n)* | O(log n) | O(log n)* | O(log n) | O(log n)* |
| **Delete-Max** | - | - | O(log n) | - | - | - |
| **Decrease-Key** | O(log n) | **O(1)*** | O(log n) | O(log n)* | - | - |
| **Delete** | O(log n) | O(log n)* | - | O(log n)* | - | - |
| **Merge** | O(log n) | **O(1)*** | O(n) | **O(1)*** | O(log n) | O(log n)* |

*Amortized time complexity

### 2.2 Binomial Heap

#### 2.2.1 Insert Operation
**Time Complexity: O(log n)**

**Analysis:**
```
Insert(H, key):
    1. Create single-node heap H'        O(1)
    2. Merge H and H'                    O(log n)
    Total:                               O(log n)
```

**Detailed Breakdown:**
- Creating new heap: O(1)
- Merging root lists: O(log n) - at most log n + 1 trees
- Consolidating trees: O(log n) - at most log n + 1 iterations
- **Total: O(log n)**

#### 2.2.2 Find-Min Operation
**Time Complexity: O(log n) or O(1) with min pointer**

**Analysis:**
- Without min pointer: Scan root list of at most log n + 1 trees → O(log n)
- With min pointer: Direct access → O(1)

#### 2.2.3 Delete-Min Operation
**Time Complexity: O(log n)**

**Analysis:**
```
Delete-Min(H):
    1. Find minimum in root list         O(log n) or O(1)
    2. Remove from root list             O(1)
    3. Reverse children list             O(log n)
    4. Merge with main heap              O(log n)
    Total:                               O(log n)
```

#### 2.2.4 Merge Operation
**Time Complexity: O(log n)**

**Analysis:**
- Merge root lists: O(log n)
- Consolidate trees: O(log n)
- At most 2 log n + 2 trees initially
- After consolidation: at most log n + 1 trees
- **Total: O(log n)**

**Proof:**
Let n₁ and n₂ be sizes of heaps being merged.
- Number of trees in H₁: ≤ log₂(n₁) + 1
- Number of trees in H₂: ≤ log₂(n₂) + 1
- After merge: ≤ log₂(n₁ + n₂) + 1
- Consolidation processes each degree once: O(log(n₁ + n₂))

### 2.3 Fibonacci Heap

#### 2.3.1 Insert Operation
**Time Complexity: O(1) amortized**

**Analysis:**
```
Insert(H, key):
    1. Create new node                   O(1)
    2. Add to root list                  O(1)
    3. Update min pointer if needed      O(1)
    Total:                               O(1)
```

**Amortized Analysis:**
- Actual cost: O(1)
- Potential increase: O(1) (one more tree)
- Amortized cost: O(1) + O(1) = O(1)

#### 2.3.2 Decrease-Key Operation
**Time Complexity: O(1) amortized**

**Analysis:**
```
Decrease-Key(H, node, new_key):
    1. Update key                        O(1)
    2. Cut if violates heap property     O(1)
    3. Cascading cut                     O(c) where c = cuts
    Total:                               O(c)
```

**Amortized Analysis using Potential Method:**

**Potential Function:** Φ(H) = t(H) + 2m(H)
- t(H) = number of trees
- m(H) = number of marked nodes

**For Decrease-Key with c cascading cuts:**
- Actual cost: O(c)
- Potential change: ΔΦ = (c - 1) - 2(c - 1) = -(c - 1)
- Amortized cost: O(c) + (-(c - 1)) = O(1)

#### 2.3.3 Delete-Min Operation
**Time Complexity: O(log n) amortized**

**Analysis:**
```
Delete-Min(H):
    1. Remove min node                   O(1)
    2. Add children to root list         O(D(n))
    3. Consolidate                       O(D(n) + t(H))
    Total:                               O(D(n) + t(H))
```

Where D(n) = maximum degree = O(log n)

**Amortized Analysis:**
- Actual cost: O(D(n) + t(H))
- Potential before: Φ = t(H) + 2m(H)
- Potential after: Φ' ≤ D(n) + 1 (at most D(n) + 1 trees after consolidation)
- ΔΦ = Φ' - Φ ≤ D(n) + 1 - t(H)
- Amortized cost: O(D(n) + t(H)) + (D(n) + 1 - t(H)) = O(D(n)) = O(log n)

#### 2.3.4 Merge Operation
**Time Complexity: O(1)**

**Analysis:**
- Concatenate root lists: O(1)
- Update min pointer: O(1)
- No consolidation needed
- **Total: O(1)**

### 2.4 Min-Max Heap

#### 2.4.1 Insert Operation
**Time Complexity: O(log n)**

**Analysis:**
```
Insert(H, key):
    1. Append to array                   O(1)
    2. Bubble-up                         O(log n)
    Total:                               O(log n)
```

**Bubble-up Analysis:**
- At most log n levels
- Each level: O(1) comparison and swap
- **Total: O(log n)**

#### 2.4.2 Find-Min and Find-Max Operations
**Time Complexity: O(1)**

**Analysis:**
- Find-Min: Root is always minimum → O(1)
- Find-Max: Check at most 2 children of root → O(1)

#### 2.4.3 Delete-Min and Delete-Max Operations
**Time Complexity: O(log n)**

**Analysis:**
```
Delete-Min(H):
    1. Save root value                   O(1)
    2. Move last element to root         O(1)
    3. Trickle-down                      O(log n)
    Total:                               O(log n)
```

**Trickle-down Analysis:**
- At most log n levels
- Each level: Check children and grandchildren (at most 6 nodes)
- Each level: O(1) operations
- **Total: O(log n)**

#### 2.4.4 Merge Operation
**Time Complexity: O(n)**

**Analysis:**
- Must rebuild heap from combined elements
- Heapify: O(n)
- **Not efficient for merging**

### 2.5 Pairing Heap

#### 2.5.1 Insert Operation
**Time Complexity: O(1)**

**Analysis:**
- Create new node: O(1)
- Meld with root: O(1)
- **Total: O(1)**

#### 2.5.2 Delete-Min Operation
**Time Complexity: O(log n) amortized**

**Analysis:**
```
Delete-Min(H):
    1. Remove root                       O(1)
    2. Two-pass merge of children        O(log n) amortized
    Total:                               O(log n) amortized
```

**Two-Pass Merge Analysis:**
- First pass: Pair up siblings → O(k) where k = number of children
- Second pass: Merge pairs → O(k)
- Amortized analysis shows k = O(log n)
- **Total: O(log n) amortized**

#### 2.5.3 Decrease-Key Operation
**Time Complexity: O(log n) amortized, often O(1) in practice**

**Analysis:**
- Cut node from parent: O(1)
- Meld with root: O(1)
- Amortized analysis: O(log n)
- **Practical performance: Often O(1)**

#### 2.5.4 Merge Operation
**Time Complexity: O(1)**

**Analysis:**
- Meld two roots: O(1)
- No consolidation needed
- **Total: O(1)**

### 2.6 Leftist Heap

#### 2.6.1 Merge Operation
**Time Complexity: O(log n)**

**Analysis:**
```
Merge(H1, H2):
    Recursion depth = length of right path
    Right path length ≤ log₂(n + 1)
    Each recursive call: O(1)
    Total: O(log n)
```

**Proof of Right Path Length:**
- Let r(x) = length of right path from node x
- Leftist property: npl(left) ≥ npl(right)
- A node with npl = k has at least 2^(k+1) - 1 nodes
- Therefore: npl(root) ≤ log₂(n + 1)
- Right path length ≤ npl(root) + 1 ≤ log₂(n + 1) + 1
- **Right path = O(log n)**

#### 2.6.2 Insert Operation
**Time Complexity: O(log n)**

**Analysis:**
- Create single-node heap: O(1)
- Merge with main heap: O(log n)
- **Total: O(log n)**

#### 2.6.3 Delete-Min Operation
**Time Complexity: O(log n)**

**Analysis:**
- Remove root: O(1)
- Merge left and right subtrees: O(log n)
- **Total: O(log n)**

### 2.7 Skew Heap

#### 2.7.1 Merge Operation
**Time Complexity: O(log n) amortized**

**Analysis using Heavy/Light Nodes:**

**Definitions:**
- Heavy node: right subtree has more than half the nodes
- Light node: right subtree has at most half the nodes

**Key Observations:**
1. At most log n light nodes on any path from root to leaf
2. Heavy nodes become light after swap
3. Amortized cost per merge: O(log n)

**Potential Function:** Φ(H) = number of heavy nodes

**Amortized Analysis:**
- Actual cost: O(h + l) where h = heavy nodes, l = light nodes on right path
- l ≤ log n (at most log n light nodes)
- After merge: heavy nodes become light
- ΔΦ ≤ l - h
- Amortized cost: O(h + l) + (l - h) = O(l) = O(log n)

#### 2.7.2 Insert Operation
**Time Complexity: O(log n) amortized**

**Analysis:**
- Create single-node heap: O(1)
- Merge: O(log n) amortized
- **Total: O(log n) amortized**

#### 2.7.3 Delete-Min Operation
**Time Complexity: O(log n) amortized**

**Analysis:**
- Remove root: O(1)
- Merge subtrees: O(log n) amortized
- **Total: O(log n) amortized**

---

## 3. Space Complexity Analysis

### 3.1 Space Complexity Table

| Heap Type | Space per Node | Total Space | Auxiliary Space |
|-----------|----------------|-------------|-----------------|
| Binomial | 4 pointers + key + degree | O(n) | O(log n) for merge |
| Fibonacci | 5 pointers + key + degree + marked | O(n) | O(log n) for consolidate |
| Min-Max | key only (array) | O(n) | O(1) |
| Pairing | 3 pointers + key | O(n) | O(log n) for two-pass |
| Leftist | 2 pointers + key + npl | O(n) | O(log n) for merge |
| Skew | 2 pointers + key | O(n) | O(log n) for merge |

### 3.2 Detailed Analysis

#### 3.2.1 Binomial Heap
**Space per Node:**
```
struct BinomialNode {
    key: value           // 4-8 bytes
    degree: int          // 4 bytes
    parent: pointer      // 8 bytes
    child: pointer       // 8 bytes
    sibling: pointer     // 8 bytes
}
Total: ~40 bytes per node
```

**Total Space:** O(n) for n nodes
**Auxiliary Space:** O(log n) for merge operation (recursion stack)

#### 3.2.2 Fibonacci Heap
**Space per Node:**
```
struct FibonacciNode {
    key: value           // 4-8 bytes
    degree: int          // 4 bytes
    marked: bool         // 1 byte
    parent: pointer      // 8 bytes
    child: pointer       // 8 bytes
    left: pointer        // 8 bytes
    right: pointer       // 8 bytes
}
Total: ~45 bytes per node
```

**Total Space:** O(n) for n nodes
**Auxiliary Space:** O(log n) for consolidate (degree array)

#### 3.2.3 Min-Max Heap
**Space per Node:**
```
Array element: key only  // 4-8 bytes
```

**Total Space:** O(n) for n elements
**Auxiliary Space:** O(1) - in-place operations
**Most space-efficient!**

#### 3.2.4 Pairing Heap
**Space per Node:**
```
struct PairingNode {
    key: value           // 4-8 bytes
    child: pointer       // 8 bytes
    sibling: pointer     // 8 bytes
    parent: pointer      // 8 bytes
}
Total: ~32 bytes per node
```

**Total Space:** O(n) for n nodes
**Auxiliary Space:** O(log n) for two-pass merge

#### 3.2.5 Leftist Heap
**Space per Node:**
```
struct LeftistNode {
    key: value           // 4-8 bytes
    npl: int             // 4 bytes
    left: pointer        // 8 bytes
    right: pointer       // 8 bytes
}
Total: ~28 bytes per node
```

**Total Space:** O(n) for n nodes
**Auxiliary Space:** O(log n) for merge (recursion)

#### 3.2.6 Skew Heap
**Space per Node:**
```
struct SkewNode {
    key: value           // 4-8 bytes
    left: pointer        // 8 bytes
    right: pointer       // 8 bytes
}
Total: ~24 bytes per node
```

**Total Space:** O(n) for n nodes
**Auxiliary Space:** O(log n) for merge (recursion)
**Simplest pointer-based structure!**

---

## 4. Amortized Analysis

### 4.1 Accounting Method

#### Example: Fibonacci Heap Insert

**Credit Assignment:**
- Each insert operation is charged 3 credits
- 1 credit for actual work (O(1))
- 2 credits saved for future consolidation

**Credit Usage:**
- Delete-min uses saved credits for consolidation
- Amortized cost remains O(1) for insert

### 4.2 Potential Method

#### Example: Skew Heap Merge

**Potential Function:** Φ(H) = number of heavy nodes

**For a merge operation:**
```
Actual cost: c_i = O(h_i + l_i)
Potential change: ΔΦ_i = l_i - h_i
Amortized cost: ĉ_i = c_i + ΔΦ_i
                    = O(h_i + l_i) + (l_i - h_i)
                    = O(l_i)
                    = O(log n)
```

### 4.3 Aggregate Method

#### Example: Sequence of n Operations

**Fibonacci Heap:**
- n inserts: n × O(1) = O(n)
- k delete-mins: k × O(log n) = O(k log n)
- Total: O(n + k log n)
- Average per operation: O((n + k log n) / (n + k))

---

## 5. Comparative Analysis

### 5.1 Best Use Cases by Complexity

#### When Insert Dominates:
**Winner: Fibonacci Heap or Pairing Heap**
- O(1) insert
- Best for building large heaps

#### When Merge Dominates:
**Winner: Fibonacci Heap or Pairing Heap**
- O(1) merge
- Best for union-find-like operations

#### When Decrease-Key Dominates:
**Winner: Fibonacci Heap**
- O(1) amortized decrease-key
- Best for Dijkstra's and Prim's algorithms

#### When Both Min and Max Needed:
**Winner: Min-Max Heap**
- Only heap with O(1) find-max
- Best for double-ended priority queues

#### When Simplicity Matters:
**Winner: Skew Heap**
- Simplest pointer-based implementation
- No balance information needed
- Good amortized performance

#### When Predictability Matters:
**Winner: Leftist Heap or Binomial Heap**
- Guaranteed O(log n) worst-case
- No amortized analysis needed

### 5.2 Theoretical vs Practical Performance

| Heap | Theoretical Advantage | Practical Consideration |
|------|----------------------|-------------------------|
| Fibonacci | Best amortized bounds | High constant factors, complex |
| Pairing | Simple + good amortized | Often faster than Fibonacci in practice |
| Binomial | Predictable performance | Moderate constant factors |
| Leftist | Guaranteed merge time | Simple, predictable |
| Skew | Simplest self-adjusting | Good practical performance |
| Min-Max | Double-ended operations | Best space efficiency |

### 5.3 Complexity Summary

**Fastest Operations:**
- **Insert:** Fibonacci, Pairing (O(1))
- **Find-Min:** All except Binomial (O(1))
- **Merge:** Fibonacci, Pairing (O(1))
- **Decrease-Key:** Fibonacci (O(1) amortized)

**Most Space-Efficient:**
- Min-Max Heap (array-based, no pointers)

**Most Predictable:**
- Binomial Heap, Leftist Heap (no amortized analysis)

**Best Overall (Theory):**
- Fibonacci Heap (optimal amortized bounds)

**Best Overall (Practice):**
- Pairing Heap (simple + fast in practice)

---

## 6. Lower Bounds

### 6.1 Comparison-Based Lower Bounds

**Theorem:** Any comparison-based priority queue must have:
- Ω(log n) for delete-min in worst case
- Ω(log n) for merge in worst case (for some operations)

**Proof Sketch:**
- Information-theoretic argument
- n! possible orderings
- log₂(n!) = Ω(n log n) bits of information
- Each comparison reveals 1 bit
- Therefore: Ω(log n) comparisons needed

### 6.2 Fibonacci Heap Optimality

**Theorem:** Fibonacci heap achieves optimal amortized bounds for:
- Insert: O(1)
- Decrease-key: O(1)
- Delete-min: O(log n)

**Significance:**
- These bounds are optimal for comparison-based heaps
- No comparison-based heap can do better asymptotically

---

## 7. Conclusion

### Key Takeaways:

1. **Fibonacci Heap** has best theoretical amortized complexity
2. **Pairing Heap** often performs best in practice despite weaker theoretical bounds
3. **Min-Max Heap** is unique in providing O(1) access to both min and max
4. **Leftist/Skew Heaps** provide good merge performance with simpler implementation
5. **Binomial Heap** provides predictable worst-case performance

### Complexity Trade-offs:

- **Time vs Space:** Min-Max heap is most space-efficient
- **Theory vs Practice:** Pairing heap often beats Fibonacci heap practically
- **Simplicity vs Performance:** Skew heap offers good balance
- **Worst-case vs Amortized:** Leftist heap for guaranteed bounds, Fibonacci for amortized