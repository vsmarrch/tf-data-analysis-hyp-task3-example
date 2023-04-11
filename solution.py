import pandas as pd
import numpy as np


chat_id = 260376781 # Ваш chat ID, не меняйте название переменной

from scipy.stats import ttest_ind

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    p_val = ttest_ind(x, y, equal_var=False).pvalue
    answer = False if p_val > 0.01 else True
    return answer # Ваш ответ, True или False
