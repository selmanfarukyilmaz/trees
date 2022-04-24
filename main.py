from typing import Optional
import re


class Tree:

    def __init__(self):
        self.head: Optional[Node] = None

    def __str__(self) -> str:
        return f"{self.head.data}"


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"{self.data}"


def print_inorder(root, traversal=""):
    """Left->Root->Right"""
    if root:
        traversal = print_inorder(root.left, traversal)
        traversal += (str(root.data) + "-")
        traversal = print_inorder(root.right, traversal)
    return traversal


def print_preorder(root, traversal=""):
    """Root->Left->Right"""
    if root:
        traversal += (str(root.data) + "-")
        traversal = print_preorder(root.left, traversal)
        traversal = print_preorder(root.right, traversal)
    return traversal


def print_postorder(root, traversal=""):
    """Left->Right->Root"""
    if root:
        traversal = print_postorder(root.left, traversal)
        traversal = print_postorder(root.right, traversal)
        traversal += (str(root.data) + "-")
    return traversal


def insert(root, data):
    if root.data == None:
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


def create_tree(n: int, root):
    lst = list(range(1, n + 1))
    print(lst)
    for value in lst:
        insert(root, value)


def deleteTree(root):
    if root:
        deleteTree(root.left)
        deleteTree(root.right)
        print("Deleting Node:", root.data)
        del root.data, root.right, root.left


def find_max(root):
    all_data = print_inorder(root)
    all_data = map(int, re.findall(r'\d+', all_data))
    print(max(list(all_data)))


def find_min(root):
    all_data = print_inorder(root)
    all_data = map(int, re.findall(r'\d+', all_data))
    print(min(list(all_data)))


def findNumNode(root):
    all_data = print_inorder(root)
    all_data = map(int, re.findall(r'\d+', all_data))
    print(len(list(all_data)))


def calculateAverage(root):
    all_data = print_inorder(root)
    all_data = list(map(int, re.findall(r'\d+', all_data)))

    sum_num = 0
    for value in all_data:
        sum_num = sum_num + value

    avg = sum_num / len(all_data)
    print(avg)


tree = Tree()
tree.head = Node(None)
create_tree(6, tree.head)
find_min(tree.head)
find_max(tree.head)
print_inorder(tree.head)
deleteTree(tree.head)
findNumNode(tree.head)
calculateAverage(tree.head)
print(tree.head)
print(tree.head.left)
print(tree.head.right)
