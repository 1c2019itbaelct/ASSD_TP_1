f0 = 2500;          %Frecuencia de la señal diente de sierra
A = 1;              %amplitud de la señal diente de sierra
a0 = A/2;             %valor medio
N  = 100;           %cantidad de armonicos que se muestran

filtro_on = false;   %true: muestra armonicos de salida, false: muestra armonicos de entrada
diente_de_sierra = false; %true: diente de sierra, false: sen3/2(x)

armonico = 1 : N;
armonico  = armonico*f0;
amplitud = zeros([1 N]);
fase = zeros([1 N]);

for n = 1:N
    if diente_de_sierra == true
        amplitud(n) = (-1)^(n+1)*A / n / pi();  %diente de sierra
    else
        amplitud(n) = (12*cos(pi()*n)^2)/(9*pi()-4*pi()*n^2);  %sen3/2(x)
    end
end;

R = 500;
C = 4.7e-9;
tau = R*C;
%modH(f) = 1/((2*pi*tau*f)^2+1);
%phsH(f) = -arctg(2*pi*tau);


   Fs = armonico(N) * 100;      % samples per second
   dt = 1/Fs;                   % seconds per sample
   StopTime = 2/f0;             % seconds
   t = (0:dt:StopTime-dt)';     % seconds
   Fc = 60;                     % hertz


% modificacion del filtro
if filtro_on == true
    for n = 1:N  
         if(rem(n,2))   %si es impar
             f = armonico(n);
             amplitud(n) = amplitud(n) * 1/sqrt((2*pi*tau*f)^2+1);
             fase(n) = fase(n) + (-atan(2* pi * tau * f));
         end;
    end;
end;


figure;
x = a0;
for n = 1:N  
    if(armonico(n))
        if diente_de_sierra == true
            x = x + amplitud(n) * sin(2*pi*armonico(n)*t + fase(n));
        else 
            x = x + amplitud(n) * cos(2*pi*armonico(n)*t + fase(n));
        end
    end;
   if n==N
       plot(t,x, 'Linewidth', 2, 'Color', 'black');
   else
       plot(t,x, 'Linewidth', 0.5, 'Color', 'red');
   end;
   hold on;
end;

xlabel('tiempo(s)');
ylabel('Amplitud(V)');

