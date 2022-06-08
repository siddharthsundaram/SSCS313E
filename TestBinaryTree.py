

#  File: TestBinaryTree.py

#  Description: Methods for a Binary Tree

#  Student Name: Siddharth Sundaram

#  Student UT EID: svs833

#  Partner Name: Lauren Adams

#  Partner UT EID: la27334

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 03/22/2022

#  Date Last Modified:


import sys


class Node (object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):

        if self.lChild != None:
            self.lChild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rChild != None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild != None and self.rChild != None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild != None:
            return 1 + self.lChild.get_height()
        elif self.rChild != None:
            return 1 + self.rChild.get_height()
        else:
            return 1

    def sumNodes(self):
        current = self

        # base case
        if current.lChild == None and current.rChild == None: return current.data

        # recursion until base case
        if current.lChild != None and current.rChild != None:
            return current.lChild.sumNodes() + current.rChild.sumNodes()
        if current.lChild == None and current.rChild != None:
            return current.rChild.sumNodes()
        if current.rChild == None and current.lChild != None:
            return current.lChild.sumNodes()

    def getLevel(self, level, count = 0, lis = None):
        if self == None: return []

        if lis == None: lis = []

        current = self

        # base case
        if count == level: lis.append(current)

        # recursion until base case
        elif count != level and (current.lChild != None or current.rChild != None):
            count += 1
            if current.lChild != None:
                current.lChild.getLevel(level, count, lis)
            if current.rChild != None:
                current.rChild.getLevel(level, count, lis)

        return lis


class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        if self.root.lChild == None and self.root.rChild == None: return 0
        currentL = self.root
        currentR = self.root

        # moves currentL to smallest value
        while currentL.lChild != None:
            currentL = currentL.lChild

        # moves currentR to largest value
        while currentR.rChild != None:
            currentR = currentR.rChild

        # returns largest - smallest
        return currentR.data - currentL.data

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        # returns empty list if root is none
        if self.root == None: return []

        # calls helper function from Node class so recursion can be used
        lis = self.root.getLevel(level)

        return lis

    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        lis = []
        h = self.get_height()

        # loop runs for however many levels the tree has
        for i in range(h):

            # calls get_level func on each level of tree and stores into leftMost (type list)
            leftMost = self.get_level(i)

            # adds first element of list (leftmost node of each level) to lis
            if len(leftMost) > 0:
                lis.append(leftMost[0].data)

        return lis


    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_node(self):
        # call to helper function in Node class
        total = self.root.sumNodes()

        return total



def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is: ",   t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_node())
    print("##########################")

# Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())

    print("Tree range is: ",   t2.range())
    print("Tree left side view is: ", t2.left_side_view())
    print("Sum of leaf nodes is: ", t2.sum_leaf_node())
    print("##########################")
# Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print("Tree range is: ",   t3.range())
    print("Tree left side view is: ", t3.left_side_view())
    print("Sum of leaf nodes is: ", t3.sum_leaf_node())
    print("##########################")


if __name__ == "__main__":
    main()



