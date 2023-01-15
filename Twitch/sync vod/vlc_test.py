import vlc
import time
import _thread
import cv2


Instance1 = vlc.Instance()
player1 = Instance1.media_player_new()
Instance2 = vlc.Instance()
player2 = Instance2.media_player_new()

Media1 = Instance1.media_new(
    "https://dgeft87wbj63p.cloudfront.net/66e1ae92b4c192d2dc0d_zwave69_42371119852_1623875388/chunked/index-dvr.m3u8"
)
Media1.get_mrl()
Media2 = Instance1.media_new(
    "https://dgeft87wbj63p.cloudfront.net/66e1ae92b4c192d2dc0d_zwave69_42371119852_1623875388/chunked/index-dvr.m3u8"
)
Media2.get_mrl()

player1.set_media(Media1)
player2.set_media(Media2)
player1.play()
player2.play()

black = cv2.imread("Twitch\\sync vod\\Black.jpg")

time.sleep(5)  # Or however long you expect it to take to open vlc
while player1.is_playing():

    cv2.imshow("", black)

    key = cv2.waitKey(1)

    if key == ord("i"):
        mval = "%.0f" % (1.0 * 1000)
        player1.set_time(int(mval))
        player2.set_time(int(mval))
        print("initialised")

    if key == ord("p"):
        player1.pause()
        player2.pause()
        print("paused")

    if key == ord("t"):
        print(player1.get_time(), player2.get_time())

    if key == ord("q"):
        cv2.destroyAllWindows()
        player1.stop()
        player2.stop()
        break
