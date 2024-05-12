class Fruit:
    name = 'frooloops'

    # initialization (careful is not the same as a constructur perse)
    def __init__(self, name):
        self.name = name

    # called when the attribute does not exists
    def __getattr__(self, key):
        return 'apple'

    # called every time an attribute is requested, does not
    # matter if it exist or not (higher precedence than getattr)
    def __getattribute__(self, key):
        return 'orange'

    # called when the key requested does not exist
    def __getitem__(self, key):
        return 'grape'


fruit = Fruit('Cherry')
print(fruit.name)
print(fruit.flavor)
print(fruit['something'])
