import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive

def decision_efficiency(probability, forest_raining, home_raining, forest_sunny, home_sunny):
    # Compute decision efficiencies
    forest_efficiency = probability * forest_raining + (1 - probability) * forest_sunny
    home_efficiency = probability * home_raining + (1 - probability) * home_sunny
    return forest_efficiency, home_efficiency

def plot_efficiency(forest_raining, home_raining, forest_sunny, home_sunny):
    probabilities = np.linspace(0, 1, 100)
    forest_efficiencies = []
    home_efficiencies = []
    
    for prob in probabilities:
        forest_eff, home_eff = decision_efficiency(prob, forest_raining, home_raining, forest_sunny, home_sunny)
        forest_efficiencies.append(forest_eff)
        home_efficiencies.append(home_eff)
    
    plt.figure(figsize=(8, 6))
    plt.plot(probabilities, forest_efficiencies, label='Forest Efficiency')
    plt.plot(probabilities, home_efficiencies, label='Home Efficiency')
    plt.xlabel('Probability of Rain')
    plt.ylabel('Decision Efficiency')
    plt.title('Decision Efficiency vs Probability of Rain')
    plt.legend()
    plt.grid(True)
    plt.show()

probability = float(input('Enter the percentage chance of rain (from 0 to 100): '))

if (probability < 0) or (probability > 100):
    print('Please, enter a value between 0 and 100')
else:
    probability = probability / 100

    print('On the scale from 0 to 10, where 0 - very bad, 5 - satisfactory, 10 - very good, estimate your state, when:')
    forest_raining = int(input('- it is raining and you are in the forest: '))
    home_raining = int(input('- it is raining and you are at home: '))
    forest_sunny = int(input('- it is sunny and you are in the forest: '))
    home_sunny = int(input('- it is sunny and you are at home: '))

    forest_efficiency, home_efficiency = decision_efficiency(probability, forest_raining, home_raining, forest_sunny, home_sunny)

    # Print results
    print(f"Decision Efficiency (Forest): {forest_efficiency}")
    print(f"Decision Efficiency (Home): {home_efficiency}")

    if forest_efficiency > home_efficiency:
        print('Decision to go to the forest has a higher efficiency.')
    elif forest_efficiency < home_efficiency:
        print('Decision to stay at home has a higher efficiency.')
    else:
        print('Both decisions have the same efficiency.')

    # Interactive plot
    interactive_plot = interactive(plot_efficiency, forest_raining=(0, 10), home_raining=(0, 10),
                                   forest_sunny=(0, 10), home_sunny=(0, 10))
    interactive_plot
