import tkinter as tk

def sumar():
    a = float(entry1.get())
    b = float(entry2.get())
    resultado = a + b
    resultado_label.config(text=f"Resultado: {resultado}")

def restar():
    pass  # Jhaider

def multiplicar():
    a = float(entry1.get())
    b = float(entry2.get())
    resultado = a * b
    resultado_label.config(text=f"Resultado: {resultado}")


# Interfaz
root = tk.Tk()
root.title("Calculadora Colaborativa")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

btn_suma = tk.Button(root, text="Sumar", command=sumar)
btn_suma.pack()

btn_resta = tk.Button(root, text="Restar", command=restar)
btn_resta.pack()

btn_multi = tk.Button(root, text="Multiplicar", command=multiplicar)
btn_multi.pack()

resultado_label = tk.Label(root, text="Resultado:")
resultado_label.pack()

root.mainloop()
