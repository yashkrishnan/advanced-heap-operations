# Algorithm Design and Pseudocode

## Table of Contents
1. [Binomial Heap](#binomial-heap)
2. [Fibonacci Heap](#fibonacci-heap)
3. [Min-Max Heap](#min-max-heap)
4. [Pairing Heap](#pairing-heap)
5. [Leftist Heap](#leftist-heap)
6. [Skew Heap](#skew-heap)

---

## 1. Binomial Heap

### 1.1 Data Structure

**Binomial Tree Bk:**
- Has exactly 2^k nodes
- Root has degree k
- Children are binomial trees B0, B1, ..., Bk-1

**Binomial Heap:**
- Collection of binomial trees
- Each tree satisfies min-heap property
- At most one binomial tree of each degree

### 1.2 Node Structure
```
BinomialNode:
    key: value
    degree: integer
    parent: pointer to BinomialNode
    child: pointer to BinomialNode (leftmost child)
    sibling: pointer to BinomialNode (right sibling)
```

### 1.3 Key Operations

#### Insert Operation
```
Algorithm: INSERT(H, key)
Input: Heap H, key to insert
Output: Updated heap H

1. Create new heap H' with single node containing key
2. MERGE(H, H')
3. Update min pointer if necessary
4. Return H

Time Complexity: O(log n)
```

#### Link Trees Operation
```
Algorithm: LINK_TREES(tree1, tree2)
Input: Two binomial trees of same degree
Output: Combined tree

1. If tree1.key > tree2.key:
       Swap tree1 and tree2
2. Make tree2 a child of tree1:
       tree2.parent = tree1
       tree2.sibling = tree1.child
       tree1.child = tree2
       tree1.degree += 1
3. Return tree1

Time Complexity: O(1)
```

#### Merge Operation
```
Algorithm: MERGE(H1, H2)
Input: Two binomial heaps H1, H2
Output: Merged heap

1. Merge root lists in increasing order of degree
2. Consolidate trees of same degree:
   prev = null
   current = head
   next = current.sibling
   
   While next != null:
       Case 1: current.degree != next.degree
           → Move forward
       
       Case 2: current.degree == next.degree == next.sibling.degree
           → Move forward
       
       Case 3: current.degree == next.degree, current.key <= next.key
           → Link next under current
           → current.sibling = next.sibling
       
       Case 4: current.degree == next.degree, current.key > next.key
           → Link current under next
           → Update pointers

3. Update min pointer
4. Return merged heap

Time Complexity: O(log n)
```

#### Delete-Min Operation
```
Algorithm: DELETE_MIN(H)
Input: Heap H
Output: Minimum key, updated heap

1. Find minimum node in root list
2. Remove minimum from root list
3. Create new heap H' from children of minimum
4. Reverse child list of minimum
5. MERGE(H, H')
6. Return minimum key

Time Complexity: O(log n)
```

### 1.4 Flowchart: Insert Operation

```
┌─────────────────┐
│  Start Insert   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Create new node │
│  with key value │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Create heap H'  │
│ with single node│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  MERGE(H, H')   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Update min ptr  │
│  if necessary   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Return heap   │
└─────────────────┘
```

---

## 2. Fibonacci Heap

### 2.1 Data Structure

**Fibonacci Heap:**
- Collection of min-heap-ordered trees
- Circular doubly-linked list at root level
- Lazy consolidation (delayed until delete-min)
- Marked nodes for cascading cuts

### 2.2 Node Structure
```
FibonacciNode:
    key: value
    degree: integer
    marked: boolean
    parent: pointer to FibonacciNode
    child: pointer to FibonacciNode
    left: pointer to FibonacciNode (circular)
    right: pointer to FibonacciNode (circular)
```

### 2.3 Key Operations

#### Insert Operation
```
Algorithm: INSERT(H, key)
Input: Heap H, key to insert
Output: Updated heap, pointer to new node

1. Create new node with key
2. If H is empty:
       H.min = node
   Else:
       Add node to root list
       If key < H.min.key:
           H.min = node
3. H.size += 1
4. Return node

Time Complexity: O(1)
```

#### Decrease-Key Operation
```
Algorithm: DECREASE_KEY(H, node, new_key)
Input: Heap H, node to update, new key value
Output: Updated heap

1. If new_key > node.key:
       Error: new key is larger
2. node.key = new_key
3. parent = node.parent
4. If parent != null AND node.key < parent.key:
       CUT(H, node, parent)
       CASCADING_CUT(H, parent)
5. If node.key < H.min.key:
       H.min = node

Time Complexity: O(1) amortized
```

#### Cut Operation
```
Algorithm: CUT(H, node, parent)
Input: Heap H, node to cut, parent node
Output: Updated heap

1. Remove node from parent's child list
2. parent.degree -= 1
3. Add node to root list
4. node.parent = null
5. node.marked = false

Time Complexity: O(1)
```

#### Cascading Cut Operation
```
Algorithm: CASCADING_CUT(H, node)
Input: Heap H, node to check
Output: Updated heap

1. parent = node.parent
2. If parent != null:
       If node.marked == false:
           node.marked = true
       Else:
           CUT(H, node, parent)
           CASCADING_CUT(H, parent)

Time Complexity: O(1) amortized
```

#### Delete-Min Operation
```
Algorithm: DELETE_MIN(H)
Input: Heap H
Output: Minimum key, updated heap

1. min_node = H.min
2. If min_node.child != null:
       Add all children to root list
       Clear parent pointers
3. Remove min_node from root list
4. If min_node == min_node.right:
       H.min = null
   Else:
       H.min = min_node.right
       CONSOLIDATE(H)
5. H.size -= 1
6. Return min_node.key

Time Complexity: O(log n) amortized
```

#### Consolidate Operation
```
Algorithm: CONSOLIDATE(H)
Input: Heap H
Output: Consolidated heap

1. max_degree = floor(log2(H.size)) + 1
2. Create array A[0..max_degree] initialized to null
3. For each root node in root list:
       degree = node.degree
       While A[degree] != null:
           other = A[degree]
           If node.key > other.key:
               Swap node and other
           LINK(other, node)
           A[degree] = null
           degree += 1
       A[degree] = node
4. Rebuild root list from A
5. Find new minimum

Time Complexity: O(log n) amortized
```

### 2.4 Flowchart: Decrease-Key Operation

```
┌──────────────────┐
│ Start Decrease   │
│      Key         │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Validate new_key │
│  < current key   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Update node.key  │
│  = new_key       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Has parent AND   │◄─────────┐
│ violates heap?   │          │
└────┬────────┬────┘          │
     │Yes     │No             │
     ▼        │               │
┌──────────┐  │               │
│   CUT    │  │               │
│  node    │  │               │
└────┬─────┘  │               │
     │        │               │
     ▼        │               │
┌──────────┐  │               │
│ CASCADING│  │               │
│   CUT    │──┘               │
│  parent  │                  │
└──────────┘                  │
     │                        │
     └────────────────────────┘
         │
         ▼
┌──────────────────┐
│ Update min ptr   │
│  if necessary    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│      Done        │
└──────────────────┘
```

---

## 3. Min-Max Heap

### 3.1 Data Structure

**Min-Max Heap:**
- Complete binary tree (array-based)
- Even levels (0, 2, 4, ...) are min levels
- Odd levels (1, 3, 5, ...) are max levels
- Root is always minimum
- Children of root are on max level

### 3.2 Level Determination
```
Algorithm: IS_MIN_LEVEL(index)
Input: Array index
Output: Boolean

1. level = floor(log2(index + 1))
2. Return (level % 2 == 0)

Time Complexity: O(1)
```

### 3.3 Key Operations

#### Insert Operation
```
Algorithm: INSERT(H, key)
Input: Heap H (array), key to insert
Output: Updated heap

1. Append key to end of array
2. index = H.size - 1
3. BUBBLE_UP(H, index)

Time Complexity: O(log n)
```

#### Bubble-Up Operation
```
Algorithm: BUBBLE_UP(H, index)
Input: Heap H, index of element
Output: Updated heap

1. If index == 0:
       Return
2. parent = (index - 1) / 2
3. If IS_MIN_LEVEL(index):
       If H[index] > H[parent]:
           Swap H[index] and H[parent]
           BUBBLE_UP_MAX(H, parent)
       Else:
           BUBBLE_UP_MIN(H, index)
   Else:  // Max level
       If H[index] < H[parent]:
           Swap H[index] and H[parent]
           BUBBLE_UP_MIN(H, parent)
       Else:
           BUBBLE_UP_MAX(H, index)

Time Complexity: O(log n)
```

#### Bubble-Up-Min Operation
```
Algorithm: BUBBLE_UP_MIN(H, index)
Input: Heap H, index on min level
Output: Updated heap

1. While index has grandparent:
       grandparent = parent of parent of index
       If H[index] < H[grandparent]:
           Swap H[index] and H[grandparent]
           index = grandparent
       Else:
           Break

Time Complexity: O(log n)
```

#### Delete-Min Operation
```
Algorithm: DELETE_MIN(H)
Input: Heap H
Output: Minimum value, updated heap

1. If H is empty:
       Error
2. min_val = H[0]
3. H[0] = H[H.size - 1]
4. H.size -= 1
5. TRICKLE_DOWN(H, 0)
6. Return min_val

Time Complexity: O(log n)
```

#### Trickle-Down-Min Operation
```
Algorithm: TRICKLE_DOWN_MIN(H, index)
Input: Heap H, index on min level
Output: Updated heap

1. While index has children:
       m = index of smallest among children and grandchildren
       If H[m] < H[index]:
           Swap H[m] and H[index]
           If m is grandchild:
               parent_m = parent of m
               If H[m] > H[parent_m]:
                   Swap H[m] and H[parent_m]
               index = m
           Else:
               Break
       Else:
           Break

Time Complexity: O(log n)
```

### 3.4 Flowchart: Insert Operation

```
┌──────────────────┐
│  Start Insert    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Append key to    │
│  end of array    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ index = size - 1 │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Is min level?   │
└────┬────────┬────┘
     │Yes     │No
     ▼        ▼
┌─────────┐ ┌─────────┐
│ Compare │ │ Compare │
│  with   │ │  with   │
│ parent  │ │ parent  │
└────┬────┘ └────┬────┘
     │           │
     ▼           ▼
┌─────────┐ ┌─────────┐
│ Bubble  │ │ Bubble  │
│Up Min or│ │Up Max or│
│Up Max   │ │Up Min   │
└────┬────┘ └────┬────┘
     │           │
     └─────┬─────┘
           │
           ▼
     ┌──────────┐
     │   Done   │
     └──────────┘
```

---

## 4. Pairing Heap

### 4.1 Data Structure

**Pairing Heap:**
- Multiway tree (nodes can have any number of children)
- Min-heap ordered
- Simple structure with excellent practical performance

### 4.2 Node Structure
```
PairingNode:
    key: value
    child: pointer to PairingNode (leftmost child)
    sibling: pointer to PairingNode (right sibling)
    parent: pointer to PairingNode
```

### 4.3 Key Operations

#### Meld Operation
```
Algorithm: MELD(heap1, heap2)
Input: Two pairing heap roots
Output: Merged heap root

1. If heap1 is null:
       Return heap2
2. If heap2 is null:
       Return heap1
3. If heap1.key <= heap2.key:
       heap2.sibling = heap1.child
       heap1.child = heap2
       heap2.parent = heap1
       Return heap1
   Else:
       heap1.sibling = heap2.child
       heap2.child = heap1
       heap1.parent = heap2
       Return heap2

Time Complexity: O(1)
```

#### Insert Operation
```
Algorithm: INSERT(H, key)
Input: Heap H, key to insert
Output: Updated heap, new node

1. Create new node with key
2. H.root = MELD(H.root, node)
3. H.size += 1
4. Return node

Time Complexity: O(1)
```

#### Delete-Min Operation
```
Algorithm: DELETE_MIN(H)
Input: Heap H
Output: Minimum key, updated heap

1. min_key = H.root.key
2. If H.root.child != null:
       H.root = TWO_PASS_MERGE(H.root.child)
   Else:
       H.root = null
3. H.size -= 1
4. Return min_key

Time Complexity: O(log n) amortized
```

#### Two-Pass Merge Operation
```
Algorithm: TWO_PASS_MERGE(node)
Input: First sibling in list
Output: Merged tree

1. If node is null or node.sibling is null:
       Return node

2. // First pass: pair up siblings left to right
   pairs = []
   current = node
   While current != null:
       first = current
       second = current.sibling
       If second is null:
           pairs.append(first)
           Break
       current = second.sibling
       first.sibling = null
       second.sibling = null
       pairs.append(MELD(first, second))

3. // Second pass: merge pairs right to left
   result = pairs[last]
   For i from (pairs.length - 2) down to 0:
       result = MELD(pairs[i], result)

4. Return result

Time Complexity: O(log n) amortized
```

### 4.4 Flowchart: Two-Pass Merge

```
┌──────────────────┐
│ Start Two-Pass   │
│      Merge       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  First Pass:     │
│  Pair siblings   │
│  left to right   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Take two siblings│
│  at a time       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  MELD the pair   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Store in pairs[] │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ More siblings?   │
└────┬────────┬────┘
     │Yes     │No
     │        │
     └────┐   │
          │   │
          ▼   ▼
┌──────────────────┐
│  Second Pass:    │
│  Merge pairs     │
│  right to left   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Return merged    │
│      tree        │
└──────────────────┘
```

---

## 5. Leftist Heap

### 5.1 Data Structure

**Leftist Heap:**
- Binary tree with leftist property
- NPL(left child) >= NPL(right child)
- Right path is always short

**Null Path Length (NPL):**
- NPL of null = -1
- NPL of leaf = 0
- NPL of node = min(NPL(left), NPL(right)) + 1

### 5.2 Node Structure
```
LeftistNode:
    key: value
    npl: integer (null path length)
    left: pointer to LeftistNode
    right: pointer to LeftistNode
```

### 5.3 Key Operations

#### Merge Operation
```
Algorithm: MERGE(heap1, heap2)
Input: Two leftist heap roots
Output: Merged heap root

1. If heap1 is null:
       Return heap2
2. If heap2 is null:
       Return heap1
3. If heap1.key > heap2.key:
       Swap heap1 and heap2
4. heap1.right = MERGE(heap1.right, heap2)
5. If NPL(heap1.left) < NPL(heap1.right):
       Swap heap1.left and heap1.right
6. heap1.npl = NPL(heap1.right) + 1
7. Return heap1

Time Complexity: O(log n)
```

#### Insert Operation
```
Algorithm: INSERT(H, key)
Input: Heap H, key to insert
Output: Updated heap

1. Create new node with key
2. H.root = MERGE(H.root, node)
3. H.size += 1

Time Complexity: O(log n)
```

#### Delete-Min Operation
```
Algorithm: DELETE_MIN(H)
Input: Heap H
Output: Minimum key, updated heap

1. min_key = H.root.key
2. H.root = MERGE(H.root.left, H.root.right)
3. H.size -= 1
4. Return min_key

Time Complexity: O(log n)
```

### 5.4 Flowchart: Merge Operation

```
┌──────────────────┐
│  Start Merge     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Either heap null?│
└────┬────────┬────┘
     │Yes     │No
     ▼        │
┌─────────┐   │
│ Return  │   │
│ other   │   │
└─────────┘   │
              ▼
┌──────────────────┐
│ Ensure heap1 has │
│  smaller root    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Recursively merge│
│ heap2 with right │
│ subtree of heap1 │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ NPL(left) <      │
│ NPL(right)?      │
└────┬────────┬────┘
     │Yes     │No
     ▼        │
┌─────────┐   │
│  Swap   │   │
│ left &  │   │
│ right   │   │
└────┬────┘   │
     │        │
     └────┬───┘
          │
          ▼
┌──────────────────┐
│  Update NPL      │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Return merged    │
│      tree        │
└──────────────────┘
```

---

## 6. Skew Heap

### 6.1 Data Structure

**Skew Heap:**
- Self-adjusting binary tree
- No explicit balance information (no NPL)
- Unconditional swapping during merge

### 6.2 Node Structure
```
SkewNode:
    key: value
    left: pointer to SkewNode
    right: pointer to SkewNode
```

### 6.3 Key Operations

#### Merge Operation
```
Algorithm: MERGE(heap1, heap2)
Input: Two skew heap roots
Output: Merged heap root

1. If heap1 is null:
       Return heap2
2. If heap2 is null:
       Return heap1
3. If heap1.key > heap2.key:
       Swap heap1 and heap2
4. heap1.right = MERGE(heap1.right, heap2)
5. // UNCONDITIONALLY swap left and right
   Swap heap1.left and heap1.right
6. Return heap1

Time Complexity: O(log n) amortized
```

#### Insert Operation
```
Algorithm: INSERT(H, key)
Input: Heap H, key to insert
Output: Updated heap

1. Create new node with key
2. H.root = MERGE(H.root, node)
3. H.size += 1

Time Complexity: O(log n) amortized
```

#### Delete-Min Operation
```
Algorithm: DELETE_MIN(H)
Input: Heap H
Output: Minimum key, updated heap

1. min_key = H.root.key
2. H.root = MERGE(H.root.left, H.root.right)
3. H.size -= 1
4. Return min_key

Time Complexity: O(log n) amortized
```

### 6.4 Comparison: Leftist vs Skew Heap

```
┌─────────────────────────────────────────────────────┐
│              Leftist Heap vs Skew Heap              │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Leftist Heap:                                      │
│  ┌──────────┐                                       │
│  │   Node   │                                       │
│  ├──────────┤                                       │
│  │   key    │                                       │
│  │   npl    │ ← Maintains NPL                       │
│  │   left   │                                       │
│  │   right  │                                       │
│  └──────────┘                                       │
│       │                                             │
│       ▼                                             │
│  Swap if NPL(left) < NPL(right)                     │
│                                                     │
│  Skew Heap:                                         │
│  ┌──────────┐                                       │
│  │   Node   │                                       │
│  ├──────────┤                                       │
│  │   key    │                                       │
│  │   left   │ ← No NPL needed                       │
│  │   right  │                                       │
│  └──────────┘                                       │
│       │                                             │
│       ▼                                             │
│  ALWAYS swap left and right                         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## Summary of Algorithmic Approaches

### Merge-Based Heaps (Binomial, Fibonacci, Pairing, Leftist, Skew)
- Core operation: Efficient merging
- Insert = Create single-node heap + Merge
- Delete-Min = Remove root + Merge children

### Array-Based Heap (Min-Max)
- Core operation: Bubble-up and Trickle-down
- Maintains complete binary tree property
- Level-based min/max alternation

### Lazy vs Eager Consolidation
- **Lazy** (Fibonacci, Pairing): Delay consolidation until delete-min
- **Eager** (Binomial, Leftist, Skew): Consolidate immediately

### Balance Maintenance
- **Explicit** (Binomial: degree, Leftist: NPL, Fibonacci: marked nodes)
- **Implicit** (Skew: self-adjusting, Min-Max: complete tree)
- **None** (Pairing: relies on amortized analysis)