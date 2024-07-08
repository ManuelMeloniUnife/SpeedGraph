# tests/integration/test_integration.py
import pytest
from src.utils import read_speeds_from_file, populate_table
from src.graph import create_plot
from tkinter import Tk, ttk

def test_integration(tmp_path):
    data = "0,00\n1,23\n4,56\n7,89\n"
    file_path = tmp_path / "speeds.txt"
    file_path.write_text(data)

    speeds = read_speeds_from_file(file_path)
    assert speeds == [1.23, 4.56, 7.89]

    root = Tk()
    table = ttk.Treeview(root)
    populate_table(table, speeds, 1.52)

    rows = table.get_children()
    assert len(rows) == 3
    assert table.item(rows[0])['values'] == ['1.52', '1.23']
    assert table.item(rows[1])['values'] == ['3.04', '4.56']
    assert table.item(rows[2])['values'] == ['4.56', '7.89']

    fig, ax = create_plot(speeds, 1.52)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
