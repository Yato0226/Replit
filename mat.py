import matplotlib.pyplot as plt
import networkx as nx
import datetime
import sys

# Define the graph
G = nx.DiGraph()

# Node data
def get_node_data():
    return {
        "Start": ("Start", "ellipse", "lightblue"),
        "Brainstorm": ("Brainstorming\n(Feb 3)", "box", "lightgrey"),
        "MarketResearch": ("Market Research", "box", "lightblue"),
        "CustomerValidation": ("Customer Validation", "box", "lightblue"),
        "ChooseProduct": ("Choosing Product\n(Feb 5)", "box", "lightgrey"),
        "CD": ("Concept Development", "box", "lightgrey"),
        "Proposal": ("Product Proposal\n(Feb 6-10)", "box", "lightgrey"),
        "Approval": ("Product Approval\n(Feb 10)", "box", "lightgrey"),
        "RRL": ("Gathering RRLs & RRS\n(Feb 13)", "box", "lightgrey"),
        "DP": ("Design & Planning", "box", "lightgrey"),
        "Sketch": ("Draft Sketch\n(Feb 21)", "box", "lightgrey"),
        "Materials": ("Materials & Costing\n(Feb 24-35)", "box", "lightgrey"),
        "MP": ("Material Procurement", "box", "lightgrey"),
        "PD": ("Prototype Development\n(Mar 6-36)", "box", "lightgrey"),
        "TC": ("Testing & Calibration\n(Mar 28)", "box", "lightgrey"),
        "AN": ("Adjustments Needed?", "diamond", "lightyellow"),
        "FA": ("Final Adjustments", "box", "lightgrey"),
        "Marketing": ("Marketing Strategy", "box", "lightgreen"),
        "Production": ("Production", "box", "lightgreen"),
        "Distribution": ("Distribution", "box", "lightgreen"),
        "DD": ("Deployment & Demo\n(Apr 3)", "box", "lightgreen"),
        "End": ("End", "ellipse", "lightcoral"),
    }

nodes = get_node_data()
for key, (label, shape, color) in nodes.items():
    G.add_node(key, label=label, shape=shape, color=color)

# Edges and labels
edges = [
    ("Start", "Brainstorm"), ("Brainstorm", "MarketResearch"), ("MarketResearch", "CustomerValidation"),
    ("CustomerValidation", "ChooseProduct"), ("ChooseProduct", "CD"), ("CD", "Proposal"),
    ("Proposal", "Approval"), ("Approval", "RRL"), ("RRL", "DP"),
    ("DP", "Sketch"), ("Sketch", "Materials"), ("Materials", "MP"),
    ("MP", "PD"), ("PD", "TC"), ("TC", "AN"), ("AN", "FA"),
    ("FA", "TC"), ("AN", "Marketing"), ("Marketing", "Production"),
    ("Production", "Distribution"), ("Distribution", "DD"), ("DD", "End"),
]
edge_labels = {("AN", "FA"): "Yes", ("AN", "Marketing"): "No"}
G.add_edges_from(edges)

# --- Adjust node spacing ---
# Option A: Scale manual positions by a factor (<1 packs nodes closer)
scale_factor = 0.4  # reduce from 0.6 to 0.4 to compress nodes
manual_positions = {
    "Start": (0, 0), "Brainstorm": (2, 0), "MarketResearch": (4, 0), "CustomerValidation": (6, 0),
    "ChooseProduct": (8, 0), "CD": (10, 0), "Proposal": (10, -2), "Approval": (8, -2),
    "RRL": (6, -2), "DP": (4, -2), "Sketch": (4, -4), "Materials": (6, -4),
    "MP": (8, -4), "PD": (10, -4), "TC": (12, -4), "AN": (12, -6),
    "FA": (10, -6), "Marketing": (12, -8), "Production": (10, -8),
    "Distribution": (8, -8), "DD": (6, -8), "End": (4, -8),
}
compressed_pos = {n: (x*scale_factor, y*scale_factor) for n,(x,y) in manual_positions.items()}

# # Option B: Automatic spring layout (uncomment to use)
#compressed_pos = nx.spring_layout(G, k=0.3, iterations=50)

# Draw
plt.figure(figsize=(14, 9))
nx.draw_networkx_edges(G, compressed_pos, arrows=True, arrowstyle='-|>', connectionstyle='arc3,rad=0.05')
for node, (label, shape, color) in nodes.items():
    x, y = compressed_pos[node]
    boxstyle = "circle,pad=0.5" if shape=="ellipse" else ("round4,pad=0.5" if shape=="diamond" else "round,pad=0.5")
    plt.text(x, y, label, ha="center", va="center", bbox=dict(boxstyle=boxstyle, fc=color, ec="black"), fontsize=9)
for (u,v),lbl in edge_labels.items():
    x1,y1=compressed_pos[u]
    x2,y2=compressed_pos[v]
    mx,my=(x1+x2)/2,(y1+y2)/2
    offset=(10,12) if (u,v)==("AN","Marketing") else (0,12)
    plt.annotate(lbl,(mx,my),textcoords="offset points",xytext=offset,ha='center',color='red',fontsize=9)
plt.axis('off')
plt.tight_layout()
filename = f"dripomatic_flowchart_{datetime.datetime.now():%Y%m%d_%H%M%S}.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
print(f"Saved flowchart as {filename}")
sys.exit()
