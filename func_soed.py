import csv, codecs

def main():
    slovar = otkr_csv("dictionary.csv")
    print("Что вы хотите перевести? ")
    slovo = input().lower()
    slovar2 = otkr_csv("Словарь Ожегов1.csv")
    slovo2 = function(slovo, slovar)
    function(slovo2, slovar2)
    
    
def otkr_csv(file_csv): # открытие файла csv
    slovar = codecs.open(file_csv, 'r', encoding = 'utf-8-sig')  # такая кодировка, просто потому что так сложилось, что в ней удобней
    slovar = csv.DictReader(slovar, delimiter = ';')
    # for row in slovar:  -- можно напечатать и посмотреть, как выглядит словарь
        # print(row)  (на всякий случай)
    return slovar

def function(slovo, slovar): 
    for slovzo in slovar:
        if slovo == slovzo['WORD1'].lower():
            print(slovzo['WORD2'].lower())
            return(slovzo['WORD2'].lower())

if __name__ == "__main__":
    main()
    
''' остается проблема с неодносложными переводами,
    например: detectivity -- обнаруживающая способность, в словаре Ожегова,
    конечно, нет в 1-ой колонке двухсложных словосочетаний...
    хотя в принципе, какое ещё к этому всему толкование нужно?'''
