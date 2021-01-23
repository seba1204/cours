% To display figure on my 2nd screen
figure('units', 'normalized', 'outerposition', [-1 0 1 1])

% Données pour l'image
% Nb_bit = 84000;
% Donnee = bits;
F0 = 1180;
F1 = 980;

% Données aléatoires
Nb_bit = 100;
Donnee = randi([0, 1], 1, Nb_bit);
% F0 = 6000;
% F1 = 2000;
debit = 300;
Ts = 1 / debit;
Fe = 48000; Te = 1 / Fe;
Ns = round(Ts / Te);
NRZ = kron(Donnee, ones(1, Ns));
t = (0:Te:(Ns * Nb_bit - 1) * Te);
plot(t, NRZ, 'LineWidth', 2, 'Color', [0.20 0.29 0.37]);
axis([0 0.333 -0.1 1.1])
title('Signal NRZ généré au cours du temps')
xlabel('Temps (s)')
ylabel('Signal NRZ')
set(gca, 'FontSize', 20)
set(gcf, 'position', [10, 10, 1275, 675])
ax = gca;
ax.XAxis.MinorTick = 'on';
ax.XAxis.MinorTickValues = 0:Ts:(Ns * Nb_bit - 1) * Te;
ax.XMinorGrid = 'on';
ax.MinorGridAlpha = 0.7;

periodogram(NRZ, [], length(NRZ), 1 / Ts)
% subplot(4,2,1), plot(t,NRZ);

phi0 = rand * 2 * pi;
phi1 = rand * 2 * pi;
x = (1 - NRZ) .* cos(2 * pi * F0 * t + phi0) + NRZ .* cos(2 * pi * F1 * t + phi1);
subplot(4, 2, 1), title("x"), plot(t, x); hold on

plot(t, x, 'LineWidth', 2, 'Color', [0.18 0.80 0.44]);
title('Signal modulé en fréquence')
xlabel('Temps (s)')
ylabel('Signal')
axis([0.004 0.01 -1.05 1.05])
set(gca, 'FontSize', 20)
set(gcf, 'position', [10, 10, 1275, 675])

plot(t, changem(NRZ, -1, 0), 'r')

%bruit :
Px = mean(abs(x).^2); % puissance du signal
SNRdb = 50; % rapport signal sur bruit
Pb = Px / (10^(SNRdb / 10)); % puissance du bruit
x = x + Pb * randn(1, Ns * Nb_bit);
plot(t, x, 'LineWidth', 2, 'Color', [0.09 0.63 0.52]);
title('Signal bruité')
xlabel('Temps (s)')
ylabel('Signal')
axis([0 0.05 -2.5 2.5])
set(gca, 'FontSize', 20)
set(gcf, 'position', [10, 10, 1275, 675])
subplot(4, 2, 2), plot(t, x);

%% filtre passe bas :

Fc = 1000;
Ordre = 101;
Retard = (Ordre - 1) / 2;

h = 2 * Fc * Te * sinc(2 * Fc * Te * (-Retard:Retard));
H = fft(h);
subplot(4, 2, 3), plot(linspace(-Fe / 2, Fe / 2, Ordre), fftshift(abs(H)));

plot(2 * Fc * Te * (-Retard:Retard), h, 'LineWidth', 2, 'Color', [0.16 0.50 0.73]);
title('Réponse impulsionnelle du filtre passe-bas')
xlabel('Temps (s)')
axis([-10 10 -0.05 0.2])
set(gca, 'FontSize', 20)
set(gcf, 'position', [10, 10, 1275, 675])

plot(linspace(-Fe / 2, Fe / 2, Ordre), fftshift(abs(H)), 'LineWidth', 2, 'Color', [0.16 0.50 0.73]);
xline(4500, 'r--', 'Fc', 'LineWidth', 2, 'Color', [0.75 0.22 0.17]);
xline(-4500, 'r--', 'Fc', 'LineWidth', 2, 'Color', [0.75 0.22 0.17]);
title('Réponse fréquentielle du filtre passe-bas')
xlabel('Fréquence (Hz)')
ylabel('')
axis([-8000 8000 0 1.12])
set(gca, 'FontSize', 20)
set(gcf, 'position', [10, 10, 1275, 675])

psdx = (1 / (Fe)) * abs(fft(x)).^2;
freq = 0:Fe / N:Fe - 1;
plot(freq, psdx, 'r', 'DisplayName', 'DSP de x(t)', 'LineWidth', 2, 'Color', [0.09 0.63 0.52 0.5])
hold on;
plot(linspace(-Fe / 2, Fe / 2, Ordre), fftshift(abs(H)), 'DisplayName', 'Filtre', 'LineWidth', 2, 'Color', [0.16 0.50 0.73]);
title('Réponse fréquentielle du filtre passe-bas')
xlabel('Fréquence (Hz)')
ylabel('')
axis([0 7000 0 1.12])
set(gca, 'FontSize', 20)
set(gcf, 'position', [10, 10, 1275, 675])
legend

y_prov = filter(h, 1, [x zeros(1, Retard)]);
y = y_prov(Retard + 1:end);
plot(t, y, 'DisplayName', 'Signal filtré', 'LineWidth', 2, 'Color', [0.16 0.50 0.73]); hold on
plot(t, NRZ, 'DisplayName', 'NRZ', 'LineWidth', 2, 'Color', [0.17 0.24 0.31])
title('Signal filtré')
xlabel('Temps (s)')
ylabel('')
axis([0.006 0.028 -1.1 1.1])
set(gca, 'FontSize', 20)
set(gcf, 'position', [10, 10, 1275, 675])
legend

% ------
psdy = (1 / (Fe)) * abs(fft(y)).^2;
freq = 0:Fe / N:Fe - 1;
plot(freq, psdy, 'r', 'DisplayName', 'DSP de x(t) filtré', 'LineWidth', 2, 'Color', [0.16 0.50 0.73])
title('DSP du signal filtré')
xlabel('Fréquence (Hz)')
ylabel('')
axis([0 7000 0 160])
set(gca, 'FontSize', 20)
set(gcf, 'position', [10, 10, 1275, 675])
% ------
% ---------------------------------------------------------------------------
h2 = -h;
h2(Retard) = 1 - Fc / Fe;
H2 = fft(h2);
y2_prov = filter(h2, 1, [x zeros(1, Retard)]);
y2 = y2_prov(Retard + 1:end);

plot(2 * Fc * Te * (-Retard:Retard), h2, 'LineWidth', 2, 'Color', [0.16 0.50 0.73]);
title('Réponse impulsionnelle du filtre passe-haut')
xlabel('Temps (s)')
axis([-6.5 6.5 -0.2 1.12])
set(gca, 'FontSize', 20)
set(gcf, 'position', [10, 10, 1275, 675])

plot(linspace(-Fe / 2, Fe / 2, Ordre), fftshift(abs(H2)), 'LineWidth', 2, 'Color', [0.16 0.50 0.73]);
xline(4500, 'r--', 'Fc', 'LineWidth', 2, 'Color', [0.75 0.22 0.17]);
xline(-4500, 'r--', 'Fc', 'LineWidth', 2, 'Color', [0.75 0.22 0.17]);
title('Réponse fréquentielle du filtre passe-haut')
xlabel('Fréquence (Hz)')
ylabel('')
axis([-6500 6500 0 1.12])
set(gca, 'FontSize', 20)
set(gcf, 'position', [10, 10, 1275, 675])

psdx = (1 / (Fe)) * abs(fft(x)).^2;
freq = 0:Fe / N:Fe - 1;
plot(freq, psdx, 'r', 'DisplayName', 'DSP de x(t)', 'LineWidth', 2, 'Color', [0.09 0.63 0.52 0.5])
hold on;
plot(linspace(-Fe / 2, Fe / 2, Ordre), fftshift(abs(H2)), 'DisplayName', 'Filtre', 'LineWidth', 2, 'Color', [0.16 0.50 0.73]);
title('Réponse fréquentielle du filtre passe-haut')
xlabel('Fréquence (Hz)')
ylabel('')
axis([0 7000 0 1.12])
set(gca, 'FontSize', 20)
set(gcf, 'position', [10, 10, 1275, 675])
legend

plot(t, y2, 'DisplayName', 'Signal filtré', 'LineWidth', 2, 'Color', [0.16 0.50 0.73]); hold on
plot(t, NRZ, 'DisplayName', 'NRZ', 'LineWidth', 2, 'Color', [0.17 0.24 0.31])
title('Signal filtré')
xlabel('Temps (s)')
ylabel('')
axis([0.006 0.028 -1.3 1.3])
set(gca, 'FontSize', 20)
set(gcf, 'position', [10, 10, 1275, 675])
legend

% ------
psdy = (1 / (Fe)) * abs(fft(y2)).^2;
freq = 0:Fe / N:Fe - 1;
plot(freq, psdy, 'DisplayName', 'DSP de x(t) filtré', 'LineWidth', 2, 'Color', [0.16 0.50 0.73])
title('DSP du signal filtré')
xlabel('Fréquence (Hz)')
ylabel('')
axis([0 7000 0 160])
set(gca, 'FontSize', 20)
set(gcf, 'position', [10, 10, 1275, 675])
% ------

%détection d'énergie :
K = 11; % seuil d'énergie à déteminer
y_reshape = reshape(y, Ns, Nb_bit);
X = sum(y_reshape.^2, 1);
Donnee_retrouve = X > K;
plot(t, NRZ, 'DisplayName', 'Signal original', 'LineWidth', 2, 'Color', [0.17 0.24 0.31]); hold on
plot(t, kron(Donnee_retrouve, ones(1, Ns)), 'DisplayName', 'Signal reconstruit', 'LineWidth', 2, 'Color', [0.56 0.27 0.68])
title('Différence signal original / retrouvé')
xlabel('Temps (s)')
ylabel('')
axis([0 0.35 -0.1 1.1])
set(gca, 'FontSize', 20)
set(gcf, 'position', [10, 10, 1275, 675])
legend
Nb_erreur = sum(Donnee ~= Donnee_retrouve);
taux_erreur = Nb_erreur / Nb_bit

%% 3.4 Application de la recommandation V21
% réponse question : oui, en modifiant Fc, et K

%% 4.1 Démodulateur FSK - Contexte de synchronisation idéale

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
subplot(4, 2, 8), plot(t, NRZ, 'r'); hold on
plot(t, kron(Donnee_retrouve_2, ones(1, Ns)), 'b')

Nb_erreur_2 = sum(Donnee ~= Donnee_retrouve_2);
taux_erreur_2 = Nb_erreur_2 / Nb_bit;

%% 4.2 Démodulateur FSK avec gestion d'une erreur de synchronisation de
% phase porteuse
% 1. en faisant les calculs de 4.1.1, simplification qui ne se simplifient
% pas => X2 que négatif ou que positif

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
subplot(4, 2, 8), plot(t, kron(Donnee_retrouve_3, ones(1, Ns)), 'g'); hold on

Nb_erreur_3 = sum(Donnee ~= Donnee_retrouve_3);
taux_erreur_3 = Nb_erreur_3 / Nb_bit;

reconstitution_image(Donnee_retrouve_3);
