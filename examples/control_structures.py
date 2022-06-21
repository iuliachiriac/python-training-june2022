temperature = 25
print('Hi!')

if temperature > 20:
    print('Warm weather.')
elif temperature > 0:
    print('Cold weather.')
else:
    print('Extremely cold weather.')

while temperature < 40:
    temperature += 1
    print('Increasing temperature to', temperature)

while True:
    if temperature == 30:
        break
    temperature -= 1
    print('Decreasing temperature to', temperature)

greeting = "Bună dimineața!"
for elem in greeting:
    if elem.isalpha():
        print(elem)

for elem in greeting:
    if elem.isspace():
        break
    print(elem)

for elem in greeting:
    if elem == 'a':
        continue
    print(elem)

print('Goodbye.')
