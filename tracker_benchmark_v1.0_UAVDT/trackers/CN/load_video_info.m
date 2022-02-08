function [img_files, pos, target_sz] = load_video_info(seq)

s_frames = seq.s_frames;
initstate = seq.init_rect;%initial tracker

% text_files = [gt_path title '.txt'];
% f = fopen(text_files);
% ground_truth = textscan(f, '%f,%f,%f,%f');  %[x, y, width, height]
% ground_truth = cat(2, ground_truth{:});
% frames{1} = 1;
% frames{2} = size(ground_truth, 1);
% fclose(f);

%set initial position and size
target_sz = [initstate(4), initstate(3)];
pos = [initstate(2), initstate(1)];

img_files = s_frames;

% dataset = dir([video_path '*.jpg']);
% cnt = 0;
% for i = frames{1}:frames{2}
%     cnt = cnt + 1;
%     img_files{cnt} = dataset(i).name;
% end