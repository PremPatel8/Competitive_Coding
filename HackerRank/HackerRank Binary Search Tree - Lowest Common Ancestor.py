class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    v1Path = set()
    v2Path = set()

    current = root

# Getting the path to V1
    while True:
        v1Path.add(current)

        if v1 < current.info:
            current = current.left
        elif v1 > current.info:
            current = current.right
        elif v1 == current.info:
            break
    
    current = root

    # Getting the path to V2
    while True:
        v2Path.add(current)

        if v2 < current.info:
            current = current.left
        elif v2 > current.info:
            current = current.right
        elif v2 == current.info:
            break
    
    # print("v1Path-")
    # for node in v1Path:
    #     print(node, end = ' ')
    
    # print("\n\nv2Path-")
    # for node in v2Path:
    #     print(node, end = ' ')

    c = list(v1Path & v2Path)

    # print("\n\nIntersection list-")
    # for nodes in c:
    #     print(nodes)

    return c[0]

tree = BinarySearchTree()
t = 6

arr = [4,2,3,1,7,6]

for i in range(t):
    tree.create(arr[i])

v = [1,7]

ans = lca(tree.root, v[0], v[1])
print (ans.info)
