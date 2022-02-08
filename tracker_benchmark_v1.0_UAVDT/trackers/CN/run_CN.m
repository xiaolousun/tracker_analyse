function results = run_CN(seq, res_path, bSaveImage)

%parameters according to the paper
params.padding = 1.0;         			   % extra area surrounding the target
params.output_sigma_factor = 1/16;		   % spatial bandwidth (proportional to target)
params.sigma = 0.2;         			   % gaussian kernel bandwidth
params.lambda = 1e-2;					   % regularization (denoted "lambda" in the paper)
params.learning_rate = 0.075;			   % learning rate for appearance model update scheme (denoted "gamma" in the paper)
params.compression_learning_rate = 0.15;   % learning rate for the adaptive dimensionality reduction (denoted "mu" in the paper)
params.non_compressed_features = {'cn'}; % features that are not compressed, a cell with strings (possible choices: 'gray', 'cn')
params.compressed_features = {'cn'};       % features that are compressed, a cell with strings (possible choices: 'gray', 'cn')
params.num_compressed_dim = 2;             % the dimensionality of the compressed features
params.visualization = 0;

%ask the user for the video
[img_files, pos, target_sz] = load_video_info(seq);

params.init_pos = floor(pos) + floor(target_sz/2);
params.wsize = floor(target_sz);
params.img_files = img_files;

[positions, fps] = color_tracker(params, res_path, bSaveImage);

results.res = positions;
results.type = 'rect';
results.fps = fps;
disp(['fps: ' num2str(results.fps)]);