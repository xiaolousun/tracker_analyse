function out = getScaleSubwindow(im, pos, base_target_sz, scale_factors, scale_window, scale_model_sz, hog_scale_cell_size)

% code from DSST
global opts
% code from DSST
w2c = opts.w2c;
num_scales = length(scale_factors);

for s = 1:num_scales
    patch_sz = floor(base_target_sz * scale_factors(s));
    %make sure the size is not to small
    patch_sz = max(patch_sz, 2);
 
    xs = floor(pos(2)) + (1:patch_sz(2)) - floor(patch_sz(2)/2);
    ys = floor(pos(1)) + (1:patch_sz(1)) - floor(patch_sz(1)/2);
    
    %check for out-of-bounds coordinates, and set them to the values at
    %the borders
    xs(xs < 1) = 1;
    ys(ys < 1) = 1;
    xs(xs > size(im,2)) = size(im,2);
    ys(ys > size(im,1)) = size(im,1);
    
    %extract image
    im_patch = im(ys, xs, :);
    
    % resize image to model size
    im_patch_resized = mexResize(im_patch, scale_model_sz, 'auto');
    
    % extract scale features
    temp_hog = fhog(single(im_patch_resized), hog_scale_cell_size);
    temp = temp_hog(:,:,1:31);
    
    im_patch_resized = mexResize(im_patch, [size(temp_hog,1), size(temp_hog,2)], 'auto');    
    out_npca = get_feature_map(im_patch_resized, 'gray', w2c);
    out_pca = get_feature_map(im_patch_resized, 'cn', w2c);
    if(opts.color)
        temp = cat(3,temp,out_npca);
        temp = cat(3,temp,out_pca);    
    end
    if s == 1
        out = zeros(numel(temp), num_scales, 'single');
    end
    
    % window
    out(:,s) = temp(:) * scale_window(s);
end
