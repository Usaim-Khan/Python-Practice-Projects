def display_inventory(inv):
    keys = list(inv.keys())
    values = list(inv.values())
    # print(keys)
    # print(values)
    total_items = sum(values)
    print('Inventory')
    for i in range(len(keys)):
        print(f'{keys[i]}: {values[i]}')
    print('total number of items:',total_items)



inventory = {'log' : 5, 'raw wood': 14, 'raw metal' : 18, 'steel': 10,
             'canned apple' : 12, 'torch' : 4, 'gun' : 1, 'bed' : 1}
enemy_inventory = ['torch','canned apple','rope','canned apple','canned apple',
                   'gun','raw metal','raw metal','raw metal','torch','firewood',
                   'rope','rope','rope','rope']

def update_inventory(inv,lis):
    for item in lis:
        # print(item)
        if item in inv:
            # print(item,'is in dictionary')
            old_value = (inv[item])
            inv[item] = old_value + 1
        else:
            # print(item,'not in dict')
            inv[item] = 1

    return inv



display_inventory(inventory)
# print(inventory)
inventory = update_inventory(inventory,enemy_inventory)
print()
print()
display_inventory(inventory)
# print(inventory)

