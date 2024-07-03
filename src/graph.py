from matplotlib.figure import Figure
import matplotlib.pyplot as plt

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
    
    return fig, ax
