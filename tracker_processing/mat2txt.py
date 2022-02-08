from scipy.io import loadmat
import numpy as np
import os

def load_mat_data(filename):
    data_dict = loadmat(filename)
    data_list = list(data_dict['results'][0][0][0][0])
    data_list.sort(key=lambda x: x.shape[0])
    data = data_list[-1]
    # data_name = data.keys()
    # a = list(data_name)
    # data_name = a[-1]
    # data = data[data_name]
    return data

def mat2txt(mat_path:str, save_path:str, dataset_name:str):

    save_txt_folder_path = save_path + '/' + 'tracker_txt_results/%s_txt_results/' % (dataset_name)
    fileList = os.listdir(mat_path)  # 读取某个文件夹下的全部文件名字 ，存列表，
    fileList_txt = os.listdir(save_txt_folder_path)
    fileList = list(set(fileList).difference(set(fileList_txt)))

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for i, filename in enumerate(fileList):
        filepath = os.path.join(mat_path, filename)
        mat_file = os.listdir(filepath)
        for mat in mat_file:
            if 'mat' not in mat:
                mat_file.remove(mat)

        for idx, file in enumerate(mat_file):
            real_path = os.path.join(filepath, file)
            data2 =  (real_path)
            name = file.split('.', 1)
            save_txt_path = save_path + '/' + 'tracker_txt_results/%s_txt_results/%s' % (dataset_name, filename)
            if not os.path.exists(save_txt_path):
                os.makedirs(save_txt_path)
            np.savetxt(save_txt_path + '/%s.txt' % (name[0][:len(name[0]) - len(filename) - 1]), data2, fmt='%f',
                       delimiter=',')

        print(filename + ' is complete')

if __name__ == '__main__':
    path = 'D:/Tranditional_algorithm/results_OPE_win10_i7_2080_R2019a/OPE_UAV123'
    savepath = './result_txt_UAV123'
    mat2txt(path, savepath)
