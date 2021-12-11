close all; clear; clc;
%% Terrian
%{
Water : b
Forest : g
Swamp : m
Mount : w
Desert : y
%}
Grid1={'b','b','b','b','g','g';'m','m','b','y','g','g';'m','m','y','y','y','g'};
Grid2={'m','g','g','g','g','g';'m','m','g','y','y','y';'m','w','w','w','w','y'};
Grid3={'m','m','g','g','g','b';'m','m','w','w','w','w';'w','w','w','w','b','b'};
Grid4={'y','y','w','w','w','w';'y','y','w','b','b','b';'y','y','y','g','g','g'};
Grid5={'m','m','m','w','w','w';'m','y','y','b','w','w';'y','y','b','b','b','b'};
Grid6={'y','y','m','m','m','g';'w','w','m','m','g','g';'w','b','b','b','b','g'};

dirG1=flip(Grid1);
dirG1=flip(dirG1,2);

dirG2=flip(Grid2);
dirG2=flip(dirG2,2);

dirG3=flip(Grid3);
dirG3=flip(dirG3,2);

dirG4=flip(Grid4);
dirG4=flip(dirG4,2);

dirG5=flip(Grid5);
dirG5=flip(dirG5,2);

dirG6=flip(Grid6);
dirG6=flip(dirG6,2);

map=[Grid1,Grid2;Grid3,Grid4;Grid5,Grid6];
% Map=input('123');
%% Honeycomb map making
r=10;
a=0;
b=0;
pause(1);

figure(1)
for i=1:12
    for j=1:9
        t=0:pi/3:2*pi;
        x=a+(1.5*(i-1)*r)+r*cos(t);
        y=b-(1/2*cos(i*pi)*sqrt(3)*(r/2))+(j*sqrt(3)*(r))+r*sin(t);
        figure(1)
    %     pause(1);
        plot(x,y,'k')
        a1=a+(1.5*(i-1)*r)-0.7*r;
        b1=b-(1/2*cos(i*pi)*sqrt(3)*(r/2))+(j*sqrt(3)*(r));
        
        fill(x,y,map{10-j,i});
        %% display cell number
        txt=[num2str(i),',',num2str(j)];
        text(a1,b1,txt);
        
        axis([-15 180 -15 180]);
        hold on
    end
end

%% Find Cryptid
fprintf("Water : b\nForest : g\nSwamp : m\nMount : w\nDesert : y\n\n");
prompt = 'non tile: ';
while 1
    non = input(prompt,'s');
    
    if non == 'end'
        close all;
        break;
    end
    
    for k=1:108
        if map{k} == non
            map{k}='k';
        end
    end

    for i=1:12
        for j=1:9
            t=0:pi/3:2*pi;
            x=a+(1.5*(i-1)*r)+r*cos(t);
            y=b-(1/2*cos(i*pi)*sqrt(3)*(r/2))+(j*sqrt(3)*(r))+r*sin(t);
            figure(1)
        %     pause(1);
            plot(x,y,'k')
            a1=a+(1.5*(i-1)*r)-0.7*r;
            b1=b-(1/2*cos(i*pi)*sqrt(3)*(r/2))+(j*sqrt(3)*(r));

            fill(x,y,map{10-j,i});
            %% display cell number
            txt=[num2str(i),',',num2str(j)];
            text(a1,b1,txt);

            axis([-15 180 -15 180]);
            hold on
        end
    end
end