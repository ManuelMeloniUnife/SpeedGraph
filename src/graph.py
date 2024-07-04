from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, FuncFormatter

def create_plot(speeds_1, distance_per_revolution, speeds_2=None):
    x_1 = [(i + 1) * distance_per_revolution for i in range(len(speeds_1))]
    y_1 = speeds_1
    
    fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
    ax.plot(x_1, y_1, marker='o', linestyle='-', markersize=3.5)
    
    if speeds_2 is not None:
        x_2 = [(i + 1) * distance_per_revolution for i in range(len(speeds_2))]
        y_2 = speeds_2
        ax.plot(x_2, y_2, marker='o', linestyle='-', markersize=3.5, color='orange')
    
    ax.set_xlabel('DISTANCE [m]')
    ax.set_ylabel('SPEED [km/h]')
    ax.legend()

    # Configurazione della griglia principale e secondaria
    ax.grid(True, which='both')
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    # Impostazioni della griglia principale
    ax.grid(which='major', linestyle='-', linewidth='0.7', color='gray')

    # Impostazioni della griglia secondaria
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')

    # Formattatori per i tick principali e secondari senza decimali
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x)}'))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{int(y)}'))
    ax.xaxis.set_minor_formatter(FuncFormatter(lambda x, _: f'{int(x)}'))
    ax.yaxis.set_minor_formatter(FuncFormatter(lambda y, _: f'{int(y)}'))

    # Aggiunta delle etichette secondarie
    for label in ax.xaxis.get_minorticklabels():
        label.set_fontsize(8)  # Imposta la dimensione del font delle etichette secondarie
        label.set_color('gray')  # Imposta il colore delle etichette secondarie
    
    for label in ax.yaxis.get_minorticklabels():
        label.set_fontsize(6)
        label.set_color('gray')

    return fig, ax
