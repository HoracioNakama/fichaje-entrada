import cv2

# Inicializar la captura de video desde la cámara web (usualmente el dispositivo 0)
cap = cv2.VideoCapture(0)

# Verificar si la cámara se abrió correctamente
if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

# Bucle para capturar y mostrar los fotogramas de la cámara
while True:
    # Capturar un fotograma de la cámara
    ret, frame = cap.read()

    # Si el fotograma se leyó correctamente, 'ret' es True
    if not ret:
        print("Error: No se pudo leer el fotograma.")
        break

    # Mostrar el fotograma en una ventana llamada "Cámara Web"
    cv2.imshow('Cámara Web', frame)

    # Esperar por la tecla 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y destruir todas las ventanas
cap.release()
cv2.destroyAllWindows()