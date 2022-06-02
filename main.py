import cv2

cam = cv2.VideoCapture('test1.mp4')
fps = cam.get(cv2.CAP_PROP_FPS)
print(fps)

cap = cv2.VideoCapture("test1.mp4")
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

video_capture = cv2.VideoCapture("test1.mp4")
video_capture.set(cv2.CAP_PROP_FPS, fps)

saved_frame_name = 0
n = 15
dsize = (119, 119)
while video_capture.isOpened():

    frame_is_read, frame = video_capture.read()
    if n % 15 == 0:

        if frame_is_read:

            frame = frame[210:445, 115:350]
            frame = cv2.resize(frame, dsize)
            cv2.imwrite(f"frame{str(saved_frame_name)}.jpg", frame)
            saved_frame_name += 15

            print(round(((n - 15) / length) * 100, 2), "%")

        else:
            print("Could not read the frame.")
    n += 1
