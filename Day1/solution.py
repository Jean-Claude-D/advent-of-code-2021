previous = float('inf')
count = 0

for line in open('input', 'r'):
  current = int(line)
  if current > previous:
    count += 1
  previous = current

print(f'Count is : {count}')