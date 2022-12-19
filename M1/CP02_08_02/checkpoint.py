# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

# Recordar utilizar la ruta relativa, no la absoluta para ingestar los datos desde los CSV
# EJ: 'datasets/xxxxxxxxxx'

import pandas as pd
import numpy as np

def Ret_Pregunta01():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros cuya entidad sea Argentina retornando ese valor en un dato de tipo entero.
    Pista averiguar la función Shape
    '''
    #Tu código aca:
    df1 = pd.read_csv('datasets\Fuentes_Consumo_Energia.csv',encoding='utf-8')
    argentina = pd.Series(elemento for elemento in df1['Entity'])
    mask = argentina == 'Argentina'
    return argentina[mask].count()

def Ret_Pregunta02():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe eliminar las columnas 'Code' y 'Entity' y luego informar la cantidad de columnas
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df2 = pd.read_csv('datasets\Fuentes_Consumo_Energia.csv',encoding='utf-8')
    df22 = df2.drop(columns = ['Code','Entity'], axis=1)
    return len(df22.columns)

def Ret_Pregunta03():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros, sin tener en cuenta aquellos con valores faltantes, para el campo 'Code' 
    y retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df3 = pd.read_csv('datasets\Fuentes_Consumo_Energia.csv',encoding='utf-8')
    df33 = df3.dropna(subset=['Code'])
    return len(df33.index)

def Ret_Pregunta04():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    El ExaJulio es una unidad diferent al TWh, es decir, no tiene sentido sumarlos o
    buscar proporciones entre ellos. 
    La fórmula de conversión es: 277.778 Teravatios/Hora (TWh) = 1 Exajulio
    Los campos terminados en "_EJ" corresponden a mediciones en Exajulios,
    y los terminados en "_TWh" corresponden a Teravatios/Hora.
    La consigna es crear un nuevo campo, que se denomine "Consumo_Total"
    y que guarde la sumatoria de todos los consumos expresados en Teravatios/Hora
    (convirtiendo a esta medida los que están en Exajulios).
    Esta función debe informar el consumo total para la entidad 'World' y año '2019',
    redondeado a 2 decimales, retornando ese valor en un dato de tipo float.
    '''
    #Tu código aca:
    df4 = pd.read_csv('datasets\Fuentes_Consumo_Energia.csv',encoding='utf-8')
    df41 = df4[(df4['Entity'] == 'World') & (df4['Year'] == 2019)]
    return (round(((df41.iloc[0,3]+df41.iloc[0,4]+df41.iloc[0,10])*277.778+df41.iloc[0,5]+df41.iloc[0,6]+df41.iloc[0,7]+df41.iloc[0,8]+df41.iloc[0,9]),2))

def Ret_Pregunta05():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar el año de mayor generación de energía solar (Solar_Generation_TWh)
    para la entidad 'Europe' retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df5 = pd.read_csv('datasets\Fuentes_Consumo_Energia.csv',encoding='utf-8')
    df51 = df5[df5.Entity == 'Europe']
    registro = df51.loc[df51.Solar_Generation_TWh.idxmax()]
    return (registro['Year'])

def Ret_Pregunta06(m1, m2):
    '''
    Esta función recibe dos arrays de Numpy, de 2 dimensiones cada uno y devuelve el valor booleano True si es posible realizar una multiplicación entre ambas matrices,
    y el valor booleano False si no lo es.
    Ej:
        n1 = np.array([[0,0,0],[1,1,1],[2,2,2]])
        n2 = np.array([[3,3],[4,4],[5,5]])
        print(Ret_Pregunta06(n1,n2))
            True            -> Valor devuelto por la función en este ejemplo
        print(Ret_Pregunta06(n2,n1))
            False            -> Valor devuelto por la función en este ejemplo
    '''
    #Tu código aca:
    if ((m1.shape[0] == m2.shape[1]) or (m1.shape[1] == m2.shape[0])):  return True
    else: return False

def Ret_Pregunta07():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar cuál de la siguiente lista de países tuvo mayor generación de
    energía solar (Solar_Generation_TWh) en el año 2019:
        * Argentina
        * Brazil
        * Chile
        * Colombia
        * Ecuador
        * Mexico
        * Peru
    Debe retornar el valor en un dato de tipo string.
    '''
    #Tu código aca:
    df7 = pd.read_csv('datasets\Fuentes_Consumo_Energia.csv',encoding='utf-8')
    df71 = df7[(df7.Year == 2019)].reset_index(drop = True)
    lista = ['Argentina','Brazil','Chile','Colombia','Ecuador','Mexico','Peru']
    solar = []
    for n in lista:
        solar.append([n , float(df71.loc[df71.Entity == n, 'Solar_Generation_TWh'])])
    dfSolar = pd.DataFrame(solar)
    dfSolar.sort_values(by = 1, ascending = False, inplace = True)
    return dfSolar.iloc[0,0]

def Ret_Pregunta08():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de entidades diferentes que están presentes en el dataset, retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df8 = pd.read_csv('datasets\Fuentes_Consumo_Energia.csv',encoding='utf-8')
    df81 = df8['Entity']
    df81.drop_duplicates(inplace = True)
    return df81.count()

def Ret_Pregunta09():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Tabla1_ejercicio.csv" y "datasets/Tabla2_ejercicio.csv".
    Esta función debe retornar: score_promedio_femenino y score_promedio_masculino en formato tupla, teniendo en cuenta que no debe haber registros repetidos.
    '''
    #Tu código aca:
    df91 = pd.read_csv('datasets\Tabla1_ejercicio.csv', delimiter = ';', encoding='utf-8')
    df91.drop_duplicates(inplace = True)
    df92 = pd.read_csv('datasets\Tabla2_ejercicio.csv', delimiter = ';',encoding='utf-8')
    df91.drop_duplicates(inplace = True)   
    df9Pers = df92.values
    df9Pers = df9Pers[:,0]
    for elemento in df9Pers:
        sexodf1 = ((df91.loc[df91['pers_id'] == elemento,'sexo']).values[0])
        df92.loc[df92['pers_id'] == elemento,'Sexo'] = sexodf1
    df92f = df92.loc[df92['Sexo'] == 'F']
    df92m = df92.loc[df92['Sexo'] == 'M']
    dff = df92f.mean()
    dfm = df92m.mean()
    dff = round(float(dff[2]),2)
    dfm = round(float(dfm[2]),2)
    tupla = (dff, dfm)
    return tupla


def Ret_Pregunta10(lista):
    '''
    Esta función recibe como parámetro un objeto de la clase Lista() definida en el archivo Lista.py. Debe recorrer la lista y retornan la cantidad de nodos que posee. Utilizar el método de la clase
    Lista llamado getCabecera()
    Ejemplo:
        lis = Lista()
        lista.agregarElemento(1)
        lista.agregarElemento(2)
        lista.agregarElemento(3)
        print(Ret_Pregunta10(lista))
            3    -> Debe ser el valor devuelto por la función Ret_Pregunta10() en este ejemplo
    '''
    return lista.contarElementos()

class Nodo():
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    def getDato(self):
        return self.__dato

    def getSiguiente(self):
        return self.__siguiente

    def setDato(self, val):
        self.__dato = val

    def setSiguiente(self, val):
        self.__siguiente = val

class Lista():
    def __init__(self):
        self.__cabecera = None

    def agregarElemento(self,dato):
        if (self.__cabecera != None):
            puntero = self.__cabecera
            while(puntero != None):
                if(puntero.getSiguiente() == None):
                    puntero.setSiguiente(Nodo(dato))
                    break
                puntero = puntero.getSiguiente()
        else:
            self.__cabecera = Nodo(dato)

    def contarElementos(self):
        if (self.__cabecera == None):
            return 0
        else:
            contador = 1
            puntero = self.__cabecera
            while(puntero.getSiguiente() != None):
                contador += 1
                puntero = puntero.getSiguiente()
            return contador

    def getCabecera(self):
        return self.__cabecera    