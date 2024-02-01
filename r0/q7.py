words = int(input())
interactions = 0
learnt = 0
while words > 0:
  interactions += 5+learnt
  words -= 5
  learnt += 5
while words < 0:
  interactions -= 1
  words += 1
print(interactions)
