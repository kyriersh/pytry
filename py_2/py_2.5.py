# money and friends
# program to calculate is it enough money to buy something for friends
money = int(input( " How much money : " ))
friends = int(input( " How much friends : "))
price_of_thing = int(input( " Price : " ))
if money >= ( friends * price_of_thing ):
    print(" Enough ! ")
    if money >= (friends * price_of_thing):
        print( str(money - ( friends * price_of_thing )) + "$ also have ! " )
if money <= ( friends * price_of_thing ):
    print( " Not enough ! ")
    if money <= (friends * price_of_thing):
        print(str(money - ( friends * price_of_thing )) + "$ not enough ! ")
