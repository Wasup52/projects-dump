import cv2
import time


url1 = "https://dgeft87wbj63p.cloudfront.net/66e1ae92b4c192d2dc0d_zwave69_42371119852_1623875388/chunked/index-dvr.m3u8"
vcap1 = cv2.VideoCapture(url1)
fps = vcap1.get(cv2.CAP_PROP_FPS)
wt = 1 / fps

while True:
    start_time = time.time()
    # Capture frame-by-frame
    ret, frame = vcap1.read()

    if frame is not None:
        # Display the resulting frame
        cv2.imshow("frame", frame)

        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord("q"):
            break
        dt = time.time() - start_time
        if wt - dt > 0:
            time.sleep(wt - dt)
    else:
        print("Frame is None")
        break

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

# When everything done, release the capture
vcap1.release()
cv2.destroyAllWindows()
print("Video stop")
