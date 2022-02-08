import cv2
import os
import re

def picture2video(path:str, savepath:str, *fps):

    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    save_video_path = savepath + '/' + 'picture2video_results'
    if not os.path.exists(save_video_path):
        os.makedirs(save_video_path)
    folder_List = os.listdir(path)
    save_folder_List = os.listdir(save_video_path)
    save_folder_List = list(map(lambda x: x.split('.')[0], save_folder_List))
    folder_List = list(set(folder_List).difference(set(save_folder_List)))

    if len(folder_List) == 0:
        raise FileNotFoundError('No file needs to transform')

    def sort_picture(picture):
        picture_d_str = re.sub("\D", "", picture)
        picture_d = float(picture_d_str)
        return picture_d

    for i, filename in enumerate(folder_List):
        folder_path = os.path.join(path, filename)
        file_list = os.listdir(folder_path)
        file_list.sort(key=sort_picture)
        imgsize = (cv2.imread(folder_path + '/' + file_list[0])).shape
        size = (imgsize[1], imgsize[0])
        videoWriter = cv2.VideoWriter(save_video_path + '/' + '%s.avi' % (filename), fourcc, fps[i], size)
        for file in file_list:
            file_path = folder_path + '/' + file
            test_img = cv2.imread(file_path)
            cv2.imshow('img', test_img)
            cv2.waitKey(1)
            videoWriter.write(test_img)
        print(filename + ' is completed')
    videoWriter.release()

if __name__ == '__main__':
    path = 'D:/test_video3'
    savepath = './test_video_results'
    fps = [20, 25]
    imgsize = (544, 960)
    picture2video(path, savepath, *fps)

