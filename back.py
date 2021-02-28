import random
from TimeZoneList import DictTimeZone
import math

# для живого поиска 
with open("RU.txt", encoding='utf-8') as file:
    arRAY = []
    arrarow = []
    for row in file:
        a = row.split()
        arRAY.append(a[0])
        arrarow.append(a)
    
# функция для возвращения информации об одном городе    
def ReturnGeodata(geonamied):
    with open("RU.txt", encoding='utf-8') as file:
        for row in file:
            PreArray = []
            array1 = []
            array12 = []
            PreArray+=row.split()
            if str(geonamied) == PreArray[0]:
                array1+=row.split()
                s=''
                array12+=array1[:-10]
                del array12[0]
                for i in array12:
                    s+=i+"   "
                return "Geonamied: {0} | Town names: {1} | Latitude: {2} | Longitude: {3} | Population: {4} | TimeZone: {5} | Modification Date: {6}".format(array1[0], s, array1[-10], array1[-9], array1[-3], array1[-2], array1[-1])


# функция для возвращения информации о двух городах и о различии временных зон
def ReturnGeodataTwoTowns(geonamied1, geonamied2):
    with open("RU.txt", encoding='utf-8') as file:
        
        WestPoint = ''
        a = ''
        b=0
        names = []
        array1 = []
        array2 = []
        FinalArray1 = []
        FinalArray2 = []

        # заполнения массива элементами из строки файла
        for row in file:                    
            if geonamied1 in row:
                array1.append(row.split())
            if geonamied2 in row:
                array2.append(row.split())

        # нахождение города с максимальным кол-ыом населения для первого города
        if len(array1) > 1:                  
            for i in range(len(array1)-1):
                MaxArray1 = array1[i][-5]
                if MaxArray1 < array1[i+1][-5]:
                    MaxArray1 = array1[i+1]
                else:
                    MaxArray1 = array1[0]
            FinalArray1 = MaxArray1        
        else:
            FinalArray1 = array1[0]
           
        # нахождение города с максимальным кол-ыом населения для второго города
        if len(array2) > 1:  
            for i in range(len(array2)-1):
                MaxArray2 = array2[i][-5]
                if MaxArray2 < array2[i+1][-5]:
                    MaxArray2 = array2[i+1]
                else:
                    MaxArray2 = array2[0]
            FinalArray2 = MaxArray2        
        else:
            FinalArray2 = array2[0]

        # сравнение временных зон
        if FinalArray1[-2] == FinalArray2[-2]:
            a+= "Временная зона одинаковая"
        else:
            b += int(math.fabs(int(DictTimeZone[FinalArray1[-2]])-int(DictTimeZone[FinalArray2[-2]])))
            a+= "Временная зона отличается на "+str(b)

        #какой город севернее
        if FinalArray1[-10] > FinalArray2[-10]:
            WestPoint += 'Первый город севернее'
        elif FinalArray1[-10] < FinalArray2[-10]:
            WestPoint+='Второй город севернее'

    Town1 = "Geonamied: {0} | Town name: {1} | Latitude: {2} | Longitude: {3} | Population: {4} | TimeZone: {5} | Modification Date: {6}".format(FinalArray1[0], geonamied1, FinalArray1[-10], FinalArray1[-9], FinalArray1[-3], FinalArray1[-2], FinalArray1[-1])
    Town2 = "Geonamied: {0} | Town name: {1} | Latitude: {2} | Longitude: {3} | Population: {4} | TimeZone: {5} | Modification Date: {6}".format(FinalArray2[0], geonamied2, FinalArray2[-10], FinalArray2[-9], FinalArray2[-3], FinalArray2[-2], FinalArray2[-1])
    ArrayList = []
    ArrayList.append(Town1)
    ArrayList.append(Town2)
    ArrayList.append(a)
    ArrayList.append(WestPoint)
    return ArrayList



def ReturnFewTowns(number):
    towns = []
    i=0
    for i in range(int(number)):
        towns.append(arrarow[i])
        
    
    return towns
        



    