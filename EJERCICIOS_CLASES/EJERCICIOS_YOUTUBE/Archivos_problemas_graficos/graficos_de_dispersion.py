import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('EJERCICIOS_CLASES\EJERCICIOS_YOUTUBE\Archivos_problemas_graficos\\dispersion.csv')

#creando el gráfico de barras
sns.scatterplot(x='tiempo', y='dinero', data=df, palette='viridis')


#Mostrando el grafico
plt.show()