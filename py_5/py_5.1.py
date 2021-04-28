# practice with block try/except/finally
coffee = ['Cafe latte', 'Caffe Americano', 'Espresso', 'Cappuccino', 'Macchiato']
try:
    choice = int(input(" Select : "))
    print(coffee[choice])
except:
    print("invalid number")
finally:
    print("have a good day")
