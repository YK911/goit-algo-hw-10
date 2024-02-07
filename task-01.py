import pulp


# Максимізація виробництва напоїв
def drinks_production():
    model = pulp.LpProblem("Drinks_production", pulp.LpMaximize)

    # Визначення змінних
    A = pulp.LpVariable("A", lowBound=0, cat="Integer")  # Кількість Лимонаду
    B = pulp.LpVariable("B", lowBound=0, cat="Integer")  # Кількість Фруктового соку

    # Максимізація прибутку
    model += A + B, "Profit"

    # Система обмежень
    model += 2 * A + 1 * B <= 100  # Обмеження для води
    model += 1 * A <= 50  # Обмеження для цукру
    model += 1 * A <= 30  # Обмеження для лимонного соку
    model += 2 * B <= 40  # Обмеження для фруктового пюре

    # Розв'язання моделі
    model.solve()

    # Вивід результатів
    print("Статус:", pulp.LpStatus[model.status])  # Optimal
    print("Лимонад, од.:", A.varValue)  # 30 од.
    print("Фруктовий сік, од.:", B.varValue)  # 20 од.
    print("Загальний обсяг, од.:", pulp.value(model.objective))  # 50 од.


if __name__ == "__main__":
    drinks_production()
