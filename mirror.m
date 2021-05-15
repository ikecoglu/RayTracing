function [Ximg,Yimg,Way] = mirror(Xobj,Yobj,Xmirror,f,Way)
%% Calculations
Xdiff = Xmirror-Xobj;
Xdiffimg = (Xdiff*f)/(Xdiff-f);
Ximg = Xmirror-Xdiffimg;
Yimg = -(Xdiffimg*Yobj)/Xdiff;
if Way=='L'
    Way='R';
else
    Way='L';
end
%% Draw Mirror
angle=[2*pi/3:0.001:4*pi/3];R=Yobj*1.5;
if f>0
    plot(Xmirror-R+R*cos(angle+pi),R*sin(angle+pi),'b','LineWidth', 2)
else
    plot(Xmirror+R+R*cos(angle),R*sin(angle),'b','LineWidth', 2)
end

%% Draw Lines
plot([Xobj Xmirror], [Yobj 0], 'k--', 'LineWidth', 1)
plot([Xmirror Ximg], [0 Yimg], 'k--', 'LineWidth', 1)


plot([Xobj Xmirror], [Yobj Yobj], 'k--', 'LineWidth', 1)
plot([Xmirror Ximg], [Yobj Yimg], 'k--', 'LineWidth', 1)
end

