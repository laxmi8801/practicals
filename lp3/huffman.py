class Node:
    def __init__(self,char,freq,left=None,right=None):
        self.char = char
        self.freq= freq
        self.left = left
        self.right = right
        self.huff = ' '
        
def printnode(Node,val = ''):
    nval = val + str(Node.huff)
    
    if Node.left:
        printnode(Node.left,nval)
    if Node.right:
        printnode(Node.right,nval)
    
    if len(Node.char)==1:
        print(f"{Node.char}==>{nval}")
        


chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [ 5, 9, 12, 13, 16, 45]
nodes = []

for i in range(len(chars)):
    nodes.append(Node(chars[i],freq[i]))

while len(nodes)>1:
    nodes = sorted(nodes,key=lambda x:x.freq)
    left = nodes[0]
    left.huff = 0
    right = nodes[1]
    right.huff = 1
    newnode = Node(left.char+right.char,left.freq+right.freq,left,right)
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newnode)
    
printnode(nodes[0])
