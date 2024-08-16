
import inspect
# ДЗ интроспеция
def introspection_info(obj):
    lst = dir(obj)
    meth = []
    atr =[]
    for l in lst:
        get_atr = type(getattr(obj,l))
        #print(l,isinstance(get_atr,str),type(get_atr),get_atr)
        if  str(get_atr).find('method')>0:
            meth.append(l)
        else:
            atr.append(l)
    return {'type': type(obj), 'attributes': atr, 'methods': meth, 'module': inspect.getmodule(obj)}

class Rutiner():
    def __init__(self, alfa, betta):
        self.alfa = alfa
        self.betta = betta

    def Sum(self):
        return self.alfa+self.betta

if __name__ == '__main__':
    Rute = Rutiner( 50,60)
    print(introspection_info(Rute))
    #introspection_info(42)