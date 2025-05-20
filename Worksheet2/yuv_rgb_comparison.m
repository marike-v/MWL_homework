clc;	% Clear command window.
clear;	% Delete all variables.

fontSize=15;

folder='/';
baseFileName='nordkap.png';

fullFileName = fullfile(folder, baseFileName);
if ~exist(fullFileName, 'file')
	% Didn't find it there.  Check the search path for it.
	fullFileName = baseFileName; % No path this time.
	if ~exist(fullFileName, 'file')
		% Still didn't find it.  Alert user.
		errorMessage = sprintf('Error: %s does not exist.', fullFileName);
		uiwait(warndlg(errorMessage));
		return;
	end
end
rgbImage = imread(fullFileName);
% Get the dimensions of the image.  numberOfColorBands should be = 3.
[rows columns numberOfColorBands] = size(rgbImage);
% Display the original color image.
subplot(3, 4, 1);
imshow(rgbImage);
title('Original color Image', 'FontSize', fontSize);
% Enlarge figure to full screen.
set(gcf, 'Position', get(0,'Screensize')); 

% Extract the individual red, green, and blue color channels.
redChannel = rgbImage(:, :, 1);
greenChannel = rgbImage(:, :, 2);
blueChannel = rgbImage(:, :, 3);

% Display the individual red, green, and blue color channels.
subplot(3, 4, 2);
imshow(redChannel);
title('Red Channel', 'FontSize', fontSize);
subplot(3, 4, 3);
imshow(greenChannel);
title('Green Channel', 'FontSize', fontSize);
subplot(3, 4, 4);
imshow(blueChannel);
title('Blue Channel', 'FontSize', fontSize);

% Convert to YCbCr
ycbcrImage = rgb2ycbcr(rgbImage);

% Extract the individual Y, Cb, and Cr color channels.
YChannel = ycbcrImage(:, :, 1);
CbChannel = ycbcrImage(:, :, 2);
CrChannel = ycbcrImage(:, :, 3);

% Display the individual Y, Cb, and Cr color channels.
subplot(3, 4, 6);
imshow(YChannel);
title('Y Channel', 'FontSize', fontSize);
subplot(3, 4, 7);
CbC=zeros(size(YChannel,1),size(YChannel,2),3);
CbC(:,:,2)=CbChannel;
CbC(:,:,3)=255-CbChannel;
imshow(CbChannel);
title('Cb Channel', 'FontSize', fontSize);
subplot(3, 4, 8);
CrC=zeros(size(YChannel,1),size(YChannel,2),3);
CrC(:,:,1)=CrChannel;
CrC(:,:,3)=255-CrChannel;
imshow(CrChannel);
title('Cr Channel', 'FontSize', fontSize);

% Reconstruct the RGB image from the individual Y, Cb, and Cr color channels.
reconRGBImage = ycbcr2rgb(ycbcrImage);
subplot(3, 4, 11);
imshow(reconRGBImage);
title('Reconstructed RGB Image', 'FontSize', fontSize);
