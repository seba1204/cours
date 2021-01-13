Nb_bit = 84000;
Donnee = bits;
F0 = 1180;
F1 = 980;
debit = 300;
Ts = 1/debit;
Fe = 48000;
Te = 1/Fe;
Ns = round(Ts/Te);
NRZ = kron(Donnee,ones(1,Ns));
t = [0:Te:(Ns*Nb_bit-1)*Te];
%subplot(4,2,1), plot(t,NRZ);
phi0 = rand*2*pi
phi1 = rand*2*pi;
x = (1-NRZ).*cos(2*pi*F0*t + phi0) + NRZ.*cos(2*pi*F1*t + phi1);
subplot(4,2,1), title("x") ,plot(t,x);


%bruit :
Px = mean(abs(x).^2); % puissance du signal
SNRdb = 5; % rapport signal sur bruit
Pb = Px/(10^(SNRdb/10)); % puissance du bruit
x = x + Pb*randn(1,Ns*Nb_bit);
subplot(4,2,2) , plot(t,x);

%filtre passe bas :
fc=1000;
ordre = 101;
h= 2*fc*Te*  sinc(2*fc*Te*[-(ordre-1)/2:(ordre-1)/2]);
% [b,a] = butter(10,fc/(Fe/2),'low');
% y = filter(b,a,x);
% subplot(4,2,4), plot(t,y);
% %filtre passe haut :
% [b,a] = butter(10,fc/(Fe/2),'high');
% z = filter(b,a,x);
% subplot(4,2,5), plot(t,z);
retard = ((ordre-1)/2);
H = fft(h);
subplot(4,2,3), plot(linspace(-Fe/2,Fe/2,ordre), fftshift(abs(H)));
y_prov=filter(h,1,[x zeros(1,retard)]);
y=y_prov(retard+1:end);
subplot(4,2,5), plot(t,y); hold on
plot(t,NRZ, 'r')

h2 = -h;
h2((ordre-1)/2) = 1- fc/Fe;
H2 = fft(h2);
subplot(4,2,4), plot(linspace(-Fe/2,Fe/2,ordre), fftshift(abs(H2)));
y2_prov=filter(h2,1,[x zeros(1,retard)]);
y2=y2_prov(retard+1:end);

subplot(4,2,6), plot(t,y2); hold on
plot(t,NRZ, 'r')

%détection d'énergie :
K = 11 ;% seuil d'énergie à déteminer
y_reshape = reshape(y,Ns,Nb_bit);
X = sum(y_reshape.^2,1);
Donnee_retrouve = X>K;
subplot(4,2,7), plot(t,NRZ, 'r'); hold on
plot(t,kron(Donnee_retrouve,ones(1,Ns)), 'b')
Nb_erreur = sum(Donnee ~= Donnee_retrouve);
taux_erreur = Nb_erreur/Nb_bit

%% 3.4 Application de la recommandation V21
% réponse question : oui, en modifiant Fc, et K

%% 4.1 Démodulateur FSK - Contexte de synchronisation idéale

phi0 = rand*2*pi
phi1 = rand*2*pi;

x0 = x .* cos(2*pi*F0*t + phi0);
x1 = x .* cos(2*pi*F1*t + phi1);


x0_reshape = reshape(x0,Ns,Nb_bit);
X0 = sum(x0_reshape*Ts,1);

x1_reshape = reshape(x1,Ns,Nb_bit);
X1 = sum(x1_reshape*Ts,1);

X2 = X1 - X0;
Donnee_retrouve_2 = X2>0;
subplot(4,2,8), plot(t,NRZ, 'r'); hold on
plot(t,kron(Donnee_retrouve_2,ones(1,Ns)), 'b')

Nb_erreur_2 = sum(Donnee ~= Donnee_retrouve_2);
taux_erreur_2 = Nb_erreur_2/Nb_bit
 
%% 4.2 Démodulateur FSK avec gestion d'une erreur de synchronisation de
% phase porteuse
% 1. en faisant les calculs de 4.1.1, simplification qui ne se simplifient 
% pas => X2 que négatif ou que positif


x0c = x .* cos(2*pi*F0*t);
x0s = x .* sin(2*pi*F0*t);
x1c = x .* cos(2*pi*F1*t);
x1s = x .* sin(2*pi*F1*t);


x0c_reshape = reshape(x0c,Ns,Nb_bit);
X0c = sum(x0c_reshape*Te,1).^2;

x0s_reshape = reshape(x0s,Ns,Nb_bit);
X0s = sum(x0s_reshape*Te,1).^2;

x1c_reshape = reshape(x1c,Ns,Nb_bit);
X1c = sum(x1c_reshape*Te,1).^2;

x1s_reshape = reshape(x1s,Ns,Nb_bit);
X1s = sum(x1s_reshape*Te,1).^2;

X2 = (X1c+X1s) - (X0c+X0s);

Donnee_retrouve_3 = X2>0;
subplot(4,2,8), plot(t,kron(Donnee_retrouve_3,ones(1,Ns)), 'g'); hold on


Nb_erreur_3 = sum(Donnee ~= Donnee_retrouve_3);
taux_erreur_3 = Nb_erreur_3/Nb_bit

reconstitution_image(Donnee_retrouve_3);
