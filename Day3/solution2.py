def rating(type: str):
    i = 0
    prev = open('input').readlines()
    next0 = []
    next1 = []

    while len(prev) > 1:
        for line in prev:
            if line[i] == '0':
                next0.append(line)
            else:
                next1.append(line)

        if type == 'oxy':
            if len(next1) >= len(next0):
                prev = next1
            else:
                prev = next0
        elif type == 'co2':
            if len(next0) <= len(next1):
                prev = next0
            else:
                prev = next1
        i += 1
        next0 = []
        next1 = []

    print(f'Type {type}, Rating : {prev}')


rating('oxy')
rating('co2')
