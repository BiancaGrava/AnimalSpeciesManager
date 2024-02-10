class Consola:
    def __init__(self,service):
        self.__service=service
        self.__comenzi={
            "filtreaza dupa data":self.__ui_filter,
            "statistici":self.__ui_stats
        }
    def __ui_filter(self,params):
        if len(params)!=1:
            print("nr parametrii incorect!")
        else:
            try:
                data=params[0]
                f=self.__service.filtrare(data)
                for animal in f:
                    print(animal)
            except Exception as ex:
                print(ex)
    def __ui_stats(self,params):
        if len(params)!=0:
            print("nr parametrii incorect!")
        else:
            try:
                s=self.__service.stats()
                for animal in s:
                    print(animal)
            except Exception as ex:
                print(ex)
    def run(self):
        while True:
            input_initial=input("introduceti comanda: ")
            input_initial=input_initial.strip()
            if input_initial=="exit":
                return
            else:
                partile_comenzii=input_initial.split('>')
                numele_comenzii=partile_comenzii[0].strip()
                if len(partile_comenzii)==1:
                    params=[]
                else:
                    params=partile_comenzii[1].strip().split(',')
                if numele_comenzii in self.__comenzi:
                    try:
                        self.__comenzi[numele_comenzii](params)
                    except Exception as ex:
                        print(ex)
                else:
                    print("comanda nu este cunoscuta!")
