function [theta_Dorth_2,rho_Dorth_2] = estimation_4(x_donnees_bruitees,y_donnees_bruitees)

    [~, size_x] = size (x_donnees_bruitees);
    [~, size_y] = size (y_donnees_bruitees);
    Gx = sum(x_donnees_bruitees()) / size_x;
    Gy = sum(y_donnees_bruitees()) / size_y;

    x_centree = x_donnees_bruitees - Gx;
    y_centree = y_donnees_bruitees - Gy;
    
    C = [x_centree; y_centree].';
    A = C.' * C;
    [V,D] = eig(A);
    [~,i] = min(diag(D));
    Y = V(:,i);
    theta_Dorth_2 = atan(Y(2)/Y(1));
    rho_Dorth_2 = Gx * cos(theta_Dorth_2) + Gy * sin (theta_Dorth_2);
end

