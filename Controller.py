from datetime import date
from Domain import DTO
from Repository import FileSpeciiRepo
class SpeciiService:
    def __init__(self,repo):
        self.__repository=repo

    def filtrare(self,d):
        try:
            params=d.strip().split("/")
            if len(params)!=3:
                raise Exception("format incorect! try: year/month/day")
            an=int(params[0])
            luna=int(params[1])
            ziua=int(params[2])
            da=date(an,luna,ziua)
        except Exception:
            raise Exception("data introdusa nu este corecta dpdv logic!")


        all_species=self.__repository.get_all()
        animale_filtrate=[]
        for specie in all_species:
            if specie.get_data()<d:
                animale_filtrate.append(specie)
        if animale_filtrate==[]:
            raise Exception("nu exista astfel de animale")
        return animale_filtrate

    def stats(self):
        all_species=self.__repository.get_all()
        final=[]
        for tip in ["mammal","reptile","bird","arachnides"]:
            maxim="0000/00/00"
            nume=""
            nra=0
            nrs=0
            for animal in all_species:
                if animal.get_tip()==tip:
                    nrs+=1
                    nra+=animal.get_lp()
                    if animal.get_data()>maxim:
                        maxim=animal.get_data()
                        nume=animal.get_nume()
            dto=DTO(tip,nume,0)
            if nrs!=0:
                media=nra/nrs
                dto.set_medie(media)
                dto.set_nrtot(nrs)
                dto.set_anitot(nra)
                final.append(str(dto))
        if final==[]:
            raise Exception("nu s au introdus animale")
        return final

def test_filtrare():
    repo=FileSpeciiRepo("test.txt")
    service=SpeciiService(repo)
    f=service.filtrare("2020/07/31")
    assert len(f)==2
    assert f[0].get_id()==2

def test_stats_and_str_dto():
    repo=FileSpeciiRepo("test.txt")
    service=SpeciiService(repo)
    s=service.stats()
    assert len(s)==2
    assert s==["mammal: Bobber, 10.0","reptile: Amazonica impennis, 32.0"]

test_filtrare()
test_stats_and_str_dto()


