import cv2
from face_recognition import detect_faces
from emotion_analysis import analyze_emotion

def main():
    # 카메라 초기화
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 얼굴 인식
        faces = detect_faces(frame)

        for (x, y, w, h) in faces:
            # 얼굴 부분 추출
            face_frame = frame[y:y+h, x:x+w]
            emotion = analyze_emotion(face_frame)

            # 결과 출력
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

        cv2.imshow('Real-time Face Recognition and Emotion Analysis', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
