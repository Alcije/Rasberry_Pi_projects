import cv2

MIN_AREA = 1200

camera = cv2.VideoCapture(0)
ok, old_frame = camera.read()
ok2, new_frame = camera.read()

if not ok or not ok2:
    print("Camera not available.")
    camera.release()
    raise SystemExit

print("Motion monitor started. Press ESC to quit.")

while True:
    difference = cv2.absdiff(old_frame, new_frame)
    gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, mask = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < MIN_AREA:
            continue

        x, y, width, height = cv2.boundingRect(contour)
        cv2.rectangle(old_frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
        cv2.putText(old_frame, "movement", (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow("Raspberry Pi motion monitor", old_frame)

    old_frame = new_frame
    ok, new_frame = camera.read()
    if not ok:
        break

    if cv2.waitKey(10) == 27:
        break

camera.release()
cv2.destroyAllWindows()
