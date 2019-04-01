'''from pprint import	pprint
message	=	'It	was	a	bright	cold	day	in	April,	and	the	clocks	were	striking thirteen.'
count	=	{}
for	character	in	message:
    count.setdefault(character,	0)
    count[character]	=	count[character]	+	1
pprint(count)
'''
kit={'rope':	1,	'torch':	6,	'gold coin':	42,	'dagger':1,	'arrow':	12}

dragonLoot	=	['gold coin',	'dagger',	'gold coin',	'gold coin',	'ruby']

def display_inventory(showkit):
    count	=	0
    print()
    print("Inventory :")
    print()
    for k, v in showkit.items():
        count+=v
        print(k  + ':   ' + str(v))

    print()
    print("Total Inventory Items : " + str(count))

def	addToInventory(inventory,	addedItems):
    #Code it up boy!
    for i in range(len(addedItems)):
        print(inventory.keys())
        if addedItems[i] in inventory.keys():
            inventory[addedItems[i]]+=1
        else:
            inventory.setdefault(addedItems[i], 1)
    return(inventory)
kit	=	addToInventory(kit,	dragonLoot)

print(kit)

display_inventory(kit)
