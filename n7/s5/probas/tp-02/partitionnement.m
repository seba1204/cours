function bornes = partitionnement(selection_frequences)
%BORNES Summary of this function goes here
%   Detailed explanation goes here
b = zeros(length(selection_frequences)+1, 1);
b(1) = 0;
for i = 1:length(selection_frequences)
    b(i+1) = b(i) + selection_frequences(i);
end
bornes(:,1) = b(1:end-1);
bornes(:,2) = b(2:end);
end

