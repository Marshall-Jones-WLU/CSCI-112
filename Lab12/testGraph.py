"""
File: testGraph.py

Marshall Jones
"""

from modules.graph.graph import LinkedDirectedGraph
from modules.graph.pathEntry import PathEntry
from modules.stack.linkedStack import LinkedStack
from modules.queue.linkedQueue import LinkedQueue
from modules.utils.grid import Grid
from modules.utils.arrays import Array
from modules.math.infinity import *


# Exercise
def traverseFromVertex(graph, startVertex, showProcess, collection = LinkedStack()):
    # graph = LinkedDirectedGraph(collection) # Instatiate a collection with a list
    graph.clearVertexMarks() # Mark all vertices in the graph as unvisited
    collection.add(startVertex) # Add the startVertex to the collection

    while not collection.isEmpty():
        vertex = collection.pop()
        if not vertex.isMarked():
            vertex.setMark()
            if showProcess:
                print(vertex.getLabel())
            neighbors = vertex.neighboringVertices()
            for i in neighbors:
                collection.add(i)
            
    
# Exercise
def depthFirstTraverse(graph, startVertex, showProcess):
    """Uses a stack to force traversal to move deeply into the graph 
    before backtracking to another path"""
    s = LinkedStack()
    traverseFromVertex(graph, startVertex, showProcess, s)

# Exercise
def breadthFirstTraverse(graph, startVertex, showProcess):
    """Uses a queue to force traversal to visit all adjacent vertices
    before moving to the next level"""
    q = LinkedQueue()
    traverseFromVertex(graph, startVertex, showProcess, q)


def newEdges(graph):
    graph.addEdge("A", "J", 1)
    graph.addEdge("A", "I", 8)
    graph.addEdge("A", "B", 3)
    graph.addEdge("B", "C", 2)
    graph.addEdge("C", "E", 4)
    graph.addEdge("C", "G", 2)
    graph.addEdge("D", "I", 1)
    graph.addEdge("D", "B", 1)
    graph.addEdge("D", "C", 1)
    graph.addEdge("F", "C", 2)
    graph.addEdge("G", "D", 1)
    graph.addEdge("G", "F", 1)
    graph.addEdge("H", "B", 2)
    graph.addEdge("H", "E", 1)
    graph.addEdge("J", "B", 1)
    graph.addEdge("J", "H", 6)

          
def main():
        
    # Create a directed graph using an adjacency list
    graph = LinkedDirectedGraph()
    
    # Exercise: Add vertices with appropriate labels and print the graph
    verts = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for i in verts:
        graph.addVertex(i)
    print("\nThe graph: \n" + str(graph))
    
    # Exercise: Insert edges with weights and print the graph
    newEdges(graph)
    print("\nThe graph: \n" + str(graph))
    
    # Print the vertices adjacent to vertex A
    print("\nExpect vertices adjacent to A:")
    print(", ".join(list(map(str,graph.getVertex("A").neighboringVertices()))))
    
    # Print the edges incident to A
    print("Expect edges incident to A:")
    print(", ".join(list(map(str,graph.getVertex("A").incidentEdges()))))
    
    # Exercise
    print("\nTraverse from vertex A:")
    traverseFromVertex(graph, graph.getVertex("A"), True)

    # Exercise
    print("\nDepth first traversal:")
    depthFirstTraverse(graph, graph.getVertex("A"), True)
    
    # Exercise
    print("\nBreadth first traversal:")
    breadthFirstTraverse(graph, graph.getVertex("A"), True)
    

if __name__ == '__main__':
    main()