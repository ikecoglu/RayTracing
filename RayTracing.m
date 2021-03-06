clear;close all;clc;figure, hold on
%% Setup
Way='L';
[Xobj,Yobj]=obj(15,1);

[Ximg,Yimg] = lens(Xobj,Yobj,30,-10,Way,1);
imagePlane(Ximg,Yimg);

[Ximg,Yimg,Way] = mirror(Ximg,Yimg,60,10,Way);
imagePlane(Ximg,Yimg);

[Ximg,Yimg] = lens(Ximg,Yimg,30,-10,Way,0);
imagePlane(Ximg,Yimg);
m=Yimg/Yobj;

%%
lim=xlim;
plot([lim(1) lim(2)],[0 0],'k','LineWidth', 1.5)
set(gcf,'renderer','painters');