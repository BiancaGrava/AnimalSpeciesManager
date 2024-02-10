from Repository import FileSpeciiRepo
from Controller import SpeciiService
from UI import Consola
def main():
    repo=FileSpeciiRepo("specii.txt")
    serv=SpeciiService(repo)
    cons=Consola(serv)
    cons.run()

main()
