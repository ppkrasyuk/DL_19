# -*- coding: utf-8 -*-
"""lesson_6_tf

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wmKAUwXKuIYavJRl1M2RNtkslAW7tiqF

### Задание 1. Реализация линейной функции  $y = W \cdot x + b$

Первым заданием будет подсчет следующего выражения: $Y = WX + b$, где $W$и  $X$ - это случайные матрицы, а b - случайный вектор. 

**Задание**: Рассчитать $W\cdot x + b$, где $W, x $, и $b$ получены из стандартного нормального распределения. W имеет размер (4, 3), x - (3,1), b - (4,1). В кач-ве примера показано, как реализовать объявление X с размером (3,1):
```python
X = tf.constant(np.random.randn(3,1), name = "X")

```
Также обратите внимание на следующие функции: 
- tf.matmul(..., ...) - перемножение матриц;
- tf.add(..., ...) - сложение двух объектов;
- np.random.randn(...) - метод numpy для инициализации массивов случайными значениями.

**NB** Обратите внимание на аргумент name функции tf.constant. Не забудьте его тоже правильно указать.
"""

import numpy as np
import tensorflow as tf

def linear_function():
    """
    Implements a linear function: 
            Initializes W to be a random tensor of shape (4,3)
            Initializes X to be a random tensor of shape (3,1)
            Initializes b to be a random tensor of shape (4,1)
    Returns: 
    result -- runs the session for Y = WX + b 
    """
    
    np.random.seed(11)
    
    ### START CODE HERE ### (4 lines of code)
    X = tf.constant(np.random.randn(3, 1), name="X")
    W = tf.constant(np.random.randn(4, 3), name="W")
    b = tf.constant(np.random.randn(4, 1), name="b")
    Y = tf.add(tf.matmul(W, X), b)
    ### END CODE HERE ### 
    #print(X,W,b,Y)
    # Create the session using tf.Session() and run it with sess.run(...) on the variable you want to calculate
    
    ### START CODE HERE ###
    sess = tf.Session()
    result = sess.run(Y)
    ### END CODE HERE ### 
    
    # close the session 
    sess.close()

    return result
  
#linear_function()

"""### Задание 2. Реализация функции активации (сигмоиды)

Итак, мы реализовали сверху линейную часть шага forward_propagation. Tensorflow уже имеет реализации таких функций активации как сигмоида или ReLU. В данном задании необходимо будет реализовать шаг подсчета сигмоиды. 

Для выполнения этого задания надо будет воспользоваться типом tf.placeholder. При запуске сессии надо будет передать словарь feed_dict со значением z (результат предыдущей функции).
Порядок будет следующим:
 - создать placeholder x;
 - записать вычисления, которые над ним будут проводиться (tf.sigmoid);
 - запустить сессию.

Сессию можно запустить двумя способами: 

**Способ 1:**
```python
sess = tf.Session()
# Вычислительные шаги
result = sess.run(..., feed_dict = {...})
sess.close() # Закрытие сессии
```
** Способ 2:**
```python
with tf.Session() as sess: 
    # Вычислительные шаги
    result = sess.run(..., feed_dict = {...})
    # Нет необходимости явно закрывать сессию :)
```
"""

def sigmoid(z):
    """
    Computes the sigmoid of z
    
    Arguments:
    z -- input value, scalar or vector
    
    Returns: 
    results -- the sigmoid of z
    """
    
    ### START CODE HERE ###
    # Create a placeholder for x. Name it 'x'.
    x = tf.placeholder(tf.float32, name="x")

    # compute sigmoid(x)
    sigmoid = tf.sigmoid(x)

    # Create a session, and run it.
    # You should use a feed_dict to pass z's value to x. 
    sess = tf.Session()
    # Вычислительные шаги
    result = sess.run(sigmoid, feed_dict={x: z})
    sess.close() # Закрытие сессии
    

    
    ### END CODE HERE ###
    
    return result
  
#sigmoid(linear_function())

"""### Задание 3 -  Подсчет функции ошибки

Многие функции ошибки также содержатся в библиотеке TensorFlow, в том числе бинарная кросс-энтропия: 
$$ J = - \frac{1}{m}  \sum_{i = 1}^m  \large ( \small y^{(i)} \log a^{ [2] (i)} + (1-y^{(i)})\log (1-a^{ [2] (i)} )\large ).\small\tag{2}$$


**Задание**: Реализуйте подсчет функции ошибки, используя следующую функцию: 


- `tf.nn.sigmoid_cross_entropy_with_logits(logits = ...,  labels = ...)`

Шаги должны быть следующими: подать сигмоиде входные данные z, посчитать сигмоиду, затем вызвать функцию ошибки, где logits - это вывод нейросети до применения сигмоиды, labels - истинный ответ. Таким образом, будет осуществляться подсчет следующего выражения:

$$- \frac{1}{m}  \sum_{i = 1}^m  \large ( \small y^{(i)} \log \sigma(z^{[2](i)}) + (1-y^{(i)})\log (1-\sigma(z^{[2](i)})\large )\small\tag{2}$$
"""

def cost(logits, labels):
    """
    Computes the cost using the sigmoid cross entropy
    
    Arguments:
    logits -- vector containing z, output of the last linear unit (before the final sigmoid activation)
    labels -- vector of labels y (1 or 0) 
    
    Note: What we've been calling "z" and "y" in this class are respectively called "logits" and "labels" 
    in the TensorFlow documentation. So logits will feed into z, and labels into y. 
    
    Returns:
    cost -- runs the session of the cost (formula (2))
    """
    
    ### START CODE HERE ### 
    
    # Create the placeholders for "logits" (z) and "labels" (y)
    z = tf.placeholder(tf.float32, name="z")
    y = tf.placeholder(tf.float32, name="y")
    
    # Use the loss function 
    cost = tf.nn.sigmoid_cross_entropy_with_logits(logits=z, labels=y)
    
    # Create a session (approx. 1 line). See method 1 above.
    sess = tf.Session()
    
    # Run the session (approx. 1 line).
    cost = sess.run(cost, feed_dict={z: logits, y: labels})
    
    # Close the session (approx. 1 line). See method 1 above.
    sess.close()
    
    ### END CODE HERE ###
    
    return cost
