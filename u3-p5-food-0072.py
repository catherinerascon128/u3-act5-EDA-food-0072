import pandas as pd
import matplotlib.pyplot as plt
# catherine rascon NC = 0072
# 1. Leer el archivo CSV
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEÍDOS DESDE CSV, comida India 0072 ---")
print(df_food_india)

print("\n--- Mostrar nombre comida + ingredientes, 0072 ---")
recetas = df_food_india [['name', 'ingredients']]
print(recetas)

print("\n--- Tiempo de coccion mostrar 10 registros con head 0072 ---")
nombre_y_hora = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_hora)

print("--- grafica comida (X) tiempo de coccion (Y) 0072 ---")
print("--- grafica comida (X) texto a 30 grados ---")
nombre_y_hora.plot.bar(x='name',y='cook_time', rot=30)
plt.title("comidas tipicas de india catherine 0072")
plt.xlabel("nombre platilo")
plt.ylabel("tiempo de coccion")
plt.show()

print("--- gráfica de varias columnas 0072 ---")
nombre_y_hora = df_food_india[['name', 'prep_time', 'cook_time']].head(10)
nombre_y_hora.plot.bar(x='name', rot=30)
plt.title("graficas de 2 columnas catherine 0072")
plt.xlabel("nombre platilo")
plt.ylabel("tiempo de coccion prep y comida")
plt.show()

print("--- gráfica apiladas una tras otra verticalmente 0072 ---")
nombre_y_hora.plot.bar(x='name', stacked=True, rot=30)
plt.title("grafica apilada catherine 0072")
plt.xlabel("nombre platilo")
plt.ylabel("tiempo de coccion prep y comida")
plt.show()









