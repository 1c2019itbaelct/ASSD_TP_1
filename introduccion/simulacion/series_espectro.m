f0 = 2500;          %Frecuencia de la señal diente de sierra
A = 0.5;              %amplitud de la señal diente de sierra
a0 = A;             %valor medio
N  = 100;           %cantidad de armonicos que se muestran

x = 1 : N;
x  = x*f0;
y = zeros([0 N]);

for n = 1:N  
    y(n) = (-1)^(n+1)*2*A / n / pi();
end;



xlim([0 (N+1)*f0]);
set(gca,'color','none') 

scatter(x,y,'*');
title('Diagrama espectral de señal de entrada')
grid on;

xticklabels = {'f_0', '3f_0', '5f_0', '7f_0', '9f_0', '11f_0', '13f_0', '15f_0', '17f_0', '19f_0'};
set(gca,'xtick',f0:2*f0:N*f0); 
set(gca,'xticklabel',xticklabels,'interpreter','latex');
set(gca, 'xlabel', 'Frecuencia (Hz)','interpreter','latex');
ylabel('Amplitud(V)','interpreter','latex');


set(gca,'TickLabelInterpreter','latex');
xticks(f0:2*f0:19*f0);
xlabel('Frecuencia','interpreter','latex');
ylabel('Amplitud(V)','interpreter','latex');
title('Diagrama espectral de se\~nal de entrada', 'interpreter', 'latex');