import csv
import random
import numpy as np
import matplotlib.pyplot as plt


def generate_data(n, min=0, max=1000):
    """
    Функция generate_data() генерирует случайные двумерные данные.

    Аргументы:
    n (int): количество точек, которые нужно сгенерировать.
    min (int): минимальное значения случайной переменной. По умолчанию 0.
    max (int): максимальное значения случайной переменной. По умолчанию 1000.

    Возвращая:
    data (list): список, состоящий из n-кол-во 2-д-двумя точками, [x, y], x, y -
    случайыыe float-двумя прямыми.
    """
    data = []
    for i in range(n):
        x = random.uniform(min, max)
        y = random.uniform(min, max)
        data.append([x, y])
    return data


def sort_data_by_x(data):
    """
    Данная функция сортирует переданный ей список данных (data) по значению,
    находящемуся в первом элементе.

    Аргументы:
    data - список, который нужно отсортировать.

    Возвращаемое значение:
    data - список, отсортированный по значению, находящемуся в первом элементе.
    """
    data.sort(key=lambda x: x[0])
    return data


def write_data_csv(data):
    """
    Данная функция используется для записи данных в файл csv.

    Parameters:
    data - двумерный список, который содержит данные, которые необходимо записать.

    Returns:
    None.
    """
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def plot_csv_data(csv_filename, x_axis_name, y_axis_name, plot_name, dot_color):
    """
    plot_csv_data(csv_filename, x_axis_name, y_axis_name, plot_name, dot_color) 
    - функция для отрисовки данных из csv файла.

    Параметры:
    csv_filename - путь к csv файлу;
    x_axis_name - название оси X;
    y_axis_name - название оси Y;
    plot_name - название графика;
    dot_color - цвет точек.
    """
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        data = [[float(x[0]), float(x[1])] for x in data]
        x = [x[0] for x in data]
        y = [x[1] for x in data]
        plt.xlabel(x_axis_name)
        plt.ylabel(y_axis_name)
        plt.scatter(x, y, s=20, c=dot_color, zorder=10)
        plt.title(plot_name)
        plt.grid(True)
        plt.show()


def generate_rising_data(n, min=0, max=1000):
    """
    generate_rising_data(n, min=0, max=1000) - функция для генерации данных с
    возрастающей тенденцией.

    Аргументы:
    n - число точек, которые нужно сгенерировать;
    min - минимальное значение (по умолчанию 0);
    max - максимальное значение (по умолчанию 1000).

    Функция возвращает: data - список, содержащий n-кол-во точек, имеющих
    возрастающую тенденцию.
    """
    data = []
    num = 1
    for i in range(n):
        x = i
        y = num
        data.append([x, y])
        num *= 1.1
    return data


def plot_csv_data_with_line(csv_filename, plot_name='', x_axis_name='x',
                            y_axis_name='y', dot_color='red',
                            line_color=u'#1f77b4'):
    """
    plot_csv_data_with_line(filename, plot_name='', x_axis_name='x', 
    y_axis_name='y', dot_color='red', line_color=u'#1f77b4')

    Функция позволяет строить график данных с линией. 
    Аргументы: 
    filename - имя файла csv, содержащего данные;
    plot_name - название графика;
    x_axis_name - название оси x;
    y_axis_name - название оси y;
    dot_color - цвет точки;
    line_color - цвет линии.
    """
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        data = [[float(x[0]), float(x[1])] for x in data]
        x = [x[0] for x in data]
        y = [x[1] for x in data]
    plt.xlabel(x_axis_name)
    plt.ylabel(y_axis_name)
    plt.plot(x, y, c=line_color)
    plt.scatter(x, y, s=20, c=dot_color, zorder=10)
    plt.title(plot_name)
    plt.grid(True)
    plt.show()


def plot_csv_data_method_least_squares(csv_filename, x_axis_name='x',
                                       y_axis_name='y', dot_color='red',
                                       line_color=u'#1f77b4'):
    """
    plot_csv_data_method_least_squares() - это функция для построения графика, 
    используя метод наименьших квадратов.

    Параметры: 
    csv_filename - имя файла csv, содержащего x-y данные;
    x_axis_name - название оси x;
    y_axis_name - название оси y;
    dot_color - цвет точки;
    line_color - цвет линии.
    """
    N = 100
    sigma = 3
    k = 0.5
    b = 2
    # load x and y from file csv
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        data = [[float(x[0]), float(x[1])] for x in data]
        x = np.array([x[0] for x in data])
        y = np.array([x[1] for x in data])
    # get max y or x value, cast int to int
    N = int(max(x))
    f = np.array([k*z+b for z in range(N)])
    # name axes
    plt.xlabel(x_axis_name)
    plt.ylabel(y_axis_name)
    mx = x.sum()/N
    my = y.sum()/N
    a2 = np.dot(x.T, x)/N
    a11 = np.dot(x.T, y)/N
    kk = (a11 - mx*my)/(a2 - mx**2)
    bb = my - kk*mx
    ff = np.array([kk*z+bb for z in range(N)])
    # extrapolate
    ff = np.append(ff, [kk*z+bb for z in range(N, N+10)])
    plt.plot(ff, c=line_color)
    plt.scatter(x, y, s=20, c=dot_color, zorder=10)
    # set plot name, kk and bb, round to 3 digits
    plt.title('Метод наименьших квадратов\nk = {}, b = {}'.format(
        round(kk, 3), round(bb, 3)))
    # zoom to points
    plt.xlim(min(x)-1, max(x)+1)
    plt.ylim(min(min(y), min(ff))-1, max(max(y), max(ff))+1)
    plt.grid(True)
    plt.show()
