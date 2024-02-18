import random

auto = ['vesta', 'cherry', 'mersedes', 'toyota', 'audi', 'lamborghini']
zhenya = random.choice(auto)
print(zhenya)
print ('da') if (zhenya=='vesta' or zhenya == 'toyota') else print('net')
