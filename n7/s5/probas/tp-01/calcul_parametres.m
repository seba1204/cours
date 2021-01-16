function [r,a,b] = calcul_parametres(X,Y)
    x_moy = mean(X);
    y_moy = mean(Y);
    sig_x = sqrt(mean((X - x_moy).^2));
    sig_y = sqrt(mean((Y - y_moy).^2));
    sig_xy = mean((Y - y_moy).*(X - x_moy));
    r = sig_xy / (sig_x .* sig_y);
    a = sig_xy / (sig_x ^ 2);
    b = y_moy - x_moy .* (sig_xy ./ (sig_x .^ 2));
end

