import numpy as np
import pandas as pd
from random import choices
import matplotlib.pyplot as plt
from math import comb

# --- Теоретическая вероятность ---
n_throws = 6  # число бросков
p_six = 1/6   # вероятность выпадения шестерки на одном броске
prob_theory = {k: comb(n_throws, k) * (p_six**k) * ((1-p_six)**(n_throws-k)) for k in range(n_throws+1)}

# --- Эксперимент ---
N = 50000  # количество серий
freq = {k: 0 for k in range(n_throws+1)}
for _ in range(N):
    results = choices(range(1, 7), k=n_throws)
    count_six = results.count(6)
    freq[count_six] += 1

# --- Нормируем частоты ---
for k in freq:
    freq[k] /= N

# --- Сравнение ---
df = pd.DataFrame({
    'Теория': [prob_theory[k] for k in range(n_throws+1)],
    'Эксперимент': [freq[k] for k in range(n_throws+1)],
    'Отклонение': [abs(prob_theory[k] - freq[k]) for k in range(n_throws+1)]
}, index=range(n_throws+1))

print("Сравнение теории и эксперимента (количество шестерок в 6 бросках):")
print(df)

# --- График ---
x = np.arange(n_throws+1)
plt.figure(figsize=(8, 5))
plt.bar(x-0.2, [prob_theory[k] for k in x], width=0.4, label='Теория', alpha=0.7)
plt.bar(x+0.2, [freq[k] for k in x], width=0.4, label='Эксперимент', alpha=0.7)
plt.xticks(x)
plt.xlabel("Количество шестерок")
plt.ylabel("Вероятность")
plt.title(f"Сравнение теории и эксперимента ({N} серий по 6 бросков)")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

