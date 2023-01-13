import random
secret = int(random.randint(1, 10)) #1에서 10 사이의 정수가 임의로 발생
guess = int(random.randint(1, 10))
print(guess, secret)

if guess < secret:
    print('too low')
elif guess > secret:
    print('too high')
elif guess == secret:
    print('just right')