function [C_x,C_y,M] = matrice_inertie(E_x,E_y,G_norme_E)
%MATRICE_INERTIE Summary of this function goes here
%   Detailed explanation goes here
Pi = sum(G_norme_E);
C_x = sum(E_x .* G_norme_E) / Pi;
C_y = sum(E_y .* G_norme_E) / Pi;

M(1,1) = sum(G_norme_E .* (E_x - C_x) .^ 2) / Pi;
M(1,2) = sum(G_norme_E .* (E_x - C_x) .* (E_y - C_y)) / Pi;
M(2,1) = sum(G_norme_E .* (E_x - C_x) .* (E_y - C_y)) / Pi;
M(2,2) = sum(G_norme_E .* (E_y - C_y) .^ 2) / Pi;


end

