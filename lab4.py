import numpy as np
from scipy.optimize import minimize

returns = np.array([[15, 16], [13, 20], [12, 19], [13, 12], [17, 12]])  # Норми прибутку акцій (A1, A2)
mean_returns = np.mean(returns, axis=0)  
cov_matrix = np.cov(returns.T)  

def portfolio_mean(weights, mean_returns):
    return np.dot(weights, mean_returns)

def portfolio_variance(weights, cov_matrix):
    return np.dot(weights.T, np.dot(cov_matrix, weights))

def minimize_risk(mean_returns, cov_matrix):
    num_assets = len(mean_returns)
    weights = np.ones(num_assets) / num_assets
    bounds = [(0, 1) for _ in range(num_assets)]
    constraints = [{"type": "eq", "fun": lambda weights: np.sum(weights) - 1}]
    
    result = minimize(portfolio_variance, weights, args=(cov_matrix), bounds=bounds, constraints=constraints)
    return result.x, portfolio_mean(result.x, mean_returns), result.fun

def optimal_portfolio_with_target(mean_returns, cov_matrix, target_return):
    num_assets = len(mean_returns)
    weights = np.ones(num_assets) / num_assets
    bounds = [(0, 1) for _ in range(num_assets)]
    constraints = [
        {"type": "eq", "fun": lambda weights: np.sum(weights) - 1},
        {"type": "eq", "fun": lambda weights: portfolio_mean(weights, mean_returns) - target_return}
    ]
    
    result = minimize(portfolio_variance, weights, args=(cov_matrix), bounds=bounds, constraints=constraints)
    return result.x, portfolio_mean(result.x, mean_returns), result.fun

# а) Мінімізація ризику
weights_min_risk, exp_return_min_risk, risk_min = minimize_risk(mean_returns, cov_matrix)

# б) Структура ринкового портфеля
weights_market, exp_return_market, risk_market = optimal_portfolio_with_target(mean_returns, cov_matrix, 0)

# в) Оптимальна структура з нормою прибутку 15,25%
target_return_1 = 15.25
weights_target_1, exp_return_target_1, risk_target_1 = optimal_portfolio_with_target(mean_returns, cov_matrix, target_return_1)

# г) Оптимальна структура з нормою прибутку 3,5%
target_return_2 = 3.5
weights_target_2, exp_return_target_2, risk_target_2 = optimal_portfolio_with_target(mean_returns, cov_matrix, target_return_2)

print("а) Мінімальний ризик:")
print(f"Ваги: {weights_min_risk}, Очікуваний прибуток: {exp_return_min_risk:.2f}%, Ризик: {risk_min:.2f}")

print("\nб) Ринковий портфель:")
print(f"Ваги: {weights_market}, Очікуваний прибуток: {exp_return_market:.2f}%, Ризик: {risk_market:.2f}")

print("\nв) Оптимальна структура для очікуваного прибутку 15,25%:")
print(f"Ваги: {weights_target_1}, Очікуваний прибуток: {exp_return_target_1:.2f}%, Ризик: {risk_target_1:.2f}")

print("\nг) Оптимальна структура для очікуваного прибутку 3,5%:")
print(f"Ваги: {weights_target_2}, Очікуваний прибуток: {exp_return_target_2:.2f}%, Ризик: {risk_target_2:.2f}")
