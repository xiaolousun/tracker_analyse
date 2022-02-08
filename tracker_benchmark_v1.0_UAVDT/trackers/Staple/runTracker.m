function runTracker
% RUN_TRACKER  is the external function of the tracker - does initialization and calls trackerMain
    close all;
    warning off;
    sequence = 'matrix';
    global opts
    opts.color = 1;
    %% Read params.txt
    params = readParams('params.txt');
	%% load video info
	sequence_path = ['E:\Datasets\SOT\vot2016\' sequence '\'];
% 	sequence_path = ['E:\Datasets\MOT\MOT16\test\MOT16-14\img1\'];    
    img_path = sequence_path;
    %% Read files
    text_files = dir([sequence_path '*.jpg']);
    params.bb_VOT = csvread([sequence_path 'groundtruth.txt']);
%     params.bb_VOT = csvread(['E:\Datasets\MOT\MOT16\test\MOT16-14\det\det.txt']);
        
    region = params.bb_VOT(1,:);
    n_imgs = length(text_files);
    img_files = cell(n_imgs, 1);
    for ii = 1:n_imgs
        img_files{ii} = text_files(ii).name;
    end
       
    im = imread([img_path img_files{1}]);
    % is a grayscale sequence ?
    if(size(im,3)==1)
        params.grayscale_sequence = true;
    end

    params.img_files = img_files;
    params.img_path = img_path;

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if(numel(region)==8)
        % polygon format
        [cx, cy, w, h] = getAxisAlignedBB(region);
    else
        x = region(1);
        y = region(2);
        w = region(3);
        h = region(4);
        cx = x+w/2;
        cy = y+h/2;
    end

    % init_pos is the centre of the initial bounding box
    params.init_pos = [cy cx];
    params.target_sz = round([h w]);
    [params, bg_area, fg_area, area_resize_factor] = initializeAllAreas(im, params);
	if params.visualization
		params.videoPlayer = vision.VideoPlayer('Position', [100 100 [size(im,2), size(im,1)]+30]);
	end
    % in runTracker we do not output anything
	params.fout = -1;
	% start the actual tracking
	trackerMain(params, im, bg_area, fg_area, area_resize_factor);
    fclose('all');
end
