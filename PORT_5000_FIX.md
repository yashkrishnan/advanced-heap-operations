# Port 5000 Already in Use - Quick Fix

## Problem
You're seeing this error:
```
Address already in use
Port 5000 is in use by another program.
```

##  Solution (Automatic)

**Good news!** The app has been updated to automatically find an available port.

Just run the server again:
```bash
./start_web_interface.sh
```

The app will now:
1. Try port 5000
2. If busy, try ports 5001, 5002, 5003, etc.
3. Tell you which port it's using
4. Show you the correct URL to open

**Example output:**
```
Starting server on port 5001...
Open your browser and navigate to: http://localhost:5001

Note: Port 5000 was in use, using port 5001 instead
```

##  Manual Solutions

### Option 1: Disable AirPlay Receiver (macOS)

Port 5000 is often used by macOS AirPlay Receiver.

**Steps:**
1. Open **System Settings**
2. Go to **General** → **AirDrop & Handoff**
3. Turn off **AirPlay Receiver**
4. Restart the server

### Option 2: Kill the Process Using Port 5000

```bash
# Find what's using port 5000
lsof -i :5000

# Kill the process (replace PID with actual number)
kill -9 PID
```

### Option 3: Use a Different Port Manually

Edit `web_interface/app.py` and change the port:
```python
# Line 253 (approximately)
app.run(debug=True, host='0.0.0.0', port=8080)  # Use 8080 instead
```

##  Recommended Approach

**Just restart the server** - it will automatically find an available port!

```bash
cd ads/advanced_heap_operations
./start_web_interface.sh
```

Then open the URL shown in the terminal output.

##  Common Ports

If 5000-5009 are all busy, you can manually specify:
- 8000 - Common alternative
- 8080 - HTTP alternative
- 3000 - Node.js default
- 4000 - Another common choice

##  Verification

After starting, you should see:
```
==========================================
Advanced Heap Operations - Web Interface
==========================================

Starting server on port 5001...
Open your browser and navigate to: http://localhost:5001

Press Ctrl+C to stop the server
==========================================
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5001
```

**Success!** The server is running. Open the URL shown.

##  Next Steps

1. Note the port number shown in the output
2. Open your browser
3. Navigate to `http://localhost:PORT` (use the port from output)
4. Start using the web interface!

---

**The automatic port detection is now active, so this issue should resolve itself!**