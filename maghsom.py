i = 0
count = 0
while i < 1:
    num = int(input())
    i += 1
    for e in range(2, num + 1):
        if num % e == 0:
            count = 1
            for j in range(2, (e // 2 + 1)):
                count = 0
                break
            if count == 1:
                print(e)
