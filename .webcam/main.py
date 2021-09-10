import cv2
#conectando ao webcam do pc
webcam = cv2.VideoCapture(0) #inicia conexao com a webcam

if webcam.isOpened():
    validacao, frame = webcam.read()
    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow('video', frame)
        key = cv2.waitKey(5)
        if key == 27: # numero para tecla ESC
            break
    cv2.imwrite('foto.png', frame) # tira a foto

webcam.release() # finaliza conexao com a webcam
cv2.destroyAllWindows() #fecha a janela de frame       
