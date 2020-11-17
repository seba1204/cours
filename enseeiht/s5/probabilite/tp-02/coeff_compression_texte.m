function coeff_compression = coeff_compression_texte(texte,texte_encode)
%COEFF_COMPRESSION_TEXTE Summary of this function goes here
%   Detailed explanation goes here
a = length(texte) * 8;
b = length(texte_encode);

coeff_compression = a/b;
end

