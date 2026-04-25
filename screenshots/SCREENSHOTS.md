# Web Interface Screenshots

This document showcases the Advanced Heap Operations web interface through screenshots.

---

## Tab 1 — Examples

### Examples Overview
![Examples Tab](01_examples.png)
*The Examples tab — landing page — showing three runnable demo cards: Basic Operations, Graph Algorithms, and Performance Comparison.*

### Basic Operations Output
![Basic Operations Output](02_examples_basic_output.png)
*Output from running Basic Operations, demonstrating insert, find-min, delete-min, and merge for all 6 heap types.*

### Graph Algorithms Output
![Graph Algorithms Output](03_examples_graph_output.png)
*Output from running Graph Algorithms, showing Dijkstra's shortest path and Prim's minimum spanning tree using different heap backends.*

### Performance Comparison Output
![Performance Comparison Output](04_examples_perf_output.png)
*Performance benchmark results comparing all 6 heap implementations across insert, delete-min, and merge operations.*

---

## Tab 2 — Heap Playground

### Initial View
![Heap Playground](05_heap_playground.png)
*The Heap Playground tab showing a grid of 6 selectable heap cards: Binomial, Fibonacci, Min-Max, Pairing, Leftist, and Skew.*

### Binomial Heap Operations
![Binomial Heap Operations](06_heap_playground_binomial.png)
*Binomial Heap selected (card highlighted). Insert, Find Min, and Delete Min operations performed with results displayed.*

### Fibonacci Heap Operations
![Fibonacci Heap Operations](07_heap_playground_fibonacci.png)
*Fibonacci Heap selected. Multiple insert operations followed by Find Min and Delete Min, showing heap size and current minimum.*

### Min-Max Heap Operations
![Min-Max Heap Operations](08_heap_playground_minmax.png)
*Min-Max Heap selected, showing the exclusive Find Max button alongside the standard operation buttons. Find Max result displayed.*

### Pairing Heap Operations
![Pairing Heap Operations](09_heap_playground_pairing.png)
*Pairing Heap selected. Insert, Find Min, and Delete Min operations performed with results displayed.*

### Leftist Heap Operations
![Leftist Heap Operations](10_heap_playground_leftist.png)
*Leftist Heap selected. Insert, Find Min, and Delete Min operations performed with results displayed.*

### Skew Heap Operations
![Skew Heap Operations](11_heap_playground_skew.png)
*Skew Heap selected. Insert, Find Min, and Delete Min operations performed with results displayed.*

---

## Tab 3 — Interactive Code

### Code Editor
![Interactive Code](12_interactive_code.png)
*The Interactive Code tab with a Python console pre-loaded with example code. All 6 heap classes are pre-imported and ready to use.*

### Code Execution Output
![Interactive Code Output](13_interactive_code_output.png)
*Output after executing custom Python code using FibonacciHeap and MinMaxHeap, displayed in a terminal-style format.*

---

## Tab 4 — Heap Information

### Heap Cards Overview
![Heap Information](14_heap_information.png)
*The Heap Information tab showing 6 clickable cards, one per heap type, with brief descriptions.*

### Binomial Heap Detail
![Binomial Heap Detail](15_heap_information_binomial.png)
*Detailed view for Binomial Heap: time complexity table for Delete Min, Find Min, Insert, and Merge, plus recommended use cases.*

### Fibonacci Heap Detail
![Fibonacci Heap Detail](16_heap_information_fibonacci.png)
*Detailed view for Fibonacci Heap: amortized complexities for Decrease Key, Delete Min, Find Min, Insert, and Merge, plus use cases.*

### Min-Max Heap Detail
![Min-Max Heap Detail](17_heap_information_minmax.png)
*Detailed view for Min-Max Heap: O(1) Find Min and Find Max complexities, plus use cases for double-ended priority queues.*

### Pairing Heap Detail
![Pairing Heap Detail](18_heap_information_pairing.png)
*Detailed view for Pairing Heap: amortized complexities and use cases for simple priority queues with good practical performance.*

### Leftist Heap Detail
![Leftist Heap Detail](19_heap_information_leftist.png)
*Detailed view for Leftist Heap: time complexities and use cases, highlighting efficient merge as the primary advantage.*

### Skew Heap Detail
![Skew Heap Detail](20_heap_information_skew.png)
*Detailed view for Skew Heap: amortized complexities and use cases for self-adjusting heaps with minimal overhead.*

---

## Tab 5 — Run Tests

### Tests Overview
![Run Tests](21_run_tests.png)
*The Run Tests tab with a button to execute the complete unit test suite (18 tests for Fibonacci Heap implementation).*

### Test Results
![Test Results](22_run_tests_results.png)
*All 18 unit tests completed successfully, with colour-coded results for each test method.*

---

## Features Highlighted

- **Modern UI**: Purple gradient theme with large, readable fonts (18–24px)
- **Responsive Design**: Clean layout that adapts to different screen sizes
- **Syntax Highlighting**: VS Code-style colour scheme for all output
- **Real-time Feedback**: Immediate results for every operation
- **Heap Playground**: Interactive operations on all 6 heap types with live state display

## Technical Details

- **Framework**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Port**: Auto-detection (5000–5009), typically runs on 5001 on macOS
- **Browser Compatibility**: Chrome, Firefox, Safari, Edge
- **Screenshots**: 1440×900, headless Chrome 147, captured 2026-04-25

---

*Screenshots show the interface running on localhost. Appearance may vary slightly by browser and screen resolution.*
