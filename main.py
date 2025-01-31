import cv2
import mediapipe as mp

# Inicializar o opencv e o mediapipe
webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecer_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    # Ler as informações da webcam
    verificador, frame = webcam.read()
    if not verificador:
        break

    # Reconhecer os rostos
    lista_rostos = reconhecer_rostos.process(frame)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            desenho.draw_detection(frame, rosto)

        # Contar o número de rostos detectados
        numero_de_rostos = len(lista_rostos.detections)

        # Adicionar o número de rostos detectados na imagem
        cv2.putText(frame, f'Rostos Detectados: {numero_de_rostos}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    else:
        cv2.putText(frame, 'Nenhum rosto detectado', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Mostrar a imagem com o número de rostos
    cv2.imshow("Rostos na Webcam", frame)

    # Quando apertar o ESC para o loop
    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
