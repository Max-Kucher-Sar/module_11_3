from inspect import getmodule

class Animal:
    def __init__(self, pet):
        self.pet = pet
        self.voice = None

    def sound(self):
        if self.pet == 'Dog':
            self.voice = 'Bark'
        elif self.pet == 'Cat':
            self.voice = 'Mew'
        return self.voice


pet_sound = Animal('Dog')

def introspection_info(arg):
    practice = {}
    practice['type'] = type(arg).__name__
    practice['attributes'] = [atribute for atribute in dir(arg) if not callable(getattr(arg, atribute))]
    practice['methods'] = [method for method in dir(arg) if callable(getattr(arg, method))]
    practice['module'] = getmodule(arg)

    return practice

number_info = introspection_info(pet_sound)
print(number_info)
