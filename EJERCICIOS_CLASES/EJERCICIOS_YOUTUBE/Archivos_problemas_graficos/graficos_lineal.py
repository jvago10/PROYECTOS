import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('EJERCICIOS_CLASES\EJERCICIOS_YOUTUBE\Archivos_problemas_graficos\\pedos.csv')

sns.lineplot(x='fecha', y='pedos', data=df)

#creando un punto en el momento de mas pedos
plt.plot('01-09',17,"o")

#Mostrando el grafico
plt.show()