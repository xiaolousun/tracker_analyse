function [overLap, trackError] = calcError(imgdat, targetPos, gtPos)

[imgHeight, imgWidth, ~] = size(imgdat);

left = max(1,targetPos(1));
top = max(1,targetPos(2));        
right = min(imgWidth, targetPos(1) + targetPos(3) - 1);
down = min(imgHeight, targetPos(2) + targetPos(4) - 1);
realout = zeros(imgHeight, imgWidth);
realout(top:down,left:right) = 1;    
realout = realout > 0;
realPos = [left+right, top+down]/2;

[X, Y] = meshgrid(1:imgWidth, 1:imgHeight);
xv = gtPos(1:2:end);
xv = [xv xv(1)];
yv = gtPos(2:2:end);
yv = [yv yv(1)];
output = inpolygon(X, Y, xv, yv);    
ourPos = [mean(xv(1:4)), mean(yv(1:4))];


% calculate the pixel error
trackError = sqrt(sum((ourPos-realPos).^2));
% calculate the intersect-to-union ratio 
interArea = realout & output;
unionArea = realout | output;
overLap = double(nnz(interArea))/double(nnz(unionArea));
overLap = overLap*100;