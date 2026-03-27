
# Напиши цикл, который посчитает общее количество минут. Результат сохрани в переменную и выведи на экран. Используй в решении методы split(), replace() и оператор in.
time = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

time_replace = time.replace(' ',',')
time_lst = time_replace.split(',')

for i in time_lst:
    if i ==' ':
        continue
    elif 'h' in i:
        total_minutes += int(i.replace('h', '')) * 60
    elif 'm' in i:
        total_minutes += int(i.replace('m',''))
    elif 's' in i:
        total_minutes += int(i.replace('s', '')) // 60      

print(total_minutes)