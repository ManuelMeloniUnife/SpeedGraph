
import pytest
from src.utils import read_speeds_from_file, populate_table

def test_read_speeds_from_file():
    file_path = 'path_to_your_test_file.txt'  
    speeds = read_speeds_from_file(file_path)
    assert speeds == [10.0, 20.0, 30.0]  

def test_populate_table():
    from tkinter import ttk, Tk
    root = Tk()
    table = ttk.Treeview(root, columns=("Metri", "Velocità"), show="headings")
    table.heading("Metri", text="meters")
    table.heading("Velocità", text="speed [Km/h]")
    table.column("Metri", width=100)
    table.column("Velocità", width=100)
    
    speeds = [10.0, 20.0, 30.0]
    distance_per_revolution = 1.52
    populate_table(table, speeds, distance_per_revolution)
    
    rows = table.get_children()
    assert len(rows) == 3
    assert table.item(rows[0])['values'] == ('1.52', '10.00')
