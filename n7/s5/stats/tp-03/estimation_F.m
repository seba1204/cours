function [rho_F,theta_F] = estimation_F(rho,theta)
    X = [cos(theta) sin(theta)] \ rho;
    xf = X(1);
    yf = X(2);

    rho_F = sqrt(xf^2 + yf^2);
    theta_F = atan2(yf, xf);
end
