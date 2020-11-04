function image_RVB = ecriture_RVB(image_originale)
    [m,n] = size(image_originale);
    image_RVB(:,:,1) = image_originale(2:2:m,1:2:n);
    image_RVB(:,:,3) = image_originale(1:2:m,2:2:n);
    image_RVB(:,:,2) = (image_originale(1:2:m,1:2:n) + image_originale(2:2:m,2:2:n)) / 2;
end

