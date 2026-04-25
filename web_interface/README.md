# Web Interface for Advanced Heap Operations

A beautiful, interactive web interface to run and visualize heap operations through your browser.

## Features

### ⚙️ Basic Operations Tab
- Run demonstrations of all 6 heap types (insert, find-min, delete-min, merge)

### 🗺️ Graph Algorithms Tab
- Execute Dijkstra's shortest path and Prim's minimum spanning tree algorithms

### 📈 Performance Comparison Tab
- Benchmark all 6 heap implementations across insert, delete-min, find-min, and merge
- Embedded chart gallery: 1 combined overview + 4 per-operation charts
- Charts auto-refresh (cache-busted) after each run

### 🎮 Heap Playground Tab
- **Interactive heap operations** with real-time feedback
- Select any of the 6 heap types
- Perform operations: Insert, Find Min, Delete Min, Find Max (Min-Max only)
- View heap state after each operation
- Reset heap at any time

###  Interactive Code Tab
- Write and execute Python code in real-time
- Pre-imported heap classes ready to use
- Instant output display

###  Heap Information Tab
- Detailed information about each heap type
- Time complexity tables
- Use case recommendations

###  Tests Tab
- Run complete unit test suite
- View test results in real-time

## Quick Start

### Option 1: Using the Startup Script (Recommended)

```bash
cd ads/advanced_heap_operations
./start_web_interface.sh
```

### Option 2: Manual Start

```bash
# Activate virtual environment
source venv/bin/activate

# Navigate to web interface directory
cd web_interface

# Start the server
python3 app.py
```

### Option 3: Direct Python Execution

```bash
cd ads/advanced_heap_operations/web_interface
python3 app.py
```

## Accessing the Interface

Once started, open your web browser and navigate to:

```
http://localhost:5000
```

## Screenshots

### Main Interface
The interface features a modern, gradient design with tabbed navigation for easy access to different features.

### Running Examples
Click any "Run" button to execute examples and see real-time output in a terminal-style display.

### Interactive Console
Write custom Python code using any of the heap implementations and execute it instantly.

### Heap Information
Click on any heap card to view detailed information including time complexity and use cases.

## API Endpoints

The web interface provides the following REST API endpoints:

### GET `/`
Main page with the web interface

### GET `/run/<example_type>`
Run a specific example program
- `example_type`: `basic_operations`, `graph_algorithms`, `performance_comparison`, or `tests`
- Returns: JSON with output and status

### POST `/run_interactive`
Execute custom Python code
- Body: `{"code": "your python code"}`
- Returns: JSON with output and status

### GET `/heap_info/<heap_type>`
Get information about a specific heap
- `heap_type`: `binomial`, `fibonacci`, `minmax`, `pairing`, `leftist`, or `skew`
- Returns: JSON with heap details

### POST `/playground_operation`
Perform heap operations in the playground
- Body: `{"heap_type": "fibonacci", "operation": "insert", "value": 42}`
- Operations: `insert`, `find_min`, `find_max`, `delete_min`, `reset`
- Returns: JSON with operation result and heap state

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Custom CSS with gradient themes
- **Icons**: Unicode emoji for visual appeal

## Security Notes

️ **Important**: This web interface is designed for local development and educational purposes only.

- The interactive code execution uses Python's `exec()` function
- Do not expose this interface to the internet without proper security measures
- Only run trusted code in the interactive console

## Troubleshooting

### Port Already in Use
The server auto-detects the first free port in the range 5000–5009 (typically 5001 on macOS, where AirPlay Receiver occupies 5000). The exact URL is printed in the terminal on startup.

### Module Not Found Errors
Ensure you've activated the virtual environment and installed all dependencies:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Flask Not Installed
Install Flask manually:
```bash
pip install flask
```

## Development

### File Structure
```
web_interface/
├── app.py                 # Flask application
├── templates/
│   └── index.html        # Main HTML template
└── README.md             # This file
```

### Adding New Features

To add a new example or feature:

1. Add a new route in `app.py`
2. Update the HTML template in `templates/index.html`
3. Add corresponding JavaScript functions for interactivity

## Browser Compatibility

Tested and working on:
-  Chrome/Chromium (Recommended)
-  Firefox
-  Safari
-  Edge

## Performance

The web interface is lightweight and responsive:
- Initial load: < 1 second
- Example execution: Depends on complexity (typically 1-5 seconds)
- Interactive code: Near-instant execution for simple operations

## Contributing

Improvements welcome! Consider adding:
- Visualization of heap structures
- More interactive examples
- Export functionality for results
- Dark/light theme toggle
- Code syntax highlighting

## License

Same as the main project (MIT License)