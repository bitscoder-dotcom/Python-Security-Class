import random

class Fruit:
    examples = ['banana', 'mango', 'orange', 'pinneaple', 'avocado']

    @classmethod
    def sort(cls, name):
        print(f'Today, {name} prefers', random.choice(cls.examples),'.')

Fruit.sort("John")