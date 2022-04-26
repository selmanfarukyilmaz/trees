class Node:

    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

    # def __gt__(self, other):
    #     return self.data > other.data

    def __str__(self) -> str:
        return f"{self.data}"

    def __int__(self):
        return self.data


def print_inorder(root: Node, traversal="") -> str:
    """Left->Root->Right"""
    if root:
        traversal = print_inorder(root.left, traversal)
        traversal += (str(root.data) + "-")
        traversal = print_inorder(root.right, traversal)
    return traversal


def print_preorder(root: Node, traversal="") -> str:
    """Root->Left->Right"""
    if root:
        traversal += (str(root.data) + "-")
        traversal = print_preorder(root.left, traversal)
        traversal = print_preorder(root.right, traversal)
    return traversal


def print_postorder(root: Node, traversal="") -> str:
    """Left->Right->Root"""
    if root:
        traversal = print_postorder(root.left, traversal)
        traversal = print_postorder(root.right, traversal)
        traversal += (str(root.data) + "-")
    return traversal


def insert(root: Node, data: int):
    if root.data is None:
        root.data = Node(data)
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

    if type(curdata) != int:
        curdata = int(curdata)
        # print(res)
    if ldata > curdata:
        curdata = ldata

    if rdata > curdata:
        curdata = rdata

    if curdata > temp_max:
        temp_max = curdata

    return temp_max


def find_min(root: Node, temp_min: int) -> int or float:
    # Base case
    if root is None:
        return float('+inf')

    curdata = root.data
    ldata = find_min(root.left, temp_min)
    rdata = find_min(root.right, temp_min)

    if type(curdata) != int:
        curdata = int(curdata)
        # print(res)
    if ldata < curdata:
        curdata = ldata

    if rdata < curdata:
        curdata = rdata

    if curdata < temp_min:
        temp_min = curdata

    return temp_min


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

    total = lvalues + rvalues + int(curvalue)

    return total


def calculate_average(root: Node) -> float:
    return calculate_sum(root) / find_num_node(root)


def find_num_leaf(root: Node):
    if root.left is None:
        return 1

    lvalues = find_num_leaf(root.left)
    rvalues = find_num_leaf(root.right)

    leaf = lvalues + rvalues

    return leaf


def calculate_depth(root: Node): #todo
    pass


tree = Node(None)
create_tree(13, tree)
print(print_inorder(tree))

print(find_max(tree, int(tree.data)))
print(find_min(tree, int(tree.data)))
print(find_num_node(tree))
print(calculate_average(tree))
print(find_num_leaf(tree)) #todo

# remove_tree(tree)
