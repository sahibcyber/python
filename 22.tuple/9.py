# eger yenede tuple - in deyerine deyismek isteyirikse onda ilk once bu tuple - i

#lsit - e cevirmek lazimdir sonra ise geri tuple - a

telebe =  ("alexs", 21, "male", "green","baku" )

siyahi = list(telebe)

siyahi[0] = 'bob'

yenitelebe = tuple(siyahi)

print(yenitelebe)