# Тут я всё пропустил минут на 10


## Ближайший центроид
Nearest centroid algorithm

Звадача классификации на пересекающие классы с вещественным признаками

И тут формулы пропустил




![nearest_centroid.png](nearest_centroid.png)
Плюсы:
- Хранить только центроиды (их можно адаптивно менять)
- Понятие центроида можно менять ("Средний объект")
- Простая реализация
- Размер модели = число классов * описание центроида

Минусы:
- Очень простой алгоритм (Интуитивно подходит в задачах, где объекты разных классов распределены "колоколообразно")


### Минутка кода
> from sklearn.neighbors.nearest_centroid import NearestCentroid
> model = NearestCentroid(metric='euclidean')
> model.fix(X, y)
> a = model.predict(X2)


## Подход, основанный на близости
**Задача классификации:** $a(x) = mode(y_i | x_i \in N(x))$

**Задача регрессии:** $a(x) = mean(y_i | x_i \in N(x))$


## Метод k ближайших соседей (kNN)
Гиперпараметр k (а также метрику, ядро и т.п.) можно выбрать на скользящем контроле (об этом потом)

**Термины:**
- Нетерпеливый алгоритм:  Обучение - получение значений параметров. После обучения данные не нужны
- Ленивый алгоритм: Не использует обучающую выборку до классификации, нормально нет обучения - храним всю выборку


## Решение модельной задачи
При разном числе соседей 

![solved_model_task.png](solved_model_task.png)

При большом k почти плавная прямая, при маленьком k строго делят

k отвечает за "Сложность модели"

### Минутка кода 
> from sklearn.neighbors import KNeighborsClassifier
> model = KneighborsClassifier(  
>       n_neighbors=5, # число соседей  
>       algorithm='auto',  
>       leaf_size=30,  
>       wights='uniform',  
>       metric='minkowski',  
>       p=2,  
>       metric_params=None)  
> model.fit(X, y)  
> a = model.predict(X2)  
> p = model.predict_proba(X2)[:, 1]  
> 
> 

## Регрессия

### Метод ближайшего соседа в регрессии
Обобщается на регрессию 
![k_regression.png](k_regression.png)


### Подбор гипермараметров 
Специальными методами контроля

### Минутка кода
```python
from sklearn.model_selection import Kfold
cv = Kfold(n_splits=10, shuffle=True, random_state=2)

from sklearn.neighbors import KneighborsClassifier
model = KneighborsClassifier(n_neighbors=5)

param_name = 'n_neighbors'

pars = np.arrange(1, 41)

from sklearn.model_selection import validation_curve

train_errors, test_errors = validation_curve(model,
                                             X, y,
                                             param_name=param_name,
                                             param_range=pars,
                                             cv=cv.split(X),
                                             scoring='accuracy',
                                             n_jobs=-1)
```

## Проблема классического kNN
![weiths_knn.png](weiths_knn.png)

### Весовые обобщения kNN
- Классика $mode(y_i | x_i \in N(x)) = argmax \sum_{t=1}^k I\[y(x_t) = a\]$
- Обобщение $argmax \sum_{t=1}^k w_t I\[y(x_t)) =a \]$
- Разные весовые схемы $w_1 \geq w_2 \geq ... \geq w_k > 0$