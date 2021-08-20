class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

root = node(10)

root.left = node(9)
root.right = node(11)

def check_binary_tree(root):
    flag = True
    stack = []
    curr = root
    while flag:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
            if curr is not None:
                if curr.left > curr.right:
                    flag = False

        elif stack:
            curr = stack.pop()
            print(curr.data,end=" ")
            curr = curr.right
            if curr is not None:
                if curr.left>curr.right:
                    flag = False

        else:
            break

print(check_binary_tree(root))