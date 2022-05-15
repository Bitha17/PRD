import pandas as pd
import schedule
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
gc = gspread.service_account(filename="ecm-prd-60a7a09437a3.json")
gsheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1E5meDeWAvRxHYpssbGNqbvW8x4j8sBySBw63ZX3YavQ/edit#gid=0")
mydata = gsheet.sheet1.get_all_records()


data_daya=pd.read_excel("C:/Users/ASUS/OneDrive/Dokumen/TUBES PRD/data_daya.xlsx")
print(data_daya)


# Input ID Rumah
ID = input("Masukkan ID_Rumah: ")
data_user= data_daya.loc[data_daya["ID_Rumah"]==ID]
print(data_user)
C=int(data_user["Carbon"]) # kadar karbon daerah setempat
Gol_P=str(data_user["Gol"]) # golongan daya
cuaca=str(data_user["Cuaca"])[0] # Cuaca daerah setempat
Jumlah_daya=int(data_user["Jumlah_daya"]) # jumlah daya

limit=-9999
if 0<C<=50:
    if cuaca=="A":
        limit=Jumlah_daya
    elif cuaca == "B":
        if Gol_P=="R-1" or Gol_P=="R-2" or Gol_P=="R-3":
            limit=(Jumlah_daya - Jumlah_daya*(3/100))
        elif Gol_P=="B-2" or Gol_P=="B-3" or Gol_P=="I-3" or Gol_P=="I-4":
            limit=(Jumlah_daya - Jumlah_daya*(2/100))
        else:
            limit=(Jumlah_daya - Jumlah_daya*(3/100))
    else:
        if Gol_P=="R-1" or Gol_P=="R-2" or Gol_P=="R-3":
            limit=(Jumlah_daya - Jumlah_daya*(4/100))
        elif Gol_P=="B-2" or Gol_P=="B-3" or Gol_P=="I-3" or Gol_P=="I-4":
            limit=(Jumlah_daya - Jumlah_daya*(3/100))
        else:
            limit=(Jumlah_daya - Jumlah_daya*(4/100))
        
elif 50<C<=100:
    if cuaca=="A":
        if Gol_P=="R-1" or Gol_P=="R-2" or Gol_P=="R-3":
            limit=(Jumlah_daya - Jumlah_daya*(5/100))
        elif Gol_P=="B-2" or Gol_P=="B-3" or Gol_P=="I-3" or Gol_P=="I-4":
            limit=(Jumlah_daya - Jumlah_daya*(4/100))
        else:
            limit=(Jumlah_daya - Jumlah_daya*(5/100))
    elif cuaca == "B":
        if Gol_P=="R-1" or Gol_P=="R-2" or Gol_P=="R-3":
            limit=(Jumlah_daya - Jumlah_daya*(6/100))
        elif Gol_P=="B-2" or Gol_P=="B-3" or Gol_P=="I-3" or Gol_P=="I-4":
            limit=(Jumlah_daya - Jumlah_daya*(5/100))
        else:
            limit=(Jumlah_daya - Jumlah_daya*(6/100))
    else:
        if Gol_P=="R-1" or Gol_P=="R-2" or Gol_P=="R-3":
            limit=(Jumlah_daya - Jumlah_daya*(7/100))
        elif Gol_P=="B-2" or Gol_P=="B-3" or Gol_P=="I-3" or Gol_P=="I-4":
            limit=(Jumlah_daya - Jumlah_daya*(6/100))
        else:
            limit=(Jumlah_daya - Jumlah_daya*(7/100))

elif 100<C<=199:
    if cuaca=="A":
        if Gol_P=="R-1" or Gol_P=="R-2" or Gol_P=="R-3":
            limit=(Jumlah_daya - Jumlah_daya*(10/100))
        elif Gol_P=="B-2" or Gol_P=="B-3" or Gol_P=="I-3" or Gol_P=="I-4":
            limit=(Jumlah_daya - Jumlah_daya*(8/100))
        else:
            limit=(Jumlah_daya - Jumlah_daya*(10/100))
    elif cuaca == "B":
        if Gol_P=="R-1" or Gol_P=="R-2" or Gol_P=="R-3":
            limit=(Jumlah_daya - Jumlah_daya*(11/100))
        elif Gol_P=="B-2" or Gol_P=="B-3" or Gol_P=="I-3" or Gol_P=="I-4":
            limit=(Jumlah_daya - Jumlah_daya*(9/100))
        else:
            limit=(Jumlah_daya - Jumlah_daya*(11/100))
    else:
        if Gol_P=="R-1" or Gol_P=="R-2" or Gol_P=="R-3":
            limit=(Jumlah_daya - Jumlah_daya*(12/100))
        elif Gol_P=="B-2" or Gol_P=="B-3" or Gol_P=="I-3" or Gol_P=="I-4":
            limit=(Jumlah_daya - Jumlah_daya*(10/100))
        else:
            limit=(Jumlah_daya - Jumlah_daya*(12/100))

elif 199<C<=299:
    if cuaca=="A":
        if Gol_P=="R-1" or Gol_P=="R-2" or Gol_P=="R-3":
            limit=(Jumlah_daya - Jumlah_daya*(15/100))
        elif Gol_P=="B-2" or Gol_P=="B-3" or Gol_P=="I-3" or Gol_P=="I-4":
            limit=(Jumlah_daya - Jumlah_daya*(12/100))
        else:
            limit=(Jumlah_daya - Jumlah_daya*(15/100))
    elif cuaca == "B":
        if Gol_P=="R-1" or Gol_P=="R-2" or Gol_P=="R-3":
            limit=(Jumlah_daya - Jumlah_daya*(18/100))
        elif Gol_P=="B-2" or Gol_P=="B-3" or Gol_P=="I-3" or Gol_P=="I-4":
            limit=(Jumlah_daya - Jumlah_daya*(16/100))
        else:
            limit=(Jumlah_daya - Jumlah_daya*(18/100))
    else:
        if Gol_P=="R-1" or Gol_P=="R-2" or Gol_P=="R-3":
            limit=(Jumlah_daya - Jumlah_daya*(20/100))
        elif Gol_P=="B-2" or Gol_P=="B-3" or Gol_P=="I-3" or Gol_P=="I-4":
            limit=(Jumlah_daya - Jumlah_daya*(22/100))
        else:
            limit=(Jumlah_daya - Jumlah_daya*(20/100))

else:
    if cuaca=="A":
        if Gol_P=="R-1" or Gol_P=="R-2" or Gol_P=="R-3":
            limit=(Jumlah_daya - Jumlah_daya*(30/100))
        elif Gol_P=="B-2" or Gol_P=="B-3" or Gol_P=="I-3" or Gol_P=="I-4":
            limit=(Jumlah_daya - Jumlah_daya*(25/100))
        else:
            limit=(Jumlah_daya - Jumlah_daya*(30/100))
    elif cuaca == "B":
        if Gol_P=="R-1" or Gol_P=="R-2" or Gol_P=="R-3":
            limit=(Jumlah_daya - Jumlah_daya*(32/100))
        elif Gol_P=="B-2" or Gol_P=="B-3" or Gol_P=="I-3" or Gol_P=="I-4":
            limit=(Jumlah_daya - Jumlah_daya*(28/100))
        else:
            limit=(Jumlah_daya - Jumlah_daya*(32/100))
    else:
        if Gol_P=="R-1" or Gol_P=="R-2" or Gol_P=="R-3":
            limit=(Jumlah_daya - Jumlah_daya*(35/100))
        elif Gol_P=="B-2" or Gol_P=="B-3" or Gol_P=="I-3" or Gol_P=="I-4":
            limit=(Jumlah_daya - Jumlah_daya*(30/100))
        else:
            limit=(Jumlah_daya - Jumlah_daya*(35/100))

print("="*24)
print("LIMIT AWAL: ",str(limit))
limitAwal = limit


def readPower():

    df= pd.DataFrame(mydata)
    last_30min=df.loc[len(df)-1]
    VAd=last_30min["Daya"] # VAd adalah daya yang disipasikan dalam satu detik
    return(VAd)

while limit>0:
    schedule.every(3).seconds.do(readPower)
    VAd=readPower() 
    limit-=VAd
    print(f"Sisa limit: {'{:.2f}'.format(limit)}")
    time.sleep(3)
    # FUNGSI 03: WARNING SAAT LIMIT TINGGAL 15%
    if limitAwal*13/100<=limit<=limitAwal*18/100:
        print(f"Sisa Limit Anda tinggal 15% sebesar {limit}" )
        print("Mohon Segera Mengatur Rencana Penghematan Daya Anda!")
    elif limit==0:
        print("LIMIT PENGGUNAAN DAYA LISTRIK TELAH HABIS")
        print("KETIK 'YA' JIKA INGIN MENAMBAH LIMIT DENGAN TAMBAHAN CHARGE, KETIK 'TIDAK' JIKA TIDAK")
        pil=input()

# MENGULANGI LOOPING LIMIT
while limit>0:
    schedule.every(30).minutes.do(readPower)
    VAd=readPower()
    limit-=VAd
    print(f"Sisa limit: {'{:.2f}'.format(limit)}")
    time.sleep(1)
    print("Sisa limit: ",str(limit))
        # FUNGSI 03: WARNING SAAT LIMIT TINGGAL 15%
    if limitAwal*13/100<=limit<=limitAwal*18/100:
            print("SISA LIMIT DAYA TINGGAL 15% LIMIT AWAL")
    elif limit==0:
            print("MAAF LIMIT PENGGUNAAN DAYA TELAH HABIS, SILAHKAN HUBUNGI CALL SERVICE JIKA ADA HAL PENTING")

# jika ada hal yang penting petugas akan memanipulasi limit pada program sehingga dapat bekerja
# Saat limit=0 maka harus dipastikan listrik pada tempat tersebut juga terputus sementara sampai bulan berikutnya
    def looplimit(limit,limitAwal):
        while limit>0:
            Pd=float(input()) # misal pd adalah p disipasi yang didisipasikan suatu elemen
            limit = limit - Pd
            print("Sisa limit:",str(limit))
           # FUNGSI 03: WARNING SAAT LIMIT TINGGAL 15%
        if limitAwal*13/100<=limit<=limitAwal*18/100:
            print("SISA LIMIT DAYA TINGGAL 15% LIMIT AWAL")
        elif limit==0:
            print("LIMIT PENGGUNAAN DAYA LISTRIK TELAH HABIS")


def login():
    print("Apakah ada petugas yang ingin login?")
    pilihan=input() # yes/no
    if pilihan=="yes":
            logged_in=False
            found=False
            data_petugas=pd.read_excel("C:/Users/ASUS/OneDrive/Dokumen/TUBES PRD/data_pengguna.xlsx")
            IDP=input("Masukkan ID: ")
            pin=input("Masukkan pin: ")
            if data_petugas.loc[data_petugas["ID"]==IDP]:
                found=True
                if data_petugas.loc[data_petugas["pin"]==pin]:
                    logged_in=True
                else: 
                    print("Password Anda salah.")
    if found==False:
        print("ID tidak ditemukan.")
    elif logged_in==True:
        limit1=int(input("Masukkan limit: "))
        limitAwal1=limit1
        looplimit(limit1,limitAwal1)
def help():
    print("Hubungi nomor berikut untuk mendapatkan informasi mengenai program....")

print("Silahkan pilih opsi berikut untuk bantuan dan informasi lebih lanjut")
print("1. HELP")
print("2. LOGIN PETUGAS")
pil=int(input("Ketikkan di sini: "))
print("="*24)
if pil==1:
    help()
elif pil==2:
    login()
