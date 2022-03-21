class Component:
    def __init__(self, name):
        self.name = name
        self.type = ''
            # IC, resistance, capacitance
        self.specification = {}
            # feature, electrical characteristics
        self.pin = {}
            # pin description
        self.picture = ''
            # block diagram, real picture

    def __str__(self):
        return str(self.name)

    def set_spec(self, **spec):
        self.specification = spec
    
    def get_spec(self):
        pass

if __name__ =='__main__':
    timer555 = Component('Timer-555')
    timer555.set_spec({''})
