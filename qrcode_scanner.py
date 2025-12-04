import cv2

def scan_qr():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        data, bbox, _ = detector.detectAndDecode(frame)
        cv2.imshow("QR Scanner - Tekan Q untuk keluar", frame)

        if data:
            cap.release()
            cv2.destroyAllWindows()
            return data

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None
