import random

auto = ['vesta', 'cherry', 'mersedes', 'toyota', 'audi', 'lamborghini']
zhenya = random.choice(auto)
result = 'Машина под санкцией' if 'audi' in auto else 'все норм'
print('res:\n', result)
