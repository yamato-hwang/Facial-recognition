import dlib
import cv2

# 이미지 읽기
image = cv2.imread('이미지_파일.jpg')

# 얼굴 검출기 초기화
detector = dlib.get_frontal_face_detector()

# 이미지를 흑백으로 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 얼굴 검출
faces = detector(gray_image)

# 각 얼굴 주위에 사각형 그리기
for face in faces:
    x, y, w, h = face.left(), face.top(), face.width(), face.height()
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# 결과 이미지를 화면에 표시
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
