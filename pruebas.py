# Importación de las librerías
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Creación de un conjunto de datos aleatorio
data = pd.DataFrame(np.random.random((5, 5)))
# Representación del mapa de calor
sns.heatmap(data, center=0, cmap='Blues_r', annot=True, fmt='.3f')
plt.show()
