import matplotlib.pyplot as plt 
import numpy as np 


import time
import datetime

class Equilibrio ():
    def __init__(self,p,cv,cf):
        self.__p=p
        self.__cv=cv
        self.__cf=cf
        
    
    def proceso(self):
        print(separador)
        equilibrio=(cf/(p-cv))
        print(f"Estas son las unidades que tienes que vender para tener un Equilibrio (Ni ganancia , Ni perdida): {equilibrio} ")
        print(separador)
        It=(equilibrio*self.__p)
        costoV=(equilibrio*self.__cv)
        margenC=(It-costoV)
        utilidad=(margenC-self.__cf)
        print(separador,"RESPUESTAS",separador)
        print("Calculando Respuestas...")
        print(separador)
        time.sleep(3)
        print(f"Ventas: {It}")
        print(f"(-)Costo Variable : {costoV}")
        print(f"(=)Margen de Contribucion : {margenC}")
        print(f"(-)Costos Fijos : {self.__cf}")
        print(f"Utilidad,Perdida o punto de equilibrio : {utilidad}")
        print(separador)
        x=[0,equilibrio]
        y=[0,It]
        plt.plot(x,y,"r")
        plt.plot(It,label=r"$IT$",color="r")
        x1=[0,equilibrio]
        y2=[self.__cf,It]
        plt.plot(x1,y2,"g")
        plt.plot(costoV,label=r"$CT$",color="g")
        plt.grid(True)

        plt.plot(self.__cf,label=r"$Costo Fijo$",color="k")
        plt.axhline(self.__cf,color="k",lw=2)
        
        plt.legend(loc=4)
        plt.xlabel("Unidades")
        plt.ylabel("$ DINERO")
        plt.title("Grafica de Punto de Equilibrio")
        print("Dibujando tabla...")
        time.sleep(5)
        print(separador)
        plt.text(equilibrio,It,". Equilibrio",rotation=45)
        plt.show()
        print("Quieres saber la utilidad o perdida dependiendo de las unidades vendidas")
        minimenu=int(input("1=SI\n2=NO\n:"))
        

        while minimenu==1:
            print(separador)
            unidad=int(input("Dime las unidades vendidas : "))
            It2=(unidad*self.__p)
            costoV=(unidad*self.__cv)
            margenC=(It2-costoV)
            utilidad=(margenC-self.__cf)
            print(separador)
            print("Calculando Respuestas...")
            time.sleep(3)
            print(separador,"RESPUESTAS",separador)
            print(f"Ventas: {It2}")
            print(f"(-)Costo Variable : {costoV}")
            print(f"(=)Margen de Contribucion : {margenC}")
            print(f"(-)Costos Fijos : {self.__cf}")
            print(f"Utilidad,Perdida o punto de equilibrio : {utilidad}")
            print(separador)
            
            x=[0,equilibrio]
            y=[0,It]
            plt.plot(x,y,"ko")
            plt.plot(It,label=r"$Punto de Equilibrio$",color="k")
            
            x3=[0,unidad]
            y4=[0,It2]
            plt.plot(x3,y4,"r")
            plt.plot(It2,label=r"$IT$",color="r")

            x5=[0,unidad]
            y6=[self.__cf,It2]
            plt.plot(x5,y6,"g")
            plt.plot(costoV,label=r"$CT$",color="g")

            plt.grid(True)
            plt.plot(self.__cf,label=r"$Costo Fijo$",color="k")
            plt.axhline(self.__cf,color="k",lw=2)
            plt.legend(loc=4)
            plt.xlabel("Unidades")
            plt.ylabel("$ DINERO")
            plt.title("Grafica de Utilidad")
            print(separador)
            print("Dibujando Tabla...")
            time.sleep(5)
            plt.text(equilibrio,It,". Equilibrio",rotation=45)
            plt.show()
            print(separador)
            print("Quieres intentar con otro dato de Unidad ")
            minimenu=int(input("1=SI\n2=NO\n:"))