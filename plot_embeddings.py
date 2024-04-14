from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Definiere die Datenpunkte mit den zugehörigen Symbolen
data = {
    '.': (0.7253, -0.4097, -0.5502),
    'A': (0.6031, 0.0315, -0.5754),
    'B': (0.2058, 0.0782, -0.2502),
    'C': (0.2795, -0.1045, -0.2608),
    'D': (0.1513, 0.0603, -0.3379),
    'E': (0.5425, 0.1827, -0.6108),
    'F': (0.1361, -0.0425, -0.2632),
    'G': (0.3017, -0.0558, -0.2900),
    'H': (-0.6221, 2.0425, 2.6877),
    'I': (0.3897, 0.1356, -0.5745),
    'J': (0.0491, 0.0389, -0.3698),
    'K': (0.1780, -0.0296, -0.3189),
    'L': (-0.0703, 0.3261, -0.4160),
    'M': (0.0762, -0.0029, -0.3560),
    'N': (0.1558, 0.1076, -0.5502),
    'O': (0.5599, 0.1499, -0.6273),
    'P': (0.3054, -0.1133, -0.1969),
    'Q': (-0.0872, 0.6001, -0.8430),
    'R': (0.0672, 0.1242, -0.3458),
    'S': (0.2768, -0.0460, -0.3367),
    'T': (0.2620, -0.0426, -0.3156),
    'U': (0.5143, 0.0851, -0.5594),
    'V': (0.0713, 0.0332, -0.2089),
    'W': (0.1631, 0.0909, -0.3058),
    'X': (0.1944, 0.0790, -0.4279),
    'Y': (0.3192, 0.1362, -0.6340),
    'Z': (0.0358, 0.1164, -0.4221)
}

# Erstelle 3D-Achsen
ax = plt.axes(projection='3d')

# Füge jeden Punkt als Text mit seinem spezifischen Symbol hinzu
for label, (x, y, z) in data.items():
    # Berechne den Offset, um die Textlabels über den Punkten anzuzeigen
    z_offset = 1  # Du kannst diesen Wert anpassen
    ax.text(x, y, z + z_offset, label, fontsize=9, color='blue', ha='center', va='center')

# Achsen und Titel konfigurieren
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('Scatter Plot der erlernten Buchstaben Embeddings\naus 32.033 amerikanischen Vornamen')

# Zeige das Diagramm
plt.show()