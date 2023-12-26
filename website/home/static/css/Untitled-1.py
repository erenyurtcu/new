sifrelimsj=input("şifrelenecek mesajı giriniz:")
anahtar=int(input("şifrenin anahtarını girin:"))
l2=[]
alfabe=["a","b","c","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","t","u","ü","v","y","z"]
for i in sifrelimsj:
    for c in alfabe:
        if i==c :
             kacinci=(alfabe.index(i)+anahtar)
             x=alfabe.pop(kacinci)