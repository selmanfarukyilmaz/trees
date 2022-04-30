class Tree:
    def __init__(self, root):
        self.root = root


class Node:

    def __init__(self, data: int or bool):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"{self.data}"


def print_inorder(root: Node):
    """Left->Root->Right"""
    if root:
        print_inorder(root.left)
        print(str(root.data), end="-")
        print_inorder(root.right)


def print_preorder(root: Node):
    """Root->Left->Right"""
    if root:
        print(str(root.data), end="-")
        print_preorder(root.left)
        print_preorder(root.right)


def print_postorder(root: Node):
    """Left->Right->Root"""
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(str(root.data), end="-")


def insert(root: Node, data: int):
    if root.data is None:
        root.data = data
        return
    q = [root]

    while len(q):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Node(data)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = Node(data)
            break
        else:
            q.append(temp.right)


def create_tree(n: int, root: Node):
    lst = list(range(1, n + 1))
    for value in lst:
        insert(root, value)


def remove_tree(root: Node):
    if root:
        remove_tree(root.left)
        remove_tree(root.right)
        print("Deleting Node:", root.data)
        del root.data, root.right, root.left


def find_max(root: Node, temp_max: int) -> int or float:
    # Base case
    if root is None:
        return float('-inf')

    curdata = root.data
    ldata = find_max(root.left, temp_max)
    rdata = find_max(root.right, temp_max)

    return max(temp_max, rdata, ldata, curdata)


def find_min(root: Node) -> int or float:
    if root is None:
        return float('+inf')

    curdata = root.data
    ldata = find_min(root.left)
    rdata = find_min(root.right)
    print(rdata, ldata, curdata)

    return min(rdata, ldata, curdata)


def find_num_node(root: Node) -> int:
    if root is None:
        return 0

    lcount = find_num_node(root.left)
    rcount = find_num_node(root.right)

    count = lcount + rcount + 1

    return count


def calculate_sum(root: Node) -> int:
    if root is None:
        return 0

    curvalue = root.data
    lvalues = calculate_sum(root.left)
    rvalues = calculate_sum(root.right)

    total = lvalues + rvalues + curvalue

    return total


def calculate_average(root: Node) -> float:
    return calculate_sum(root) / find_num_node(root)


def find_num_leaf(root: Node):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    lvalues = find_num_leaf(root.left)
    rvalues = find_num_leaf(root.right)

    leaf = lvalues + rvalues

    return leaf


def calculate_depth(root: Node):
    if not root:
        return 0

    if not root.left and not root.right:
        return 0

    rdepth = calculate_depth(root.right)
    ldepth = calculate_depth(root.left)

    return max(rdepth, ldepth) + 1


tree = Tree(Node(None))
create_tree(8, tree.root)
# print(print_inorder(tree.root))
# print_inorder(tree.root)
print(calculate_depth(tree.root))
# print(find_min(tree.root))
# print(find_min(tree, int(tree.root)))
# print(find_num_node(tree.root))
# print(calculate_average(tree.root))
# print(find_num_leaf(tree.root))


# remove_tree(tree.root)
