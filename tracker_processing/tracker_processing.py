from .capture_video import capture_video
from .draw_bbox import draw_bbox
from .mat2txt import mat2txt
from .picture2video import picture2video
from .txt2mat import txt2mat

class tracker_analyse(object):

    def __init__(self):
        pass

    def capture_video(self, video_path, save_folder, frame_frequency=1):
        return capture_video(video_path, save_folder, frame_frequency)

    def draw_bbox(self, image_path, save_folder, *results_path):
        return draw_bbox(image_path, save_folder, *results_path)

    def mat2txt(self, mat_path, save_path, dataset_name):
        return mat2txt(mat_path, save_path, dataset_name)

    def picture2video(self, path, save_path, *fps):
        return picture2video(path, save_path, *fps)

    def txt2mat(self, txt_path, save_path, dataset_name):
        return txt2mat(txt_path, save_path, dataset_name)