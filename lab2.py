investments = {
    "stocks": {"success_prob": 0.6, "success_profit": 500, "failure_prob": 0.4, "failure_profit": 300},
    "bonds": {"success_prob": 0.9, "success_profit": 440, "failure_prob": 0.1, "failure_profit": 120}
}

def calculate_expected_return_and_risk(option):
    p_success = option["success_prob"]
    p_failure = option["failure_prob"]
    profit_success = option["success_profit"]
    profit_failure = option["failure_profit"]

    expected_return = p_success * profit_success + p_failure * profit_failure

    variance = (
        p_success * (profit_success - expected_return) ** 2 +
        p_failure * (profit_failure - expected_return) ** 2
    )

    return expected_return, variance

results = {}
for investment, data in investments.items():
    expected_return, risk = calculate_expected_return_and_risk(data)
    results[investment] = {"expected_return": expected_return, "risk": risk}

less_risky = min(results, key=lambda x: results[x]["risk"])

for investment, result in results.items():
    print(f"{investment.capitalize()}: Expected Return = {result['expected_return']}, Risk = {result['risk']}")
print(f"Less risky investment: {less_risky.capitalize()}")
