from typing import List

FS = 3 # frame-size
skip_value = FS-1
frame = [0]*FS
previous = float('inf')
count = 0

def push(frame: List[int], val: int, fs: int = FS):
  for i in range(1,fs):
    frame[-i] = frame[-(i+1)]
  frame[0] = val

for line in open('input', 'r'):
  push(frame, int(line)) # push new value onto frame
  current = sum(frame)
  if skip_value > 0:
    skip_value -= 1
  else:
    if current > previous:
      count += 1
    previous = current

print(f'Count is : {count}')