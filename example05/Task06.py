# 5 Задача
def same_by(characteristic, val):
    r = list(map(characteristic, val))
    if len(set(r)) == 1 and r[0] == 0:
        return True
    else:
        return False
    
    
value = [0, 2, 10, 6]
#value = list(range(1, 5))
if same_by(lambda x: x % 2, value):
    print('same')
else:
    print('different')
