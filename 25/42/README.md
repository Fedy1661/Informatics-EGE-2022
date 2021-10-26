# Задание №42

---

Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [4202865; 4202923], простые числа. Выведите все найденные простые числа в порядке возрастания, слева от каждого числа выведите его номер по порядку. 

---

### Решение

```python
place = 0
for i in range(420_2865, 420_2923+1):
    divs = 0
    for d in range(1, i+1):
        if i % d == 0:
            divs += 1
    if divs == 2:
        place +=1
        print(place, i)
```

**Ответ:** 
```
1 4202897
2 4202899
3 4202903
4 4202911
5 4202923
```