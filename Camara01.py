
import cv2
import pyrealsense2 as rs
from pyzbar.pyzbar import decode
import numpy as np

# Inicializar la cámara RealSense
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

profile = pipeline.start(config)



try:
    while True:
        # Capturar un fotograma desde la cámara
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        if not color_frame:
            continue

        # Convertir el fotograma a una matriz de imagen OpenCV
        color_image = np.asanyarray(color_frame.get_data())

        # Convertir la imagen a escala de grises
        gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

        # Decodificar los códigos de barras
        barcodes = decode(gray_image)

        # Iterar sobre los códigos de barras detectados
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            print(f"Código de barras detectado: {barcode_data}")

            # Dibujar un rectángulo alrededor del código de barras
            rect_points = barcode.polygon
            if rect_points is not None and len(rect_points) == 4:
                rect_points = np.array(rect_points, dtype=int)
                cv2.polylines(color_image, [rect_points], isClosed=True, color=(0, 255, 0), thickness=2)

        # Mostrar la imagen en una ventana (solo con fines de depuración)
        cv2.imshow('RealSense Camera', color_image)

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Detener la captura y cerrar las ventanas al salir
    pipeline.stop()
    cv2.destroyAllWindows()
