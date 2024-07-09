
import pytest
import src.graph as graph

def test_create_plot():
    speeds = [10, 20, 30]
    distance_per_revolution = 1.52
    fig, ax = graph.create_plot(speeds, distance_per_revolution)
    assert ax is not None
