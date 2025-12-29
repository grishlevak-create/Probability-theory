import math

# Базовые функции принадлежности (как ранее)
def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

def trapezoidal(x, a, b, c, d):
    if x <= a or x >= d:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1
    else:
        return (d - x) / (d - c)

def gaussian(x, c, sigma):
    return math.exp(-((x - c) ** 2) / (2 * sigma ** 2))


def conjunction(mu1, mu2, method='min'):
    """
    Конъюнкция (И, пересечение)

    Аргументы:
    mu1, mu2 - значения принадлежности из двух множеств
    method - метод вычисления: 'min' или 'product'

    Возвращает:
    значение принадлежности для пересечения множеств
    """
    if method == 'min':
        return min(mu1, mu2)
    elif method == 'product':
        return mu1 * mu2
    else:
        raise ValueError("Метод должен быть 'min' или 'product'")


def disjunction(mu1, mu2, method='max'):
    """
    Дизъюнкция (ИЛИ, объединение)

    Аргументы:
    mu1, mu2 - значения принадлежности из двух множеств
    method - метод вычисления: 'max' или 'sum' (ограниченная сумма)

    Возвращает:
    значение принадлежности для объединения множеств
    """
    if method == 'max':
        return max(mu1, mu2)
    elif method == 'sum':
        return min(1, mu1 + mu2)  # ограниченная сумма
    else:
        raise ValueError("Метод должен быть 'max' или 'sum'")


def negation(mu):
    """
    Инверсия (НЕ, дополнение)

    Аргумент:
    mu - значение принадлежности

    Возвращает:
    значение принадлежности для дополнения множества
    """
    return 1 - mu


def implication(mu1, mu2, method='mamdani'):
    """
    Импликация (ЕСЛИ-ТО)

    Аргументы:
    mu1, mu2 - значения принадлежности
    method - метод вычисления: 'mamdani', 'larsen', 'lukasiewicz'

    Возвращает:
    значение принадлежности для импликации
    """

    if method == 'mamdani':
        return min(mu1, mu2)
    elif method == 'larsen':
        return mu1 * mu2
    elif method == 'lukasiewicz':
        return min(1, 1 - mu1 + mu2)
    else:
        raise ValueError("Неизвестный метод импликации")


def main():
    print("Программа для операций над нечеткими множествами")
    print("=" * 50)

    while True:
        print("\nВыберите операцию:")
        print("1 - Базовые функции принадлежности")
        print("2 - Операции над множествами")
        print("0 - Выход")

        choice = input("Ваш выбор: ").strip()

        if choice == '0':
            print("Выход из программы.")
            break

        elif choice == '1':
            # Код для базовых функций (как ранее)
            handle_basic_functions()

        elif choice == '2':
            handle_set_operations()

        else:
            print("Неверный выбор. Попробуйте снова.")


def handle_basic_functions():
    """Обработка базовых функций принадлежности"""
    print("\n--- Базовые функции принадлежности ---")
    print("1 - Треугольная")
    print("2 - Трапециевидная")
    print("3 - Гауссова")

    choice = input("Ваш выбор: ").strip()

    if choice == '1':
        a = float(input("a (левая граница): "))
        b = float(input("b (вершина): "))
        c = float(input("c (правая граница): "))
        x = float(input("x: "))
        result = triangular(x, a, b, c)
        print(f"μ_треуг({x}) = {result:.4f}")

    elif choice == '2':
        a = float(input("a (начало подъема): "))
        b = float(input("b (начало плато): "))
        c = float(input("c (конец плато): "))
        d = float(input("d (конец спада): "))
        x = float(input("x: "))
        result = trapezoidal(x, a, b, c, d)
        print(f"μ_трап({x}) = {result:.4f}")

    elif choice == '3':
        c = float(input("c (центр): "))
        sigma = float(input("σ (> 0): "))
        x = float(input("x: "))
        result = gaussian(x, c, sigma)
        print(f"μ_гаусс({x}) = {result:.4f}")


def handle_set_operations():
    """Обработка операций над множествами"""
    print("\n--- Операции над нечеткими множествами ---")
    print("1 - Конъюнкция (И)")
    print("2 - Дизъюнкция (ИЛИ)")
    print("3 - Инверсия (НЕ)")
    print("4 - Импликация (ЕСЛИ-ТО)")

    operation = input("Выберите операцию: ").strip()

    if operation == '1':
        mu1 = float(input("μ1 (принадлежность первому множеству): "))
        mu2 = float(input("μ2 (принадлежность второму множеству): "))
        method = input("Метод (min/product) [min]: ").strip() or 'min'
        result = conjunction(mu1, mu2, method)
        print(f"Конъюнкция({mu1}, {mu2}) = {result:.4f}")

    elif operation == '2':
        mu1 = float(input("μ1: "))
        mu2 = float(input("μ2: "))
        method = input("Метод (max/sum) [max]: ").strip() or 'max'
        result = disjunction(mu1, mu2, method)
        print(f"Дизъюнкция({mu1}, {mu2}) = {result:.4f}")

    elif operation == '3':
        mu = float(input("μ: "))
        result = negation(mu)
        print(f"Инверсия({mu}) = {result:.4f}")

    elif operation == '4':
        mu1 = float(input("μ1 (условие): "))
        mu2 = float(input("μ2 (следствие): "))
        method = input("Метод (mamdani/larsen/lukasiewicz) [mamdani]: ").strip() or 'mamdani'
        result = implication(mu1, mu2, method)
        print(f"Импликация({mu1}, {mu2}) = {result:.4f}")


if __name__ == "__main__":
    main()