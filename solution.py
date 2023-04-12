import pandas as pd
import numpy as np
from scipy.stats import cramervonmises_2samp


chat_id = 1112700607  # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    cnst = 0.03
    return cramervonmises_2samp(x, y).pvalue([x, y]).pvalue <= cnst
