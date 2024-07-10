# tests/unit/test_graph.py
import pytest
import matplotlib.pyplot as plt
from src.graph import create_plot

@pytest.fixture
def single_speed_data():
    speeds = [10, 20, 30, 40]
    distance_per_revolution = 2.0
    return speeds, distance_per_revolution

@pytest.fixture
def dual_speed_data():
    speeds_1 = [10, 20, 30, 40]
    speeds_2 = [15, 25, 35, 45]
    distance_per_revolution = 2.0
    return speeds_1, speeds_2, distance_per_revolution

@pytest.mark.mpl_image_compare
def test_create_plot_single_speed(single_speed_data):
    speeds, distance_per_revolution = single_speed_data

    fig, ax = create_plot(speeds, distance_per_revolution)
    ax.set_title('Test Plot - Single Speed')

    return fig

@pytest.mark.mpl_image_compare
def test_create_plot_dual_speed(dual_speed_data):
    speeds_1, speeds_2, distance_per_revolution = dual_speed_data

    fig, ax = create_plot(speeds_1, distance_per_revolution, speeds_2)
    ax.set_title('Test Plot - Dual Speed')

    return fig
