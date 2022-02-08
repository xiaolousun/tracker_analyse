import cv2
import os

def draw_bbox(image_path:str, save_folder:str, *results_path):

    color = [(255, 255, 0), (255, 0, 0), (1, 0, 0), (0, 0, 255), ]
    if len(color) < len(results_path):
        raise IndexError('color out of index range')

    save_folder_real = save_folder + '/' + 'draw_bbox_results' + '/' + results_path[0].split('/')[-1].split('.')[0]

    if not os.path.exists(save_folder_real):
        os.makedirs(save_folder_real)

    list_get = dict()
    for i, result_path in enumerate(results_path):
        list_x1 = 'list_x1_' + result_path.split('/')[-2]
        list_y1 = 'list_y1_' + result_path.split('/')[-2]
        list_x2 = 'list_x2_' + result_path.split('/')[-2]
        list_y2 = 'list_y2_' + result_path.split('/')[-2]

        list_get[list_x1] = []
        list_get[list_y1] = []
        list_get[list_x2] = []
        list_get[list_y2] = []

        f_result = open(result_path, 'r', encoding='utf-8')
        list_of_lines = f_result.readlines()

        for line in list_of_lines:
            line = line.split(',')
            line = [l.strip() for l in line]
            BBox = list(map(lambda x: int(float(x)), line))
            [x, y, w, h] = BBox
            # x1, y1 = int(x - w/2), int(y - h/2)
            x2, y2 = int(x + w), int(y + h)
            list_get[list_x1].append(x)
            list_get[list_y1].append(y)
            list_get[list_x2].append(x2)
            list_get[list_y2].append(y2)

    list_keys = list(list_get.keys())
    for idx, filename in enumerate(os.listdir(image_path)):
        img = cv2.imread(image_path + '/' + filename)
        # img = np.rollaxis(img, 2, 0)
        for j in range(len(list_keys) // 4):
            x1_y1 = (list_get[list_keys[j * 4:j * 4 + 4][0]][idx], list_get[list_keys[j * 4:j * 4 + 4][1]][idx])
            x2_y2 = (list_get[list_keys[j * 4:j * 4 + 4][2]][idx], list_get[list_keys[j * 4:j * 4 + 4][3]][idx])
            img = cv2.rectangle(img, x1_y1, x2_y2, color[j], thickness=2)
            # img = cv2.rectangle(img, (list_x1_gt[idx], list_y1_gt[idx]), (list_x2_gt[idx], list_y2_gt[idx]), (255, 255, 0), thickness=1)
        print('已完成的帧数：' + str(idx))
        cv2.imwrite(save_folder_real + '/' + '/%s_%0.7d.jpg' % (filename.split('.')[0], idx), img)

    # f_gt.close()
    f_result.close()

if __name__ == '__main__':
    ground_truth = 'D:/UAV_datasets/Dataset-UAV-123/data/Dataset_UAV123/UAV123/anno/UAV123/bike1.txt'
    results_path = ['D:/无人机跟踪项目/capture_video/SiamFC/bike1.txt', ground_truth]
    our_result_path = ''
    image_path = 'D:/UAV_datasets/Dataset-UAV-123/data/Dataset_UAV123/UAV123/data_seq/UAV123/bike1'
    save_folder = 'C:/Master_Library/My Reasearch Code Library/tracker_analyse/tracker_processing/Save'
    draw_bbox(image_path, save_folder, *results_path)





