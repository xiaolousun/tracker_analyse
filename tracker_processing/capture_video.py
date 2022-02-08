import cv2
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFont

def capture_video(video_path:str, save_folder:str, frame_frequency:int=1):
    # video_path = './DJI_video/track_video'  # 这里处理一个文件夹中的视频
    ttf_path = 'C:/Users/Documents/times.ttf'
    for vid in os.listdir(video_path):
        video_name = video_path + '/' + vid
        save_folder_real = save_folder + '/' + 'capture_video_results'  + '/' + vid[:-4]  # 检个图片放在同名文件夹内
        picture_name = vid[:-4]
        if not os.path.exists(save_folder_real):
            os.makedirs(save_folder_real)
        capture = cv2.VideoCapture(video_name)  # 打开视频
        # cv2.namedWindow('video', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)

        idx = 0
        if capture.isOpened():
            while True:
                ret, prev = capture.read()  # ret是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，返回值就为False。frame就是每一帧的图像
                if ret == True:
                    idx += 1
                    if idx % frame_frequency == 0:
                        Img_prev = Image.fromarray(prev)
                        Img_draw = ImageDraw.Draw(Img_prev)
                        ttf = ImageFont.truetype(ttf_path, 320)
                        Img_draw.text((10, prev.shape[0]-320), '#%0.4d' % (idx), font=ttf, fill=(0, 255, 255)) #1850 240
                        prev = np.array(Img_prev)
                        # cv2.putText(prev, '#%0.4d' % (idx), (10, 230), cv2.FONT_HERSHEY_TRIPLEX, 10, (0, 255, 255), 30 ) #10 230 10 30 // 0 50 2 8 cv2.FONT_HERSHEY_DUPLEX
                        cv2.imwrite(save_folder_real + '/' + '/%s_%0.7d.jpg' % (picture_name, idx), prev)
                        prev = cv2.resize(prev, (prev.shape[1]//8, prev.shape[0]//8))
                        cv2.imshow('video', prev)
                        print(vid + " img output: %d" % idx)
                else:
                    break
                if cv2.waitKey(20) == 27:
                    break
        cv2.destroyAllWindows()

if __name__ == '__main__':
    video_path = 'D:/无人机跟踪项目/capture_video/DJI_video/track_video'
    save_folder = 'C:/Master_Library/My Reasearch Code Library/tracker_analyse/tracker_processing'
    # frame_frequency = 25
    capture_video(video_path, save_folder)
