# finaly - kod ister xeta versin ister xeta vermesin, yenede en sonda, finalda nese 

# ekrana yazdirmaq isteyirikse yaxud her hansisa bir kod ise salmaq isteyirikse finally kod 

# blokunan istifade edirik

try:
    bolunen = int(input("bir deyer daxiil edin"))
    bolen = int(input("bir eded daxil edin"))
    netice = bolunen / bolen  
except ZeroDivisionError as e:
    print(e)
    print("sifira bolmek olmaz")
except ValueError as e:
    print(e)
    print("string-e bolmek olmaz")
except Exception as e:
    print(e)
    print("bir xeeta var") 
else:
    print("netice")
finally:
    print("bura her zaman isleyecek hissedir") 



    