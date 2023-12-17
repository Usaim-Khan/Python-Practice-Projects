a = ['muh', 'ha', 'mmad', 'usaim', 'k', 'h', 'a', 'n']
b = ['apple', 'banana', 'orange', 'mango', 'grapes']


def comma(lis):
    mystr = ''
    lenght = len(lis)
    for i in range(lenght-1):
        # print(f'{lis[i]}, ',end= '')
        mystr = mystr + ', ' + lis[i]

    mystr = mystr + ' and ' + lis[-1]
    mystr = mystr[2:]
    # print(f'and {lis[-1]}')
    return mystr


print(comma(b))
