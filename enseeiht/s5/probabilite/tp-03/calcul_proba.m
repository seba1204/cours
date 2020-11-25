function [x_min,x_max,probabilite] = calcul_proba(E_nouveau_repere,p)
%CALCUL_PROBA Summary of this function goes here
%   Detailed explanation goes here
[a, b] = size(E_nouveau_repere);
x = a * b;
probabilite = 1 - binocdf(a,x,p);
x_min = min(E_nouveau_repere(:,1));
x_max = max(E_nouveau_repere(:,1));
end

