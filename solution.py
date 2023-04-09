import pandas as pd
import numpy as np


chat_id = 260376781 # Ваш chat ID, не меняйте название переменной

from scipy.stats import mannwhitneyu

def solution(...) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    p_val = mannwhitneyu(x, y).pvalue
    answer = False if p_val > 0.01 else True
    return answer # Ваш ответ, True или False
