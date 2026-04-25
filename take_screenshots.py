"""Full-page screenshot capture for Advanced Heap Operations web interface."""

import time
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_URL = "http://localhost:5001"
OUT_DIR  = Path(__file__).parent / "screenshots"
OUT_DIR.mkdir(exist_ok=True)

VIEWPORT = {"width": 1400, "height": 900}

def save(page, name):
    path = OUT_DIR / name
    page.screenshot(path=str(path), full_page=True)
    print(f"  ✓ {name}")

def wait_ready(page, selector, timeout=30_000):
    page.wait_for_selector(selector, timeout=timeout)

def click_tab(page, tab_id):
    page.evaluate(f"""
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    """)
    page.evaluate(f"""
        const tabs = document.querySelectorAll('.tab');
        tabs.forEach(t => {{
            if (t.textContent.includes('{tab_id}')) {{
                t.classList.add('active');
            }}
        }});
        const match = Array.from(document.querySelectorAll('.tab')).find(t => t.textContent.includes('{tab_id}'));
        if (match) match.click();
    """)
    time.sleep(0.3)

def run_and_wait(page, btn_span_id, output_id, long_wait=False):
    page.evaluate(f"document.getElementById('{btn_span_id}').parentElement.click()")
    # Wait for output to appear and loading to finish
    page.wait_for_function(
        f"document.getElementById('{output_id}') && "
        f"document.getElementById('{output_id}').style.display !== 'none' && "
        f"!document.getElementById('{btn_span_id}').innerHTML.includes('Running')",
        timeout=60_000
    )
    time.sleep(0.5)


def main():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        ctx = browser.new_context(viewport=VIEWPORT)
        page = ctx.new_page()

        print("\n── Opening page ──")
        page.goto(BASE_URL, wait_until="networkidle")
        time.sleep(0.5)

        # ── 1. Basic Operations tab (empty) ──
        print("\n── Tab: Basic Operations ──")
        page.evaluate("document.querySelector('.tab').click()")
        time.sleep(0.3)
        save(page, "01_basic_operations.png")

        # run and capture output
        run_and_wait(page, "btn-basic", "output-basic")
        save(page, "02_basic_operations_output.png")

        # ── 2. Graph Algorithms ──
        print("\n── Tab: Graph Algorithms ──")
        page.click("button.tab:nth-of-type(2)")
        time.sleep(0.3)
        save(page, "03_graph_algorithms.png")
        run_and_wait(page, "btn-graph", "output-graph")
        save(page, "04_graph_algorithms_output.png")

        # ── 3. Performance Comparison ──
        print("\n── Tab: Performance Comparison ──")
        page.click("button.tab:nth-of-type(3)")
        time.sleep(0.3)
        save(page, "05_performance_comparison.png")
        # Run benchmark (slow)
        page.evaluate("document.getElementById('btn-perf').parentElement.click()")
        print("  … waiting for benchmark (up to 60 s) …")
        page.wait_for_function(
            "document.getElementById('output-perf') && "
            "document.getElementById('output-perf').style.display !== 'none' && "
            "!document.getElementById('btn-perf').innerHTML.includes('Running')",
            timeout=90_000
        )
        time.sleep(1.5)  # allow chart imgs to reload
        save(page, "06_performance_comparison_output.png")
        # scroll to charts
        page.evaluate("document.getElementById('perf-charts-card').scrollIntoView()")
        time.sleep(0.4)
        save(page, "07_performance_charts.png")

        # ── 4. Heap Playground ──
        print("\n── Tab: Heap Playground ──")
        page.click("button.tab:nth-of-type(4)")
        time.sleep(0.3)
        save(page, "08_heap_playground.png")

        heap_types = [
            ("binomial",  "Binomial"),
            ("fibonacci", "Fibonacci"),
            ("minmax",    "Min-Max"),
            ("pairing",   "Pairing"),
            ("leftist",   "Leftist"),
            ("skew",      "Skew"),
        ]
        file_idx = 9
        for heap_id, label in heap_types:
            # click heap card
            page.evaluate(f"""
                document.querySelectorAll('.heap-card').forEach(c => {{
                    if (c.querySelector('h4') && c.querySelector('h4').textContent.includes('{label}')) {{
                        c.click();
                    }}
                }});
            """)
            time.sleep(0.4)
            # Insert a few values
            for v in [42, 7, 88, 15, 3]:
                page.evaluate(f"""
                    document.getElementById('insert-value').value = '{v}';
                    document.querySelector('button.btn[onclick*=\\"insert\\"]').click();
                """)
                time.sleep(0.2)
            # find min
            page.evaluate("document.querySelector('button.btn[onclick*=\"find_min\"]').click()")
            time.sleep(0.3)
            save(page, f"{file_idx:02d}_heap_playground_{heap_id}.png")
            file_idx += 1

        # ── 5. Interactive Code ──
        print("\n── Tab: Interactive Code ──")
        page.click("button.tab:nth-of-type(5)")
        time.sleep(0.3)
        save(page, f"{file_idx:02d}_interactive_code.png")
        file_idx += 1

        sample_code = """heap = FibonacciHeap()
for v in [42, 7, 88, 15, 3, 56, 21]:
    heap.insert(v)
print(f'Min: {heap.find_min()}')
heap.delete_min()
print(f'After delete_min — new Min: {heap.find_min()}')

mm = MinMaxHeap()
for v in [10, 50, 30, 70, 20]:
    mm.insert(v)
print(f'Min-Max Heap — Min: {mm.find_min()}, Max: {mm.find_max()}')"""

        page.evaluate(f"""
            const ta = document.getElementById('code-input');
            ta.value = {repr(sample_code)};
        """)
        time.sleep(0.2)
        page.evaluate("document.getElementById('btn-interactive').parentElement.click()")
        page.wait_for_function(
            "document.getElementById('output-interactive') && "
            "document.getElementById('output-interactive').style.display !== 'none' && "
            "!document.getElementById('btn-interactive').innerHTML.includes('Executing')",
            timeout=30_000
        )
        time.sleep(0.4)
        save(page, f"{file_idx:02d}_interactive_code_output.png")
        file_idx += 1

        # ── 6. Heap Information ──
        print("\n── Tab: Heap Information ──")
        page.click("button.tab:nth-of-type(6)")
        time.sleep(0.3)
        save(page, f"{file_idx:02d}_heap_information.png")
        file_idx += 1

        info_heaps = [
            ("binomial",  "Binomial"),
            ("fibonacci", "Fibonacci"),
            ("minmax",    "Min-Max"),
            ("pairing",   "Pairing"),
            ("leftist",   "Leftist"),
            ("skew",      "Skew"),
        ]
        for heap_id, label in info_heaps:
            page.evaluate(f"""
                document.querySelectorAll('#heaps .heap-card').forEach(c => {{
                    if (c.querySelector('h4') && c.querySelector('h4').textContent.includes('{label}')) {{
                        c.click();
                    }}
                }});
            """)
            page.wait_for_function(
                "document.getElementById('heap-details').children.length > 0",
                timeout=10_000
            )
            time.sleep(0.4)
            page.evaluate("document.getElementById('heap-details').scrollIntoView()")
            time.sleep(0.3)
            save(page, f"{file_idx:02d}_heap_information_{heap_id}.png")
            file_idx += 1

        # ── 7. Run Tests ──
        print("\n── Tab: Run Tests ──")
        page.click("button.tab:nth-of-type(7)")
        time.sleep(0.3)
        save(page, f"{file_idx:02d}_run_tests.png")
        file_idx += 1

        page.evaluate("document.getElementById('btn-tests').parentElement.click()")
        print("  … waiting for tests …")
        page.wait_for_function(
            "document.getElementById('output-tests') && "
            "document.getElementById('output-tests').style.display !== 'none' && "
            "!document.getElementById('btn-tests').innerHTML.includes('Running')",
            timeout=60_000
        )
        time.sleep(0.5)
        save(page, f"{file_idx:02d}_run_tests_results.png")

        browser.close()

    print(f"\nDone — screenshots saved to {OUT_DIR}")


if __name__ == "__main__":
    main()
