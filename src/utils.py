def read_speeds_from_file(file_path):
    speeds = []
    start_reading = False
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line == "0,00":
                start_reading = True
                continue
            if start_reading:
                # Rimuovi il primo punto se esiste
                if ',' in line and '.' in line:
                    point_index = line.find('.')
                    line = line[:point_index] + line[point_index+1:]
                try:
                    speeds.append(float(line.replace(',', '.')))
                except ValueError:
                    continue
    return speeds


def populate_table(table, speeds, distance_per_revolution):
    for item in table.get_children():
        table.delete(item)
    
    for i, speed in enumerate(speeds):
        meters = (i + 1) * distance_per_revolution
        meters_formatted = f"{meters:.2f}"
        speed_formatted = f"{speed:.2f}"
        table.insert('', 'end', values=(meters_formatted, speed_formatted))