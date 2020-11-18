a,b,c = map (int, input().split())
frist = (a+b)%c
second = ((a%c)+(b%c))%c
third = (a*b)%c
fourth = ((a%c)*(b%c))%c
print(frist)
print(second)
print(third)
print(fourth)