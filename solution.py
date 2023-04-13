import pandas as pd
import numpy as np
import scipy.stats as st
from statsmodels.stats.weightstats import ztest as ztest

chat_id = 557932710 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    p_value=ztest(x, value=300, alternative = 'smaller')[1]
    if (p_value < 0.08):
    return True
    else:
    return False
