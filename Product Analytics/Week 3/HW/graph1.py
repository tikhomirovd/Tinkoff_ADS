import matplotlib.pyplot as plt

# Data
banks = ['Банк А', 'Банк Б', 'Банк В', 'Банк Г', 'Банк Д', 'Банк Е']
profitability = [10.5, 19, 8, 15.2, 4, 25]

# Sorting data by profitability in descending order
sorted_indices = [i for i, _ in sorted(enumerate(profitability), key=lambda x: -x[1])]
sorted_banks = [banks[i] for i in sorted_indices]
sorted_profitability = [profitability[i] for i in sorted_indices]

# Creating the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(sorted_banks, sorted_profitability, color=['brown', 'orange', 'red', 'green', 'blue', 'purple'])

# Adding the profitability values on top of the bars
for bar, value in zip(bars, sorted_profitability):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{value}%',
             ha='center', va='bottom', fontsize=10)

# Adding title and labels
plt.title('Коэффициент доходности капитала в 2021 году', fontsize=14)
plt.xlabel('Банки', fontsize=12)
plt.ylabel('Доходность, %', fontsize=12)

# Displaying the chart
plt.show()
