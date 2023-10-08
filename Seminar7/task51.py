values = [0, 2, 10, 6]

def same_by(f,obj):
    return len(set(map(f,obj))) == 1
    

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
