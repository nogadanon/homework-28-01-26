# START
i = 0
_up_to_16 = 0
for _ in range(1, 10 + 1) :
    x = int(input('enter age: '))
    if x > 18 :
        break
    if x < 12 :
        continue
    i += 1
    if x >= 16 :
        _up_to_16 += 1
        '''
    if x >= 12 :
        i += 1
        if x >= 16 :
            _up_to_16 += 1
        '''

print('ther is ',i , 'players')
print('ther is', _up_to_16, 'players over 16 years old (Including 16)')




# STOP