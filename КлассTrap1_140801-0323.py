# coding: utf
# python version: 2.75

from __future__ import division # Дроби без float.

from numpy import ones, sqrt, sort, array, append, histogram, histogram2d, meshgrid, zeros, ones_like
from numpy.random import rand, choice

from matplotlib.pyplot import hist, show, figure, title, plot, bar, xlabel, ylabel, hist2d

from mpl_toolkits.mplot3d import Axes3D

class Trap1:
    '''
    140801-0312 == Класс, определяющий одномерный трапециевидный кластер. N = 1..oo
    '''
    def __init__(self, a=1, b=2, c=3, d=4, N=100):
        N = int(N) # Парирование передачи float.
        # Если все границы совпадают - выдаём N одинаковых чисел:
        if a==b==d==c: return ones(N)*a
        a,b,c,d = sort([a,b,c,d])
        # Запишем функции, которые будут заполнять значениями левый треугольник, средний прямоугольник и правый треугольник неравнобокой трапеции:
        def xLeft(a,b,n):
            x=sqrt(rand(n)) # Выведено эмпирически; аналитический вывод см. у Вентцель в Теории Вероятностей 1969 на стр. двести восемьдесят какой-то.
            return x*(b-a)+a
        def xMid(a,b,n):
            x=rand(n)
            return x*(b-a)+a
        def xRight(a,b,n):
            x=1-sqrt(rand(n))
            return x*(b-a)+a
        # Вероятности для случайного выбора области:
        # Эмпирически доказано, что:
        # - Число значений должно быть пропорционально длинам отрезков.
        # - Но при этом, у прямоугольника должно быть значений в 2 раза больше, чем у двух треугольников.
        k1=(b-a)/(d-a)
        k2=(c-b)/(d-a)*2
        k3=(d-c)/(d-a)
        # Забиваем трапецию числами:
        X = array([])
        for i in xrange(N):
            way = choice([1,2,3],p=[k1/(k1+k2+k3),k2/(k1+k2+k3),k3/(k1+k2+k3)])
            if way == 1: X=append(X,xLeft(a,b,1))
            if way == 2: X=append(X,xMid(b,c,1))
            if way == 3: X=append(X,xRight(c,d,1))
        
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.set = X
        self.answer = 42
    
# Проверка:
N = 2e4 # Число реализаций
n = 50 # Число столбцов в гистограммах
a,b,c,d = 1,2,3,4 # Координаты трапеции
# a,b,c,d = sort(rand(4))+rand()*1.5*choice([-1, 1])

print 'a,b,c,d,N =', a,b,c,d,N


# Проверка набора по одному значению (работает медленнее):
# A = array([])
# for i in xrange(int(N)): A = append(A, Trap1(a,b,c,d,1).set)
# hist(A , n); title('In cycle')

# Проверка набора за одну итерацию (работает быстрее):
# figure()
# hist(Trap1(a,b,c,d,N).set, n); title('Not in cycle')


# Относительное число реализаций (relative number of realizations):
def RNR(x, n):
    '''Относительное число реализаций (ОЧР) (relative number of realizations (RNR)). На вход - вектор. На выходе данные для bar - x, y и ширина столбца.
    Пример: 
    <<< x = rand(1000)
    <<< bar(RNR(x, n)[0], RNR(x, n)[1], width=RNR(x, n)[2])'''
    a = histogram(x, n)
    return a[1][:-1], a[0]/max(a[0]), a[1][1]-a[1][0]

def RNRplot(x, n):
    '''Печатаем RNR'''
    bar(RNR(x, n)[0], RNR(x, n)[1], width=RNR(x, n)[2])

# Двумерный кластер из двух одномерных:

x = Trap1(a,b,c,d,N).set

figure()
RNRplot(x, n)
title('RNR')
plot([a,b,c,d], [0,1,1,0], lw=8, ls='--', c = 'black')

e,f,g,h = 1,1.5,2.5,4
# e,f,g,h = sort(rand(4))+rand()*1.5*choice([-1, 1])
y = Trap1(e,f,g,h,N).set

figure()
RNRplot(y, n)
title('RNR')
plot([e,f,g,h], [0,1,1,0], lw=8, ls='--', c = 'black')

n1 = 10 # Число столбцов 3D ОЧР
fig = figure()
ax = fig.add_subplot(111, projection='3d')
print 'e,f,g,h,N =', e,f,g,h,N

hist, xedges, yedges = histogram2d(x, y, n1) 
elements = (len(xedges) - 1) * (len(yedges) - 1)
ypos, xpos = meshgrid(yedges[:-1], xedges[:-1])# Внимание! Сначала ypos, а потом xpos, это не опечатка. Индексация meshgrid не вполне корректно совпадает с индексацией histogram2d.
xpos1 = xpos.flatten()
ypos1 = ypos.flatten()
zpos1 = zeros(elements)
xBarWidth = xedges[1]-xedges[0]
yBarWidth = yedges[1]-yedges[0]
dx = xBarWidth * ones_like(zpos1)
dy = yBarWidth * ones_like(zpos1)
dz = hist.flatten()

ax.bar3d(xpos1, ypos1, zpos1, dx, dy, dz/max(dz), color='b', zsort='average', alpha=1)
xlabel('x'); ylabel('y')

# Контуры пирамиды:
lw, ls, color = 8, '--', 'black'
ax.plot([a,b,c,d], [e,f,f,e], [0,1,1,0], lw=lw, ls=ls, c=color)
ax.plot([a,b,c,d], [h,g,g,h], [0,1,1,0], lw=lw, ls=ls, c=color)
ax.plot([b,b],[f,g],  [1,1], lw=lw, ls=ls, c=color)
ax.plot([c,c], [f,g], [1,1], lw=lw, ls=ls, c=color)
ax.plot([a,d,d,a,a], [e,e,h,h,e], [0,0,0,0,0], lw=lw, ls=ls, c=color)

# Цветная гистограмма:
figure()
hist2d(x,y,25)
xlabel('x'); ylabel('y')




show()
