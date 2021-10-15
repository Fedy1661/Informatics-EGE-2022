# Задание №153

---

### Исполнитель Калькулятор преобразует число, записанное на экране. У исполнителя есть две команды, которым присвоены номера:

> **1. Вычти 8**
> 
> **2. Раздели нацело на 2**

### Первая команда уменьшает число на 8, вторая – вдвое. Программа для исполнителя – это последовательность команд. Сколько существует таких программ, которые исходное число 102 преобразуют в число 5 и при этом траектория вычислений программы содержит число 43?

---

### Решение

```python
def f(start, x):
    if start < x: return 0
    if start == x: return 1
    return f(start - 8, x) + f(start // 2, x)

print(f(102, 43) * f(43, 5))

```

**Ответ:** _8_