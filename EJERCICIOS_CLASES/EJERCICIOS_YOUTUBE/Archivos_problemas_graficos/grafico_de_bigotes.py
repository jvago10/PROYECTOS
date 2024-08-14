import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('EJERCICIOS_CLASES\EJERCICIOS_YOUTUBE\Archivos_problemas_graficos\\bigotes.csv')

#creando el gráfico de barras
sns.boxplot(x='categoria', y='valor', data=df, palette='viridis')


#Mostrando el grafico
plt.show()