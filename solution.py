import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 841977 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    sample1=x_success/x_cnt
    sample1=y_success/y_cnt
    alpha = 0.06
    t_stat, p_value = ttest_ind(sample1, sample2)
    if p_value <= alpha:
        return True
    else:
        return False

