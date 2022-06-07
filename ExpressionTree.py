import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None

    # this function takes in the input string expr and 
    # creates the expression tree

    def hasChild(self, node):
        return node.lChild != None or node.rChild != None

    def create_tree (self, expr):
        stack = Stack()
        current = Node()
        self.root = current
        lis = expr.split()
        for i in range(len(lis)):
            if lis[i] == "(":
                new = Node()
                current.lChild = new
                stack.push(current)
                current = new
            elif lis[i] in operators:
                current.data = lis[i]
                stack.push(current)
                new = Node()
                current.rChild = new
                current = current.rChild
            elif lis[i] == ")":
                current = stack.pop()
            else:
                current.data = lis[i]
                current = stack.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        if aNode.data == None: return 0.0
        if aNode.data in operators:
            left = self.evaluate(aNode.lChild)
            right = self.evaluate(aNode.rChild)
            return eval(f"{left}{aNode.data}{right}")

        return float(aNode.data)
    
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        str = f"{aNode.data}"
        if aNode.lChild != None:
            str += self.pre_order(aNode.lChild)
            str += self.pre_order(aNode.rChild)
        return str


    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        str = f"{aNode.data}"
        if aNode.lChild != None:
            str = self.post_order(aNode.rChild) + str
            str = self.post_order(aNode.lChild) + str
        return str

def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
