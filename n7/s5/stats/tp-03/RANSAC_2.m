function [rho_F, theta_F] = RANSAC_2(rho, theta, parametres)
    n = length(rho);
    S1 = parametres(1);
    S2 = parametres(2);
    k_max = parametres(3);

    m_max = 0;
    rho_F = 1;
    theta_F = 1;

    for k = 1:k_max

        % On choisi deux points au hasard
        I = randperm(n, 2);
        nouveau_rho = [rho(I(1)); rho(I(2))];
        nouveau_theta = [theta(I(1)); theta(I(2))];

        % On estime les paramètres à partir de ces points
        [rho_1, theta_1] = estimation_F(nouveau_rho, nouveau_theta);

        % On teste si ce modèle colle aux autres points
        C = abs(rho - rho_1 * cos(theta - theta_1)) <= S1;
        p = sum(C) / (n - 1);

        if p > S2

            % On réestime le modèle avec tous les points qui collent
            [rho_2, theta_2] = estimation_F(rho(C), theta(C));

            % On calcule la moyenne des écarts
            m = sum(abs(rho(C) - rho_2 * cos(theta(C) - theta_2)));

            % On sélectionne la plus grande
            if m >= m_max
                rho_F = rho_2;
                theta_F = theta_2;
                m_max = m;
            end

        end

    end

end
