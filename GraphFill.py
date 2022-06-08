#  File: GraphFill.py
#  Description:
#  Student Name: Siddharth Sundaram
#  Student UT EID: svs833
#  Partner Name: Lauren Adams
#  Partner UT EID: la27334
#  Course Name: CS 313E
#  Unique Number: 51130
#  Date Created: 04/03/2022
#  Date Last Modified:

import os
import sys
# this enables printing colors on Windows somehow
os.system("")

# code to reset the terminal color
RESET_CHAR = "\u001b[0m"
# color codes for the terminal
COLOR_DICT = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m"
}
# character code for a block
BLOCK_CHAR = "\u2588"

# Input: text is some string we want to write in a specific color
#   color is the name of a color that is looked up in COLOR_DICT
# Output: returns the string wrapped with the color code
def colored(text, color):
    color = color.strip().lower()
    if not color in COLOR_DICT:
        raise Exception(color + " is not a valid color!")
    return COLOR_DICT[color] + text

# Input: color is the name of a color that is looked up in COLOR_DICT
# prints a block (two characters) in the specified color
def print_block(color):
    print(colored(BLOCK_CHAR, color)*2, end='')

# Stack class; you can use this for your search algorithms
class Stack(object):
  def __init__(self):
    self.stack = []

  # add an item to the top of the stack
  def push(self, item):
    self.stack.append(item)

  # remove an item from the top of the stack
  def pop(self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek(self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty(self):
    return len(self.stack) == 0

  # return the number of elements in the stack
  def size(self):
    return len(self.stack)

# Queue class; you can use this for your search algorithms
class Queue(object):
  def __init__(self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue(self, item):
    self.queue.append(item)

  # remove an item from the beginning of the queue
  def dequeue(self):
    return self.queue.pop(0)

  # checks the item at the top of the Queue
  def peek(self):
    return self.queue[0]

  # check if the queue is empty
  def is_empty(self):
    return len(self.queue) == 0

  # return the size of the queue
  def size(self):
    return len(self.queue)

# class for a graph node; contains x and y coordinates, a color, a list of edges and
# a flag signaling if the node has been visited (useful for serach algorithms)
# it also contains a "previous color" attribute. This might be useful for your flood fill implementation.
class ColorNode:
    # Input: x, y are the location of this pixel in the image
    #   color is the name of a color
    def __init__(self, x, y, color):
        self.color = color
        self.prev_color = color
        self.x = x
        self.y = y
        self.edges = []
        self.visited = False

    # Input: node_index is the index of the node we want to create an edge to in the node list
    # adds an edge and sorts the list of edges
    def add_edge(self, node_index):
        self.edges.append(node_index)
        self.edges.sort()

    # Input: color is the name of the color the node should be colored in;
    # the function also saves the previous color (might be useful for your flood fill implementation)
    def set_color(self, color):
        self.prev_color = self.color
        self.color = color

# class that contains the graph
class ImageGraph:
    def __init__(self, image_size):
        self.nodes = []
        self.image_size = image_size

    # prints the image formed by the nodes on the command line
    def print_image(self):
        img = [["black" for i in range(self.image_size)] for j in range(self.image_size)]

        # fill img array
        for node in self.nodes:
            img[node.y][node.x] = node.color

        for line in img:
            for pixel in line:
                print_block(pixel)
            print()
        # print new line/reset color
        print(RESET_CHAR)

    # sets the visited flag to False for all nodes
    def reset_visited(self):
        for i in range(len(self.nodes)):
            self.nodes[i].visited = False

    # implement your adjacency matrix printing here.
    def print_adjacency_matrix(self):
        print("Adjacency matrix:")

        # 2D Array filled with 0s that will represent the adjacency matrix
        size = len(self.nodes)
        adjMatr = [[0 for i in range(size)] for j in range(size)]

        # Goes through edge list of each node and changes values to 1 where the nodes of the indices have an edge
        for i in range(size):
            edges = self.nodes[i].edges
            for j in edges:
                adjMatr[i][j] = 1
                adjMatr[j][i] = 1

        # Prints matrix without brackets, commas, or spaces
        for i in adjMatr: print("".join(map(str, i)))

        # empty line afterwards
        print()

    # implement your bfs algorithm here. Call print_image() after coloring a node
    # Input: graph is the graph containing the nodes
    #   start_index is the index of the currently visited node
    #   color is the color to fill the area containing the current node with
    def bfs(self, start_index, color):
        # reset visited status
        self.reset_visited()
        # print initial state
        print("Starting BFS; initial state:")
        self.print_image()

        # Create queue, change color and visit status of starting node, and print image
        queue = Queue()
        startNode = self.nodes[int(start_index)]
        startNode.visited = True
        startNode.set_color(color)
        colorChange = startNode.prev_color
        self.print_image()

        # Put index of start node into the queue
        queue.enqueue(int(start_index))

        # Dequeue earliest node index, visit all adjacent unvisited nodes, change color and visit status, add to queue
        while not queue.is_empty():
            v = queue.dequeue()
            for u in self.nodes[v].edges:
                node = self.nodes[u]
                # Ensures next node is both unvisited and same color as startNode
                if not node.visited and node.color == colorChange:
                    queue.enqueue(int(u))
                    node.visited = True
                    node.set_color(color)
                    self.print_image()

    # Get first unvisited node adjacent to node represented by index i and the same color as color_prev
    def get_unvisited(self, i, color_prev):
        v = self.nodes[int(i)]
        numEdges = len(v.edges)
        for i in range(numEdges):
            j = v.edges[i]
            if not self.nodes[j].visited and self.nodes[j].color == color_prev:
                return v.edges[i]
        return -1

    # implement your dfs algorithm here. Call print_image() after coloring a node
    # Input: graph is the graph containing the nodes
    #   start_index is the index of the currently visited node
    #   color is the color to fill the area containing the current node with
    def dfs(self, start_index, color):
        # reset visited status
        self.reset_visited()
        # print initial state
        print("Starting DFS; initial state:")
        self.print_image()

        # Create stack, change color and visit status of starting node, and print image
        stack = Stack()
        startNode = self.nodes[int(start_index)]
        startNode.visited = True
        startNode.set_color(color)
        colorChange = startNode.prev_color
        self.print_image()

        # Put index of start node into the stack
        stack.push(start_index)

        # Pop latest node index, visit all next unvisited nodes, change color and visit status, push onto stack
        while not stack.is_empty():
            # Ensures u is both unvisited and same color as startNode
            u = self.get_unvisited(stack.peek(), colorChange)
            if u == -1:
                u = stack.pop()
            else:
                stack.push(int(u))
                self.nodes[u].visited = True
                if self.nodes[u].color == colorChange:
                    self.nodes[u].set_color(color)
                    self.print_image()


def main():

    # Creates image graph of user input size
    size = int(input())
    graph = ImageGraph(size)

    # Takes input for number of nodes
    numNodes = int(input())

    for i in range(numNodes):

        # Splits line into x pos, y pos, and color of each node and adds the node to node list
        nodeList = input().split(",")
        graph.nodes.append(ColorNode(int(nodeList[0]), int(nodeList[1]), nodeList[2]))

    # Takes input for number of edges
    numEdges = int(input())

    for i in range(numEdges):
        # Splits line into both vertex indices
        edgeList = input().split(",")

        # Adds vertex 1 index to vertex 2 edges
        index = int(edgeList[0])
        node = graph.nodes[index]
        node.add_edge(int(edgeList[1]))

        # Adds vertex 2 index to vertex 1 edges
        index = int(edgeList[1])
        node = graph.nodes[index]
        node.add_edge(int(edgeList[0]))

    # Splits line into start node index and color
    bfs = input().split(",")
    bfs_start = bfs[0]
    bfs_color = bfs[1]

    # Splits line into start node index and color
    dfs = input().split(",")
    dfs_start = dfs[0]
    dfs_color = dfs[1]

    # print matrix
    graph.print_adjacency_matrix()

    # run bfs
    graph.bfs(bfs_start, bfs_color)

    # run dfs
    graph.dfs(dfs_start, dfs_color)


if __name__ == "__main__":
    main()
