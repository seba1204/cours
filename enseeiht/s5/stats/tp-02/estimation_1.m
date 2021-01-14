function [a_DYX_1,b_DYX_1] = estimation_1(x_donnees_bruitees,y_donnees_bruitees,n_tests)
%% Centre de gravité
[~, size_x] = size (x_donnees_bruitees);
[~, size_y] = size (y_donnees_bruitees);
Gx = sum(x_donnees_bruitees()) / size_x;
Gy = sum(y_donnees_bruitees()) / size_y;

x_centree = x_donnees_bruitees - Gx;
y_centree = y_donnees_bruitees - Gy;

%% Tirages des psi
p = -pi/2 + rand(n_tests,1) * pi;


%% Matrices augmentées

p_aug = repmat(p, 1, size_y);
% Remarque : size_y = size_x

x_aug = repmat(x_centree, n_tests, 1);
y_aug = repmat(y_centree, n_tests, 1);


%% Equation (4) du sujet
E = (y_aug - tan(p_aug).*x_aug).^2;
A = sum(E, 2);

%% Minimums
[~,i] = min(A);
Psi = p(i);

%% Paramètres de sortie
a_DYX_1 = tan(Psi);
b_DYX_1 = mean(y_donnees_bruitees) - a_DYX_1 * mean(x_donnees_bruitees);

end