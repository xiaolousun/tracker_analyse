from tracker_processing.tracker_processing import tracker_analyse
import argparse



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='siamfc tracking')
    parser.add_argument('--video_path',
                        # default='D:/无人机跟踪项目/capture_video/DJI_video/track_video',
                        # default='C:/Users/孙小楼/Desktop/研究生系列比赛/视频素材/camera_uav/跟踪车辆/',
                        # default='./processing_results/picture2video_results',
                        default='C:/Users/孙小楼/Desktop/研究生系列比赛/视频素材/第二次户外飞行/',
                        type=str, help='eval one special video')
    parser.add_argument('--save_folder',
                        default='./processing_results/',
                        type=str, help='eval one special video')
    parser.add_argument('--img_path',
                        default='D:/UAV_datasets/Dataset-UAV-123/data/Dataset_UAV123/UAV123/data_seq/UAV123/bike1',
                        type=str, help='eval one special video')
    parser.add_argument('--results_path',
                        default=['D:/无人机跟踪项目/capture_video/SiamFC/bike1.txt',
                                 'D:/UAV_datasets/Dataset-UAV-123/data/Dataset_UAV123/UAV123/anno/UAV123/bike1.txt',
                                 'C:/Master_Library/My Reasearch Code Library/tracker_analyse/processing_results/tracker_txt_results/UAV123_txt_results/ARCF/bike1.txt',
                                 './processing_results/tracker_txt_results/UAV123_txt_results/AutoTrack/bike1.txt'],
                        type=tuple, help='eval one special video')
    parser.add_argument('--mat_path',
                        default='./processing_results/tracker_mat_results/UAV123_mat_results',
                        type=str, help='eval one special video')
    parser.add_argument('--txt_path',
                        default='./processing_results/tracker_txt_results/UAV123_txt_results',
                        type=str, help='eval one special video')
    parser.add_argument('--picture_path',
                        default='./processing_results/draw_bbox_results/',
                        type=str, help='eval one special video')
    parser.add_argument('--video_fps',
                        default=[25, 20],
                        type=tuple, help='eval one special video')

    args = parser.parse_args()
    tracker_analyse = tracker_analyse()
    tracker_analyse.capture_video(args.video_path, args.save_folder, frame_frequency=100)
    # tracker_analyse.draw_bbox(args.img_path, args.save_folder, *args.results_path)
    # tracker_analyse.mat2txt(args.mat_path, args.save_folder, 'UAV123')
    # tracker_analyse.txt2mat(args.txt_path, args.save_folder, 'UAV123')
    # tracker_analyse.picture2video(args.picture_path, args.save_folder, *args.video_fps)

