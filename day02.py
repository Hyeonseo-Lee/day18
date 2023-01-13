#Chap 4 if


limits = 20
tweets = "pass" * 6
diff = limits - len(tweets)
if diff >= 0:
    print(tweets)
else:
    print(f'제한 글자 수 {abs(diff)} 초과')


vowels = 'aeiou'
letter = 'u'
if letter not in vowels:
    print("실행 안됨!")


a = []

print(bool([a]))
a.append(5)
print(bool(a))
print(bool(set()))
print(bool(dict()))
print(bool("ace"))
