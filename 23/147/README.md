# Задание №147

---

Исполнитель Калькулятор преобразует число, записанное на экране. У исполнителя есть две команды, которым присвоены номера:
> **1. Прибавь 1**
>
> **2. Умножь на 2 и прибавь 1**

Сколько различных результатов можно получить из исходного числа 3 после выполнения программы, содержащей ровно 11 команд?

---

### Решение

```python
numbers = {}

def f(x, step):
    if step == 11:
        numbers[x] = True
        return
    f(x + 1, step + 1), f(x * 2 + 1, step + 1)

f(3, 0)
print(len(numbers))
```

**Ответ:** _820_