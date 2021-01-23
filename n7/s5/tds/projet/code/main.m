%% Constantes
F0 = 6000; % en Hz
F1 = 2000; % en Hz
Fe = 48000; % frequence échantillonnage (Hz)
Debit = 300; % en bits/s
Ordre = 101; % ordre du filtre
K = 11; % seuil d'énergie déterminé expérimentalement

Donnee = 'Aleatoire'; % 'Image' OU 'Aleatoire'
Numero_Image = 1; % choisir quelle image charger
Nb_bit = 100; % Si 'Aleatoire', définir nb de bit voulu
%%

%% Code

if strcmp(Donnee, 'Image')
    load './ressources/DonneesBinome' + Numero_Image + '.mat'
    Donnees = bits;
    Nb_bit = length(Donnees);
elseif strcmp(Donnee, 'Aleatoire')
    % Données aléatoires
    Donnees = randi([0, 1], 1, Nb_bit);
end

% Pour afficher la figure en plein écran
figure('units', 'normalized', 'outerposition', [0 0 1 1])

%% Constantes nécessaire pour la suite.
m = 3; n = 5; % nombre de lignes et colonnes des figures
Ts = 1 / Debit;
Te = 1 / Fe;
Ns = round(Ts / Te);
NRZ = kron(Donnees, ones(1, Ns));
t = (0:Te:(Ns * Nb_bit - 1) * Te);

%% Affichage du signal NRZ (pour avoir une grille)
% plot(t, NRZ, 'LineWidth', 2, 'Color', [0.20 0.29 0.37]);
% axis([0.004 0.01 -1.05 1.05])
% xlabel('Temps (s)')
% Affichage de la grille
% ax = gca;
% ax.XAxis.MinorTick = 'on';
% ax.XAxis.MinorTickValues = 0:Ts:(Ns * Nb_bit - 1) * Te;
% ax.XMinorGrid = 'on';
% ax.MinorGridAlpha = 0.7;

%% Affichage de la DSP par periodogramme
% periodogram(NRZ, [], length(NRZ), 1 / Ts)

%% Génération du signal x
phi0 = rand * 2 * pi;
phi1 = rand * 2 * pi;
x = (1 - NRZ) .* cos(2 * pi * F0 * t + phi0) + NRZ .* cos(2 * pi * F1 * t + phi1);
subplot(m, n, 2), plot(t, x, 'LineWidth', 2, 'Color', [0.18 0.80 0.44], 'DisplayName', 'x(t)'); hold on;
plot(t, NRZ, 'LineWidth', 2, 'Color', [0.20 0.29 0.37], 'DisplayName', 'NRZ');
title('Signal modulé en fréquence')
xlabel('Temps (s)')
axis([0.001 0.01 -1.05 1.05])

% Ajout de bruit
Px = mean(abs(x).^2); % puissance du signal
SNRdb = 5; % rapport signal sur bruit
Pb = Px / (10^(SNRdb / 10)); % puissance du bruit
x = x + Pb * randn(1, Ns * Nb_bit);
subplot(m, n, 3), plot(t, x, 'LineWidth', 2, 'Color', [0.09 0.63 0.52], 'DisplayName', 'x(t)'); hold on;
plot(t, NRZ, 'LineWidth', 2, 'Color', [0.20 0.29 0.37], 'DisplayName', 'NRZ');
title('Signal bruité')
xlabel('Temps (s)')
axis([0.001 0.01 -1.05 1.05])

%% Filtres
Fc = (min([F0 F1]) + abs(F0 - F1) / 2);
Retard = (Ordre - 1) / 2;

%% Filtre passe bas
h_bas = 2 * Fc * Te * sinc(2 * Fc * Te * (-Retard:Retard));
H_bas = fft(h_bas);

% Reponse impulsionnelle
subplot(m, n, 6), plot(2 * Fc * Te * (-Retard:Retard), h_bas, 'LineWidth', 2, 'Color', [0.16 0.50 0.73]);
title('Réponse impulsionnelle du filtre passe-bas')
xlabel('Temps (s)')
axis([-10 10 -0.05 0.2])

% Reponse fréquentielle
subplot(m, n, 7), plot(linspace(-Fe / 2, Fe / 2, Ordre), fftshift(abs(H_bas)), 'LineWidth', 2, 'Color', [0.16 0.50 0.73]);
xline(Fc, '--', 'Fc', 'LineWidth', 2, 'Color', [0.75 0.22 0.17]);
xline(-Fc, '--', 'Fc', 'LineWidth', 2, 'Color', [0.75 0.22 0.17]);
title('Réponse fréquentielle du filtre passe-bas')
xlabel('Fréquence (Hz)')
axis([-8000 8000 0 1.12])

% DSP
DSP_x = (1 / (Fe)) * abs(fft(x)).^2;
freq = 0:Fe / length(x):Fe - 1;
subplot(m, n, 8), plot(freq, DSP_x, 'r', 'DisplayName', 'DSP de x(t)', 'LineWidth', 2, 'Color', [0.09 0.63 0.52 0.5]); hold on;
plot(linspace(-Fe / 2, Fe / 2, Ordre), fftshift(abs(H_bas)), 'DisplayName', 'Filtre', 'LineWidth', 2, 'Color', [0.16 0.50 0.73]);
title('Réponse fréquentielle du filtre passe-bas')
xlabel('Fréquence (Hz)')
axis([0 7000 0 1.12])

% Sortie du filtre
y_bas_retarde = filter(h_bas, 1, [x zeros(1, Retard)]);
y_bas = y_bas_retarde(Retard + 1:end);
subplot(m, n, 9), plot(t, y_bas, 'DisplayName', 'Signal filtré', 'LineWidth', 2, 'Color', [0.16 0.50 0.73]); hold on
plot(t, NRZ, 'DisplayName', 'NRZ', 'LineWidth', 2, 'Color', [0.17 0.24 0.31])
title('Signal filtré en passe bas')
xlabel('Temps (s)')
axis([0.006 0.028 -1.1 1.1])

% DSP de la sortie du filtre
DSP_y_bas = (1 / (Fe)) * abs(fft(y_bas)).^2;
subplot(m, n, 10), plot(freq, DSP_y_bas, 'r', 'DisplayName', 'DSP de x(t) filtré', 'LineWidth', 2, 'Color', [0.16 0.50 0.73])
title('DSP du signal filtré en passe bas')
xlabel('Fréquence (Hz)')
axis([0 7000 0 10])

%% Filtre passe haut
h_haut = -h_bas;
h_haut(Retard) = 1 - Fc / Fe;
H_haut = fft(h_haut);

% Reponse impulsionnelle
subplot(m, n, 11), plot(2 * Fc * Te * (-Retard:Retard), h_haut, 'LineWidth', 2, 'Color', [0.16 0.50 0.73]);
title('Réponse impulsionnelle du filtre passe-haut')
xlabel('Temps (s)')
axis([-10 10 -0.2 1.2])

% Reponse fréquentielle
subplot(m, n, 12), plot(linspace(-Fe / 2, Fe / 2, Ordre), fftshift(abs(H_haut)), 'LineWidth', 2, 'Color', [0.16 0.50 0.73]);
xline(Fc, '--', 'Fc', 'LineWidth', 2, 'Color', [0.75 0.22 0.17]);
xline(-Fc, '--', 'Fc', 'LineWidth', 2, 'Color', [0.75 0.22 0.17]);
title('Réponse fréquentielle du filtre passe-haut')
xlabel('Fréquence (Hz)')
axis([-8000 8000 0 1.12])

% DSP
subplot(m, n, 13), plot(freq, DSP_x, 'r', 'DisplayName', 'DSP de x(t)', 'LineWidth', 2, 'Color', [0.09 0.63 0.52 0.5]); hold on;
plot(linspace(-Fe / 2, Fe / 2, Ordre), fftshift(abs(H_haut)), 'DisplayName', 'Filtre', 'LineWidth', 2, 'Color', [0.16 0.50 0.73]);
title('Réponse fréquentielle du filtre passe-haut')
xlabel('Fréquence (Hz)')
axis([0 7000 0 1.12])

% Sortie du filtre
y_haut_retarde = filter(h_haut, 1, [x zeros(1, Retard)]);
y_haut = y_haut_retarde(Retard + 1:end);
subplot(m, n, 14), plot(t, y_haut, 'DisplayName', 'Signal filtré', 'LineWidth', 2, 'Color', [0.16 0.50 0.73]); hold on
plot(t, NRZ, 'DisplayName', 'NRZ', 'LineWidth', 2, 'Color', [0.17 0.24 0.31])
title('Signal filtré en passe haut')
xlabel('Temps (s)')
axis([0.006 0.028 -1.5 1.5])

% DSP de la sortie du filtre
DSP_y_haut = (1 / (Fe)) * abs(fft(y_haut)).^2;
subplot(m, n, 15), plot(freq, DSP_y_haut, 'r', 'DisplayName', 'DSP de x(t) filtré', 'LineWidth', 2, 'Color', [0.16 0.50 0.73])
title('DSP du signal filtré en passe haut')
xlabel('Fréquence (Hz)')
axis([0 7000 0 10])

%% Détection d'énergie
y_bas_r = reshape(y_bas, Ns, Nb_bit);
X = sum(y_bas_r.^2, 1);
Donnee_retrouve = X > K;
Nb_erreur = sum(Donnees ~= Donnee_retrouve);
taux_erreur = Nb_erreur / Nb_bit;
fprintf('Taux d erreur du filtre passe bas : %1.f %', taux_erreur * 100);
subplot(m, n, 4), text(0, 1, sprintf('Taux passe-bas : %1.f %%', taux_erreur * 100), 'FontSize', 18);

%% Démodulateur FSK

phi0 = rand * 2 * pi;
phi1 = rand * 2 * pi;

x0 = x .* cos(2 * pi * F0 * t + phi0);
x1 = x .* cos(2 * pi * F1 * t + phi1);

x0_reshape = reshape(x0, Ns, Nb_bit);
X0 = sum(x0_reshape * Ts, 1);

x1_reshape = reshape(x1, Ns, Nb_bit);
X1 = sum(x1_reshape * Ts, 1);

X2 = X1 - X0;
Donnee_retrouve_2 = X2 > 0;

Nb_erreur_2 = sum(Donnees ~= Donnee_retrouve_2);
taux_erreur_2 = Nb_erreur_2 / Nb_bit;
fprintf('Taux d erreur du 1er démodulateur FSK : %1.f %', taux_erreur_2 * 100);
subplot(m, n, 4), text(0, 0.8, sprintf('Taux FSK 1 : %1.f %%', taux_erreur_2 * 100), 'FontSize', 18);

x0c = x .* cos(2 * pi * F0 * t);
x0s = x .* sin(2 * pi * F0 * t);
x1c = x .* cos(2 * pi * F1 * t);
x1s = x .* sin(2 * pi * F1 * t);

x0c_reshape = reshape(x0c, Ns, Nb_bit);
X0c = sum(x0c_reshape * Te, 1).^2;

x0s_reshape = reshape(x0s, Ns, Nb_bit);
X0s = sum(x0s_reshape * Te, 1).^2;

x1c_reshape = reshape(x1c, Ns, Nb_bit);
X1c = sum(x1c_reshape * Te, 1).^2;

x1s_reshape = reshape(x1s, Ns, Nb_bit);
X1s = sum(x1s_reshape * Te, 1).^2;

X2 = (X1c + X1s) - (X0c + X0s);

Donnee_retrouve_3 = X2 > 0;
Nb_erreur_3 = sum(Donnees ~= Donnee_retrouve_3);
taux_erreur_3 = Nb_erreur_3 / Nb_bit;
fprintf('Taux d erreur du 2eme démodulateur FSK : %1.f %%', taux_erreur_3 * 100);
subplot(m, n, 4), text(0, 0.6, sprintf('Taux FSK 2 : %1.f %%', taux_erreur_3 * 100), 'FontSize', 18);
subplot(m, n, 4), text(0, 0.4, 'Voir console pour + infos', 'FontSize', 18);
axis off;

if strcmp(Donnee, 'Image')
    reconstitution_image(Donnee_retrouve_3);
end
