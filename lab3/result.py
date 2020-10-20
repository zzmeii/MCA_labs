import matplotlib.pyplot as plt
import numpy as np


def func(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(x)
    result = []
    count = []
    desp = np.mean([(i - x_mean) ** 2 for i in x])

    for i in range(len(x)):
        temp = [x[i], y[i]]
        if temp in result:
            tt = result.index(temp)
            count[tt] = count[tt] + 20
        else:
            result.append(temp)
            count.append(10)

    for i in range(len(result)):
        plt.scatter(result[i][0], result[i][1], color='blue', s=count[i])
    a_dot = (np.mean(
        [x[i] * y[i] for i in
         range(len(x))]) - x_mean * y_mean) / desp
    b_dot = y_mean - a_dot * x_mean
    # y = ax+b
    plt.plot([min(x), max(x)],
             (a_dot * min(x) + b_dot, a_dot * max(x) + b_dot), c='r')
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
    data = np.random.random([2,100])
    func(data[0],data[1])