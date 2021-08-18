import cv2

video = cv2.VideoCapture(0)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

detector = cv2.QRCodeDetector()

while True:

    validation, frame = video.read()
    if validation is not True:
        break

    data, bbox, straight_qrcode = detector.detectAndDecode(frame)
    roi = frame[int(height/2) -100: int(height/2) +100, int(width/2) -100: int(width/2) +100]
    blured_frame = cv2.blur(frame, (60, 60))
    blured_frame[int(height/2) -100: int(height/2) +100, int(width/2) -100: int(width/2) +100] = roi

    if bbox is not None:
        if data:
            cv2.putText(blured_frame, "QR Code detected: {}".format(data), (50, 50),
            cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)

    cv2.imshow('output', blured_frame)
    cv2.waitKey(30)