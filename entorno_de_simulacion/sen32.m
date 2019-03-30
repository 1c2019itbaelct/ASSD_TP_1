amp=1; 
fs=300000;  % sampling frequency, tiene que ser igual a la de grc
freq=2500;
duration=1/freq;
values=0:1/fs:duration;
a=amp*sin(2*pi*3/2*freq*values);
plot(a);
audiowrite('sen32.wav',a,fs)

