from typing import List
class Épület:
    név: str    
    város: str
    ország: str
    magasság: float
    emelet: int
    épült: int

    def __init__(self, sor: str)-> None:
          név, város, ország, magasság, emelet, épült=sor.split(';')
          self.név=név          
          self.város=város
          self.ország=ország
          self.magasság=float(magasság.replace(',','.'))
          self.emelet=int(emelet)
          self.épült=int(épült)


def main() -> None:

    épületek: List[Épület]=[]
    with open('legmagasabb.txt','r',encoding='UTF-8') as file:
            for sor in file.read().splitlines()[1:]:
                épületek.append(Épület(sor))

    
    #Készítsen statisztikát országok szerint az épületek számáról szótár nélkül:
    print('Ország statisztika:')
    orszagok: List[str]=[]
    for i in épületek:
        if i.ország not in orszagok:
            orszagok.append(i.ország)

    for i in orszagok:
        sg:int=0
        for j in épületek:
            if i ==j.ország:
                sg+=1
        print(f'{i} - {sg} db')



    # nemet.txt állományba írja ki azoknak a német városoknak a nevét:
    német_v: List=[]
    for i in épületek:
        if i.ország=='Németország' and i.város not in német_v:
            német_v.append(i.város)
    try:
        with open('nemet.txt','w',encoding='UTF-8') as file:
            file.write('Német városok:\n')
            for i in német_v:
                file.write(f'\t{i}\n') 
    except:
        print('Hiba! Az írás nem sikerült!')


if __name__ == "__main__":
    main()