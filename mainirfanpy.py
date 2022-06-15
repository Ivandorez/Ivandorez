
class menubakso
    def __init__(self, menubakso):
       self.menubakso = menubakso


p1 =menubakso("bakso janda : Rp 15.000")
p2 =menubakso("bakso beranak : RP 15.000")
p3 =menubakso("bakso mercon : Rp 12.000")

print('selamat menikmati!')
while True:
    print('---menu---')
    print('1.bakso janda')
    print('2.bakso beranak')
    print('3.bakso mercon')

    menu = int(input('Pilih Menu: '))
    jumlahpesan=int(input("masukkan jumlah pesanan : "))


    if menu == 1:
        print(p1.bakso)
        harga = 15.000 * jumlahpesan
        print("total yang harus di bayar Rp." +str(harga))
    
    elif menu == 2:
        print(p2.bakso)
        harga = 15.000 * jumlahpesan
        print("total yang harus di bayar Rp." +str(harga))
    
    elif menu == 3:
        print(p3.bakso)
        harga = 12.000 * jumlahpesan
        print("total yang harus di bayar Rp." +str(harga))
        
      
