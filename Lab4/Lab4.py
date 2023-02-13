import math
import matplotlib.pyplot as plt

y = [1.845, 1.416, 1.286, 0.708, 0.580]  # Oppgitt i volt
speed_of_light = 299792458  # m/s
list_of_nm = [365, 405, 436, 546, 577]
x = []
for i in range(len(list_of_nm)):
    temp = speed_of_light / (list_of_nm[i] * (10 **(-9)))
    x.append(temp)  # Oppgitt i frekvens

x_sum = 0
x_kvadrat_sum = 0
y_sum = 0
xy_sum = 0
N = len(x)
sigma_y = 0
for i in range(len(x)):
    x_sum += x[i]
    xy_sum += x[i] * y[i]
    y_sum += y[i]
    x_kvadrat_sum += x[i] ** 2

delta = N * x_kvadrat_sum - x_sum ** 2

A = (y_sum * x_kvadrat_sum - x_sum * xy_sum) / delta
B = (N * xy_sum - x_sum * y_sum) / delta
to_B = B * 2
# print('A:', A, '   B:', B, '     lambda:', to_B)

for i in range(len(x)):
    sigma_y += math.sqrt((1 / (N - 2)) * (y[i] - A - B * x[i]) ** 2)

sigma_A = sigma_y * math.sqrt(x_kvadrat_sum / delta)
sigma_B = sigma_y * math.sqrt(N / delta)

print('A:', A, '  B: ', B, '     usikkerthet til A:', sigma_A, 'usikkerheten til y:', sigma_y,
      'sigma b:', sigma_B)

list_plot_y = []
for i in range(len(x)):
    y_1 = A + B*x[i]
    list_plot_y.append(y_1)

plt.scatter(x, y, color='blue')
plt.plot(x, list_plot_y, color='green')
e = 1.60217656535 * (10 **(-19))  # Oppgitt i Colomb
# B is eV * s, we need to turn it to Js.
print(B*e)

h = 6.62607015 * (10**-34)
list_plot_y = []
for i in range(len(x)):
    y_1 = A + h/e*x[i]
    list_plot_y.append(y_1)
plt.plot(x, list_plot_y, color='red')
plt.show()
