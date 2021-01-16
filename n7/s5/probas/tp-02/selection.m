function [selection_frequences,selection_alphabet] = selection(frequences,alphabet)
% frequences : frequences des caractères
% alphabet : vecteurs des caractères
indices = find(frequences > 0);
selection_frequences = frequences(indices);
selection_alphabet = alphabet(indices);

end

