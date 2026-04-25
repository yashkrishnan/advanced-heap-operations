# START HERE - Quick Launch Guide

## Your Web Interface is Ready!

Everything has been set up and verified. Follow these simple steps to launch the web interface.

---

## Quick Start (3 Steps)

### Step 1: Open Terminal
Open a terminal and navigate to the project:
```bash
cd ads/advanced_heap_operations
```

### Step 2: Start the Server
Run the startup script:
```bash
./start_web_interface.sh
```

### Step 3: Open Browser
Open your web browser and go to:
```
http://localhost:5001
```

> **Note:** macOS AirPlay Receiver occupies port 5000. The server automatically uses port 5001 (or the next free port). The exact URL is printed in the terminal.

**That's it!**

---

## What You'll See

### In Terminal:
```
==========================================================
Advanced Heap Operations - Web Interface
==========================================================

Starting server on port 5001...
Open your browser and navigate to: http://localhost:5001

Press Ctrl+C to stop the server
==========================================================
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
```

### In Browser:
- Beautiful purple gradient interface
- 5 tabs: Examples, Heap Playground, Interactive Code, Heap Info, Tests
- Click buttons to run programs
- See output in real-time

---

## Try These First

### 1. Run Basic Operations
- Click the **Examples** tab
- Click "Run Basic Operations" button
- Watch output appear showing all 6 heap types

### 2. Use the Heap Playground
- Click the **Heap Playground** tab
- Click any heap card (e.g., "Fibonacci Heap") — it highlights on selection
- Type a number in the input field and click **Insert**
- Click **Find Min** to see the current minimum
- Click **Delete Min** to remove it
- For Min-Max Heap, the **Find Max** button also appears

### 3. Try Interactive Code
- Click **Interactive Code** tab
- The example code is already there
- Click "Execute Code"
- See the results instantly

### 4. View Heap Information
- Click **Heap Information** tab
- Click on any heap card (e.g., "Fibonacci Heap")
- See detailed complexity and use cases

### 5. Run Tests
- Click **Tests** tab
- Click "Run All Tests"
- Watch 18 tests execute

---

## Alternative: Manual Start

If the script doesn't work, use these commands:

```bash
# Navigate to project
cd ads/advanced_heap_operations

# Activate virtual environment
source venv/bin/activate

# Go to web interface directory
cd web_interface

# Start server
python3 app.py
```

Then open the URL shown in the terminal output.

---

## Troubleshooting

### Problem: "Permission denied"
```bash
chmod +x start_web_interface.sh
./start_web_interface.sh
```

### Problem: "Virtual environment not found"
```bash
./setup.sh
./start_web_interface.sh
```

### Problem: "Flask not found"
```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
cd web_interface
python3 app.py
```

---

## Features Available

### Examples Tab
- **Basic Operations**: Demonstrates insert, delete, merge for all 6 heaps
- **Graph Algorithms**: Runs Dijkstra's and Prim's algorithms
- **Performance Comparison**: Benchmarks different implementations

### Heap Playground Tab
- Select any of 6 heap types interactively
- **Insert** a value, **Find Min**, **Delete Min**, **Find Max** (Min-Max only), **Reset**
- Live display of heap size and current min/max after each operation
- All 6 heap types fully functional

### Interactive Code Tab
- Write custom Python code
- Pre-imported: BinomialHeap, FibonacciHeap, MinMaxHeap, PairingHeap, LeftistHeap, SkewHeap
- Execute instantly and see results

### Heap Information Tab
- Click any heap to see:
  - Time complexity for all operations
  - Use case recommendations
  - Detailed descriptions

### Tests Tab
- Run complete test suite (18 tests)
- See pass/fail status
- View detailed output

---

## Interface Preview

```
┌─────────────────────────────────────────────────────────────────┐
│  Advanced Heap Operations                                       │
│  Interactive Web Interface for Heap Data Structures            │
├─────────────────────────────────────────────────────────────────┤
│  [Examples] [Heap Playground] [Interactive Code] [Info] [Tests]│
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Select a Heap Type:                                           │
│  [Binomial] [Fibonacci] [Min-Max] [Pairing] [Leftist] [Skew]  │
│                                                                 │
│  Value: [___]  [Insert] [Find Min] [Delete Min] [Reset]        │
│                                                                 │
│  > Heap initialized. Ready for operations.                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Security Note

**Important**: This server is for local development only.
- Runs on localhost (127.0.0.1)
- Not configured for internet access
- Only run trusted code in interactive console

---

## Additional Documentation

- **README.md** - Main project documentation
- **FINAL_PROJECT_STATUS.md** - Complete project status and technical details
- **WEB_INTERFACE_SETUP.md** - Detailed setup instructions
- **TESTING_GUIDE.md** - Testing procedures
- **SCREENSHOTS.md** - Web interface screenshots
- **AGENTS.md** - Development guidelines
- **web_interface/README.md** - Feature documentation

---

## Verification Checklist

Before starting, verify:
- [x] Virtual environment exists (`venv/` directory)
- [x] Flask is installed (version 3.1.3)
- [x] All dependencies installed
- [x] All 5 UI tabs functional
- [x] Heap Playground working for all 6 heap types

All checks passed!

---

## Ready to Launch!

Everything is set up and verified. Just run:

```bash
cd ads/advanced_heap_operations
./start_web_interface.sh
```

Then open the URL shown in the terminal in your browser.

**Enjoy exploring heap data structures!**

---

*For questions or issues, refer to the documentation files listed above.*
