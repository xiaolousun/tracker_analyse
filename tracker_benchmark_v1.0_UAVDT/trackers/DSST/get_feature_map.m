function out = get_feature_map(im_patch)

global opts
w2c = opts.w2c;
% allocate space
out = zeros(size(im_patch, 1), size(im_patch, 2), 28, 'single');

% if grayscale image
if size(im_patch, 3) == 1
    out(:,:,1) = single(im_patch)/255 - 0.5;
    temp = fhog(single(im_patch), 1);
    out(:,:,2:28) = temp(:,:,1:27);
else
    out(:,:,1) = single(rgb2gray(im_patch))/255 - 0.5;
    temp = fhog(single(im_patch), 1);
    out(:,:,2:28) = temp(:,:,1:27);
    
    out_pca = get_cn_feature_map(im_patch, 'cn', w2c);
    out = cat(3,out,out_pca);    
end
