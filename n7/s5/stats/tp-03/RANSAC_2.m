function [rho_F, theta_F] = RANSAC_2(rho, theta, parametres)
    S1 = parametres(1);
    S2 = parametres(2);
    k_max = parametres(3);

    n = length(rho);

    m_max = 0;
    rho_F = 1;
    theta_F = 1;

    for k = 1:k_max

        % On choisi deux points au hasard
        I = randperm(n, 2);
        nouveau_rho = [rho(I(1)) rho(I(2))];
        nouveau_theta = [theta(I(1)) theta(I(2))];

        % On estime les paramètres à partir de ces points
        [rho_1, theta_1] = estimation_F(nouveau_rho, nouveau_theta);

        % On test les autres données
        C = rho - rho_1 * cos(theta - theta_1) <= S1;
        p = sum(C) / n;

        if p >= S2
            rho_conforme = rho(C);
            theta_conforme = theta(C);
            [rho_2, theta_2, m] = estimation_F_bis(rho_conforme, theta_conforme);

            if m >= m_max
                rho_F = rho_2;
                theta_F = theta_2;
                m_max = m;
            end

        end

    end

end
