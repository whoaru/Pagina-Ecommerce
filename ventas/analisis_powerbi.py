import pandas as pd
import matplotlib.pyplot as plt

print("=" * 50)
print("CARGANDO ARCHIVO")
print("=" * 50)

df = pd.read_csv("ventas.csv")

print(df)

print("\nVENTAS TOTALES")
print(df["Ventas"].sum())

df["Comision"] = df["Ventas"] * 0.10

df.to_csv("ventas_procesadas.csv", index=False)

print("\nARCHIVO EXPORTADO")

plt.bar(df["Vendedor"], df["Ventas"])

plt.title("Ventas por vendedor")

plt.xlabel("Vendedor")

plt.ylabel("Ventas")

plt.show()
