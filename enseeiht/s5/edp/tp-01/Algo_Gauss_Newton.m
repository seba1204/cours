function [beta, norm_grad_f_beta, f_beta, norm_delta, nb_it, exitflag] ...
          = Algo_Gauss_Newton(residu, J_residu, beta0, option)
%*****************************************************************
% Fichier  ~gergaud/ENS/Optim1a/TP-optim-20-21/TP-ref/GN_ref.m   *
% Novembre 2020                                                  *
% Université de Toulouse, INP-ENSEEIHT                           *
%*****************************************************************
%
% GN resout par l'algorithme de Gauss-Newton les problemes aux moindres carres
% Min 0.5||r(beta)||^2
% beta \in \IR^p
%
% Paramètres en entrés
% --------------------
% residu : fonction qui code les résidus
%          r : \IR^p --> \IR^n
% J_residu : fonction qui code la matrice jacobienne
%            Jr : \IR^p --> real(n,p)
% beta0 : point de départ
%         real(p)
% option(1) : Tol_abs, tolérance absolue
%             real
% option(2) : Tol_rel, tolérance relative
%             real
% option(3) : n_itmax, nombre d'itérations maximum
%             integer
%
% Paramètres en sortie
% --------------------
% beta      : beta
%             real(p)
% norm_gradf_beta : ||gradient f(beta)||
%                   real
% f_beta : f(beta)
%          real
% r_beta : r(beta)
%          real(n)
% norm_delta : ||delta||
%              real
% nbit : nombre d'itérations
%        integer
% exitflag   : indicateur de sortie
%              integer entre 1 et 4
% exitflag = 1 : ||gradient f(beta)|| < max(Tol_rel||gradient f(beta0)||,Tol_abs)
% exitflag = 2 : |f(beta^{k+1})-f(beta^k)| < max(Tol_rel|f(beta^k)|,Tol_abs)
% exitflag = 3 : ||delta)|| < max(Tol_rel delta^k),Tol_abs)
% exitflag = 4 : nombre maximum d'itérations atteint
%      
% ---------------------------------------------------------------------------------

% TO DO %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    norm_grad_f_beta_0 = norm(J_residu(beta0));
    beta_k = beta0;
    f_beta_k = 0;
    nb_it = 0;
    
    c_1 = true;
    c_2 = true;
    c_3 = true;
    c_4 = true;
    
    while c_1 && c_2 && c_3 && c_4
        beta_k_1 = beta_k;
        f_beta_k_1 = f_beta_k;
        
        J = J_residu(beta_k);
        Jt = J';
        r = residu(beta_k);
        
        A = Jt * J;
        B = Jt * r;
        beta_k = beta_k - A\B;
        
        f_beta_k = (1/2)*norm(r)^2;
        norm_grad_f_beta = norm(B);
        
        norm_delta = norm(beta_k_1 - beta_k);
        
        nb_it = nb_it + 1;
        
        c_1 = norm_grad_f_beta > max(option(2)*norm_grad_f_beta_0,option(1));
        c_2 = abs(f_beta_k - f_beta_k_1) > max(option(2)*abs(f_beta_k),option(1));
        c_3 = norm_delta > max (option(2)*norm(beta_k), option(1));
        c_4 = nb_it < option(3);
    end
    
    beta = beta_k;
    f_beta = f_beta_k;
    
    if ~c_1
        exitflag = 1;
    elseif ~c_2 
        exitflag = 2;
    elseif ~c_3 
        exitflag = 3;
    elseif ~c_4
        exitflag = 4;
    end
end
