close all; clear; clc;
%% CRYTID Boardgame assist tool
% Cryptid online : https://ospreypublishing.com/playcryptid/
% made ny sisi21
% github : https://github.com/sisin21/boardgame-tool
%% Terrain
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
%% Typing map Tile
fprintf("Typing map number.\n\n");
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
fprintf("Typing Reverse map number.\n\n");
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
terrainmap=map;
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
%% My clue
clc;
fprintf("terrain : t\nanimal : a\nstruckColor : sc\nstructType : st\nGame End : end\n\n");
prompts = 'What type>> ';
now = input(prompts,'s');
if now == 't'
    prompts = 'How much distancd>> ';
    now = input(prompts);
    if now == 0
        prompts = 'Inverse tile?[Y/S]>> ';
        now = input(prompts,'s');
        if now == 'Y'
            for i=1:2
                fprintf("Water : b\nForest : g\nSwamp : m\nMount : w\nDesert : y\n\n");
                prompts = 'Type>> ';
                now = input(prompts,'s');
                for k=1:108
                    if map{k} == now
                        map{k}='k';
                    end
                end
            end
        elseif now == 'N'
            fprintf("Water : b\nForest : g\nSwamp : m\nMount : w\nDesert : y\n\n");
            prompts = 'Type>> ';
            now1 = input(prompts,'s');
            fprintf("Water : b\nForest : g\nSwamp : m\nMount : w\nDesert : y\n\n");
            prompts = 'Type>> ';
            now2 = input(prompts,'s');
            for k=1:108
                if map{k} != now1
                    if map{k} != now2
                        map{k}='k';
                    end
                end
            end
        end
    elseif now == 1
        prompts = 'Inverse tile?[Y/S]>> ';
        now = input(prompts,'s');
        if now == 'Y'
            fprintf("Water : b\nForest : g\nSwamp : m\nMount : w\nDesert : y\n\n");
            prompts = 'Type>> ';
            now = input(prompts,'s');
            if map{1,1} == now
                map{1,1} = 'k';
                map{2,1} = 'k';
                map{1,2} = 'k';
            end
            if map{1,12} == now
                map{1,11} = 'k';
                map{1,12} = 'k';
                map{2,11} = 'k';
                map{2,12} = 'k';
            end
            if map{9,1} == now
                map{8,1} = 'k';
                map{8,2} = 'k';
                map{9,1} = 'k';
                map{9,2} = 'k';
            end
            if map{9,12} == now
                map{8,12} = 'k';
                map{9,11} = 'k';
                map{9,12} = 'k';
            end
            for j = 2:11
                if ~mod(j,2) == 1
                    if map{1,j} == now
                        map{1,j} = 'k';
                        map{1,j-1} = 'k';
                        map{1,j+1} = 'k';
                        map{2,j} = 'k';
                        map{2,j-1} = 'k';
                        map{2,j+1} = 'k';
                    end
                elseif ~mod(j,2) == 0
                    if map{1,j} == now
                        map{1,j} = 'k';
                        map{1,j-1} = 'k';
                        map{1,j+1} = 'k';
                        map{2,j} = 'k';
                    end
                end
                if mod(j,2) == 1
                    if map{1,j} == now
                        map{9,j} = 'k';
                        map{9,j-1} = 'k';
                        map{9,j+1} = 'k';
                        map{8,j} = 'k';
                        map{8,j-1} = 'k';
                        map{8,j+1} = 'k';
                    end
                elseif mod(j,2) == 0
                    if map{1,j} == now
                        map{9,j} = 'k';
                        map{9,j-1} = 'k';
                        map{9,j+1} = 'k';
                        map{8,j} = 'k';
                    end
                end
            end
            for i = 2:8
               for j = 2:11
                   if map{i,j} == now
                       map{i-1,j} = 'k';
                       map{i,j} = 'k';
                       map{i+1,j} = 'k';
                       ii = ~mod(j,2);
                       map{i+ii-1,j-1} = 'k';
                       map{i+ii,j-1} = 'k';
                       map{i+ii-1,j+1} = 'k';
                       map{i+ii,j+1} = 'k';
                   end
               end
            end
            for i = 2:8
                if map{i,1} == now
                    map{i-1,1} = 'k';
                    map{i,1} = 'k';
                    map{i+1,1} = 'k';
                    map{i-1,2} = 'k';
                    map{i,2} = 'k';
                end
                if map{i,12} == now
                    map{i-1,12} = 'k';
                    map{i,12} = 'k';
                    map{i+1,12} = 'k';
                    map{i,11} = 'k';
                    map{i+1,11} = 'k';
                end
            end
        elseif now == 'N'
            %% #############################
            blackmap = {};
            for i = 1:9
                for j = 1:12
                    blackmap{i,j} = 'k';
                end
            end
            fprintf("Water : b\nForest : g\nSwamp : m\nMount : w\nDesert : y\n\n");
            prompts = 'Type>> ';
            now = input(prompts,'s');
            if map{1,1} == now
                blackmap{1,1} = map{1,1};
                blackmap{2,1} = map{2,1};
                blackmap{1,2} = map{1,2};
            end
            if map{1,12} == now
                blackmap{1,11} = map{1,11};
                blackmap{1,12} = map{1,12};
                blackmap{2,11} = map{2,11};
                blackmap{2,12} = map{2,12};
            end
            if map{9,1} == now
                blackmap{8,1} = map{8,1};
                blackmap{8,2} = map{8,2};
                blackmap{9,1} = map{9,1};
                blackmap{9,2} = map{9,2};
            end
            if map{9,12} == now
                blackmap{8,12} = map{8,12};
                blackmap{9,11} = map{9,11};
                blackmap{9,12} = map{9,12};
            end
            for j = 2:11
                if ~mod(j,2) == 1
                    if map{1,j} == now
                        blackmap{1,j} = map{1,j};
                        blackmap{1,j-1} = map{1,j-1};
                        blackmap{1,j+1} = map{1,j+1};
                        blackmap{2,j} = map{2,j};
                        blackmap{2,j-1} = map{2,j-1};
                        blackmap{2,j+1} = map{2,j+1};
                    end
                elseif ~mod(j,2) == 0
                    if map{1,j} == now
                        blackmap{1,j} = map{1,j};
                        blackmap{1,j-1} = map{1,j-1};
                        blackmap{1,j+1} = map{1,j+1};
                        blackmap{2,j} = map{2,j};
                    end
                end
                if mod(j,2) == 1
                    if map{1,j} == now
                        blackmap{9,j} = map{9,j};
                        blackmap{9,j-1} = map{9,j-1};
                        blackmap{9,j+1} = map{9,j+1};
                        blackmap{8,j} = map{8,j};
                        blackmap{8,j-1} = map{8,j-1};
                        blackmap{8,j+1} = map{8,j+1};
                    end
                elseif mod(j,2) == 0
                    if map{1,j} == now
                        blackmap{9,j} = map{9,j};
                        blackmap{9,j-1} = map{9,j-1};
                        blackmap{9,j+1} = map{9,j+1};
                        blackmap{8,j} = map{8,j};
                    end
                end
            end
            for i = 2:8
               for j = 2:11
                   if map{i,j} == now
                       blackmap{i-1,j} = map{i-1,j};
                       blackmap{i,j} = map{i,j};
                       blackmap{i+1,j} = map{i+1,j};
                       ii = ~mod(j,2);
                       blackmap{i+ii-1,j-1} = map{i+ii-1,j-1};
                       blackmap{i+ii,j-1} = map{i+ii,j-1};
                       blackmap{i+ii-1,j+1} = map{i+ii-1,j+1};
                       blackmap{i+ii,j+1} = map{i+ii,j+1};
                   end
               end
            end
            for i = 2:8
                if map{i,1} == now
                    blackmap{i-1,1} = map{i-1,1};
                    blackmap{i,1} = map{i,1};
                    blackmap{i+1,1} = map{i+1,1};
                    blackmap{i-1,2} = map{i-1,2};
                    blackmap{i,2} = map{i,2};
                end
                if map{i,12} == now
                    blackmap{i-1,12} = map{i-1,12};
                    blackmap{i,12} = map{i,12};
                    blackmap{i+1,12} = map{i+1,12};
                    blackmap{i,11} = map{i,11};
                    blackmap{i+1,11} = map{i+1,11};
                end
            end
        end
    end
    
elseif now == 'a'
    prompts = 'How much distancd>> ';
    now = input(prompts);
    if now == 1
        prompts = 'Inverse tile?[Y/S]>> ';
        now = input(prompts,'s');
        
        if now == 'N'
            
        elseif now == 'Y'
            
        end
    elseif now == 2
        prompts = 'bear or couger?[B/C]>> ';
        now = input(prompts,'s');
        
        if now == 'B'
            prompts = 'Inverse tile?[Y/S]>> ';
            now = input(prompts,'s');

            if now == 'N'

            elseif now == 'Y'

            end
        elseif now == 'C'
            prompts = 'Inverse tile?[Y/S]>> ';
            now = input(prompts,'s');

            if now == 'N'

            elseif now == 'Y'

            end
        end
    end
elseif now == 'sc'
    
elseif now == 'st'
    
elseif now == 'end'
    
end
%% Find Cryptid
fprintf("Water : b\nForest : g\nSwamp : m\nMount : w\nDesert : y\nbear : gray\ncougar : red\nGame End : end\n\n");
prompts = 'Type>> ';
while 1
    now = input(prompts,'s');
    
    if now == 'end'
%         close all;
        break;
    end
    
    for k=1:108
        if map{k} == now
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