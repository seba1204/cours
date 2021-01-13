Nb_bit = 10;
Donnee = randi([0,1],1,Nb_bit);
F0 = 6000;
F1 = 2000;
debit = 300;
Ts = 1/debit;
Fe = 48000;
Te = 1/Fe;
Ns = round(Ts/Te);
NRZ = kron(Donnee,ones(1,Ns));
t = [0:Te:(Ns*Nb_bit-1)*Te];
%subplot(3,2,1), plot(t,NRZ);

x = (1-NRZ).*cos(2*pi*F0*t + rand*2*pi) + NRZ.*cos(2*pi*F1*t + rand*2*pi);
subplot(3,2,1), title("x") ,plot(t,x);


%bruit :
Px = mean(abs(x).^2); % puissance du signal
SNRdb = 5; % rapport signal sur bruit
Pb = Px/(10^(SNRdb/10)) % puissance du bruit
x = x + Pb*randn(1,Ns*Nb_bit);
subplot(3,2,2) , plot(t,x);

%filtre passe bas :
fc=4000;
ordre = 101;
h= 2*fc*Te*  sinc(2*fc*Te*[-(ordre-1)/2:(ordre-1)/2]);
% [b,a] = butter(10,fc/(Fe/2),'low');
% y = filter(b,a,x);
% subplot(3,2,4), plot(t,y);
% %filtre passe haut :
% [b,a] = butter(10,fc/(Fe/2),'high');
% z = filter(b,a,x);
% subplot(3,2,5), plot(t,z);
retard = ((ordre-1)/2);
H = fft(h)
subplot(3,2,3), plot(linspace(-Fe/2,Fe/2,ordre), fftshift(abs(H)));
y_prov=filter(h,1,[x zeros(1,retard)]);
y=y_prov(retard+1:end)
subplot(3,2,5), plot(t,y); hold on
plot(t,NRZ, 'r')

h2 = -h;
h2((ordre-1)/2) = 1- fc/Fe;
H2 = fft(h2);
subplot(3,2,4), plot(linspace(-Fe/2,Fe/2,ordre), fftshift(abs(H2)));
y2_prov=filter(h2,1,[x zeros(1,retard)]);
y2=y2_prov(retard+1:end)

subplot(3,2,6), plot(t,y2); hold on
plot(t,NRZ, 'r')

%détection d'énergie :
K = 50 ;% seuil d'énergie à déteminer
y_reshape = reshape(y,Ns,Nb_bit);
X = sum(y_reshape.^2,1)
Donnee_retrouve = X>K;
Nb_erreur = sum(Donnee ~= Donnee_retrouve);
taux_erreur = Nb_erreur/Nb_bit



%reconstitution_image(bits);