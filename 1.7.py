hour = int(input())
minute = int(input())
second = int(input())
hour2 = int(input())
minute2 = int(input())
second2 = int(input())
hour3 = (hour2 - hour) * 3600
minute3 = (minute2 - minute) * 60
second3 = (second2 - second)
answer = hour3 + minute3 + second3
print(answer)
