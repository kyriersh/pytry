#lesson with lambda/map/filter
x = int(input("input number :"))
y = (lambda z: z**3)(x)
print(y)
birth_years = list(range(1950,2000,10))
how_old_in2050 = list(map(lambda x: 2050 - x, birth_years))
print(how_old_in2050)
names = ['David', 'John', 'Annabelle', 'Johnathan', 'Veronica']
res =  list(filter(lambda x: len(x) > 5, names))
print(res)