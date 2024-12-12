"""
Autor: DavidCambra18 (https://github.com/DavidCambra18)
Descripción: Comprobador de hash para verificar si los hashes de los archivos son iguales. 
Repositorio: https://github.com/DavidCambra18/ComprobadorHash
"""

import tkinter as tk
from tkinter import messagebox

def comprobar_hash():
    original = entry_original.get()
    comprobante = entry_comprobante.get()

    if original == comprobante:
        messagebox.showinfo("Resultado", "El hash original es igual al del archivo.")
    else:
        messagebox.showwarning("Resultado", "El hash original NO es igual al del archivo.")

ventana = tk.Tk()
ventana.title("Comprobador Hash")

tk.Label(ventana, text="Hash original:").grid(row=0, column=0, padx=10, pady=10)
entry_original = tk.Entry(ventana, width=50)
entry_original.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Hash a comprobar:").grid(row=1, column=0, padx=10, pady=10)
entry_comprobante = tk.Entry(ventana, width=50)
entry_comprobante.grid(row=1, column=1, padx=10, pady=10)

tk.Button(ventana, text="Comprobar", command=comprobar_hash).grid(row=2, column=0, columnspan=2, pady=10)



ventana.mainloop()