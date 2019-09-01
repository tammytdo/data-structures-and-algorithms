# Graphs
Implement a Graph. 

## Challenge
The graph should be represented as an adjacency list, and should include the following methods:

-add_node()
-add_edge()
-get_nodes()
-get_neighbors()
-length()

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## API
add_node():
-Adds a new node to the graph
-Takes in the value of that node
-Returns the added node

add_edge()
-Adds a new edge between two nodes in the graph
-Include the ability to have a “weight”
-Takes in the two nodes to be connected by the edge
-Both nodes should already be in the Graph

get_nodes()
-Returns all of the nodes in the graph as a collection (set, list, or similar)

get_neighbors()
-Returns a collection of nodes connected to the given node
-Takes in a given node
-Include the weight of the connection in the returned collection

length()
-Returns the total number of nodes in the graph