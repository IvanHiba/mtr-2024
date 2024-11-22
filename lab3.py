capital = 150  # тисяч доларів

fixed_return = 0.05
income_a = capital * (1 + fixed_return)

stock_success_prob = 0.7
stock_failure_prob = 0.3
stock_success_return = capital * (1 + 0.20)
stock_failure_return = capital

def utility(x):
    return 0.15 * (x ** 2)

utility_a = utility(income_a)

expected_utility_b = (
    stock_success_prob * utility(stock_success_return) +
    stock_failure_prob * utility(stock_failure_return)
)

expected_income_b = (
    stock_success_prob * stock_success_return +
    stock_failure_prob * stock_failure_return
)
risk_premium = income_a - expected_income_b

print(f"Utility (варіант а): {utility_a}")
print(f"Expected Utility (варіант б): {expected_utility_b}")
print(f"Risk Premium: {risk_premium}")
