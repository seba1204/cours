function [output] = calcul_frequences(text,ele)
% text : texte dans lequel on va compter la fréquence d'apparition des
% éléments
% 
% ele : vecteurs contenant les éléments que l'on veut compter
output = zeros(length(ele), 1);
for i = 1:length(text)
    output = output + (ele == text(i));
end
output = output / (length(text));
end

