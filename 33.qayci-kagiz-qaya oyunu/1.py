import random

# eger her defe duymesine basaraq kodu ise salmaq istemirikse onda burda butun kodlari sonsuz gonsune saliriq 
#bes sonsuz donguden ne vaxt cixiriq ?

while True:
    secmek = ["qayci", "kagiz", "qaya"]
    komputer = random.choice(secmek)

    oyuncu = None
    while oyuncu not in secmek:
        oyuncu = input("qayci, kagiz yoxsa qaya ?: ").lower()

    if oyuncu == komputer:
        print("komputer: ", komputer)
        print("oyuncu: ", oyuncu)
        print("beraber!")    

    elif oyuncu == "qaya":
        if komputer == "kagiz":
            print("komputer: " , komputer)
            print("oyuncu: ", oyuncu)
            print("sen uduzdun!")
        if komputer == "qayci":
            print("komputer: ", komputer)
            print("oyuncu: ", oyuncu)
            print("sen uddun!")

    elif oyuncu == "qayci":
        if komputer == "qaya":
            print("komputer: ", komputer)
            print("oyuncu: ", oyuncu)
            print("sen uduzdun!")
        if komputer == "kagiz":
            print("komputer: ", komputer)
            print("oyuncu", oyuncu)
            print("sen uddun!")    
    elif oyuncu == "kagiz":
        if komputer == "qayci":
            print("komputer: ", komputer)
            print("oyuncu: ", oyuncu)
            print("sen uduzdun!")
        if komputer == "qaya":
            print("komputer: ", komputer)
            print("oyuncu: ", oyuncu)
            print("sen uddun!")

    yeniden_oynuyaqmi = input("yeniden oynamaq isteyirsenmi? (beli/xeyr): ").lower()
    if yeniden_oynuyaqmi != "beli":
        break