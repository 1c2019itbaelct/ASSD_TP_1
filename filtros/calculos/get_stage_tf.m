function [ H ] = get_stage_tf(stage_number) 
    switch stage_number
        case 1
            w0 = 2*pi*45948;
            Q = 6.04;
            G = 10^(0/20);
            H = tf([G], [1/w0^2, 1/w0/Q, 1]);
        case 2
            w0 = 2*pi*39935;
            Q = 1.84;
            G = 10^(0/20);
            H = tf([G], [1/w0^2, 1/w0/Q, 1]);
        case 3
            w0 = 2*pi*30323;
            Q = 0.91;
            G = 10^(0/20);
            H = tf([G], [1/w0^2, 1/w0/Q, 1]);
        case 4
            w0 = 2*pi*21958;
            Q = 0.54;
            G = 10^(0/20);
            H = tf([G], [1/w0^2, 1/w0/Q, 1]);
    end
        


end

