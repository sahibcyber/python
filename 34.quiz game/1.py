def yeni_oyuncu():
    texminler = []
    dogru_texminler = 0 
    sualin_nomresi = 1 

    for acarlar in sual:
        print("-----------------------")
        print(acarlar)
        for i in cavablar[sualin_nomresi-1]:
            print(i)
        texminler = input("daxil edin (A, B, C veya D): ")
        texmin = texmin.upper()
        texminler.append (texmin)
        dogru_texminler += suali_yoxla(sual.get(acarlar), texmin)
        sualin_nomresi += 1
    xal_goster(dogru_texminler, texminler)

def suali_yoxla(dogruCavab, bizimtexminimiz):
    if dogruCavab == bizimtexminimiz:
        print("dogru")
        return 1 
    else:
       print("yanlis")
       return 0 
def xal_goster(dogru_cavablar, texminlerimiz):
    print("-----------------------")
    print("netice")
    print("-----------------------")

    print("cavablar: ", end=" ")
    for i in sual:
        print(sual.get(i), end=" ")
    print()

    print("texminlerimiz: ", end=" ")
    for i in texminlerimiz:
        print(i, end=" ")
    print()

    derece = int((dogru_cavablar/len(sual)) * 100)
    print("dogru texmin derex=cemiz: " + str(derece) + "%")

def yeniden_oyna():
    sorgu = input("yeniden oynamaq isteyirsen mi? (beli / xeyr) : ").upper()
    if sorgu == "BELI":
        return True
    else:
        return False
    



sual = {
    "python dilini kim yaradib? " : "A",      "python necenci ile yaranib? " : "B",       "python adi, hansi komedi klubun adindan ilhamlanmisdir? " : "C",   "dunya yuvarlaqdir mi? " : "A"
}
cavablar = [
    ["A. Guido van rossum",          "B. Elon musk",          "C. Bill Gates",            "D. Mark Zuckerburg"],
    ["A. 1989",                      "B. 1991",               "C. 2000",                  "D. 2016"], 
    ["A. Lonely Ialand",             "B. Simosh",             "C. Monty python",          "D. SNL"],
    ["A. True",                      "B. False",              "C. Sometimes",             "D. What's Earth"],
]

yeni_oyun()


while yeniden_oyna():
    yeniden_oyun()


print("sagol!!!!!!") 