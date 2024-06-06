# Завдання вирішив написати в одному файлі


# Завдання №1____________________

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_max(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.val

# Використання(У двійковому дереві пошуку найбільше значення завжди знаходиться в правому піддереві самого правого вузла):
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.right.right = TreeNode(40)
print("Найбільше значення:", find_max(root))


# Завдання №2____________________

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.val

# Приклад використання
print("Найменше значення:", find_min(root))


# Завдання №3____________________

def sum_tree(node):
    if node is None:
        return 0
    return node.val + sum_tree(node.left) + sum_tree(node.right)

# Приклад використання
print("Сума всіх значень у дереві:", sum_tree(root))
