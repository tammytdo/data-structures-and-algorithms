import pytest
from graph import Graph, Vertex

@pytest.fixture
def graph_g():
    g = Graph()
    g.add_vertex('coffee')
    g.add_vertex('tea')
    g.add_vertex('juice')
    g.add_vertex('coconut water')
    return g

def test_exists_graph():
    assert Graph

def test_exists_vertex():
    assert Vertex

def test_add_vertex_single(graph_g):
    coffee_var = graph_g.add_vertex('coffee')
    assert isinstance(coffee_var, Vertex)
    assert coffee_var.value == 'coffee'

def test_add_vertex_many(graph_g):
    coffee_var = graph_g.add_vertex('coffee')
    tea_var = graph_g.add_vertex('tea')
    juice_var = graph_g.add_vertex('juice')
    assert coffee_var.value == 'coffee'
    assert tea_var.value == 'tea'
    assert juice_var.value == 'juice'

def test_get_vertex_single(graph_g):
    nodes = graph_g.get_vertices()
    assert len(nodes) == 4
    assert nodes[2].value == 'juice'

def test_get_vertex_many(graph_g):
    nodes = graph_g.get_vertices()
    assert len(nodes) == 4
    assert {node.value for node in nodes} == set(['coffee','tea','juice', 'coconut water'])

def test_length(graph_g):
    assert len(graph_g) == 4

def test_graph_empty():
    g = Graph()
    assert g.get_vertices() == None

def test_add_edge(graph_g):
    coffee_var = graph_g.add_vertex('coffee')
    tea_var = graph_g.add_vertex('tea')
    graph_g.add_edge(coffee_var, tea_var, 10)
    coffee_tea_edge = coffee_var.neighbors[0]
    
    assert coffee_tea_edge.vertex == tea_var
    assert coffee_tea_edge.weight == 10
    assert len(tea_var.neighbors) == 0

def test_get_vertex_neighbors():
    g = Graph()
    coffee_var = g.add_vertex('coffee')
    tea_var = g.add_vertex('tea')
    juice_var = g.add_vertex('juice')
    g.add_edge(coffee_var, tea_var, 10)
    g.add_edge(coffee_var, juice_var, 20)
    neighbors = g.get_neighbors(coffee_var)
    
    assert neighbors[0].vertex.value == 'tea'
    assert neighbors[0].weight == 10
    assert neighbors[1].vertex.value == 'juice'
    assert neighbors[1].weight == 20

def test_self_loop():
    g = Graph()
    coffee_var = g.add_vertex('coffee')
    g.add_edge(coffee_var, coffee_var)

    neighbors = g.get_neighbors(coffee_var)
    nodes = g.get_vertices()
    assert neighbors[0].vertex.value == 'coffee'
    assert neighbors[0].weight == 0
    assert [node.value for node in nodes] == ['coffee']