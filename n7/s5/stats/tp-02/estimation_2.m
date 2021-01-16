function [a_DYX_2,b_DYX_2] = estimation_2(x_donnees_bruitees,y_donnees_bruitees)
    [~, size_x] = size (x_donnees_bruitees);
    A_t = [x_donnees_bruitees; ones(1, size_x)];
    A = A_t.';
    B = y_donnees_bruitees.';
    A_plus = (A_t*A)\A_t;
    X = transpose(A_plus * B);
    a_DYX_2 = X(1);
    b_DYX_2 = X(2);
end

