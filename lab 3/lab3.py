import numpy as np
import pandas as pd
import statsmodels.api as sm
import patsy as pt
import sklearn.linear_model as lm

# загружаем файл с данными
df = pd.read_csv("http://roman-kh.github.io/files/linear-models/simple1.csv")
# x - таблица с исходными данными факторов (x1, x2, x3)
x = df.iloc[:, :-1]
# y - таблица с исходными данными зависимой переменной
y = df.iloc[:, -1]
# создаем новый фактор
x["x4"] = x["x2"] * x["x3"]
# создаем пустую модель
skm = lm.LinearRegression()
# запускаем расчет параметров для указанных данных
skm.fit(x, y)
# и выведем параметры рассчитанной модели
print(skm.intercept_, skm.coef_)
