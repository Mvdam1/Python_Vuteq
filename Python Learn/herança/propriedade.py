#property() serve para criar atributos genrenciados em suas classes. Voce pode usar atributos
#gerenciados quando precisar modificar  sua implementação interna sem alterar a API publicada classe


class Foo:
    def __init__(self, x =None):
        self._x = x
    @property 
    def x(self):
            return self._x or 0
        
        
    @x.setter
    def x(self, value):
        self._x += value
        
    @x.deleter
    def x(self):
        self._x -= 1    


foo = Foo(9)
print(foo.x)
foo.x = 12
print(foo.x)
del foo.x
print(foo._x)