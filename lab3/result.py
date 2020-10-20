from typing import Union

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


def definite_func(func: str):
    """
    :param func: функцию вида x = f(u) вводить как f(u)
    :return: Возвращает фунцию которая считает значения по описанному закону
    """

    def df(u: Union[float, int]):
        return eval(func)

    return df


def func(noise_sigma: Union[int, float], sample_len: int,
         sample_interval: Union[list, tuple], noise_mean: int = 0, dependency_function: str = '(u**2*np.sin(u-1))/u',
         d: int = 1):
    data_u = 1 / (sample_interval[1] - sample_interval[0])
    step_interval = sp.linspace(sample_interval[0], sample_interval[1], sample_len)
    noise = np.random.normal(loc=noise_mean, scale=noise_sigma, size=sample_len)
    dep_func = definite_func(dependency_function)
    data = np.array(
        [[step_interval[i] for i in range(sample_len)], [dep_func(data_u) + noise[i] for i in range(sample_len)]])

    '''Вот дальше то что тебе нужно'''

    x_mean = np.mean(data[0])
    y_mean = np.mean(data[1])
    result = []
    count = []
    desp = np.mean([(i - x_mean) ** 2 for i in data[0]])

    for i in range(len(data[0])):
        temp = [data[0][i], data[1][i]]
        if temp in result:
            tt = result.index(temp)
            count[tt] = count[tt] + 20
        else:
            result.append(temp)
            count.append(10)

    for i in range(len(result)):
        plt.scatter(result[i][0], result[i][1], color='blue', s=count[i])
    a_dot = (np.mean(
        [data[0][i] * data[1][i] for i in
         range(len(data[0]))]) - x_mean * y_mean) / desp
    b_dot = y_mean - a_dot * x_mean
    # y = ax+b
    plt.plot([min(data[0]), max(data[0])],
             (a_dot * min(data[0]) + b_dot, a_dot * max(data[0]) + b_dot), c='r')
    plt.minorticks_on()

    #  Определяем внешний вид линий основной сетки:
    plt.grid(which='major',
             color='k',
             linewidth=1)

    #  Определяем внешний вид линий вспомогательной
    #  сетки:
    plt.grid(which='minor',
             color='k',
             linestyle=':')

    plt.show()
    return a_dot, b_dot


if __name__ == '__main__':
    func(3, 100, (0, 10), d=4)
