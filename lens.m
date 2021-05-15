function [Ximg,Yimg] = lens(Xobj,Yobj,Xlens,f,Way,DrawLens)
%% Calculations
if Way=='L'
    Xdiff = Xlens-Xobj;
    Xdiffimg = (Xdiff*f)/(Xdiff-f);
    Ximg = Xlens+Xdiffimg;
    Yimg = -(Xdiffimg*Yobj)/Xdiff;
else
    Xdiff = Xobj-Xlens;
    Xdiffimg = (Xdiff*f)/(Xdiff-f);
    Ximg = Xlens-Xdiffimg;
    Yimg = -(Xdiffimg*Yobj)/Xdiff;  
end
%% Draw Lens
if DrawLens==1
    angle=[2*pi/3:0.001:4*pi/3];R=Yobj*1.5;
    if f>0
        plot(Xlens+R/2+R*cos(angle),R*sin(angle),'b','LineWidth', 2)
        plot(Xlens-R/2+R*cos(angle+pi),R*sin(angle+pi),'b','LineWidth', 2)
    else
        plot(Xlens-R+R*cos(angle+pi),R*sin(angle+pi),'b','LineWidth', 2)
        plot(Xlens+R+R*cos(angle),R*sin(angle),'b','LineWidth', 2)
    end
end
%% Draw Lines
plot([Xobj Ximg], [Yobj Yimg], 'k--', 'LineWidth', 1)

plot([Xobj Xlens], [Yobj Yobj], 'k--', 'LineWidth', 1)
plot([Xlens Ximg], [Yobj Yimg], 'k--', 'LineWidth', 1)
end

