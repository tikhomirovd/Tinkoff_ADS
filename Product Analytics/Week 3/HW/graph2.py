import matplotlib.pyplot as plt

# Данные
price_segments = ['До 100', '100-200', '200-500', '500-1000', '1000-2000']
sales = [320, 770, 400, 250, 100]

# Цвета для разных ценовых сегментов
colors = ['#ff9999','#ffcc99', '#99ff99', '#99ffcc', '#99ccff']

# Создание диаграммы
plt.figure(figsize=(12, 6))
wedges, texts, autotexts = plt.pie(sales, autopct='%1.1f%%', startangle=140, colors=colors,
                                    textprops=dict(color="black"))

# Добавление легенды сбоку
plt.legend(wedges, price_segments,
           title="Ценовые сегменты",
           loc="center left",
           bbox_to_anchor=(1, 0, 0.5, 1))

# Добавление заголовка
plt.title('Продажи игрушек по ценовым сегментам', fontsize=14)

# Отображение диаграммы
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()  # Adjusts the plot to ensure everything fits without overlapping
plt.show()
