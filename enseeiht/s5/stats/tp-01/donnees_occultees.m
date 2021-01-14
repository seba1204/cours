clear;
close all;

taille_ecran = get(0,'ScreenSize');
L = taille_ecran(3);
H = taille_ecran(4);

% Fenetre d'affichage :
figure('Name','Points situes au voisinage d''un cercle', ...
       'Position',[0.4*L,0.05*H,0.6*L,0.7*H]);
axis equal;
hold on;
set(gca,'FontSize',20);
hx = xlabel('$x$','FontSize',30);
set(hx,'Interpreter','Latex');
hy = ylabel('$y$','FontSize',30);
set(hy,'Interpreter','Latex');

% Bornes d'affichage des donnees centrees en (0,0) :
taille = 20;
bornes = [-taille taille -taille taille];

% angles
tetha_1 = rand * 2 * pi;
tetha_2 = rand * 2 * pi;

% Creation du cercle et des donnees bruitees :
n = 50;
sigma = 0.5;
[x_cercle,y_cercle,x_donnees_bruitees,y_donnees_bruitees,theta_donnees_bruitees] ...
		= creation_cercle_et_donnees_bruitees(taille,n,sigma);
T = theta_donnees_bruitees;
if tetha_1 <= tetha_2
    A = T>=tetha_1 & T<=tetha_2;
else
    A = (T>=0 & T<=tetha_2) | (T>=tetha_1 & T<2*pi);
end
x_donnees_bruitees = x_donnees_bruitees(A);
y_donnees_bruitees = y_donnees_bruitees(A);
% Affichage du cercle :
plot(x_cercle([1:end 1]),y_cercle([1:end 1]),'r','LineWidth',3);

% Affichage des donnees bruitees :
plot(x_donnees_bruitees,y_donnees_bruitees,'k+','MarkerSize',10,'LineWidth',2);
axis(bornes);
lg = legend(' Cercle', ...
		' Donnees bruitees', ...
		'Location','Best');
grid on;
