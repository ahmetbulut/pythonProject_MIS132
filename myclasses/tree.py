class Tree:
    """
    Each node stores a value in attributed named value.
    Each node has a left child, and a right child.
    Any of the children could be Null, None, NaN.
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def compute_total_value(tree):
    if tree is None: return 0
    # compute the sum of the values in the left subtree
    # compute the sum of the values in the right subtree
    # add your own value to the above two sums.
    return tree.value \
           + compute_total_value(tree.left) \
           + compute_total_value(tree.right)

def print_computation(tree):
    if tree is None: return ""
    return print_computation(tree.left) + str(tree.value) + print_computation(tree.right)


leaf_node1 = Tree(3)
leaf_node2 = Tree(7)
internal_node1 = Tree("+", leaf_node1, leaf_node2)

leaf_node3 = Tree(9)
root = Tree("*", internal_node1, leaf_node3)

print(print_computation(root))