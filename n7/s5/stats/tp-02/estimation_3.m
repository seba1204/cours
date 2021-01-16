function [theta_Dorth_1,rho_Dorth_1] = estimation_3(x_donnees_bruitees,y_donnees_bruitees,n_tests)
%% Centre de gravité
[~, size_x] = size (x_donnees_bruitees);
[~, size_y] = size (y_donnees_bruitees);
Gx = sum(x_donnees_bruitees()) / size_x;
Gy = sum(y_donnees_bruitees()) / size_y;

x_centree = x_donnees_bruitees - Gx;
y_centree = y_donnees_bruitees - Gy;

%% Tirages des theta
t = rand(n_tests,1) * pi;


%% Matrices augmentées
t_aug = repmat(t, 1, size_y);
% Remarque : size_y = size_x

x_aug = repmat(x_centree, n_tests, 1);
y_aug = repmat(y_centree, n_tests, 1);


%% Equation (4) du sujet
E = (x_aug .* cos(t_aug) + y_aug .* sin (t_aug)).^2;
A = sum(E, 2);

%% Minimums
[~,i] = min(A);
theta_Dorth_1 = t(i);
%% Paramètres de sortie


rho_Dorth_1 = Gx * cos(theta_Dorth_1) + Gy * sin (theta_Dorth_1);

if rho_Dorth_1 < 0 
    theta_Dorth_1 = theta_Dorth_1 - pi;
    rho_Dorth_1 = - rho_Dorth_1;
end

