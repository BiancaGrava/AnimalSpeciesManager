from Domain import Specii
class SpeciiRepo:
    def __init__(self):
        self._animals={}
    def get_all(self):
        return [self._animals[ida] for ida in self._animals.keys()]

class FileSpeciiRepo(SpeciiRepo):
    def __init__(self,calef):
        SpeciiRepo.__init__(self)
        self.__calef=calef

    def __read_all_species_from_file(self):
        with open(self.__calef,"r") as f:
            self._animals.clear()
            lines=f.readlines()
            for line in lines:
                if line!="":
                    parts=line.split(",")
                    id=int(parts[0])
                    nume=parts[1]
                    data=parts[2]
                    locatia=parts[3]
                    tip=parts[4]
                    lp=int(parts[5])
                    specie=Specii(id,nume,data,locatia,tip,lp)
                    self._animals[id]=specie

    def __write_all_events_to_file(self):
        with open(self.__calef,"w") as f:
            for id in self._animals.keys():
                f.write(str(self._animals[id])+"\n")

    def golire(self):
        with open(self.__calef,"w") as f:
            f.write("")

    def get_all(self):
        self.__read_all_species_from_file()
        return SpeciiRepo.get_all(self)





