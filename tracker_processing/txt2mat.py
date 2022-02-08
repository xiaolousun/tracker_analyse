import os
import numpy as np
import scipy.io as sio

def txt2mat(txt_path:str, save_path:str, dataset_name:str):

    save_mat_folder_path = save_path + '/' + 'tracker_mat_results/%s_mat_results/' %(dataset_name)
    txt_folder_List = os.listdir(txt_path)
    mat_List = os.listdir(save_mat_folder_path)
    txt_folder_List = list(set(txt_folder_List).difference(set(mat_List)))

    for idx_f, folder_txt in enumerate(txt_folder_List):
        real_txt_path = os.path.join(txt_path, folder_txt)
        txt_List = os.listdir(real_txt_path)

        for txt_name in txt_List:
            if 'txt' not in txt_name:
                txt_List.remove(txt_name)

        for i, txt_name in enumerate(txt_List):
            folder_path = os.path.join(real_txt_path, txt_name)
            txt_file = open(folder_path)
            list_txt = txt_file.readlines()
            data_txt = []
            for idx in range(len(list_txt)):
                line_txt = list_txt[idx].rstrip('\n').split(',')
                line_txt = list(map(lambda x: float(x), line_txt))
                data_txt.append(line_txt)
            data_txt = np.array(data_txt)
            data = np.empty((1, 1), dtype=object)
            data[0, 0] = {}
            data[0, 0]['res'] = data_txt
            data[0, 0]['len'] = len(data_txt)
            data[0, 0]['type'] = 'rect'
            # sio.savemat(save_path + txt_name.split('.')[0] + '_' + txt_path.split('/')[-1] + '.mat', {'results': {'res': data_txt}})
            save_mat_path = save_path + '/' + 'tracker_mat_results/' + '%s_mat_results/%s' % (dataset_name, folder_txt)
            if not os.path.exists(save_mat_path):
                os.makedirs(save_mat_path)
            sio.savemat(save_mat_path + '/' + txt_name.split('.')[0] + '_' + folder_txt + '.mat',
                        {'results': data})
        print(folder_txt + ' is complete')
        # print(data_txt)

if __name__ == '__main__':
    txt_path = './SiamFC'
    save_path = 'D:/test_video/result_mat_UAV123/'
    txt2mat(txt_path, save_path, 'UAV123')


