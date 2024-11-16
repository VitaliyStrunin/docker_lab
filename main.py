import cv2
import sys

def detect_faces(image_path):
    # Загружаем изображение
    image = cv2.imread(image_path)
    if image is None:
        print("Не удалось загрузить изображение.")
        return

    # Загрузка классификатора для обнаружения лиц
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Преобразуем изображение в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    print(f"Найдено {len(faces)} лиц(о) на изображении.")

    # Рисуем прямоугольники вокруг лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Показываем изображение с выделенными лицами
    #cv2.imshow("Detected Faces", image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

if __name__ == "__main__":
    # Принимаем аргумент из командной строки или используем изображение из репозитория

    image_path = sys.argv[1] if len(sys.argv) > 1 else "photo.jpg"
    detect_faces(image_path)
