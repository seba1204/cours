function [E,contour,G_somme] = recursion(E,contour,G_somme,i,j,voisins,G_x,G_y,card_max,cos_alpha)
% Fonction recursive permettant de construire un ensemble candidat E

    contour(i,j) = 0;
    G_somme_normalise = G_somme/norm(G_somme);
    nb_voisins = size(voisins,1);
    k = 1;
    while k<=nb_voisins & size(E,1)<=card_max
        i_voisin = i + voisins(k, 1);
        j_voisin = j + voisins(k, 2);
        if contour(i_voisin,j_voisin)

            % Dans cette boucle, il vous faut :
            % - Calculer le produit scalaire entre G_somme_normalise et le gradient normalise de I au pixel voisin
            % - Si ce produit scalaire est superieur a cos_alpha :
            %	+ Mettre a jour "E" par concatenation
            %	+ Mettre a jour "G_somme"
            %	+ Lancer l'appel recursif sur le voisin


            % calcul des vecteurs normalisés
            G_somme_normalise = G_somme/norm(G_somme);
            Gradient = [G_x(i_voisin, j_voisin), G_y(i_voisin, j_voisin)];
            Gradient_normalisee = Gradient / norm(Gradient);
            
            % calcul du produit scalaire
            P_scalaire = G_somme_normalise(1) * Gradient_normalisee(1) + G_somme_normalise(2) * Gradient_normalisee(2);
            
            % si ça fait partie du contour
            if abs(P_scalaire) > cos_alpha
                E = [E; i, j];
                G_somme = [G_x(i_voisin,j_voisin) + G_somme(1),G_y(i_voisin,j_voisin) + G_somme(2)];
                [E,contour, G_somme] = recursion(E,contour,G_somme,i_voisin,j_voisin,voisins,G_x,G_y,card_max,cos_alpha);
            end
        end
        k = k+1;
    end
end
