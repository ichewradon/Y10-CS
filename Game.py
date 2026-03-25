from dataclasses import dataclass
@ dataclass

class character:
    name:str
    health:int
    no_inventory:int
    backpack:bool
    items:int
    xp:int
    speed:int
    
#intstantiating - creating an entry
james = character ("james", 20, 5, False, 0, 0, 10)
gethin = character ("gethin", 20, 5, False, 0, 0, 10)
jan = character ("jan", 20, 5, False, 0, 0, 10)

print ()
print ("=====================================================================================")
print ("            _         _    _            _      ___    _        _     _            _  ")
print ("  \    /   |_   |    |    | |   |\/|   |_       |    | |      |     |_|   |\/|   |_  ")
print ("   \/\/    |_   |_   |_   |_|   |  |   |_       |    |_|      |_|   | |   |  |   |_  ")
print()
print ("=====================================================================================")

print()
james.backpack = input(f"{james.name} would you like a backpack? It lowers speed but increases inventory space. (True or False)")
gethin.backpack = input(f"{gethin.name} would you like a backpack? It lowers speed but increases inventory space. (True or False)")
jan.backpack = input(f"{jan.name} would you like a backpack? It lowers speed but increases inventory space. (True or False)")

if james.backpack:
    james.speed = 5

else:
    james.speed = 10

    
if gethin.backpack:
    gethin.speed = 5

if jan.backpack:
    jan.speed = 5


print (james.speed)
print (gethin.speed)
print (jan.speed)
