clear all;close all;


fr =fopen('lena.raw','r');
lena_raw=fread(fr);


%grayscale?
lena_raw=reshape(lena_raw,512,512);
lena_raw=lena_raw/256;
figure;
imshow(lena_raw');
xs=0:1:255;
ys=histc(reshape(256*lena_raw(:,:),1,size(lena_raw(:,:),1)*size(lena_raw(:,:),2)),xs);
figure;
plot(xs,ys,'Color',[0.5 0.5 0.5]);
xlabel('intensity');
ylabel('frequency');
%% --> wird las 3-dimensionale Matrix interpretiert --> Farbraum rgb!
lena3(:,:,1)=lena_raw';

lena3(:,:,2:3)=zeros(512,512,2);
figure;
imshow(lena3);
%% shift durch den Farbraum
lena3(:,:,2)=lena3(:,:,1);lena3(:,:,1)=lena3(:,:,3);
figure;
imshow(lena3);
%%
lena3(:,:,3)=lena3(:,:,2);lena3(:,:,2)=lena3(:,:,1);
figure;
imshow(lena3);

%% Lena in Farbe
lenac=imread('lena512color.tiff');
figure;
imshow(lenac);
lenac=double(lenac);
lenar=zeros(512,512,3);lenar(:,:,1)=lenac(:,:,1);
lenab=zeros(512,512,3);lenab(:,:,2)=lenac(:,:,2);
lenag=zeros(512,512,3);lenag(:,:,3)=lenac(:,:,3);
figure(1);clf;
subimage((lenar/255))
figure(2);clf;
subimage((lenab/255))
figure(3);clf;
subimage((lenag/255))
%% Farbhistorgramme
xs=0:1:255;
figure(2); clf;
r_lena=histc(reshape(lenac(:,:,1),1,size(lenac(:,:,1),1)*size(lenac(:,:,1),2)),xs);
g_lena=histc(reshape(lenac(:,:,2),1,size(lenac(:,:,2),1)*size(lenac(:,:,2),2)),xs);
b_lena=histc(reshape(lenac(:,:,3),1,size(lenac(:,:,3),1)*size(lenac(:,:,3),2)),xs);
figure(1);clf;box on;hold all;
plot(xs,r_lena,'r');
plot(xs,g_lena,'g');
plot(xs,b_lena,'b');




%%
%%