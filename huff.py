import heapq

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""
    
    def __lt__(self, other):
        return self.freq < other.freq
    
def printNodes(node, val=""):
    newval = val + node.huff
    if node.left:
        printNodes(node.left, newval)
    if node.right:
        printNodes(node.right, newval)
    else:
        print(f"{node.symbol} -> {newval}")

chars = ["a", "b", "c", "d", "e", "f"]
freqs = [5, 9, 12, 13, 16, 45]
nodes = []

for i in range(len(chars)):
    heapq.heappush(nodes, node(freqs[i], chars[i]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.huff = "0"
    right.huff = "1"
    newnode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, newnode)

printNodes(nodes[0])

"""
import heapq
This imports the heapq library, which provides a min-heap implementation. A min-heap is used here to manage nodes based on their frequencies in ascending order.
Node Class Definition
python

Copy code
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""
Defines a class node, which represents each character in the Huffman Tree.
freq: Frequency of the character.
symbol: The character itself.
left and right: Pointers to the left and right children (used to build the tree).
huff: A string to store "0" or "1" based on whether the node is a left or right child.
python

Copy code
    def __lt__(self, other):
        return self.freq < other.freq
This method allows nodes to be compared based on freq. The heapq library relies on this comparison to arrange nodes by frequency in ascending order.
Printing Nodes and their Huffman Codes
python

Copy code
def printNodes(node, val=""):
    newval = val + node.huff
Defines printNodes, a recursive function to generate Huffman codes by traversing the tree.
newval appends the huff value ("0" or "1") to the existing code string val.
python

Copy code
    if node.left:
        printNodes(node.left, newval)
    if node.right:
        printNodes(node.right, newval)
If node.left exists, it recursively calls printNodes on the left child, passing the updated code.
If node.right exists, it calls printNodes on the right child with the updated code.
python

Copy code
    else:
        print(f"{node.symbol} -> {newval}")
If a node is a leaf (no children), it prints the symbol and its Huffman code, which is stored in newval.
Initializing Character and Frequency Lists
python

Copy code
chars = ["a", "b", "c", "d", "e", "f"]
freqs = [5, 9, 12, 13, 16, 45]
nodes = []
chars and freqs lists hold the characters and their frequencies.
nodes is an empty list that will become a priority queue of node objects.
Creating Nodes and Building the Priority Queue
python

Copy code
for i in range(len(chars)):
    heapq.heappush(nodes, node(freqs[i], chars[i]))
This loop iterates over each character and its frequency.
For each character-frequency pair, it creates a node object and pushes it onto the nodes heap (priority queue).
Constructing the Huffman Tree
python

Copy code
while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
This while loop continues until only one node (the root) remains in the nodes heap.
heapq.heappop(nodes) pops the two nodes with the smallest frequencies (left and right).
python

Copy code
    left.huff = "0"
    right.huff = "1"
Assigns "0" to the huff attribute of the left node and "1" to the right node to signify their binary codes.
python

Copy code
    newnode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
Creates a new node that represents the combined frequency of left and right.
left and right are set as the children of newnode, forming the next level in the Huffman Tree.
python

Copy code
    heapq.heappush(nodes, newnode)
Pushes the newly created newnode back onto the nodes heap.
The process repeats until only one node, representing the root of the Huffman Tree, remains.
Printing the Huffman Codes
python

Copy code
printNodes(nodes[0])
Calls printNodes on the root node (now the only node in nodes).
This initiates a recursive traversal of the Huffman Tree, printing each character’s symbol and its generated Huffman code."""