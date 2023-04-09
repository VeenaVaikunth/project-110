import random
print('do you want to roll a dice?')

response = str('y')

while response == 'y':
    continue

no = random.randint(1,6)

if no == 1:
    print('[-----]')
    print('[     ]')
    print('[  0  ]')
    print('[     ]')
    print('[-----]')
    print('enter Y to roll again and N to exit')

if no == 2:
    print('[-----]')
    print('[0    ]')
    print('[     ]')
    print('[    0]')
    print('[-----]')
    print('enter Y to roll again and N to exit')


if no == 3:
    print('[-----]')
    print('[0    ]')
    print('[  0  ]')
    print('[    0]')
    print('[-----]')
    print('enter Y to roll again and N to exit')

if no == 4:
    print('[-----]')
    print('[ 0 0 ]')
    print('[     ]')
    print('[ 0 0 ]')
    print('[-----]')
    print('enter Y to roll again and N to exit')

if no == 5:
    print('[-----]')
    print('[0   0]')
    print('[  0  ]')
    print('[0   0]')
    print('[-----]')
    print('enter Y to roll again and N to exit')

if no == 6:
    print('[-----]')
    print('[0   0]')
    print('[0   0]')
    print('[0   0]')
    print('[-----]')
    print('enter Y to roll again and N to exit')