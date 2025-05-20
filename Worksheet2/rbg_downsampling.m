clc;	% Clear command window.
clear;	% Delete all variables.

fontSize=15;

folder='/';
baseFileName='lena512color.tiff';

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

title('Original color Image', 'FontSize', fontSize);
% Enlarge figure to full screen.
set(gcf, 'Position', get(0,'Screensize')); 

% Extract the individual red, green, and blue color channels.
redChannel = rgbImage(:, :, 1);
greenChannel = rgbImage(:, :, 2);
blueChannel = rgbImage(:, :, 3);



% Convert to YCbCr

% Extract the individual Y, Cb, and Cr color channels.


figure(3);



dat=rgbImage;
dat2 = dat(310:375,334:399,:);
[h,w,dummy] = size(dat2);
dat2 = double(dat2);

%reduce the data. Average 2x2 blocks
for lx=1:w/2,
for ly=1:h/2,
  x = (lx-1)*2+1;
  y = (ly-1)*2+1;
  dat_reduced(ly,lx,1) = (dat2(y,x,1) + dat2(y+1,x,1) + dat2(y,x+1,1) + dat2(y+1,x+1,1))/4;
  dat_reduced(ly,lx,2) = (dat2(y,x,2) + dat2(y+1,x,2) + dat2(y,x+1,2) + dat2(y+1,x+1,2))/4;
  dat_reduced(ly,lx,3) = (dat2(y,x,3) + dat2(y+1,x,3) + dat2(y,x+1,3) + dat2(y+1,x+1,3))/4;
end
end

% use interpolation methods to reconstruct an image
% of the original size

dat_reconstructed = zeros(h-1,w-1,3);

dat_reconstructed(:,:,1) = interp2([1:2:h],[1:2:w]',dat_reduced(:,:,1), [1:h-1],[1:w-1]','nearest');
dat_reconstructed(:,:,2) = interp2([1:2:h],[1:2:w]',dat_reduced(:,:,2), [1:h-1],[1:w-1]','nearest');
dat_reconstructed(:,:,3) = interp2([1:2:h],[1:2:w]',dat_reduced(:,:,3), [1:h-1],[1:w-1]','nearest');
rgbImage2 = uint8(dat_reconstructed);




% Reconstruct the RGB image from the individual Y, Cb, and Cr color channels.
reconRGBImage = rgbImage(310:374,334:398,:);
%rgbImage2(:,:,1)=redChannel(310:374,334:398,1);
reconRGBImage2=rgbImage2;

subplot(2, 1, 1);
imshow(reconRGBImage);

subplot(2, 1, 2);
imshow(reconRGBImage2);
%title('Reconstructed RGB Image', 'FontSize', fontSize);
