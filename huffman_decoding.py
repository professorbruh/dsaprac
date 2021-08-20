class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None


def decodeHuff(root, s):
    fin = ""
    curr = root
    for i in range(0,len(s)):
        if s[i] == '0':
             curr = curr.left
        else:
            curr = curr.right
        if curr.left == None and curr.right == None:
            fin += curr.data
            curr = root
    print(fin)


