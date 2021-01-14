function [C_estime,R_moyen] = estimation_1(x_donnees_bruitees,y_donnees_bruitees,n_tests)

%% Centre de gravité
[~, size_x] = size (x_donnees_bruitees);
[~, size_y] = size (x_donnees_bruitees);
Gx = sum(x_donnees_bruitees()) / size_x;
Gy = sum(y_donnees_bruitees()) / size_y;
%% Rayon moyen
R = mean(sqrt((x_donnees_bruitees-Gx).^2 + (y_donnees_bruitees-Gy).^2));
%% Tirages des centres
Cx = Gx - R + rand(n_tests,1) * 2*R;
Cy = Gy - R + rand(n_tests,1) * 2*R;


%% Calcul du minimum
Cx_aug = repmat(Cx, 1, size_x);
Cy_aug = repmat(Cy, 1, size_y);
x_aug = repmat(x_donnees_bruitees, n_tests, 1);
y_aug = repmat(y_donnees_bruitees, n_tests, 1);

distances = sqrt ((Cx_aug - x_aug).^2 + (Cy_aug - y_aug).^2);
E = (distances - R) .^2;

A = sum(E,2);
[~,i] = min(A);

%% Resultats
R_moyen = R;
C_estime = [Cx(i) Cy(i)];

end

