close all; clear; clc;
%% CRYTID Boardgame assist tool
% Cryptid online : https://ospreypublishing.com/playcryptid/
% made ny sisi21
% github : https://github.com/sisin21/boardgame-tool
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
Grid3={'m','m','g','g','g','b';'m','m','g','w','b','b';'w','w','w','w','b','b'};
Grid4={'y','y','w','w','w','w';'y','y','w','b','b','b';'y','y','y','g','g','g'};
Grid5={'m','m','m','w','w','w';'m','y','y','b','w','w';'y','y','b','b','b','b'};
Grid6={'y','y','m','m','m','g';'w','w','m','m','g','g';'w','b','b','b','b','g'};
%{
bare : 1
kuger : 2
%}
animalmap1={0,0,0,0,0,0;0,0,0,0,0,0;0,0,0,1,1,1};
animalmap2={2,2,2,0,0,0;0,0,0,0,0,0;0,0,0,0,0,0};
animalmap3={0,0,0,0,0,0;2,2,0,0,0,0;2,0,0,0,0,0};
animalmap4={0,0,0,0,0,0;0,0,0,0,0,2;0,0,0,0,0,2};
animalmap5={0,0,0,0,0,0;0,0,0,0,0,1;0,0,0,0,1,1};
animalmap6={1,0,0,0,0,0;1,0,0,0,0,0;0,0,0,0,0,0};
%{
White ▲ : 1
White ● : 2
Blue ▲ : 3
Blue ● : 4
Green ▲ : 5
Green ● : 6
Dark ▲ : 7
Dark ● : 8
%}
sp={0,0,0,0,0,0;0,0,0,0,0,0;0,0,0,0,0,0};
structuremap=[sp,sp;sp,sp;sp,sp];
%% Typing Map Tile
fprintf("Typing Map number.\n\n");
for i=1:6
    prompt = 'Commander>> ';
    num = input(prompt);
    if num == 1
        map{i}=Grid1;
        animalmap{i}=animalmap1;
    elseif num == 2
        map{i}=Grid2;
        animalmap{i}=animalmap2;
    elseif num == 3
        map{i}=Grid3;
        animalmap{i}=animalmap3;
    elseif num == 4
        map{i}=Grid4;
        animalmap{i}=animalmap4;
    elseif num == 5
        map{i}=Grid5;
        animalmap{i}=animalmap5;
    elseif num == 6
        map{i}=Grid6;
        animalmap{i}=animalmap6;
    else
        fprintf('error\n');
        break;
    end
end
clc;
fprintf("Typing Reverse Map number.\n\n");
for i=1:6
    prompt = 'Commander>> ';
    num = input(prompt);
    if num == 1
        map{1}=flip(map{1});
        map{1}=flip(map{1},2);
        animalmap{1}=flip(animalmap{1});
        animalmap{1}=flip(animalmap{1},2);
    elseif num == 2
        map{2}=flip(map{2});
        map{2}=flip(map{2},2);
        animalmap{2}=flip(animalmap{2});
        animalmap{2}=flip(animalmap{2},2);
    elseif num == 3
        map{3}=flip(map{3});
        map{3}=flip(map{3},2);
        animalmap{3}=flip(animalmap{3});
        animalmap{3}=flip(animalmap{3},2);
    elseif num == 4
        map{4}=flip(map{4});
        map{4}=flip(map{4},2);
        animalmap{4}=flip(animalmap{4});
        animalmap{4}=flip(animalmap{4},2);
    elseif num == 5
        map{5}=flip(map{5});
        map{5}=flip(map{5},2);
        animalmap{5}=flip(animalmap{5});
        animalmap{5}=flip(animalmap{5},2);
    elseif num == 6
        map{6}=flip(map{6});
        map{6}=flip(map{6},2);
        animalmap{6}=flip(animalmap{6});
        animalmap{6}=flip(animalmap{6},2);
    else
        fprintf('null\n');
        break;
    end
end
map=[map{1},map{2};map{3},map{4};map{5},map{6}];
animalmap=[animalmap{1},animalmap{2};animalmap{3},animalmap{4};animalmap{5},animalmap{6}];
%% Honeycomb map making
r=10;
a=0;
b=0;
pause(1);

figure(1)
set(figure(1), 'OuterPosition', [3, 3, 840, 840]);
for i=1:12
    for j=1:9
        t=0:pi/3:2*pi;
        x=a+(1.5*(i-1)*r)+r*cos(t);
        y=b-(1/2*cos(i*pi)*sqrt(3)*(r/2))+(j*sqrt(3)*(r))+r*sin(t);
        figure(1)
        
        fill(x,y,map{10-j,i});        
        %% display cell number
        a1=a+(1.5*(i-1)*r)-0.7*r;
        b1=b-(1/2*cos(i*pi)*sqrt(3)*(r/2))+(j*sqrt(3)*(r));
        txt=[num2str(10-j),',',num2str(i)];
        text(a1,b1,txt);
        
        axis([-15 180 -15 180]);
        hold on
    end
end
for i=1:12
    for j=1:9
        t=0:pi/3:2*pi;
        x=a+(1.5*(i-1)*r)+r*cos(t);
        y=b-(1/2*cos(i*pi)*sqrt(3)*(r/2))+(j*sqrt(3)*(r))+r*sin(t);
        figure(1)
        if animalmap{10-j,i}==1
            plot(x,y,'color','#828282',...
            'LineWidth',5)
        elseif animalmap{10-j,i}==2
            plot(x,y,'r',...
            'LineWidth',5)
        else
        end
    end
end
%% Structure
clc;
fprintf("(1/16) x of White ▲ : ");
prompt = 'Commander>> ';
sx = input(prompt);
fprintf("(2/16) y of White ▲ : ");
prompt = 'Commander>> ';
sy = input(prompt);
structuremap{sx,sy}=1;

clc;
fprintf("(3/16) x of White ● : ");
prompt = 'Commander>> ';
sx = input(prompt);
fprintf("(4/16) y of White ● : ");
prompt = 'Commander>> ';
sy = input(prompt);
structuremap{sx,sy}=2;

clc;
fprintf("(5/16) x of Blue ▲ : ");
prompt = 'Commander>> ';
sx = input(prompt);
fprintf("(6/16) y of Blue ▲ : ");
prompt = 'Commander>> ';
sy = input(prompt);
structuremap{sx,sy}=3;

clc;
fprintf("(7/16) x of Blue ● : ");
prompt = 'Commander>> ';
sx = input(prompt);
fprintf("(8/16) y of Blue ● : ");
prompt = 'Commander>> ';
sy = input(prompt);
structuremap{sx,sy}=4;

clc;
fprintf("(9/16) x of Green ▲ : ");
prompt = 'Commander>> ';
sx = input(prompt);
fprintf("(10/16) y of Green ▲ : ");
prompt = 'Commander>> ';
sy = input(prompt);
structuremap{sx,sy}=5;

clc;
fprintf("(11/16) x of Green ● : ");
prompt = 'Commander>> ';
sx = input(prompt);
fprintf("(12/16) y of Green ● : ");
prompt = 'Commander>> ';
sy = input(prompt);
structuremap{sx,sy}=6;

clc;
fprintf("(13/16) x of Dark ▲ : ");
prompt = 'Commander>> ';
sx = input(prompt);
fprintf("(14/16) y of Dark ▲ : ");
prompt = 'Commander>> ';
sy = input(prompt);
structuremap{sx,sy}=7;

clc;
fprintf("(15/16) x of Dark ● : ");
prompt = 'Commander>> ';
sx = input(prompt);
fprintf("(16/16) y of Dark ● : ");
prompt = 'Commander>> ';
sy = input(prompt);
structuremap{sx,sy}=8;
for i=1:12
    for j=1:9     
        %% display structure
        a1=a+(1.5*(i-1)*r);
        b1=b-(1/2*cos(i*pi)*sqrt(3)*(r/2))+((10-j)*sqrt(3)*(r));
        if structuremap{j,i}==1
            txt=['▲'];
            text(a1,b1,txt,'color','w','FontSize',20);
        elseif structuremap{j,i}==2
            txt=['●'];
            text(a1,b1,txt,'color','w','FontSize',20);
        elseif structuremap{j,i}==3
            txt=['▲'];
            text(a1,b1,txt,'color','#0099FF','FontSize',20);
        elseif structuremap{j,i}==4
            txt=['●'];
            text(a1,b1,txt,'color','#0099FF','FontSize',20);
        elseif structuremap{j,i}==5
            txt=['▲'];
            text(a1,b1,txt,'color','#B9F96B','FontSize',20);
        elseif structuremap{j,i}==6
            txt=['●'];
            text(a1,b1,txt,'color','#B9F96B','FontSize',20);
        elseif structuremap{j,i}==7
            txt=['▲'];
            text(a1,b1,txt,'color','k','FontSize',20);
        elseif structuremap{j,i}==8
            txt=['●'];
            text(a1,b1,txt,'color','k','FontSize',20);
        end
        hold on
    end
end
%% Find Cryptid
clc;
fprintf("Water : b\nForest : g\nSwamp : m\nMount : w\nDesert : y\nbare : gray\nkuger : red\nGame End : end\n\n");
prompts = 'Commander>> ';
while 1
    non = input(prompts,'s');
    
    if non == 'end'
%         close all;
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