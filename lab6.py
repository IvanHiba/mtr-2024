import numpy as np

losses = np.array([[2.5, 3.5, 4.0],  # F1- для x1
                   [4.0, 2.0, 3.5],  # F1- для x2
                   [3.0, 3.5, 4.0],  # F1- для x3
                   [5.5, 1.5, 3.0]]) # F1- для x4

production = np.array([[20, 35, 50],  # F2+ для x1
                       [40, 25, 30],  # F2+ для x2
                       [30, 40, 45],  # F2+ для x3
                       [10, 25, 35]]) # F2+ для x4

probabilities = np.array([1/2, 1/3, 1/6])  # Ймовірності станів
priorities = np.array([3, 1])  # Вектор пріоритетів

expected_losses = np.dot(losses, probabilities)
expected_production = np.dot(production, probabilities)

normalized_losses = (np.max(expected_losses) - expected_losses) / (np.max(expected_losses) - np.min(expected_losses))
normalized_production = (expected_production - np.min(expected_production)) / (np.max(expected_production) - np.min(expected_production))

integral_scores = priorities[0] * normalized_losses + priorities[1] * normalized_production

optimal_index = np.argmax(integral_scores)
optimal_decision = f"x{optimal_index + 1}"

print("Очікувані значення функціоналів:")
print(f"F1- (збитки): {expected_losses}")
print(f"F2+ (виробництво): {expected_production}")

print("\nНормалізовані значення функціоналів:")
print(f"F1- норм: {normalized_losses}")
print(f"F2+ норм: {normalized_production}")

print("\nІнтегральні оцінки для рішень:")
for i, score in enumerate(integral_scores):
    print(f"x{i+1}: {score:.4f}")

print(f"\nОптимальне рішення: {optimal_decision}")
