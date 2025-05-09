import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
import seaborn as sns  # Para la paleta de colores

# Define los datos en formato CSV como una cadena de texto
data = """Producto,Ventas,Temporada,Pais,Ganancia
Celular,70,Enero,Colombia,14
Celular,80,Febrero,Panama,16
Celular,150,Marzo,Mexico,30
Celular,300,Agosto,Colombia,60
Celular,500,Noviembre,Costa,100
Celular,900,Diciembre,Panama,180
Celular,70,Enero,Chile,14
Celular,80,Febrero,?,16
Celular,150,Marzo,Panama,30
Celular,300,Agosto,Mexico,60
Celular,500,Noviembre,Colombia,100
Celular,900,Diciembre,Chile,180
Celular,300,Agosto,Panama,60
Celular,500,Noviembre,Mexico,100
Celular,900,Diciembre,Panama,180
Celular,70,Enero,Chile,14
Celular,101,Septiembre,Brasil,20.2
Celular,150,Octubre,Brasil,30
Celular,400,Diciembre,Panama,80
Celular,750,Noviembre,Paraguay,150
Celular,100,Enero,Paraguay,20
Celular,120,Agosto,Brasil,24
Celular,500,Abril,Mexico,100
Celular,70,Enero,Colombia,14
Celular,80,Febrero,Panama,16
Celular,150,Marzo,Mexico,30
Celular,300,Agosto,Colombia,60
Celular,500,Noviembre,Costa,100
Celular,900,Diciembre,Panama,180
Celular,70,Enero,Chile,14
Celular,80,Febrero,Costa,16
Celular,150,Marzo,?,30
Celular,300,?,Mexico,?
Celular,500,?,Colombia,100
Celular,900,Diciembre,Chile,180
Celular,300,Agosto,Panama,60
Celular,500,Noviembre,Mexico,100
Celular,900,Diciembre,Panama,180
Celular,70,Enero,Chile,14
Celular,101,Septiembre,Brasil,20.2
Celular,150,Octubre,Brasil,30
Celular,400,Diciembre,Panama,80
Celular,750,Noviembre,Paraguay,150
Celular,100,Enero,Paraguay,20
Celular,120,Agosto,Brasil,24
Celular,500,Abril,?,100
Celular,80,Febrero,Costa,16
Celular,150,Marzo,Panama,30
Celular,300,Agosto,Mexico,60
Celular,500,Noviembre,Colombia,100
Celular,900,Diciembre,Chile,180
Celular,300,Agosto,?,60
Celular,500,Noviembre,Mexico,100
Celular,900,Diciembre,?,180
Celular,70,Enero,Chile,14
Celular,101,Septiembre,Brasil,20.2
Celular,150,?,Brasil,30
Celular,400,Diciembre,?,80
Celular,750,Noviembre,Paraguay,150
Celular,100,Enero,Paraguay,20
Celular,120,Agosto,?,24
Celular,500,Abril,Mexico,100
Celular,70,Enero,Colombia,14
Celular,80,Febrero,Panama,16
Celular,70,Enero,Colombia,14
Celular,80,Febrero,?,16
Celular,150,?,Mexico,30
Celular,300,Agosto,Colombia,60
Celular,500,Noviembre,Costa,100
Celular,900,Diciembre,?,?
Celular,70,Julio,Chile,14
Celular,80,?,Costa,16
Celular,150,Marzo,?,30
Celular,300,Agosto,Mexico,60
Celular,500,Noviembre,Colombia,100
Celular,900,Junio,?,180
Celular,300,Junio,Panama,60
Celular,500,Junio,Mexico,100
Celular,900,?,Panama,180
Celular,70,Enero,?,14
Celular,101,?,Brasil,20.2
Celular,150,Octubre,Brasil,30
"""

# Usa StringIO para simular un archivo
data_io = StringIO(data)

# Carga los datos en un DataFrame
df = pd.read_csv(data_io)

# Limpia los nombres de las columnas (si es necesario)
df.columns = df.columns.str.strip()

# Asegúrate de que la columna 'Ganancia' sea numérica
df['Ganancia'] = pd.to_numeric(df['Ganancia'], errors='coerce')

# Agrupamos y sumamos las ganancias por temporada (mes)
ganancia_mes = df.groupby('Temporada')['Ganancia'].sum()

# Ordenamos las temporadas (si es necesario)
orden_temporadas = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
ganancia_mes = ganancia_mes.reindex(orden_temporadas)

# 4. Ganancia por Temporada (gráfico lineal)
plt.figure(figsize=(12, 8))

# Definimos el estilo de la línea
sns.lineplot(x=ganancia_mes.index, y=ganancia_mes.values, marker='o', color='teal')

plt.title('Ganancia por Temporada')
plt.xlabel('Temporada')
plt.ylabel('Ganancia Total')
plt.grid(True)
plt.tight_layout()
plt.show()
