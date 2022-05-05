import numpy as np
import base64
import  bz2

def chunk(list, n):
        return [list[i:i + n] for i in range(0, len(list), n)]

def preparationBeforeBase64(byteList):
    byteList = chunk(byteList, 24)
    newVariable = 0
    indexOfLastBlock = len(byteList) - 1
    while (byteList[newVariable] != byteList[indexOfLastBlock]):
        byteList[newVariable] = chunk(byteList[newVariable], 6)
        newVariable = newVariable + 1
    if len(byteList[indexOfLastBlock]) == 8:
       byteList[indexOfLastBlock] = byteList[indexOfLastBlock] + "00000000"*2
    elif len(byteList[indexOfLastBlock]) == 16:
        byteList[indexOfLastBlock] = byteList[indexOfLastBlock] + "00000000"
    else:
        ByteAdded = ''
        for i in range(24 - len(byteList[indexOfLastBlock])):
            ByteAdded = ByteAdded + '0'
        byteList[indexOfLastBlock] = byteList[indexOfLastBlock] + ByteAdded
    return byteList

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def encodeBase64(preparedList):
    i = 0
    k = 0
    resultText = ''
    textInLast = ''
    indexOfLastBlock = len(preparedList) - 1
    while (preparedList[i] != preparedList[indexOfLastBlock]):
        innerList = preparedList[i]
        for element in innerList:
            resultText = resultText + base64CodingBinary[element]
            k = k + 1
        i = i + 1
    lastBlock = chunk(preparedList[indexOfLastBlock],6)
    for element in lastBlock:
        textInLast = textInLast + base64CodingBinary[element]
        if base64CodingBinary[element] == 'A':
            textInLast = textInLast.replace(base64CodingBinary[element], "=")
    resultText = resultText + textInLast
    return resultText
base64CodingBinary = {'000000': 'A', '000001': 'B', '000010': 'C', '000011': 'D', '000100': 'E', '000101': 'F', '000110': 'G', '000111': 'H', '001000': 'I',
             '001001': 'J', '001010': 'K', '001011': 'L', '001100': 'M', '001101': 'N', '001110': 'O', '001111': 'P', '010000': 'Q',
              '010001': 'R', '010010': 'S', '010011': 'T', '010100': 'U', '010101': 'V', '010110': 'W', '010111': 'X', '011000': 'Y',
              '011001': 'Z', '011010': 'a', '011011': 'b', '011100': 'c', '011101': 'd', '011110': 'e', '011111': 'f', '100000': 'g',
              '100001': 'h', '100010': 'i', '100011': 'j', '100100': 'k', '100101': 'l', '100110': 'm', '100111': 'n', '101000': 'o',
              '101001': 'p', '101010': 'q', '101011': 'r', '101100': 's', '101101': 't', '101110': 'u', '101111': 'v', '110000': 'w',
              '110001': 'x', '110010': 'y', '110011': 'z', '110100': '0', '110101': '1', '110110': '2', '110111': '3', '111000': '4',
              '111001': '5', '111010': '6', '111011': '7', '111100': '8', '111101': '9', '111110': '+', '111111': '/'}
def main():
    with open("D:\\Третій курс лабораторні роботи\\Комп'ютерні системи\\Лабораторна робота № 1\\test.txt",
          encoding="utf8") as file:
          fileForAnalisis = file.readlines()
    stringForAnalisis = '/n'.join(fileForAnalisis) #не потрібна для bz2
    textForEncoding = text_to_bits(stringForAnalisis)
    preparedList = preparationBeforeBase64(textForEncoding)
    with open("D:\\Третій курс лабораторні роботи\\Комп'ютерні системи\\Лабораторна робота № 1\\testBase64.txt",
          'w') as Base64Writer:
          Base64Writer.writelines(encodeBase64(preparedList))
    #використання вбудованого модуля кодування base64:
    stringForCheck = stringForAnalisis.encode("UTF-8")
    encodedStringForCheck = base64.b64encode(stringForCheck)
    print(encodedStringForCheck)
main()
