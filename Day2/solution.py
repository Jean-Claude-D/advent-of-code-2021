
from typing import List, Tuple

count = [0]*3


def apply(line: str, count: List[int]) -> Tuple[int, int]:
    d, m = line.split(sep=' ')  # direction and magnitude
    d = d[0]
    m = int(m)

    if d == 'd':
        count[2] += m
    elif d == 'u':
        count[2] -= m
    elif d == 'f':
        count[0] += m
        count[1] += count[2] * m


for line in open('input', 'r'):
    apply(line, count)

print(f'Product is : {count[0]*count[1]}')
