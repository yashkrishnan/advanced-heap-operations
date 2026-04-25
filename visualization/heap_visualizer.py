"""
Heap Structure Visualizer

Creates visual representations of heap structures for documentation and analysis.
Generates diagrams showing the internal structure of each heap type.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
    import matplotlib
    matplotlib.use('Agg')
    PLOTTING_AVAILABLE = True
except ImportError:
    PLOTTING_AVAILABLE = False
    print("Warning: matplotlib not available. Visualizations cannot be generated.")

from heaps.binomial_heap import BinomialHeap
from heaps.fibonacci_heap import FibonacciHeap
from heaps.min_max_heap import MinMaxHeap
from heaps.pairing_heap import PairingHeap
from heaps.leftist_heap import LeftistHeap
from heaps.skew_heap import SkewHeap


class HeapVisualizer:
    """Visualize heap structures"""
    
    def __init__(self):
        if not PLOTTING_AVAILABLE:
            raise ImportError("matplotlib is required for visualization")
    
    def visualize_min_max_heap(self, values, filename="min_max_heap.png"):
        """Visualize Min-Max Heap structure"""
        heap = MinMaxHeap()
        for val in values:
            heap.insert(val)
        
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
        # Title
        ax.text(5, 9.5, 'Min-Max Heap Structure', 
               ha='center', fontsize=16, fontweight='bold')
        
        # Draw array representation
        array_y = 8.5
        box_width = 0.6
        start_x = 1
        
        ax.text(start_x - 0.5, array_y + 0.3, 'Array:', fontsize=12, fontweight='bold')
        
        for i, val in enumerate(heap.heap[:min(len(heap.heap), 15)]):
            x = start_x + i * box_width
            rect = FancyBboxPatch((x, array_y), box_width * 0.9, 0.4,
                                 boxstyle="round,pad=0.05", 
                                 edgecolor='black', facecolor='lightblue')
            ax.add_patch(rect)
            ax.text(x + box_width * 0.45, array_y + 0.2, str(val),
                   ha='center', va='center', fontsize=10)
            ax.text(x + box_width * 0.45, array_y - 0.2, str(i),
                   ha='center', va='top', fontsize=8, color='gray')
        
        # Draw tree representation
        def draw_tree_node(ax, x, y, value, level, is_min_level):
            color = 'lightgreen' if is_min_level else 'lightcoral'
            circle = Circle((x, y), 0.25, facecolor=color, edgecolor='black', linewidth=2)
            ax.add_patch(circle)
            ax.text(x, y, str(value), ha='center', va='center', 
                   fontsize=11, fontweight='bold')
            
            level_text = 'MIN' if is_min_level else 'MAX'
            ax.text(x, y - 0.4, level_text, ha='center', va='top',
                   fontsize=7, style='italic', color='darkblue')
        
        # Draw tree structure
        tree_y_start = 6.5
        if len(heap.heap) > 0:
            # Level 0 (root - min)
            draw_tree_node(ax, 5, tree_y_start, heap.heap[0], 0, True)
            
            # Level 1 (max level)
            if len(heap.heap) > 1:
                draw_tree_node(ax, 3.5, tree_y_start - 1.5, heap.heap[1], 1, False)
                ax.plot([5, 3.5], [tree_y_start - 0.25, tree_y_start - 1.25], 'k-', linewidth=1.5)
            
            if len(heap.heap) > 2:
                draw_tree_node(ax, 6.5, tree_y_start - 1.5, heap.heap[2], 1, False)
                ax.plot([5, 6.5], [tree_y_start - 0.25, tree_y_start - 1.25], 'k-', linewidth=1.5)
            
            # Level 2 (min level)
            positions = [(2.5, 3), (3.5, 4), (5.5, 5), (6.5, 6)]
            for idx, (x_pos, heap_idx) in enumerate(positions):
                if heap_idx < len(heap.heap):
                    y_pos = tree_y_start - 3
                    draw_tree_node(ax, x_pos, y_pos, heap.heap[heap_idx], 2, True)
                    parent_idx = (heap_idx - 1) // 2
                    if parent_idx == 1:
                        ax.plot([3.5, x_pos], [tree_y_start - 1.75, y_pos + 0.25], 
                               'k-', linewidth=1.5)
                    elif parent_idx == 2:
                        ax.plot([6.5, x_pos], [tree_y_start - 1.75, y_pos + 0.25], 
                               'k-', linewidth=1.5)
        
        # Add legend
        legend_y = 1.5
        ax.add_patch(Circle((1.5, legend_y), 0.15, facecolor='lightgreen', edgecolor='black'))
        ax.text(2, legend_y, 'Min Level (even)', va='center', fontsize=10)
        
        ax.add_patch(Circle((5, legend_y), 0.15, facecolor='lightcoral', edgecolor='black'))
        ax.text(5.5, legend_y, 'Max Level (odd)', va='center', fontsize=10)
        
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Min-Max Heap visualization saved to {filename}")
    
    def visualize_binomial_heap(self, values, filename="binomial_heap.png"):
        """Visualize Binomial Heap structure"""
        heap = BinomialHeap()
        for val in values:
            heap.insert(val)
        
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
        ax.text(7, 9.5, 'Binomial Heap Structure', 
               ha='center', fontsize=16, fontweight='bold')
        
        # Get binomial trees
        trees = heap.get_trees()
        
        if trees:
            x_start = 1
            for tree in trees:
                # Draw tree info
                ax.text(x_start + 1, 8.5, f'B{tree.degree}', 
                       fontsize=12, fontweight='bold',
                       bbox=dict(boxstyle='round', facecolor='wheat'))
                
                # Draw root
                circle = Circle((x_start + 1, 7.5), 0.3, 
                              facecolor='lightblue', edgecolor='black', linewidth=2)
                ax.add_patch(circle)
                ax.text(x_start + 1, 7.5, str(tree.key), 
                       ha='center', va='center', fontsize=11, fontweight='bold')
                
                # Draw children indication
                if tree.child:
                    ax.text(x_start + 1, 6.8, f'↓ {tree.degree} children', 
                           ha='center', fontsize=8, style='italic')
                
                x_start += 3
        
        # Add description
        desc_y = 5
        ax.text(7, desc_y, 'Binomial Heap Properties:', 
               ha='center', fontsize=12, fontweight='bold')
        ax.text(7, desc_y - 0.5, '• Collection of binomial trees', ha='center', fontsize=10)
        ax.text(7, desc_y - 1, '• At most one tree of each degree', ha='center', fontsize=10)
        ax.text(7, desc_y - 1.5, f'• Bk has 2^k nodes and height k', ha='center', fontsize=10)
        ax.text(7, desc_y - 2, f'• Total trees: {len(trees)}', ha='center', fontsize=10)
        ax.text(7, desc_y - 2.5, f'• Total nodes: {len(heap)}', ha='center', fontsize=10)
        
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Binomial Heap visualization saved to {filename}")
    
    def create_complexity_chart(self, filename="complexity_comparison.png"):
        """Create complexity comparison chart"""
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # Data
        heaps = ['Binomial', 'Fibonacci', 'Min-Max', 'Pairing', 'Leftist', 'Skew']
        operations = ['Insert', 'Find-Min', 'Delete-Min', 'Merge']
        
        # Complexity data (simplified for visualization)
        complexity_data = {
            'Binomial': ['O(log n)', 'O(1)*', 'O(log n)', 'O(log n)'],
            'Fibonacci': ['O(1)*', 'O(1)', 'O(log n)*', 'O(1)*'],
            'Min-Max': ['O(log n)', 'O(1)', 'O(log n)', 'O(n)'],
            'Pairing': ['O(1)*', 'O(1)', 'O(log n)*', 'O(1)*'],
            'Leftist': ['O(log n)', 'O(1)', 'O(log n)', 'O(log n)'],
            'Skew': ['O(log n)*', 'O(1)', 'O(log n)*', 'O(log n)*']
        }
        
        # Create table
        cell_text = []
        for heap in heaps:
            cell_text.append(complexity_data[heap])
        
        # Color coding
        colors = []
        for heap in heaps:
            row_colors = []
            for comp in complexity_data[heap]:
                if 'O(1)' in comp:
                    row_colors.append('#90EE90')  # Light green - best
                elif 'O(log n)' in comp:
                    row_colors.append('#FFD700')  # Gold - good
                else:
                    row_colors.append('#FFB6C1')  # Light pink - slower
            colors.append(row_colors)
        
        table = ax.table(cellText=cell_text,
                        rowLabels=heaps,
                        colLabels=operations,
                        cellColours=colors,
                        cellLoc='center',
                        loc='center',
                        bbox=[0.1, 0.2, 0.8, 0.6])
        
        table.auto_set_font_size(False)
        table.set_fontsize(11)
        table.scale(1, 2.5)
        
        # Style header
        for i in range(len(operations)):
            table[(0, i)].set_facecolor('#4472C4')
            table[(0, i)].set_text_props(weight='bold', color='white')
        
        # Style row labels
        for i in range(len(heaps)):
            table[(i+1, -1)].set_facecolor('#D9E1F2')
            table[(i+1, -1)].set_text_props(weight='bold')
        
        ax.axis('off')
        ax.set_title('Time Complexity Comparison\n(* indicates amortized complexity)', 
                    fontsize=16, fontweight='bold', pad=20)
        
        # Add legend
        legend_elements = [
            patches.Patch(facecolor='#90EE90', label='O(1) - Constant'),
            patches.Patch(facecolor='#FFD700', label='O(log n) - Logarithmic'),
            patches.Patch(facecolor='#FFB6C1', label='O(n) - Linear')
        ]
        ax.legend(handles=legend_elements, loc='upper right', fontsize=10)
        
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Complexity chart saved to {filename}")


def main():
    """Generate all visualizations"""
    if not PLOTTING_AVAILABLE:
        print("Error: matplotlib is required for visualization")
        print("Install with: pip install matplotlib")
        return
    
    print("Generating heap visualizations...")
    print("=" * 60)
    
    visualizer = HeapVisualizer()
    output_dir = os.path.dirname(__file__) or '.'
    
    # Sample data
    sample_data = [10, 5, 20, 15, 30, 25, 8, 12, 40, 3]
    
    # Generate visualizations
    try:
        print("\n1. Creating Min-Max Heap visualization...")
        visualizer.visualize_min_max_heap(
            sample_data, 
            os.path.join(output_dir, 'min_max_heap_structure.png')
        )
        
        print("\n2. Creating Binomial Heap visualization...")
        visualizer.visualize_binomial_heap(
            sample_data,
            os.path.join(output_dir, 'binomial_heap_structure.png')
        )
        
        print("\n3. Creating complexity comparison chart...")
        visualizer.create_complexity_chart(
            os.path.join(output_dir, 'complexity_comparison_chart.png')
        )
        
        print("\n" + "=" * 60)
        print("All visualizations generated successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nError generating visualizations: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()


