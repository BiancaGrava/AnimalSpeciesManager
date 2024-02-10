class Specii:
    def __init__(self,id,nume,data,locatia,tip,lifespan):
        self.__id=id
        self.__nume=nume
        self.__data=data
        self.__locatia=locatia
        self.__tip=tip
        self.__lifespan=lifespan

    def get_id(self):
        '''getter method'''
        return self.__id
    def get_tip(self):
        '''getter method'''
        return self.__tip
    def get_nume(self):
        '''getter method'''
        return self.__nume
    def get_location(self):
        '''getter method'''
        return self.__locatia
    def get_lp(self):
        '''getter method'''
        return self.__lifespan
    def get_data(self):
        '''getter method'''
        return self.__data

    def __eq__(self,gi):
        return self.get_id()==gi.get_id()

    def __str__(self):
        return f"{self.__id},{self.__nume},{self.__data},{self.__locatia},{self.__tip},{self.__lifespan}"

def test_create():
    specie=Specii(12,"Bober","2023/12/31","Poland","mammal",30.5)
    epsilon=0.00001
    assert specie.get_id()==12
    assert specie.get_nume()=="Bober"
    assert specie.get_data()=="2023/12/31"
    assert specie.get_location()=="Poland"
    assert specie.get_tip()=="mammal"
    assert abs(specie.get_lp()-30.5)<epsilon

test_create()

class DTO:
    def __init__(self,tip,nume,durata):#data
        self.__tip=tip
        self.__nume=nume
        self.__durata=durata
        self.__medie=0
        self.__nrtot=0
        self.__anitot=0

    def get_tip(self):
        return self.__tip
    def get_nume(self):
        return self.__nume
    def get_lp(self):
        return self.__durata
    def get_avglp(self):
        return self.__medie
    def set_medie(self,nr):
        self.__medie=nr
    def set_nrtot(self,nr):
        self.__nrtot=nr
    def set_anitot(self,ani):
        self.__anitot=ani

    def __str__(self):
        return f"{self.__tip}: {self.__nume}, {self.__medie}"

