N = 90;
A = 1;
f0 = 1100;
Fe = 10000;
Te = 1/Fe;
Fe2 = 1000;
Te2 = 1/Fe2;

temps = 0 : Te : (N-1)*Te;
temps2 = 0 : Te2 : (N-1)*Te2;

x = A * cos(2 * pi * f0 * temps);
x2 = A * cos(2 * pi * f0 * temps2);

% plot(temps, x)
% xlabel('t');
% ylabel('x');


for i = 1:10
    Y = fft(x, 2^i);
    semilogy(abs(Y));
end