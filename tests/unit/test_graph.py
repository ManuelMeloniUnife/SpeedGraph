# tests/unit/test_graph.py
from src.graph import create_plot
import matplotlib.pyplot as plt

def test_create_plot():
    speeds_1 = [10, 20, 30]
    distance_per_revolution = 1.5

    fig, ax = create_plot(speeds_1, distance_per_revolution)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
