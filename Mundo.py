import os
import random
import pickle


def SistemaPlanetario():
    global PlanetasRocoso
    global PlanetasGaseoso
    global Satelites
    global Estrellas
    global AgujerosNegros

    PlanetasRocoso=0
    PlanetasRocoso=random.randint(0,100)
    print("PlanetasR:_______",PlanetasRocoso)

    PlanetasGaseoso=0
    PlanetasGaseoso=random.randint(0,100)
    print("PlanetasG:_______",PlanetasGaseoso)


    Satelites=0
    Satelites=random.randint(0,100)
    Satelites
    print("Satelites:_______",Satelites)


    Estrellas=0
    Estrellas=random.randint(0,100)
    print("Estrellas:_______",Estrellas)


    AgujerosNegros=0
    AgujerosNegros=random.randint(0,100)
    print("Agujeros Negros:_",AgujerosNegros)

#Variables
Tiempo=0

def Turnos():
    global Tiempo
    Tiempo=int(Tiempo)+1
    print("Tiempo:__________",Tiempo)
    EscogerMenuInicio=int(input(">>>Presiona ENTER para continuar<<<"))

#Variables
SumaPlanetaR=0
RestaPlanetaR=0
DestinoPlanetaR=0
SumaPlanetaG=0
RestaPlanetaG=0
DestinoPlanetaG=0
SumaSatelite=0

def Continuacion():
    global PlanetasRocoso
    global PlanetasGaseoso
    global Satelites
    global Estrellas
    global AgujerosNegros
    Total=(PlanetasRocoso)+(Satelites)+(Estrellas)+(AgujerosNegros)
    print("Total de cuerpos:",Total)
    Suceso=random.randint(0,6000)
    if Suceso==59: #Choque del cual destruye o crea un Planeta del tipo Rocoso.
        PlanetasRocoso=PlanetasRocoso-1
        DestinoPlanetaR=random.randint(0,1)
        if DestinoPlanetaR==0:
            global RestaPlanetaR
            RestaPlanetaR=RestaPlanetaR+1
            if RestaPlanetaR==2:
                Satelites=Satelites+1
                RestaPlanetaR=0
        if DestinoPlanetaR==1:
            global SumaPlanetaR
            SumaPlanetaR=SumaPlanetaR+1
            if SumaPlanetaR==2:
                Estrellas=Estrellas+1
                SumaPlanetaR=0

    if Suceso==60: #Choque del cual destruye o crea un Planeta del tipo Gaseoso.
        PlanetasGaseoso=PlanetasGaseoso-1
        DestinoPlanetaG=random.randint(0,1)
        if DestinoPlanetaG==0:
            global RestaPlanetaG
            RestaPlanetaG=RestaPlanetaG+1
            if RestaPlanetaG==2:
                Satelites=Satelites+1
                RestaPlanetaG=0
        if DestinoPlanetaG==1:
            global SumaPlanetaG
            SumaPlanetaG=SumaPlanetaG+1
            if SumaPlanetaG==2:
                Estrellas=Estrellas+1
                SumaPlanetaG=0

    if Suceso==560: #Choque del cual destruye o crea un Satelite.
        Satelites=Satelites-1
        SumaSatelite=SumaSatelite+1
        if SumaSatelite==2:
            Planetas=Planetas+1
            SumaSatelite=0

    if Suceso==590: #Choque del cual crea un Agujero Negro.
        Estrellas=Estrellas-1
        AgujerosNegros=AgujerosNegros+1

    if Suceso==5900: #Choque del cual destruye un Agujero Negro.
        AgujerosNegros=AgujerosNegros-1

def Abrir():
    global PlanetasRocoso
    global PlanetasGaseoso
    global Satelites
    global Estrellas
    global AgujerosNegros
    global Tiempo
    global SumaPlaneta
    global RestaPlaneta
    global DestinoPlaneta
    global SumaSatelite
    Guardado=open("Guardado.pickle","rb")
    PlanetasRocoso=pickle.load(Guardado)
    PlanetasGaseoso=pickle.load(Guardado)
    Satelites=pickle.load(Guardado)
    Estrellas=pickle.load(Guardado)
    AgujerosNegros=pickle.load(Guardado)
    Tiempo=pickle.load(Guardado)
    SumaPlanetaR=pickle.load(Guardado)
    RestaPlanetaR=pickle.load(Guardado)
    DestinoPlanetaR=pickle.load(Guardado)
    SumaPlanetaG=pickle.load(Guardado)
    RestaPlanetaG=pickle.load(Guardado)
    DestinoPlanetaG=pickle.load(Guardado)
    SumaSatelite=pickle.load(Guardado)
    Guardado.close()

def Guardado():
    global PlanetasRocoso
    global PlanetasGaseoso
    global Satelites
    global Estrellas
    global AgujerosNegros
    global Tiempo
    global SumaPlaneta
    global RestaPlaneta
    global DestinoPlaneta
    global SumaSatelite
    Guardado=open("Guardado.pickle","wb")
    pickle.dump(PlanetasRocoso,Guardado)
    pickle.dump(PlanetasGaseoso,Guardado)
    pickle.dump(Satelites,Guardado)
    pickle.dump(Estrellas,Guardado)
    pickle.dump(AgujerosNegros,Guardado)
    pickle.dump(Tiempo,Guardado)
    pickle.dump(SumaPlanetaR,Guardado)
    pickle.dump(RestaPlanetaR,Guardado)
    pickle.dump(DestinoPlanetaR,Guardado)
    pickle.dump(SumaPlanetaG,Guardado)
    pickle.dump(RestaPlanetaG,Guardado)
    pickle.dump(DestinoPlanetaG,Guardado)
    pickle.dump(SumaSatelite,Guardado)
    Guardado.close()

def HistoriaNU():
    global PlanetasRocoso
    global PlanetasGaseoso
    global Satelites
    global Estrellas
    global AgujerosNegros
    global Tiempo
    global SumaPlanetaR
    global RestaPlanetaR
    global DestinoPlanetaR
    global SumaPlanetaG
    global RestaPlanetaG
    global DestinoPlanetaG
    global SumaSatelite
    HistoriaNU=open("Historia del Universo.txt","a")
    HistoriaNU.write("PlanetasR:_______")
    HistoriaNU.write(str(PlanetasRocoso))
    HistoriaNU.write("\n")
    HistoriaNU.write("PlanetasG:_______")
    HistoriaNU.write(str(PlanetasGaseoso))
    HistoriaNU.write("\n")
    HistoriaNU.write("Satelites:_______")
    HistoriaNU.write(str(Satelites))
    HistoriaNU.write("\n")
    HistoriaNU.write("Estrellas:_______")
    HistoriaNU.write(str(Estrellas))
    HistoriaNU.write("\n")
    HistoriaNU.write("Agujeros Negros:_")
    HistoriaNU.write(str(AgujerosNegros))
    HistoriaNU.write("\n")
    HistoriaNU.write("Tiempo:__________")
    HistoriaNU.write(str(Tiempo))
    HistoriaNU.write("\n")
    HistoriaNU.write(str(SumaPlanetaR))
    HistoriaNU.write("\n")
    HistoriaNU.write(str(RestaPlanetaR))
    HistoriaNU.write("\n")
    HistoriaNU.write(str(DestinoPlanetaR))
    HistoriaNU.write("\n")
    HistoriaNU.write(str(SumaPlanetaG))
    HistoriaNU.write("\n")
    HistoriaNU.write(str(RestaPlanetaG))
    HistoriaNU.write("\n")
    HistoriaNU.write(str(DestinoPlanetaG))
    HistoriaNU.write("\n")
    HistoriaNU.write(str(SumaSatelite))
    HistoriaNU.write("\n")
    HistoriaNU.write("------------------------------------")
    HistoriaNU.write("\n")
    HistoriaNU.close()

if os.path.isfile("Guardado.pickle"):
    Abrir()
    HNU=0
else:
    SistemaPlanetario()
    HNU=0
Turno=True
while Turno==True:
    try:
        if Tiempo==0:
            pass
        else:
            print("PlanetasR:________",PlanetasRocoso)
            print("PlanetasG:________",PlanetasGaseoso)
            print("Satelites:_______",Satelites)
            print("Estrellas:_______",Estrellas)
            print("Agujeros Negros:_",AgujerosNegros)
        Continuacion()
        Guardado()
        if HNU==1:
            HistoriaNU()
        HNU=1
        Turnos()
    except ValueError:
        pass
