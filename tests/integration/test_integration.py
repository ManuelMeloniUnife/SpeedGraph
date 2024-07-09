
import pytest
from src.utils import read_speeds_from_file, populate_table
from src.graph import create_plot
from tkinter import Tk, ttk

def test_integration():
    root = Tk()
    table = ttk.Treeview(root, columns=("Metri", "Velocità"), show="headings")
    table.heading("Metri", text="meters")
    table.heading("Velocità", text="speed [Km/h]")
    table.column("Metri", width=100)
    table.column("Velocità", width=100)

    speeds = read_speeds_from_file('path_to_your_test_file.txt') 
    distance_per_revolution = 1.52
    populate_table(table, speeds, distance_per_revolution)

    fig, ax = create_plot(speeds, distance_per_revolution)
    assert fig is not None
    assert ax is not None
