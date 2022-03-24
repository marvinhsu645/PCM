class Component:
    def __init__(self, name, type):
        self.name: str = name
        self.type: str = type       # (ic), (r)esistance, (c)apacitance
        # type = 'ic'                
        self.specification: dict    # feature, electrical characteristics
        # sepcification = {'feature_text': {'Adjustable Duty Cycle',
        #                                   ...}
        #                  'feature_value': {'High-Current Drive Capability': '200*mA'
        #                                    'Timing': [us, hr]
        #                                    'Turn off Time': '<2*us',
        #                                    ...}
        #                  'electrical_characteristics': {'parameter': [supply_voltage, supply_current, ...]      # list of Parameter
        #                                                 'note': ['Tested at V_CC=5.0*V and V_CC=15*V']          # list of string
        #                 }
        self.picture: dict          # block diagram, real picture

    def __str__(self):
        return str(self.name)

    def set_spec(self, **spec):
        self.specification = spec
    
    def get_spec(self):
        return self.specification

if __name__ =='__main__':
    timer555 = Component('Timer-555')
    timer555.set_spec(name='abc', value=123)
    print(timer555.get_spec())
