import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# --- Funciones ---

def actualizar_texto():
    """
    Obtiene el valor del campo de entrada y actualiza la etiqueta de texto.
    """
    try:
        # Obtiene el número del campo de entrada
        numero = int(entrada_numero.get())
        # Actualiza el texto de la etiqueta
        etiqueta_texto.config(text=f"El número ingresado es: {numero}")
    except ValueError:
        # Si el valor no es un número, muestra un mensaje de error
        etiqueta_texto.config(text="Por favor, ingresa un número válido.")

def mostrar_camara():
    """
    Captura un fotograma de la cámara y lo muestra en la ventana.
    """
    # Captura un fotograma de la cámara
    ret, frame = cap.read()
    if ret:
        # Convierte la imagen de BGR (formato de OpenCV) a RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convierte el fotograma a un formato que Tkinter pueda usar
        imagen = Image.fromarray(frame_rgb)
        imagen_tk = ImageTk.PhotoImage(image=imagen)

        # Muestra la imagen en la etiqueta de video
        etiqueta_video.imgtk = imagen_tk
        etiqueta_video.config(image=imagen_tk)

        # Llama a esta función de nuevo después de 10 ms para crear un flujo de video
        etiqueta_video.after(10, mostrar_camara)

# --- Configuración de la Ventana Principal ---

# Inicializa la ventana de Tkinter
ventana = tk.Tk()
ventana.title("Cámara Web con Input Numérico")

# --- Configuración de la Cámara ---

# Inicializa la captura de video
cap = cv2.VideoCapture(0)

# Crea una etiqueta para mostrar el video
etiqueta_video = tk.Label(ventana)
etiqueta_video.pack(padx=10, pady=10)

# --- Creación de los Widgets (Elementos de la Interfaz) ---

# Crea un marco para organizar el input y el botón
marco_controles = ttk.Frame(ventana)
marco_controles.pack(pady=5)

# Campo de entrada para el número
etiqueta_input = ttk.Label(marco_controles, text="Ingresa un número:")
etiqueta_input.pack(side=tk.LEFT, padx=5)

entrada_numero = ttk.Entry(marco_controles, width=10)
entrada_numero.pack(side=tk.LEFT, padx=5)

# Botón para actualizar el texto
boton_actualizar = ttk.Button(marco_controles, text="Actualizar Texto", command=actualizar_texto)
boton_actualizar.pack(side=tk.LEFT, padx=5)

# Etiqueta para mostrar el texto que cambia
etiqueta_texto = ttk.Label(ventana, text="El número ingresado es: 0", font=("Helvetica", 14))
etiqueta_texto.pack(pady=10)

# --- Iniciar la Aplicación ---

# Inicia el bucle para mostrar la cámara
mostrar_camara()

# Inicia el bucle principal de la ventana de Tkinter
ventana.mainloop()

# --- Liberar Recursos ---

# Cuando la ventana se cierra, libera la cámara
cap.release()