# Testing and Validation Guide

This document provides step-by-step instructions to run and validate all components of the Advanced Heap Operations project.

## Prerequisites

Ensure you have Python 3.7+ installed and are in the project directory:

```bash
cd ads/advanced_heap_operations
```

## Step 1: Set Up Virtual Environment (Recommended)

### Create and Activate Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows
```

**Expected Output:**
- Your prompt should now show `(venv)` prefix
- Example: `(venv) user@machine:~/ads/advanced_heap_operations$`

### Install Dependencies

```bash
# With virtual environment activated
pip install -r requirements.txt
```

**Alternative (Without Virtual Environment):**
```bash
# On macOS with Homebrew Python
pip3 install --user -r requirements.txt

# OR (not recommended)
pip3 install --break-system-packages -r requirements.txt
```

**Expected Output:**
- Installation messages for matplotlib, numpy, and other dependencies
- No error messages
- Successfully installed packages

**Validation:**
```bash
python3 -c "import matplotlib; import numpy; print('Dependencies OK')"
```

**Expected Output:**
```
Dependencies OK
```

**Note:** If using a virtual environment, remember to activate it before running any commands:
```bash
source venv/bin/activate  # Run this in each new terminal session
```

## Step 2: Verify Project Structure

```bash
# List all files
find . -type f -name "*.py" | sort
```

**Expected Output:**
```
./examples/basic_operations.py
./examples/graph_algorithms.py
./examples/performance_comparison.py
./heaps/__init__.py
./heaps/binomial_heap.py
./heaps/fibonacci_heap.py
./heaps/leftist_heap.py
./heaps/min_max_heap.py
./heaps/pairing_heap.py
./heaps/skew_heap.py
./tests/__init__.py
./tests/test_fibonacci_heap.py
./visualization/heap_visualizer.py
./visualization/performance_plots.py
```

## Step 3: Test Basic Operations

### Run Basic Operations Example

```bash
python3 examples/basic_operations.py
```

**Expected Output:**
- Section headers for each heap type (Binomial, Fibonacci, Min-Max, Pairing, Leftist, Skew)
- Insert, find-min, delete-min, and merge operations for each heap
- No error messages or exceptions

**Sample Expected Output:**
```
============================================================
Advanced Heap Operations - Basic Examples
============================================================

=== Binomial Heap Example ===
Inserting: 10, 5, 20, 3, 15
Minimum element: 3
Deleting minimum: 3
New minimum: 5
...
```

**Validation Commands:**
```bash
# Check if script runs without errors
python3 examples/basic_operations.py > /tmp/basic_ops_output.txt 2>&1
echo "Exit code: $?"
# Exit code should be 0

# Check output contains expected heap names
grep -c "Heap Example" /tmp/basic_ops_output.txt
# Should return 6 (one for each heap type)
```

## Step 4: Test Graph Algorithms

### Run Graph Algorithms Example

```bash
python3 examples/graph_algorithms.py
```

**Expected Output:**
- Dijkstra's algorithm performance comparison
- Shortest distances from starting node
- Prim's algorithm performance comparison
- Minimum spanning tree edges
- Execution times for Fibonacci and Binomial heaps

**Sample Expected Output:**
```
============================================================
Graph Algorithms with Advanced Heaps
============================================================

Graph for Dijkstra's Algorithm:
Nodes: A, B, C, D, E, F

=== Dijkstra's Algorithm Performance Comparison ===
Fibonacci Heap time: 0.000XXX seconds
Binomial Heap time: 0.000XXX seconds
...
```

**Validation Commands:**
```bash
# Run and capture output
python3 examples/graph_algorithms.py > /tmp/graph_output.txt 2>&1
echo "Exit code: $?"

# Verify Dijkstra's algorithm ran
grep -c "Dijkstra's Algorithm" /tmp/graph_output.txt
# Should return at least 1

# Verify Prim's algorithm ran
grep -c "Prim's Algorithm" /tmp/graph_output.txt
# Should return at least 1
```

## Step 5: Test Performance Comparison

### Run Performance Comparison

```bash
python3 examples/performance_comparison.py
```

**Expected Output:**
- Performance benchmarks for different heap operations
- Comparison tables
- Timing results for insert, delete-min, and merge operations
- May generate performance plots if matplotlib is configured

**Validation Commands:**
```bash
# Run performance comparison
python3 examples/performance_comparison.py > /tmp/perf_output.txt 2>&1
echo "Exit code: $?"

# Check for performance metrics
grep -i "performance\|benchmark\|time" /tmp/perf_output.txt | head -5
```

## Step 6: Run Unit Tests

### Test Fibonacci Heap

```bash
# Method 1: Using unittest directly
python3 -m unittest tests.test_fibonacci_heap -v

# Method 2: Run test file directly
python3 tests/test_fibonacci_heap.py

# Method 3: Discover all tests
python3 -m unittest discover tests/ -v
```

**Expected Output:**
- Test results showing passed tests
- Test names like `test_insert_single`, `test_delete_min`, etc.
- Final summary: "OK" or "FAILED"

**Sample Expected Output:**
```
test_delete_min (tests.test_fibonacci_heap.TestFibonacciHeap) ... ok
test_empty_heap (tests.test_fibonacci_heap.TestFibonacciHeap) ... ok
test_insert_multiple (tests.test_fibonacci_heap.TestFibonacciHeap) ... ok
...
----------------------------------------------------------------------
Ran XX tests in X.XXXs

OK
```

**Validation Commands:**
```bash
# Run tests and check exit code
python3 -m unittest tests.test_fibonacci_heap 2>&1 | tee /tmp/test_output.txt
echo "Exit code: $?"
# Exit code should be 0 if all tests pass

# Count passed tests
grep -c "ok$" /tmp/test_output.txt
```

## Step 7: Test Visualization

### Generate Sample Plots

```bash
python3 visualization/performance_plots.py
```

**Expected Output:**
- Message about generating example plots
- Plot file created: `example_comparison.png`
- No errors

**Validation Commands:**
```bash
# Run visualization
python3 visualization/performance_plots.py > /tmp/viz_output.txt 2>&1
echo "Exit code: $?"

# Check if plot file was created
ls -lh example_comparison.png 2>/dev/null && echo "Plot created successfully" || echo "Plot not created"
```

## Step 8: Test Heap Visualizer

### Run Heap Visualizer

```bash
python3 visualization/heap_visualizer.py
```

**Expected Output:**
- Visualization output or saved files
- No errors

**Validation Commands:**
```bash
python3 visualization/heap_visualizer.py > /tmp/heap_viz_output.txt 2>&1
echo "Exit code: $?"
```

## Step 9: Import Tests

### Test Module Imports

```bash
python3 -c "
from heaps import BinomialHeap, FibonacciHeap, MinMaxHeap
from heaps import PairingHeap, LeftistHeap, SkewHeap
print('All heap imports successful')
"
```

**Expected Output:**
```
All heap imports successful
```

### Test Individual Heap Operations

```bash
python3 -c "
from heaps.fibonacci_heap import FibonacciHeap
heap = FibonacciHeap()
heap.insert(10)
heap.insert(5)
heap.insert(20)
print(f'Min: {heap.find_min()}')
print(f'Deleted: {heap.delete_min()}')
print(f'New min: {heap.find_min()}')
print('Fibonacci Heap test passed')
"
```

**Expected Output:**
```
Min: 5
Deleted: 5
New min: 10
Fibonacci Heap test passed
```

## Step 10: Complete Validation Script

Create and run a complete validation script:

```bash
cat > validate_all.sh << 'EOF'
#!/bin/bash

echo "=========================================="
echo "Advanced Heap Operations - Full Validation"
echo "=========================================="
echo ""

# Test 1: Basic Operations
echo "Test 1: Basic Operations"
python3 examples/basic_operations.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo " Basic operations passed"
else
    echo " Basic operations failed"
fi

# Test 2: Graph Algorithms
echo "Test 2: Graph Algorithms"
python3 examples/graph_algorithms.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo " Graph algorithms passed"
else
    echo " Graph algorithms failed"
fi

# Test 3: Performance Comparison
echo "Test 3: Performance Comparison"
python3 examples/performance_comparison.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo " Performance comparison passed"
else
    echo " Performance comparison failed"
fi

# Test 4: Unit Tests
echo "Test 4: Unit Tests"
python3 -m unittest tests.test_fibonacci_heap > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo " Unit tests passed"
else
    echo " Unit tests failed"
fi

# Test 5: Imports
echo "Test 5: Module Imports"
python3 -c "from heaps import *" > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo " Module imports passed"
else
    echo " Module imports failed"
fi

echo ""
echo "=========================================="
echo "Validation Complete"
echo "=========================================="
EOF

chmod +x validate_all.sh
./validate_all.sh
```

**Expected Output:**
```
==========================================
Advanced Heap Operations - Full Validation
==========================================

Test 1: Basic Operations
 Basic operations passed
Test 2: Graph Algorithms
 Graph algorithms passed
Test 3: Performance Comparison
 Performance comparison passed
Test 4: Unit Tests
 Unit tests passed
Test 5: Module Imports
 Module imports passed

==========================================
Validation Complete
==========================================
```

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: Import Errors
**Error:** `ModuleNotFoundError: No module named 'heaps'`

**Solution:**
```bash
# Ensure you're in the correct directory
cd ads/advanced_heap_operations

# Run with proper Python path
PYTHONPATH=. python3 examples/basic_operations.py
```

#### Issue 2: Missing Dependencies
**Error:** `ModuleNotFoundError: No module named 'matplotlib'`

**Solution:**
```bash
pip3 install matplotlib numpy
```

#### Issue 3: Test Failures
**Error:** Tests fail with attribute errors

**Solution:**
Check that heap implementations have all required methods:
```bash
python3 -c "
from heaps.fibonacci_heap import FibonacciHeap
heap = FibonacciHeap()
print('Methods:', [m for m in dir(heap) if not m.startswith('_')])
"
```

## Summary Checklist

- [ ] Dependencies installed successfully
- [ ] Project structure verified
- [ ] Basic operations example runs without errors
- [ ] Graph algorithms example runs without errors
- [ ] Performance comparison runs without errors
- [ ] Unit tests pass (18/18)
- [ ] Visualization scripts run without errors
- [ ] Module imports work correctly
- [ ] All validation tests pass
- [ ] Heap Playground — all 6 heap types respond to insert/find_min/delete_min
- [ ] Heap Playground — Min-Max Heap responds to find_max
- [ ] Web UI — tab switching highlights the active tab
- [ ] Web UI — heap card selection highlights the selected card

## Step 11: Test Heap Playground via API

With the Flask server running, verify the Heap Playground backend:

```bash
# Test insert + find_min + delete_min for all heap types
for heap in binomial fibonacci minmax pairing leftist skew; do
  echo -n "=== $heap: "
  curl -s -X POST http://localhost:5001/playground_operation \
    -H "Content-Type: application/json" \
    -d "{\"heap_type\":\"$heap\",\"operation\":\"reset\"}" | python3 -c "import sys,json; d=json.load(sys.stdin); print('reset='+str(d['success']), end=' ')"
  curl -s -X POST http://localhost:5001/playground_operation \
    -H "Content-Type: application/json" \
    -d "{\"heap_type\":\"$heap\",\"operation\":\"insert\",\"value\":42}" | python3 -c "import sys,json; d=json.load(sys.stdin); print('insert='+str(d['success']), end=' ')"
  curl -s -X POST http://localhost:5001/playground_operation \
    -H "Content-Type: application/json" \
    -d "{\"heap_type\":\"$heap\",\"operation\":\"find_min\"}" | python3 -c "import sys,json; d=json.load(sys.stdin); print('find_min='+str(d.get('result')))"
done
```

**Expected Output:**
```
=== binomial: reset=True insert=True find_min=42
=== fibonacci: reset=True insert=True find_min=42
=== minmax: reset=True insert=True find_min=42
=== pairing: reset=True insert=True find_min=42
=== leftist: reset=True insert=True find_min=42
=== skew: reset=True insert=True find_min=42
```

## Next Steps

After validation:
1. Review the documentation in `docs/` directory
2. Explore individual heap implementations in `heaps/` directory
3. Modify examples for your specific use case
4. Add additional test cases as needed

## Support

If you encounter issues not covered in this guide:
1. Check the main README.md for additional information
2. Review the academic report in `docs/ACADEMIC_REPORT.md`
3. Examine the implementation files in `heaps/` directory