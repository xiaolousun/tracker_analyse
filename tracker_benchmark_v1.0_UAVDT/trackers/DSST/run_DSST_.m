% function results = run_Staple(seq, res_path, bSaveImage)

global opts
opts.w2c = load('w2crs.mat');

%parameters according to the paper
params.padding = 1.0;         			% extra area surrounding the target
params.output_sigma_factor = 1/16;		% standard deviation for the desired translation filter output
params.scale_sigma_factor = 1/4;        % standard deviation for the desired scale filter output
params.lambda = 1e-2;					% regularization weight (denoted "lambda" in the paper)
params.learning_rate = 0.025;			% tracking model learning rate (denoted "eta" in the paper)
params.number_of_scales = 33;           % number of scale levels (denoted "S" in the paper)
params.scale_step = 1.02;               % Scale increment factor (denoted "a" in the paper)
params.scale_model_max_area = 512;      % the maximum size of scale examples

params.visualization = 1;

[img_files, pos, target_sz, ground_truth, video_path] = load_video_info(seq);

params.init_pos = floor(pos) + floor(target_sz/2);
params.wsize = floor(target_sz);
params.img_files = seq.s_frames;
params.video_path = [];

[positions, fps] = dsst(params);

% save data for OTB-13 benchmark
results.type = 'rect';
results.res = positions;
results.fps = fps;