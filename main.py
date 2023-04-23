import cv2

# открываем видеофайл для чтения
capture = cv2.VideoCapture("video.mp4")

# устанавливаем позицию чтения на 2 секунды (2000 миллисекунд)
capture.set(cv2.CAP_PROP_POS_MSEC, 2000)

# получаем следующий кадр из видеопотока
ret, frame = capture.read()

############################################

import cv2

def extract_frame(video_path, frame_number):
    # Открытие видеофайла
    video_capture = cv2.VideoCapture(video_path)
    
    # Установка позиции кадра
    video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    
    # Извлечение кадра
    ret, frame = video_capture.read()
    
    if ret:
        return frame
    else:
        return None

# Пример использования функции
# Извлечение 10-го кадра из видеофайла "video.mp4"
frame = extract_frame("video.mp4", 10)

# Отображение кадра
cv2.imshow("Frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
