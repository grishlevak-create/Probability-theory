from scipy.stats import binom, poisson, norm
from numpy import sqrt



print(sum(poisson.pmf(range(2, 12001), mu=12000*0.0005)))

# Проверка
print(sum(binom.pmf(range(2, 12001), 12000, 0.0005)))