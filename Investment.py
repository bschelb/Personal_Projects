print("How many years do you plan on investing?")
y = float(input())
print("How much money are you investing initially?")
p = float(input())
print("What is your expected yearly interest rate?")
r = float(input())
print("How much are you investing monthly?")
d = float(input())

n = 12
i = (r / 100)  / 12
t = n * y

total = d * (((1 + i) ** t - 1) / i) * (1 + i)
pfv = p * (1 + i) ** t
final_total = pfv + total
print(final_total)