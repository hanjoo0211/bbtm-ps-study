t = int(input())
for _ in range(t):
    num, unit = input().split()
    num = float(num)
    if unit == 'kg':
        print('{:.4f} lb'.format(num * 2.2046))
    elif unit == 'lb':
        print('{:.4f} kg'.format(num * 0.4536))
    elif unit == 'l':
        print('{:.4f} g'.format(num * 0.2642))
    elif unit == 'g':
        print('{:.4f} l'.format(num * 3.7854))