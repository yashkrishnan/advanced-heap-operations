# Web Interface Setup and Testing Guide

## Current Status

The web interface is fully set up and working. Flask is installed in the `venv/` virtual environment.

## Setup Steps

### Step 1: Set Up Virtual Environment

```bash
cd ads/advanced_heap_operations

# Create virtual environment (if not already done)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows
```

### Step 2: Install Dependencies

```bash
# Install all dependencies including Flask
pip install -r requirements.txt
```

**OR** install Flask separately:

```bash
pip install flask
```

### Step 3: Start the Web Server

#### Option A: Using the startup script (Recommended)
```bash
./start_web_interface.sh
```

#### Option B: Manual start
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Navigate to web interface directory
cd web_interface

# Start the Flask app
python3 app.py
```

### Step 4: Access the Interface

Open your web browser and navigate to the URL shown in the terminal (typically port 5001 on macOS):
```
http://localhost:5001
```

> **Note:** macOS AirPlay Receiver occupies port 5000 by default. The app auto-detects and uses port 5001. The exact URL is always printed on startup.

## Verification Checklist

Before starting the server, verify:

- [ ] Virtual environment is created (`venv/` directory exists)
- [ ] Virtual environment is activated (prompt shows `(venv)`)
- [ ] Flask is installed (`python3 -c "import flask; print('OK')"` works)
- [ ] You're in the correct directory

## Quick Test Commands

### Test 1: Check Flask Installation
```bash
python3 -c "import flask; print('Flask version:', flask.__version__)"
```

**Expected Output:**
```
Flask version: 2.3.x
```

### Test 2: Check if Port 5000 is Available
```bash
lsof -i :5000
```

**Expected Output:**
- Empty (port is free) OR
- Shows existing Flask process (if already running)

### Test 3: Test Flask App Syntax
```bash
cd web_interface
python3 -c "import app; print('App loaded successfully')"
```

**Expected Output:**
```
App loaded successfully
```

## Starting the Server - Full Example

Here's a complete example session:

```bash
# 1. Navigate to project directory
cd ads/advanced_heap_operations

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Verify Flask is installed
python3 -c "import flask; print('Flask installed:', flask.__version__)"

# 5. Start the server
cd web_interface
python3 app.py
```

**Expected Server Output:**
```
==========================================================
Advanced Heap Operations - Web Interface
==========================================================

Starting server on port 5001...
Open your browser and navigate to: http://localhost:5001

Note: Port 5000 was in use, using port 5001 instead
Tip: On macOS, disable 'AirPlay Receiver' in System Settings

Press Ctrl+C to stop the server
==========================================================
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5001
 * Running on http://192.168.x.x:5001
Press CTRL+C to quit
```

## Troubleshooting

### Issue 1: "ModuleNotFoundError: No module named 'flask'"

**Solution:**
```bash
# Activate virtual environment first
source venv/bin/activate

# Then install Flask
pip install flask
```

### Issue 2: "Address already in use"

**Solution:**
```bash
# Find process using port 5000
lsof -i :5000

# Kill the process (replace PID with actual process ID)
kill -9 PID

# OR change the port in app.py (line 218):
# app.run(debug=True, host='0.0.0.0', port=5001)
```

### Issue 3: "Permission denied" when running scripts

**Solution:**
```bash
chmod +x setup.sh
chmod +x start_web_interface.sh
```

### Issue 4: Virtual environment not activating

**Solution:**
```bash
# Remove old venv and recreate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Testing the Web Interface

Once the server is running, test these features:

### 1. Test Examples Tab
- Click "Run Basic Operations" button
- Should see output from all 6 heap types
- Output appears in terminal-style display

### 2. Test Heap Playground Tab
- Click on any heap card (e.g., "Fibonacci Heap") — the card should highlight
- Type a number in the input field and click **Insert**
- Click **Find Min** — should return the minimum value
- Click **Delete Min** — should remove and return the minimum
- For **Min-Max Heap**: a **Find Max** button also appears
- Click **Reset** to clear the heap and start over
- All 6 heap types (Binomial, Fibonacci, Min-Max, Pairing, Leftist, Skew) are fully functional

### 3. Test Interactive Code Tab
- Enter code:
  ```python
  heap = FibonacciHeap()
  heap.insert(10)
  heap.insert(5)
  print(f'Min: {heap.find_min()}')
  ```
- Click "Execute Code"
- Should see: `Min: 5`

### 4. Test Heap Information Tab
- Click on "Fibonacci Heap" card
- Should see detailed information with complexity table

### 5. Test Tests Tab
- Click "Run All Tests"
- Should see 18 tests running
- All tests should pass

## What to Expect

### Browser View
- Modern purple gradient interface
- 5 tabs at the top: Examples, Heap Playground, Interactive Code, Heap Information, Run Tests
- Cards with "Run" buttons
- Terminal-style output displays
- Smooth animations

### Console Output
- Server startup messages
- Request logs when you click buttons
- Any errors will appear here

## Security Note

 **Important**: This web interface is for local development only.
- Do not expose to the internet
- Only run on localhost
- Do not run untrusted code in the interactive console

## Next Steps

After successful setup:
1. Explore all tabs in the web interface
2. Try running different examples
3. Write custom code in the interactive console
4. View information about different heap types
5. Run the test suite

## Support

If you encounter issues:
1. Check this troubleshooting guide
2. Verify all prerequisites are met
3. Check the console for error messages
4. Review `web_interface/README.md` for more details