"""
Oyun Açıklaması:
- Gemiler oyun alanına dikey veya yatay (her gemi bağımsız olarak düşünülecek, yani bir gemi 
dikey yerleşirken bir diğeri yatay olabilir) şekillerde; oyun alanının dışına çıkmayacak ve üst 
üste konumlarda olmayacak şekillerde yerleşir.  
- Gemiler oyun alanına rasgele yerleştirilecektir, gemi yönleri de (dikey-yatay) rasgele olacaktır.  
- Gemiler oyun alanına yerleştirildikten sonra kullanıcıya oyun alanı 2 mod ile gösterilebilecektir 
 
1- Gizli mod: Kullanıcı gemilerin nerde olduğunu bilmeyecektir.  
2- Açık mod: Gemilerin yerleri oyun alanında görünecektir. 
- Oyun alanında açılmayan kareler (hücreler) ? ile gösterilecektir. Karavanalar (yani yapılan seçim boş ise bir gemi parçasını tutturamadıysa) * ile gösterilecektir. 
İsabetli atışların olduğu kareler (yapılan seçim geminin bir kısmını vurdu ise) x ile gösterilecektir. 
- Yapılan her atış için kullanıcıya mesaj verilecektir. Atış isabetli ise “Tebrikler bir gemi 
vurdunuz”, isabetsiz ise “Maalesef isabet edemediniz” şeklinde mesajlar olacaktır.
Ayrıca isabetli bir atış yapıldığında söz konusu geminin tüm bölümleri vuruldu ise ek olarak “Tebrikler bir gemi batırdınız” şeklinde mesaj verilecektir.
- Yapılan her atış için oyun alanının görünümü güncellenecektir 
- Daha önce hedef alınan bir konum seçilirse kullanıcıya başka bir konum seçmesi için bilgi verilecektir. 
- Kullanıcıya atış hakkı olarak oyun alanı büyüklüğünün 1/3’ü kadar hak verilecektir. 
Örnek: 
10x10 (100) büyüklüğünde bir alan için atış hakkı = 100/3 = 33 olacaktır.  
- Oyun iki şekilde sona erecektir. Kullanıcı tüm haklarını kullanır ve gemilerin hepsini batıramaz. 
Bu durumda “Maalesef kaybettiniz” mesajı verilir. Diğer durumda ise hakları sona ermeden tüm gemiler batırılır. 
Bu durumda kullanıcının puanı hesaplanır ve “Tebrikler 12 puan ile oyunu kazandınız” şeklinde mesaj verilir. 
Oyun puanı toplam haktan yapılan atışlar çıkarılarak hesaplanır.
- Oyun bittikten sonra kullanıcıya yeni oyun oynamak için veya çıkmak için tercih sunulur. 
"""


import random

hata=0
gemi_say=0
bomba_20=[]
puan_say=0


while True:
    while True:
        satir=int(input("\nBoyut girin (en az 10): "))
        if satir<10:
            print("Geçersiz boyut girdiniz, yeniden deneyin..\n")
            continue
        else:
            break
    kalan_hata = satir*satir//3
    deniz=[]
    for i in range(satir):
        deniz.append([])
        for j in range(satir):
            deniz[i].append("?")
    

    mod=input("\nMod Girin: (Gizli: '1' or açık: '2') ")

    gemi_sayisi=20      

    AB_Dizi=[]
    sayac=0
    kontrol=0
    while sayac<gemi_sayisi:
        kontrol+=1
        rand_satir=random.randint(0 ,satir -1)
        rand_sutun=random.randint(0 ,satir -1)
        if deniz[rand_sutun][rand_satir]!='X':
            deniz[rand_sutun][rand_satir]='X'
            abList=[rand_sutun, rand_satir]
            AB_Dizi.append(abList)
            sayac+=1

    puan=0

    kontrol2=True
    while  kontrol2:
        if mod=="1":
            print("{} hakkınız kaldı\n".format(kalan_hata))
            print("    ",*range(satir))   
            print("   ", "_ "*(satir+1))
            

            for r in range(satir):
                oyun_alani=[]
                for c in range(satir):
                    if mod=="1" and deniz[c][r]=="X":
                        oyun_alani.append("?")
                    else:
                        oyun_alani.append(deniz[c][r])
                print(r, " |",*oyun_alani, "|")

            print("   ", "_ "*(satir+1))
        elif mod=="2":
            print("\n----------------------AMİRAL BATTI----------------------\n")
            print("    ",*range(satir))
            print("   ", "_ "*(satir+1))

            for r in range(satir):
                oyun_alani=[]
                for c in range(satir):
                    if mod=="1" and deniz[c][r]=="X":
                        oyun_alani.append("?")
                    else:
                        oyun_alani.append(deniz[c][r])
                print(r, " |",*oyun_alani, "|")

            print("   ", "_ "*(satir+1))
            mod=input("\nOyuna geri dönmek için '1' yaz: ")
            continue
        else:
            mod=input("\nYanlış girdiniz, lütfen yeniden deneyin: (gizli mod: '1' or açık mod: '2') ")
            continue
        while True: 
            satir_giris=int(input("\nSatir: "))
            sutun_giris=int(input("\nSütun: "))
            if satir_giris>satir or sutun_giris>satir or satir_giris<0 or sutun_giris<0:
                print("Hatalı giriş yaptınız lütfen tekrar deneyin..")
                continue
                
            else:
                break
                
        
        print("\n")
        if satir_giris>=satir or sutun_giris>=satir:
            print("Rakam çok büyük")
            hata=1
        elif deniz[sutun_giris][satir_giris]!="?" and deniz[sutun_giris][satir_giris]!="X":
            print("Başka bir konum seçin")

        if deniz[sutun_giris][satir_giris]=="X":
            gemi_say += 1
            oyun_alani.append("X")
            bomba_20.append("X")
            puan_say+=1
            print("--------------------------------------------")
            print("Tebkrikler, isabetli atış")
    
        else: 
            deniz[sutun_giris][satir_giris]="*"
            oyun_alani.append("*")
            kalan_hata-=1
            print("--------------------------------------------")
            print("Maalesef isabet ettiremediniz")
        
        if kalan_hata==0:
            print("BOOOM!!!!\nKAYBETTİN\n")
            print("\n----------------------AMİRAL BATTI----------------------\n")
            print("\t",*range(satir))
            print("   ", "_ "*(satir+1))

            for r in range(satir):
                oyun_alani=[]
                for c in range(satir):
                    oyun_alani.append(deniz[c][r])
                print(r, " |",*oyun_alani, "|")

            print("   ", "_ "*(satir+1))
            break
        elif len(bomba_20)==20:
            print("TEBRİKLER!\nKAZANDIN\nPUANIN: {}".format(kalan_hata-puan_say))
            print("\n----------------------AMİRAL BATTI----------------------\n")
            print("Tebrikler {} atışta tüm gemileri batırdınız".format(puan_say-(20-kalan_hata)))
            print("\t",*range(satir))
            print("   ", "_ "*(satir+1))

            for r in range(satir):
                oyun_alani=[]
                for c in range(satir):
                    oyun_alani.append(deniz[c][r])
                print(r, " |",*oyun_alani, "|")

            print("   ", "_ "*(satir+1))
            break
    end=input("\nYeni oyun için 'n', çıkış için 'e' tıklayın: ")
    if end=="n":
        continue
    elif end=="e":
        break
