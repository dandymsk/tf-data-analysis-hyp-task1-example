import pandas as pd
import numpy as np
import math as mth
import scipy.stats as st

chat_id = 841977 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p1=x_success/x_cnt
    p2=y_success/y_cnt
    alpha = 0.06
    p_combined = (p1*x_cnt+p2*y_cnt)/(x_cnt+y_cnt)
    z_value = (p1-p2)/(mth.sqrt(p_combined*(1-p_combined)*(1/x_cnt+1/y_cnt)))
    distr = st.norm(0, 1)
    p_value = (1 - distr.cdf(abs(z_value))) * 2
    
    if p_value <= alpha:
        return True
    else:
        return False
