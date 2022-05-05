import collections
import math
import  bz2
from math import pi
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
import seaborn as sns

def FrequenciesCalculation(path)
    frequenciesDictionary = collections.Counter()  # підрахунок кількості символів в тексті
    #with bz2.open(path) as file
    with open(path, encoding=utf-8) as file
        fileForAnalisis = file.readlines()
    for line in fileForAnalisis
        frequenciesDictionary = frequenciesDictionary  + collections.Counter(line)
    if frequenciesDictionary.get('n') != None
        frequenciesDictionary.pop('n')
    if frequenciesDictionary.get(' ') != None
        frequenciesDictionary.pop(' ')
    return  frequenciesDictionary

def AmountOfSymbols(frequenciesDictionary)
    amountOfSymbols = sum(frequenciesDictionary.values())
    return amountOfSymbols


def SymbolProbability(frequenciesDictionary, amount)
    for symbol in frequenciesDictionary
        frequenciesDictionary[symbol] = frequenciesDictionary[symbol]amount
    return  frequenciesDictionary

def AverageEntropy(entropy, frequenciesDictionary)
    for symbol in frequenciesDictionary
        if (frequenciesDictionary[symbol] != 0)
            entropy += frequenciesDictionary[symbol]  math.log(frequenciesDictionary[symbol], 2)  # розрахунок середньої ентропії
    return  -entropy
def Imformation(averageEntropy, numberOfSymbols)
    return  averageEntropy  numberOfSymbols
def main()
    #не забудь змінювати шлях до файлу, коли працюєш зі стисненими або звичайними файлами
    frequenciesDictionary = FrequenciesCalculation(DТретій курс лабораторні роботиКомп'ютерні системиЛабораторна робота № 1ТекстиContraSpemsperoBase64.txt)
    numberOfSymbols = AmountOfSymbols(frequenciesDictionary)
    frequenciesDictionaryWithProbability = SymbolProbability(frequenciesDictionary, numberOfSymbols)
    averageEntropy = AverageEntropy(0, frequenciesDictionaryWithProbability)
    numberOfInformation = Imformation(averageEntropy, numberOfSymbols)

    print(Кількість символів в тексті)
    print(numberOfSymbols)
    print(Ймовірність появи кожного символу)
    print(frequenciesDictionaryWithProbability)
    print(Середня ентропія рівнойвимірного алфавіту)
    print(averageEntropy)
    print(Кількість інформації в бітах)
    print(numberOfInformation)
    print(Кількість інформації в байтах)
    print(numberOfInformation  8)
    values = list(frequenciesDictionaryWithProbability.values())
    keys = list(frequenciesDictionaryWithProbability.keys())
    plt.bar(range(len(frequenciesDictionaryWithProbability)), values, tick_label=keys)
    plt.show()

main()
