import random

small = bool(random.getrandbits(1))
green = bool(random.getrandbits(1))

print(small, green)

if small:
    if green:
        print('pea, 완두콩은 작고 녹색이다')
    else :
        print('cherry, 체리는 작고 녹색이 아니다')

else :
    if green:
        print('watermelon, 수박은 크고 녹색이다')
    else :
        print('pumpkin, 호박은 크고 녹색이 아니다')

