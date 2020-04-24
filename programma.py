import csv, codecs

def main(slovo):
    slovar = otkr_csv("dictionary.csv")
    slovar2 = otkr_csv("Словарь Ожегов.csv")
    slovo2 = function(slovo, slovar)
    return slovo2.upper() +"\n"+ function(slovo2, slovar2)


def otkr_csv(file_csv):  # открытие файла csv
    slovar = codecs.open(file_csv, 'r',
                         encoding='utf-8-sig')  # такая кодировка, просто потому что так сложилось, что в ней удобней
    slovar = csv.DictReader(slovar, delimiter=';')
    return slovar


def function(slovo, slovar):
    per = ""
    for slovzo in slovar:
        if slovo == slovzo['WORD1'].lower():
            per = slovzo['WORD2'].lower()
    if per == "":
        return "--"
    else:
        return per