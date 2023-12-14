import cv2

def append_text(image, emotion, face_coordinates):
    # 얼굴 주위에 텍스트 추가
    x, y, w, h = face_coordinates
    text = "HAPPY!" if emotion == "happy" else "Neutral"  # 감정이 happy인 경우 HAPPY!, 그 외에는 Neutral 텍스트
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]

    # 텍스트를 얼굴 옆에 추가
    cv2.putText(image, text, (x + w + 10, y + h // 2 + text_size[1] // 2), font, font_scale, (0, 255, 0), font_thickness, cv2.LINE_AA)

    return image

# main 함수에서의 사용 예시:
# faces = detect_faces(image)  # 이미지에서 얼굴 감지 (이전에 정의한 detect_faces 함수 활용)
# for face_coordinates in faces:
#     emotion = detect_emotion(face_coordinates)  # 감정 분석 (예: happy 또는 neutral)
#     image = append_text(image, emotion, face_coordinates)

# 이미지를 화면에 표시
# cv2.imshow('Detected Faces with Text', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
