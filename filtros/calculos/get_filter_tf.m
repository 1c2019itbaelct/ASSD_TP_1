function [ H ] = get_filter_tf()
%GET_FILTER_TF Devuelve la transferencia del filtro. 
    H = get_stage_tf(1)*get_stage_tf(2)*get_stage_tf(3)*get_stage_tf(4);
end

