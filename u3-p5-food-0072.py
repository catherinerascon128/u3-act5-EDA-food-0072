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

