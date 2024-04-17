import cv2
import numpy as np


def clean_up(image, deg):
    cv2.namedWindow('Original')
    cv2.namedWindow('Rotate')
    img = cv2.imread(image)

    if img is None:
        print("Erreur de chargement de l'image. Vérifiez le chemin et l'intégrité du fichier.")
        return

    print(img)

    height, width = img.shape[:2]
    (cX, cY) = (width // 2, height // 2)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    for i in range(height):
        for j in range(width):
            if np.random.randint(2) == 0:
                gray[i, j] = min(gray[i, j] + np.random.randint(0, 1), 255)
            else:
                gray[i, j] = max(gray[i, j] - np.random.randint(0, 1), 0)

    M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
    rotated = cv2.warpAffine(gray, M, (width, height))

    cv2.imshow('Original', img)
    cv2.imshow('Rotate', rotated)

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()















clean_up('image/A/ddp-3.png', 3)