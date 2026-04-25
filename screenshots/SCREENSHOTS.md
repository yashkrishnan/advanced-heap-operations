# Web Interface Screenshots

This document showcases the Advanced Heap Operations web interface through screenshots.

---

## Tab 1 — Basic Operations

### Basic Operations (default)
![Basic Operations](01_basic_operations.png)
*The Basic Operations tab — landing tab — with a single card to run insert, find-min, delete-min and merge demos for all 6 heap types.*

### Basic Operations Output
![Basic Operations Output](02_basic_operations_output.png)
*Output from running Basic Operations, demonstrating insert, find-min, delete-min, and merge for all 6 heap types.*

---

## Tab 2 — Graph Algorithms

### Graph Algorithms (default)
![Graph Algorithms](03_graph_algorithms.png)
*The Graph Algorithms tab with a button to run Dijkstra's shortest path and Prim's minimum spanning tree.*

### Graph Algorithms Output
![Graph Algorithms Output](04_graph_algorithms_output.png)
*Output from running Graph Algorithms, showing shortest path and MST results using different heap backends.*

---

## Tab 3 — Performance Comparison

### Performance Comparison (default)
![Performance Comparison](05_performance_comparison.png)
*The Performance Comparison tab showing the run button and the embedded chart gallery (overview + 4 per-operation charts).*

### Performance Comparison Output
![Performance Comparison Output](06_performance_comparison_output.png)
*Benchmark text output and auto-refreshed charts after running the full comparison.*

---

## Tab 4 — Heap Playground

### Heap Playground (default)
![Heap Playground](07_heap_playground.png)
*The Heap Playground tab showing a grid of 6 selectable heap cards.*

### Binomial Heap Operations
![Binomial Heap Operations](08_heap_playground_binomial.png)
*Binomial Heap selected (card highlighted). Insert, Find Min, and Delete Min operations performed.*

### Fibonacci Heap Operations
![Fibonacci Heap Operations](09_heap_playground_fibonacci.png)
*Fibonacci Heap selected with multiple inserts and Find Min / Delete Min results.*

### Min-Max Heap Operations
![Min-Max Heap Operations](10_heap_playground_minmax.png)
*Min-Max Heap selected, showing the exclusive Find Max button alongside standard operations.*

### Pairing Heap Operations
![Pairing Heap Operations](11_heap_playground_pairing.png)
*Pairing Heap selected with Insert, Find Min, and Delete Min results.*

### Leftist Heap Operations
![Leftist Heap Operations](12_heap_playground_leftist.png)
*Leftist Heap selected with Insert, Find Min, and Delete Min results.*

### Skew Heap Operations
![Skew Heap Operations](13_heap_playground_skew.png)
*Skew Heap selected with Insert, Find Min, and Delete Min results.*

---

## Tab 5 — Interactive Code

### Code Editor (default)
![Interactive Code](14_interactive_code.png)
*The Interactive Code tab with a Python console pre-loaded with example code. All 6 heap classes are pre-imported.*

### Code Execution Output
![Interactive Code Output](15_interactive_code_output.png)
*Output after executing custom Python code, displayed in a terminal-style format.*

---

## Tab 6 — Heap Information

### Heap Cards Overview
![Heap Information](16_heap_information.png)
*The Heap Information tab showing 6 clickable cards, one per heap type, with brief descriptions.*

### Binomial Heap Detail
![Binomial Heap Detail](17_heap_information_binomial.png)
*Detailed view for Binomial Heap: time complexity table and recommended use cases.*

### Fibonacci Heap Detail
![Fibonacci Heap Detail](18_heap_information_fibonacci.png)
*Detailed view for Fibonacci Heap: amortized complexities and use cases.*

### Min-Max Heap Detail
![Min-Max Heap Detail](19_heap_information_minmax.png)
*Detailed view for Min-Max Heap: O(1) Find Min and Find Max complexities and use cases.*

### Pairing Heap Detail
![Pairing Heap Detail](20_heap_information_pairing.png)
*Detailed view for Pairing Heap: amortized complexities and use cases.*

### Leftist Heap Detail
![Leftist Heap Detail](21_heap_information_leftist.png)
*Detailed view for Leftist Heap: time complexities highlighting efficient merge.*

### Skew Heap Detail
![Skew Heap Detail](22_heap_information_skew.png)
*Detailed view for Skew Heap: amortized complexities for the self-adjusting variant.*

---

## Tab 7 — Run Tests

### Tests Overview
![Run Tests](23_run_tests.png)
*The Run Tests tab with a button to execute the complete unit test suite (18 tests).*

### Test Results
![Test Results](24_run_tests_results.png)
*All 18 unit tests completed successfully, with colour-coded results.*

---

## Features Highlighted

- **Modern UI**: Symmetric heap-pile SVG icon with 7 colours; purple gradient theme
- **7 Tabs**: Basic Operations, Graph Algorithms, Performance Comparison, Heap Playground, Interactive Code, Heap Information, Run Tests
- **Embedded Charts**: Performance Comparison tab shows 5 charts (overview + per-operation) that auto-refresh after each run
- **Heap Playground**: Interactive operations on all 6 heap types with live state display
- **Syntax Highlighting**: VS Code-style colour scheme for all output

## Technical Details

- **Framework**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Port**: Auto-detection (5000–5009), typically runs on 5001 on macOS
- **Screenshots**: Full-page, 1440px wide, Playwright Chromium, captured 2026-04-25

---

*Screenshots show the interface running on localhost. Appearance may vary slightly by browser and screen resolution.*
