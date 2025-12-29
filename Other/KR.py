import math
from scipy.stats import binom, poisson, norm
from numpy import sqrt


# Пуассон
print(sum(poisson.pmf(range(4), mu=1200*0.002))) 
# Сочетания
# print(math.comb(8,2)*math.comb(6,2) / math.comb(14,4))

# М-Л
# print(norm.pdf(x) / sqrt(npm))

# Интегральный М-Л
# print(sum(binom.pmf(range(210, 231), 300, 0.75)))