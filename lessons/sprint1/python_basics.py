""" company_name = "Backend AI Journey"

project_name = "CRM API"



developer_name = input("Enter your name: ")


if developer_name == "":
    print("Registration failed. Name cannot be empty.")
else:
    print("Registration successful.")
    print(f"Welcome {developer_name}") """

"""developer_name = input("Enter your name: ")
age = input("Enter your age: ")

is_adult = int(age) >= 18"""

"""age = input("Enter your age: ")
is_adult = int(age) >= 18
print(is_adult)"""

"""age = input("Enter your age: ")
is_adult = int(age) >= 18
if is_adult:
    print("Registration successful.")
if not is_adult:
    print("Registration failed.")"""

"""name = input("Enter your name: ")
is_name_valid = name != ""
if not is_name_valid:
    print("Name cannot be empty")"""

"""name = input("Enter your name: ")
age = input("Enter your age: ")
if is_name_valid := name != "":
    if is_adult := int(age) >= 18:
        print("Registration successful.")
    else:
        print("Registration Failed")"""


"""name = input("Enter your name: ")
age = input("Enter your age: ")

is_name_valid = name != ""
is_adult = int(age) >= 18

if is_name_valid and is_adult:
    print("Registration succesful.")
else:
    print("Registration failed.")"""


"""username = input("Enter your username: ")
age = input("Enter your age: ")

is_username_valid = username != ""
is_adult = int(age)>= 18

if is_username_valid and is_adult:
    print("Login successful.")
else:
    print("Login failed.")"""

"""is_premium = True
age = input("Enter your age: ")
name = input("Enter your name: ")
is_adult = int(age) >= 18
is_name_valid = name != ""
if is_adult and is_premium and is_name_valid:
    print("Registration successful.")
else:
    print("Registration failed.")"""

"""is_premium = False
is_admin = True

if is_premium or is_admin:
    print("Access granted.")
else:
    print("Access denied.")"""

"""age = input("Enter your age: ")
if 18 <= int(age) <=65:
    print("You are an adult.")
else:
    print("You are not an adult.")"""

"""is_email_verified = True
is_name_valid = True

age = input("Enter your age: ")
is_adult = int(age) >= 18
name =input("Enter your name: ") 
is_name_valid = name != ""
if is_name_valid and is_adult and is_email_verified:
    print("Campaign access granted.")
else:
    print("Campaign access denied.")"""

"""name = input("Enter your name: ")
age = input("Enter your age: ")

is_email_verified = True

is_name_valid = name != ""
is_adult = int(age) >= 18

if is_name_valid and is_adult and is_email_verified:
    print("Campaign access granted.")
else:
    print("Campaign access denied.")"""


"""is_admin = False
is_premium = True
is_suspended = False

if (is_admin or is_premium) and not is_suspended:
    print("Access granted.")
else:
    print("Login Failed.")"""

"""is_admin= True
is_active = True
is_email_verified = True

has_permission = is_admin and is_active and is_email_verified
if has_permission:
    print("Access granted.")
else:
    print("Access denied.")"""

"""is_admin = False
is_manager = True
is_active = True

dashboard_access = (is_admin or is_manager) and is_active
if dashboard_access:
    print("Dashboard opened.")
else:
    print("Access denied.")"""

"""is_admin = False
is_premium = True
is_email_verified = True
is_suspended = False

name = input("Enter your name: ")
age = input("Enter your age: ")

is_name_valid = name != ""
is_age_valid = 18 <= int(age) <= 65

can_create_campaign = (is_name_valid
                       and is_age_valid
                       and (is_admin or is_premium)
                       and not is_suspended
                       and is_email_verified
                    )
if can_create_campaign:
    print("Campaign created successfully.")
else:
    print("Campaign creation failed.")"""





"""day 3"""


"""role = input("Enter your role: ")
if role == "Admin":
    print("Welcome Admin")
elif role == "Manager":
    print("Welcome Manager")
elif role == "Employee":
    print("Welcome Employee")
else:
    print("Invalid role")"""

"""employees = [
    "Ali",
    "Veli",
    "Ayşe"
]
employees.append("Fatna")
employees.append("Can")
print(employees[-1])"""

"""
employees = ["Ali", "Veli", "Ayşe"]

employees.append("Fatma")   # Ekle
print(employees[0])         # Oku
print(employees[-1])        # Son eleman
print(len(employees))       # Kaç eleman var?
print(employees.count("Ali"))  # Kaç tane Ali var?

"""

"""
emails = [
    "ali@test.com",
    "veli@test.com",
    "ayse@test.com"
]
for email in emails:
    print(f"Mail gönderiliyor: {email}")

"""

"""emails = [
    "ali@test.com",
    "vip@firma.com",
    "veli@test.com",
    "admin@firma.com",
    "ayse@test.com"
]
for email in emails:
    if email.endswith("@firma.com"):
        print(f"Mail gönderiliyor: {email}")"""

"""emails = [
    "ali@test.com",
    "vip@firma.com",
    "veli@test.com",
    "admin@firma.com",
    "ayse@test.com"
]

for email in emails:
    if email.endswith("@firma.com"):
        print(f"Firma kullanicisi: {email}")
    else:
        print(f"Normal kullanici: {email}")"""



"""sent_count = 0
missed_emails = 0

for email in emails:
    if email.startswith("test"):
        print(f"Test hesabı atlandı. {email}")
        missed_emails += 1
    else:
        print(f"Email gönderildi: {email}")
        sent_count +=1

print(f"Toplam gönderilen mail: {sent_count}")
print(f"Atlanan mail: {missed_emails}")"""




"""sent_count = 0
skipped_count = 0

for email in emails:
    if email.startswith("test"):
        print (f"Atlandı {email}")
        skipped_count +=1
    else:
        email.endswith(".net")
        print (f"Atlandı {email}")
else:
    print (f"Mail gönderildi {email}")
    sent_count +=1

print(f"toplam gönderilen mail: {sent_count}")
print(f"atlanan mail: {skipped_count}")"""





"""sent_count = 0
skipped_count = 0

for email in emails:
    if email.startswith("test") or email.endswith(".net"):
        print (f"Atlandı: {email}")
        skipped_count +=1
    else:
        print (f"Gönderildi: {email}")
        sent_count +=1

print (f"Atlanan mail: {skipped_count}")
print (f"Gönderilen mail: {sent_count}")"""

"""emails = [
    "ali@test.com",
    "",
    "test1@test.com",
    "veli@test.com",
    "",
    "ayse@test.com"
]

sent_count = 0
skipped_count = 0
invalid_count = 0"""

"""for email in emails:
    if email == "":
        print("Geçersiz kayıt")
        invalid_count += 1
    else:
        if email.startswith("test"):
            print(f"Atlandı: {email}")
            skipped_count += 1
        else:
            print(f"Gönderildi: {email}")
            sent_count += 1

print(f"Gönderilen Mail: {sent_count}")
print(f"Atlanan Mail: {skipped_count}")
print(f"Geçersiz Kayıt: {invalid_count}")"""

"""for email in emails:
    if email == "":
        invalid_count += 1
        continue
    if email.startswith("test"):
        print(f"Atlandı: {email}")
        skipped_count +=1
    else:
        print(f"Gönderildi: {email}")
        sent_count +=1"""

"""karar verdik : if
    tekrarladık : for
    saydık : counter
    bazı kayıtları atladık : continue
"""
    
"""emails = [
    "ali@test.com",
    "",
    "test1@test.com",
    "veli@test.com",
    "",
    "ayse@test.com"
]
send_list = [

]

for email in emails:
    if email == "":
        continue
    if email.startswith("test"):
        continue
    send_list.append(email)

print(send_list)"""



"""Fonksiyonlar"""

"""def selam_ver():
    print("Merhaba Oğuzhan")

selam_ver()"""

"""def selam_ver(isim):
    print(f"Merhaba {isim}")
selam_ver("Oğuzhan")
selam_ver("Ahmet")"""

"""def bes():
    return 5
x = bes()
print(x)"""
"""def bes():
    print(5)
x = bes()
print(x)"""


"""emails = [
    "ali@test.com",
    "",
    "test1@test.com",
    "veli@test.com",
    "",
    "ayse@test.com"
]"""
"""def filtrele(emails):
    send_list = []

    for email in emails:
        if email == "":
            continue

        if email.startswith("test"):
            continue

        send_list.append(email)

    return send_list

send_list = filtrele(emails)
print(send_list)"""
   





"""def mail_bilgi():
    print("Mail gönderimi başladı.")

mail_bilgi()
mail_bilgi()"""

"""def hosgeldin(isim):
    print(f"Hoşgeldin {isim}")

hosgeldin("Oğuzhan")
hosgeldin("Ahmet")
hosgeldin("Ayşe")"""

"""def firma_adi():
    return "Related Digital"
firma = firma_adi()
print(firma)"""

"""def ulke():
    return "Türkiye"
ulke_adi = ulke()
print(ulke_adi)"""


"""def topla(sayi):
    return sayi + 5
sonuc = topla(10)
print(sonuc)"""


"""def yas_kontrol(yas):
    if yas >= 18:
        return "Onaylandı"
    else:
        return "Reddedildi"
sonuc1 = yas_kontrol(18)
sonuc2 = yas_kontrol(15)
print(sonuc1)
print(sonuc2)"""

"""def mail_kontrol(mail):
    if mail.endswith("@gmail.com"):
        return "Geçerli Mail"
    else:
        return "Geçersiz Mail"
sonuc = mail_kontrol("oguzhan@gmail.com")
sonuc2 = mail_kontrol("test@hotmail.com")
print(sonuc)
print(sonuc2)"""


"""def indirim_hesapla(tutar):
    if tutar >= 1000:
        return tutar - (tutar * 10 / 100)
    else:
        return tutar

indirim = indirim_hesapla(1500)
print(indirim)"""




"""mailler = [
    "ali@gmail.com",
    "veli@hotmail.com",
    "ayse@gmail.com",
    "mehmet@yahoo.com"
]

gmail_mailleri = [

]

for mail in mailler:
    if mail.endswith("gmail.com"):
        gmail_mailleri.append(mail)

print(gmail_mailleri)"""


"""def gmail_sayisi(mailler):
    sayac = 0
    for mail in mailler:
        if mail.endswith("@gmail.com"):
            sayac += 1
    return sayac      

sonuc = gmail_sayisi(mailler)
print(sonuc)"""

"""mails = [
    "ali@gmail.com",
    "veli@hotmail.com",
    "ayse@gmail.com",
    "mehmet@yahoo.com",
    "fatma@gmail.com",
    "can@gmail.com"
]
gmail_users = []
            
def gmailUsers(mail):
    counter = 0
    for mail in mails:
        if mail.endswith("@gmail.com"):
            gmail_users.append(mail)
            counter += 1
    return counter
results = gmail_users(mails)
print(results)
"""""  """""""""""""""""""""
mails = [
    "ali@gmail.com",
    "veli@hotmail.com",
    "ayse@gmail.com",
    "mehmet@yahoo.com",
    "fatma@gmail.com",
    "can@gmail.com"
]

def gmail_users(mailler):
    gmail_listesi = []

    for mail in mailler:
        if mail.endswith("@gmail.com"):
            gmail_listesi.append(mail)

    return gmail_listesi


sonuc = gmail_users(mails)

print(sonuc)
print(len(sonuc))"""

"""kullanicilar = [
    {"isim": "Ali", "aktif": True},
    {"isim": "Veli", "aktif": False},
    {"isim": "Ayşe", "aktif": True},
    {"isim": "Mehmet", "aktif": False},
    {"isim": "Fatma", "aktif": True}
]

def aktif_kullanicilar(kullanicilar):
    only_active = []

    for kullanici in kullanicilar:
        if kullanici["aktif"]:
            only_active.append(kullanici)
    return only_active
sonuc= aktif_kullanicilar(kullanicilar)
print(sonuc)"""

"""kullanicilar = [
    {"isim": "Ali", "mail": "ali@gmail.com", "aktif": True},
    {"isim": "Veli", "mail": "veli@hotmail.com", "aktif": True},
    {"isim": "Ayşe", "mail": "ayse@gmail.com", "aktif": False},
    {"isim": "Fatma", "mail": "fatma@gmail.com", "aktif": True},
    {"isim": "Can", "mail": "can@yahoo.com", "aktif": True}
]

def aktif_gmail(kullanicilar):
    activeAndGmail = []

    for kullanici in kullanicilar:
        if kullanici["aktif"] and kullanici["mail"].endswith("@gmail.com"):
            activeAndGmail.append(kullanici["isim"])
    return activeAndGmail
sonuc = aktif_gmail(kullanicilar)
print(sonuc)"""

"""kullanicilar = [
    {"isim": "Ali", "mail": "ali@gmail.com", "aktif": True},
    {"isim": "Veli", "mail": "veli@hotmail.com", "aktif": True},
    {"isim": "Ayşe", "mail": "ayse@gmail.com", "aktif": False},
    {"isim": "Fatma", "mail": "fatma@gmail.com", "aktif": True},
    {"isim": "Can", "mail": "can@yahoo.com", "aktif": True}
]

def aktif_sayisi(kullanicilar):
    counter = 0
    for kullanici in kullanicilar:
        if kullanici["aktif"]:
            counter += 1
    return counter
sonuc = aktif_sayisi(kullanicilar)
print(sonuc)"""

"""kullanicilar = [
    {"isim": "Ali", "mail": "ali@gmail.com", "aktif": True},
    {"isim": "Veli", "mail": "veli@hotmail.com", "aktif": True},
    {"isim": "Ayşe", "mail": "ayse@gmail.com", "aktif": False},
    {"isim": "Fatma", "mail": "fatma@gmail.com", "aktif": True},
    {"isim": "Can", "mail": "can@yahoo.com", "aktif": True}
]

def kullanici_bul(kullanicilar, isim):
    for kullanici in kullanicilar:
        if  kullanici["isim"] == isim:
            return kullanici
        
    return  "Kullanıcı Bulunamadı"
    
sonuc =  kullanici_bul(kullanicilar, "Ayşe")
print(sonuc)"""

kullanicilar = [
    {"isim": "Ali", "mail": "ali@gmail.com", "aktif": True},
    {"isim": "Veli", "mail": "veli@hotmail.com", "aktif": True},
    {"isim": "Ayşe", "mail": "ayse@gmail.com", "aktif": False},
    {"isim": "Fatma", "mail": "fatma@gmail.com", "aktif": True},
    {"isim": "Can", "mail": "can@yahoo.com", "aktif": True}
]

"""def rapor(kullanicilar):
    toplam = 0
    aktif = 0
    pasif = 0
    gmail = 0

    for kullanici in kullanicilar:
        toplam += 1

        if kullanici["aktif"]:
            aktif += 1
        else:
            pasif += 1

        if kullanici["mail"].endswith("@gmail.com"):
            gmail += 1

    print("Toplam Kullanıcı :", toplam)
    print("Aktif Kullanıcı :", aktif)
    print("Pasif Kullanıcı :", pasif)
    print("Gmail Kullanıcı :", gmail)


rapor(kullanicilar)"""

"""kullanici = {
    "isim": "Fatma",
    "yas": 30,
    "mail": "fatma@gmail.com",
    "aktif": True
}

print(kullanici["mail"])
kullanici["yas"] = 31
print(kullanici["yas"])
kullanici["sehir"] = "İstanbul"
print(kullanici)"""

"""urun = {
    "ad": "Laptop",
    "fiyat": 35000,
    "stok": 12
}
print(urun["ad"])
urun["stok"] = 10

print(urun)
urun["marka"] = "Lenovo"
print(urun["marka"])
print(urun)"""

"""urunler = [
    {
        "ad": "Laptop",
        "fiyat": 35000
    },
    {
        "ad": "Mouse",
        "fiyat": 500
    }
]
print(urunler[0]["ad"])  
print(urunler[1]["fiyat"]) """
    
filmler = [
    {
        "isim":"Inception",
        "puan":9
    },
    {
        "isim":"Interstellar",
        "puan":10
    },
    {
        "isim":"Prestige",
        "puan":8
    }
]
for film in filmler:
    print(film["isim"])






















    

    































































































