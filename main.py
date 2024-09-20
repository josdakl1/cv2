import cv2
from pyzbar.pyzbar import decode

def main():
    # Iniciar la captura de video
    cap = cv2.VideoCapture(0)

    while True:
        # Leer un frame de la cámara
        ret, frame = cap.read()

        # Decodificar los códigos de barras en el frame
        barcodes = decode(frame)

        for barcode in barcodes:
            # Extraer la información del código de barras
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type

            # Dibujar un rectángulo alrededor del código de barras
            pts = barcode.polygon
            if len(pts) == 4:
                pts = [(pt.x, pt.y) for pt in pts]
                cv2.polylines(frame, [np.array(pts, dtype=np.int32)], True, (0, 255, 0), 2)

            # Mostrar la información del código de barras
            cv2.putText(frame, f'{barcode_data} ({barcode_type})', (pts[0][0], pts[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Mostrar el frame con los códigos de barras detectados
        cv2.imshow('Barcode Scanner', frame)

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la captura de video y cerrar las ventanas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
