import os
import cv2
import numpy as np

directorio = './Dataset/1/'
dir_output = './Dataset_ejes/'
archivos_txt = [archivo for archivo in os.listdir(directorio) if archivo.endswith('.txt')]
print(archivos_txt)
#txt = archivos_txt[0]
#print("Teste:", txt[:-4])
for txt in archivos_txt:
    aux = 0
    with open(directorio + txt, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            output = linea.split()
            if(len(output) == 5):
                id_clase, cx_norm, cy_norm, w_norm, h_norm = output

                if(id_clase == "4" or id_clase == "1" or id_clase  =="2"):
                    print("target")
                    cx_norm = float(cx_norm)
                    cy_norm = float(cy_norm)
                    w_norm = float(w_norm)*1.2
                    h_norm = float(h_norm)*1.2
                    imagen = cv2.imread(directorio + txt[:-4] + ".jpg")
                    print(directorio + txt[:-4] + ".jpg")
                    alto, ancho = imagen.shape[:2]
                    alto = alto
                    ancho = ancho


                    # Convertir las coordenadas normalizadas a píxeles
                    cx = int(cx_norm * ancho)
                    cy = int(cy_norm * alto)
                    w = int(w_norm * ancho)
                    h = int(h_norm * alto)

                    # Calcular las coordenadas del recorte (esquina superior izquierda y esquina inferior derecha)
                    x1 = max(0, int(cx - w / 2))
                    y1 = max(0, int(cy - h / 2))
                    x2 = min(ancho, int(cx + w / 2))
                    y2 = min(alto, int(cy + h / 2))

                    # Recortar la región de la imagen
                    recorte = imagen[y1:y2, x1:x2]

                    """# Mostrar el recorte (presione cualquier tecla para continuar)
                    cv2.imshow("Recorte", recorte)
                    cv2.waitKey(0)"""

                    cv2.imwrite(dir_output + txt[:-4] + str(aux)+".jpg", recorte)
                aux = aux +1
cv2.destroyAllWindows()