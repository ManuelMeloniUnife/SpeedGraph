from utils import read_speeds_from_file, populate_table
from graph import create_plot


import tkinter as tk
from tkinter import ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# giro ruota in metri
giroRuota = 1.52  

# Inizializzazione dei vettori delle velocità dai file
speeds_1 = []
speeds_2 = []

# Funzione per aggiornare speed_1 e table_1 dal primo file inserito
def update_data_1(file_path):
    global speeds_1
    speeds_1 = read_speeds_from_file(file_path)
    populate_table(table_1, speeds_1, giroRuota)
    update_plot()

# Funzione per aggiornare speed_2 e table_2 dal secondo file inserito
def update_data_2(file_path):
    global speeds_2, table_2, table_frame_2
    speeds_2 = read_speeds_from_file(file_path)

    if not table_2:
        table_frame_2 = tk.Frame(root)
        table_frame_2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False, padx=10, pady=10)
        
        table_2 = ttk.Treeview(table_frame_2, columns=("Metri", "Velocità"), show="headings", style="Orange.Treeview")
        table_2.heading("Metri", text="meters")
        table_2.heading("Velocità", text="speed [Km/h]")
        
        table_2.column("Metri", width=100)
        table_2.column("Velocità", width=100)
        
        table_2.bind('<ButtonRelease-1>', on_table2_click)
        
        table_2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    populate_table(table_2, speeds_2, giroRuota)
    update_plot()

# Funzione per aggiornare il grafico con i nuovi dati
def update_plot():
    global fig, ax, canvas
    fig, ax = create_plot(speeds_1, giroRuota, speeds_2)
    ax.grid(True)
    canvas.get_tk_widget().pack_forget()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
    fig.canvas.mpl_connect('button_press_event', on_plot_click)

# Funzione per aprire il primo file
def open_file_1():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        update_data_1(file_path)

# Funzione per sovrapporre un secondo file
def open_file_2():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        update_data_2(file_path)

# Funzione per gestire il click sulla tabella
def on_table1_click(event):
    selected_row_1 = table_1.focus()
    selected_row_2 = table_2.focus() if table_2 else None

    if selected_row_1:
        values_1 = table_1.item(selected_row_1)['values']
        if values_1:
            index = table_1.index(selected_row_1)  # Ottieni l'indice della riga selezionata
            meters = float(values_1[0])  # Converti in float
            speed = float(values_1[1])
            update_table(table_1, index)
            update_table(table_2, index) if table_2 else None
            highlight_point(meters, speed)
    
def on_table2_click(event):
    selected_row_1 = table_1.focus()
    selected_row_2 = table_2.focus() if table_2 else None
    
    if selected_row_2:
        values_2 = table_2.item(selected_row_2)['values']
        if values_2:
            index = table_2.index(selected_row_2)  # Ottieni l'indice della riga selezionata
            meters = float(values_2[0])  # Converti in float
            speed = float(values_2[1])
            update_table(table_2, index)
            update_table(table_1, index)
            highlight_point(meters, speed)

# Funzione per gestire il click sul grafico
def on_plot_click(event):
    x_click = event.xdata
    if x_click is not None:
        index_1 = find_nearest_index(speeds_1, x_click)
        index_2 = find_nearest_index(speeds_2, x_click) if speeds_2 else None
        if index_1 is not None:
            meters_1 = (index_1 + 1) * giroRuota
            speed_1 = speeds_1[index_1]
            update_table(table_1, index_1)
            highlight_point_from_plot_click(meters_1, speed_1)
        if index_2 is not None:
            meters_2 = (index_2 + 1) * giroRuota
            speed_2 = speeds_2[index_2]
            update_table(table_2, index_2)
            highlight_point_from_plot_click(meters_2, speed_2)

def find_nearest_index(speeds, x_click):
    min_distance = float('inf')
    nearest_index = None
    for i in range(len(speeds)):
        x_value = (i + 1) * giroRuota
        distance = abs(x_click - x_value)
        if distance < min_distance:
            min_distance = distance
            nearest_index = i
    return nearest_index

# Funzione per evidenziare il punto esatto sul grafico
def highlight_point(meters, speed):
    # Resetta solo i marker rossi e le linee rosse di intersezione
    lines_to_remove = [line for line in ax.lines if line.get_label() in ['highlight_marker', 'highlight_vline', 'highlight_hline']]
    for line in lines_to_remove:
        line.remove()

    ax.axvline(x=meters, color='red', linestyle='-', linewidth=0.7, label='highlight_vline')
    ax.axhline(y=speed, color='red', linestyle='-', linewidth=0.7, label='highlight_hline')
    ax.plot(meters, speed, 'ro', markersize=4, label='highlight_marker')
    
    # Aggiorna il grafico
    canvas.draw()

def highlight_point_from_plot_click(meters, speed):
    # Resetta solo i marker rossi e le linee rosse di intersezione
    lines_to_remove = [line for line in ax.lines if line.get_label() in ['highlight_marker', 'highlight_vline', 'highlight_hline']]
    for line in lines_to_remove:
        line.remove()

    ax.axvline(x=meters, color='red', linestyle='-', linewidth=0.7, label='highlight_vline')    
    ax.axhline(y=speed, color='red', linestyle='-', linewidth=0.7, label='highlight_hline')    

    # Aggiorna il grafico
    canvas.draw()

def update_table(table, index):
    # Ottieni tutti gli elementi della tabella
    items = table.get_children()
    if 0 <= index < len(items):
        item = items[index]
        table.selection_set(item)
        table.focus(item)
        table.see(item)

# Funzione per ripristinare le tabelle e il grafico allo stato iniziale
def clear_tables():
    global speeds_1, speeds_2, table_1, table_2, table_frame_2, fig, ax, canvas
    
    speeds_1 = []
    speeds_2 = []
    
    # Ripristina la tabella 1
    for item in table_1.get_children():
        table_1.delete(item)
    
    # Ripristina la tabella 2 se esiste
    if table_2:
        for item in table_2.get_children():
            table_2.delete(item)
        table_frame_2.pack_forget()
        table_2 = None  # Resetta anche la variabile globale table_2
        table_frame_2 = None  # Resetta anche la variabile globale table_frame_2
    
    # Ripristina il grafico
    fig, ax = create_plot(speeds_1, giroRuota)
    ax.grid(True)
    canvas.get_tk_widget().pack_forget()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    fig.canvas.mpl_connect('button_press_event', on_plot_click)

def main():
    global root, canvas, table_1, fig, ax, table_2, table_frame_2
    root = tk.Tk()
    root.title("Speed Graph")
    root.minsize(1100 , 700)

    # Aggiunta della barra dei menu
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # Aggiunta della voce "File" nella barra dei menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=open_file_1)
    file_menu.add_command(label="Sovrapponi file", command=open_file_2)
    file_menu.add_command(label="Clear tables", command=clear_tables)  

    # Creazione della tabella con bordi visibili alle celle
    style = ttk.Style()

    # Impostazione dello stile per la tabella 1 (sfondo blu)
    style.configure("Blue.Treeview", background="#ADD8E6", foreground="black", rowheight=30, font=('Verdana', 10))
    style.configure("Orange.Treeview", background="#FFD700", foreground="black", rowheight=30, font=('Verdana', 10))

    table_frame_1 = tk.Frame(root)
    table_frame_1.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False, padx=10, pady=10)

    # Impostazione delle colonne della tabella 1
    table_1 = ttk.Treeview(table_frame_1, columns=("Metri", "Velocità"), show="headings", style="Blue.Treeview")
    table_1.heading("Metri", text="meters")
    table_1.heading("Velocità", text="speed [Km/h]")
    table_1.column("Metri", width=100)
    table_1.column("Velocità", width=100)

    # Gestore di eventi per il click sulla tabella 1
    table_1.bind('<ButtonRelease-1>', on_table1_click)

    # Inizializzazione della seconda tabella e del suo frame come None (aggiornati poi nella funzione)
    table_2 = None
    table_frame_2 = None

    # Creazione del grafico
    fig, ax = create_plot(speeds_1, giroRuota)

    # Impostazioni della griglia principale e secondaria
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Connette l'evento di click del mouse al grafico
    cid = fig.canvas.mpl_connect('button_press_event', on_plot_click)

    # Posizionamento della tabella nella finestra
    table_1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Avvio del loop principale di Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()