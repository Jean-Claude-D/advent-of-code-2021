bin1 = [0]*12

bin0 = [0]*12

def f(x):
  for i,bit in enumerate(x):
    if bit == '1':
      bin1[i] += 1
    elif bit == '0':
      bin0[i] += 1

def g(x,y):
  pass

for line in open('input', 'r'):
    f(list(line))
  
most = [0]*12

for i,x in enumerate(bin0):
  if bin1[i] > bin0[i]:
    most[i] = 1
  else:
    most[i] = 0

print(f'Product is : {most}')
