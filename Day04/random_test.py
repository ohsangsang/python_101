import random

player = ['손흥민','김민재','황희찬','이강인']
a = random.randint(0, 3) #0~3 정수 하나
print(random.choice(player)) #리스트에서 한명 뽑기
b = random.shuffle(player)
c = random.uniform(1.5, 2.5) #주어진 범위에서 무작위 실수

