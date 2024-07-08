# tests/unit/test_utils.py
import pytest
from src.utils import read_speeds_from_file, populate_table
from tkinter import ttk

def test_read_speeds_from_file(tmp_path):
    # Creare un file temporaneo con dati di esempio
    data = "0,00\n1,23\n4,56\n7,89\n"
    file_path = tmp_path / "speeds.txt"
    file_path.write_text(data)

    # Verificare che la funzione legga correttamente i dati
    speeds = read_speeds_from_file(file_path)
    assert speeds == [1.23, 4.56, 7.89]

def test_populate_table():
    table = ttk.Treeview()
    speeds = [1.23, 4.56, 7.89]
    distance_per_revolution = 1.52

    populate_table(table, speeds, distance_per_revolution)

    rows = table.get_children()
    assert len(rows) == 3
    assert table.item(rows[0])['values'] == ['1.52', '1.23']
    assert table.item(rows[1])['values'] == ['3.04', '4.56']
    assert table.item(rows[2])['values'] == ['4.56', '7.89']
