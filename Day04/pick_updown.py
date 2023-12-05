# 유저에게 해당 범위를 지정 받습니다. 1 ~ n
# n의 범위를 지정해주세요!
# 1~n 어떤 정수를 임의로 뽑히고
# 총 5번 기회를 통해서 해당 숫자를 맞추기
# 맞는다면 맞습니다! 축하드립니다!😁
# 틀리면 틀렸습니다. 다시 한번 맞춰보세요😂
import random
user = int(input("n의 범위를 지정하세요:"))
pick = random.randint(1, user)
target = int(input("해당 랜덤 숫자를 맞춰보세요!"))
msg = "맞습니다! 축하드립니다!" if pick == target else "틀렸습니다."
print(msg)