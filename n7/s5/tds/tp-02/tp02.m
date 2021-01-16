
%% Q3.1.1

% Paramètres
A = 1;
f1 = 1000;
f2 = 3000;
Fe = 10000;
Te = 1/Fe;
nb_points = 100;

% Temps
t = linspace(0, nb_points/Fe, nb_points);
x = A * (cos(2*pi*f1*t) + cos(2*pi*f2*t));

%% Q 3.1.2
xlabel('Time (s)')
ylabel('signal (V)')
plot(t, x)

%% Q 3.1.3
tfd = fft(x);
hz = linspace(0, Fe, nb_points);
semilogy(hz, abs(tfd))
grid on

%% Q 3.2.1 
% la réponse impulsionnelle est un sinus cardinal 

%% Q 3.2.2

% ordre = 11
ordre = 11;
support = (-5:5);
f = 2*f1/Fe;
h = f*sinc(f*support);
H = fft(h);

subplot(2,1,1), plot(h);
subplot(2,1,2), semilogy(linspace(-Fe/2, Fe/2, ordre), fftshift(abs(H)));


