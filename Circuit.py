from Component import Component

class Circuit:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def add_component(self, component):
        pass

if __name__ =='__main__':
    print('Circuit test')