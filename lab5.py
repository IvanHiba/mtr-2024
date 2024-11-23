import numpy as np

profits = np.array([
    [6.0, 3.5, 4.5],  # Прибутки для x1
    [6.5, 7.0, 4.0],  # Прибутки для x2
    [3.5, 3.5, 8.5]   # Прибутки для x3
])
probabilities = np.array([0.2, 0.4, 0.4])  

expected_profits = np.dot(profits, probabilities)

optimal_index = np.argmax(expected_profits)
optimal_decision = f"x{optimal_index + 1}"
optimal_profit = expected_profits[optimal_index]

for i, profit in enumerate(expected_profits):
    print(f"Очікуваний прибуток для x{i+1}: {profit:.2f}")
print(f"\nОптимальне рішення: {optimal_decision} з очікуваним прибутком {optimal_profit:.2f}")
