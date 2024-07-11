import pytest
import tkinter as tk
from tkinter import ttk
from unittest.mock import patch, MagicMock
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.main import *
import src.utils as utils
import src.graph as graph

@pytest.fixture(scope="module")
def setup_root():
    # Setup della root Tkinter una sola volta per tutti i test del modulo
    yield root
    # Cleanup della root Tkinter
    root.destroy()


def test_update_data_1(setup_root):
    # Mock della finestra di dialogo per il file
    with patch('tkinter.filedialog.askopenfilename', return_value='../test_datas/velocita.txt'):
        update_data_1('../test_datas/velocita.txt')
    
    # Verifica dell'aggiornamento dei dati e della tabella
    # Assicurati che speeds_1 sia aggiornato correttamente
    assert speeds_1 == [aggiornamento_fittizio]
    # Assicurati che la tabella 1 sia popolata correttamente
    assert table_1.get_children() == [children_fittizi]


def test_update_data_2(setup_root):
    # Mock della finestra di dialogo per il file
    with patch('tkinter.filedialog.askopenfilename', return_value='/path/to/second_file.txt'):
        update_data_2('/path/to/second_file.txt')
    
    # Verifica dell'aggiornamento dei dati e della tabella
    # Assicurati che speeds_2 sia aggiornato correttamente
    assert speeds_2 == [aggiornamento_fittizio]
    # Assicurati che la tabella 2 sia popolata correttamente
    assert table_2.get_children() == [children_fittizi]


def test_clear_tables(setup_root):
    # Chiamata diretta alla funzione clear_tables
    clear_tables()
    
    # Verifica che entrambe le tabelle siano vuote dopo la pulizia
    assert len(table_1.get_children()) == 0
    assert len(table_2.get_children()) == 0
    # Verifica che il grafico sia stato ripristinato correttamente
    # Utilizzare metodi di confronto appropriati per il grafico ripristinato


def test_on_table1_click(setup_root):
    # Simulazione di un click sulla tabella 1
    event = tk.Event()
    on_table1_click(event)
    
    # Verifica che il comportamento atteso sia avvenuto
    # Utilizzare metodi di confronto appropriati per verificare il comportamento


def test_on_table2_click(setup_root):
    # Simulazione di un click sulla tabella 2
    event = tk.Event()
    on_table2_click(event)
    
    # Verifica che il comportamento atteso sia avvenuto
    # Utilizzare metodi di confronto appropriati per verificare il comportamento


def test_on_plot_click(setup_root):
    # Simulazione di un click sul grafico
    event = tk.Event()
    event.xdata = 10.0  # Imposta una posizione x simulata per il click sul grafico
    on_plot_click(event)
    
    # Verifica che il comportamento atteso sia avvenuto
    # Utilizzare metodi di confronto appropriati per verificare il comportamento
