function coeff_compression_avant_decorrelation = coeff_compression_image(histogramme,dico)
a = sum(histogramme) * 8;
b = 0;
for i = 1:length(histogramme)
   b = b + histogramme(i) * length(dico{i,2}); 
end
coeff_compression_avant_decorrelation = a/b;
end

