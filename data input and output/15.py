n = int(input())
m = int(input())
t = int(input())
minutes =(n * 60 + m + t)
ans_hours = minutes // 60
ans_minutes = minutes % 60
if ans_hours > 24:
    ans_hours %= 24

print(f'{ans_hours :02}:{ans_minutes :02}')