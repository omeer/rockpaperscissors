from pyfiglet import Figlet
from time import sleep
import random
#2 kisilik tas kagit makas oyunu kodluyoruz

info = Figlet(font='big')
print(info.renderText('Tas Kagit Makas\nOyunu'))

def sonuctext():
	info = Figlet(font='big')
	print(info.renderText('Sonuc'))
def puantext():
	info = Figlet(font='big')
	print(info.renderText('Puanlar'))
def secimtext():
	info = Figlet(font='big')
	print(info.renderText('Secim'))

#oyun hakkında bilgi verelim
print("""
----------------OYUN HAKKINDA BİLGİLER------------------

Taş için 'T' harf tuşuna basmanız yeterlidir.
Makas için 'M' harf tuşuna basmanız yeterlidir
Kağıt için 'K' harf tuşuna basmanız yeterlidir.
  """)

def computer_random():
	number=random.randint(1,3)
	if number==1:
		return "T"
	elif number==2:
		return "K"
	else:
		return "M"

bilgpuan=0
benimpuan=0
while True:
	print("_____________________________________")
	print("\n")
	secim=input("Tas Kagit Makas ? :")
	print("_____________________________________")
	secimtext()
	print("-------------------------------------")
	print("Sizi Seçiminiz : {} ".format(secim))
	print("\n")
	computerrandom=computer_random()
	print("Bilgisayar     : ",computerrandom)
	print("-------------------------------------")
	sonuctext()
	print("##############################")
	if secim==computerrandom:
		print("BERABERE")
		print("##############################")
		print("\n")
		puantext()
		print("Bilgisayar Puanı :{}".format(bilgpuan))
		print("Benim Puanım     :{}".format(benimpuan))


	elif secim=='T' and computerrandom=="K":
		print("Bilgisayar Kazandi...")
		print("##############################")
		print("\n")
		puantext()
		bilgpuan=bilgpuan+1
		print("Bilgisayar Puanı :{}".format(bilgpuan))
		print("Benim Puanım     :{}".format(benimpuan))


	elif secim=='T' and computerrandom=="M":
		print("Siz Kazandiniz...")
		print("##############################")
		print("\n")
		puantext()
		benimpuan=benimpuan+1
		print("Bilgisayar Puanı :{}".format(bilgpuan))
		print("Benim Puanım     :{}".format(benimpuan))

	elif secim=='M' and computerrandom=="K":
		print("Siz Kazandiniz...")
		print("##############################")
		print("\n")
		puantext()
		benimpuan=benimpuan+1
		print("Bilgisayar Puanı :{}".format(bilgpuan))
		print("Benim Puanım     :{}".format(benimpuan))

	elif secim=='M' and computerrandom=="K":
		print("Siz Kazandiniz...")
		print("##############################")
		print("\n")
		puantext()
		benimpuan=benimpuan+1
		print("Bilgisayar Puanı :{}".format(bilgpuan))
		print("Benim Puanım     :{}".format(benimpuan))

	elif secim=='K' and computerrandom=="T":
		print("Siz Kazandiniz...")
		print("##############################")
		print("\n")
		puantext()
		benimpuan=benimpuan+1
		print("Bilgisayar Puanı :{}".format(bilgpuan))
		print("Benim Puanım     :{}".format(benimpuan))
	elif secim=='K' and computerrandom=="M":
		print("Bilgisayar Kazandi...")
		print("##############################")
		print("\n")
		puantext()
		print("Bilgisayar Puanı :{}".format(bilgpuan))
		print("Benim Puanım     :{}".format(benimpuan))

	else:
		print("Yanlış Tuşlama Girdiniz..!")
		

		




