import networkx as nx
import matplotlib.pyplot as plt

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_linked_list_graph(head):
    G = nx.Graph()
    current = head
    while current and current.next:
        G.add_edge(current.val, current.next.val)
        current = current.next
    return G

def generate_spanning_trees(G):
    spanning_trees = []
    for spanning_tree_edges in nx.generators.trees.all_spanning_trees(G):
        T = nx.Graph()
        T.add_edges_from(spanning_tree_edges)
        spanning_trees.append(T)
    return spanning_trees

def visualize_spanning_trees(spanning_trees):
    for i, tree in enumerate(spanning_trees, start=1):
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(tree)
        nx.draw(tree, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=20, font_weight="bold")
        plt.title(f"Spanning Tree {i}")
        plt.show()

# Example usage:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

# Generate the graph from linked list
G = generate_linked_list_graph(head)

# Generate all possible spanning trees
spanning_trees = generate_spanning_trees(G)

# Visualize all spanning trees
visualize_spanning_trees(spanning_trees)
