import pandas as pd

input_file = "prueba.xlsx"
output_file = "prueba.csv"
df = pd.read_excel(input_file)
df.to_csv(output_file, index=None, header=True)

print("Archivo convertido exitosamente a formato CSV.")
