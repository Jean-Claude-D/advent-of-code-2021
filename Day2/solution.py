
from typing import Tuple

count = [0]*2


def parse(line: str) -> Tuple[int, int]:
    d, m = line.split(sep=' ')  # direction and magnitude

    return (0 if d[0] == 'f' else 1, -int(m) if d[0] == 'u' else int(m))


for line in open('input', 'r'):
    d, m = parse(line) # direction and magnitude
    count[d] += m

print(f'Product is : {count[0]*count[1]}')