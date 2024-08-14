import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('EJERCICIOS_CLASES\EJERCICIOS_YOUTUBE\Archivos_problemas_graficos\\cofla_ingresos.csv')

#creando el gráfico de barras
sns.barplot(x='fuente', y='ingresos', data=df, palette='viridis')

#obteniendo el total de ingresos

total_ingresos = df['ingresos'].sum()

#Mostrando el total de ingresos

print(f'El total de ingresos es: $/{total_ingresos}.00')

#Mostrando el grafico
plt.show()