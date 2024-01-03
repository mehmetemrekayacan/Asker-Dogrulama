from tkinter import *
import sqlite3 as sql

window=Tk()
window.title("Asker Doğrulama")
window.iconbitmap("tr.ico")
window.geometry("600x600")
window.configure(bg="red")

menubar=Menu(window)

con=sql.connect("asker.db")
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS asker (isim TEXT,soyad TEXT,yaş İNT,bölüm TEXT,sağlık sorunu TEXT)")

def ekle():
    yeniisim=isim.get()
    yenisoyad=soyad.get()
    yeniyaş=yas.get()
    def sg():
        if var2.get() == True:
            sag = "SAĞLAM"
        elif var1.get() == True:
            sag = "ÇÜRÜK"
        return sag
    def sd():
        sayıbölüm = x.get()
        if sayıbölüm == 1:
            yenibölüm = "KARACI"
        elif sayıbölüm == 2:
            yenibölüm = "DENİZCİ"
        elif sayıbölüm == 3:
            yenibölüm = "HAVACI"
        return yenibölüm
    cur.execute("INSERT INTO asker VALUES('" + yeniisim + "','" + yenisoyad + "','" + yeniyaş + "','" + sd() + "','" + sg() + "')")
    Label(window,text="Asker bilgisi Başarıyla Eklendi!",font="times 15 bold",bg="red",relief=RAISED).place(x=10,y=300)
    con.commit()
filemenu=Menu(menubar,tearoff=0,font="ariel 10 bold",bg="red",fg="black")
filemenu.add_command(label="Asker Bilgisini Ekle",command=ekle)
menubar.add_cascade(label="Ekle",menu=filemenu)

def göster():
    window2 = Tk()
    window2.geometry("600x600")
    window2.iconbitmap("tr.ico")
    window2.config(bg="red")
    cur.execute("SELECT * FROM asker")
    asker_bilgi=cur.fetchall()
    Label(window2, text="Asker Bilgileri", font="ariel 20 bold", bg="red").place(x=10,y=10)
    i=0
    h=25
    for asker in asker_bilgi:
        i+=1
        h+=30
        a=Label(window2,text="Asker {} = {}".format(i,asker),font="ariel 10 bold",bg="red")
        a.place(x=25,y=h)
    window2.mainloop()
filemenu2=Menu(menubar,tearoff=0,font="ariel 10 bold",bg="red",fg="black")
filemenu2.add_command(label="Asker Bilgilerini Göster",command=göster)
menubar.add_cascade(label="Göster",menu=filemenu2)


Label(window,text="İsim:",font="ariel 10 bold",bg="red").place(x=10,y=20)
isim=Entry(window,relief=RAISED,font="ariel 8 bold")
isim.place(x=75,y=20)


Label(window,text="Soyad:",font="ariel 10 bold",bg="red").place(x=10,y=50)
soyad=Entry(window,relief=RAISED,font="ariel 8 bold")
soyad.place(x=75,y=50)


Label(window,text="Yaş:",font="ariel 10 bold",bg="red").place(x=10,y=80)
yas=Spinbox(window,from_=18,to=65,font="times 10 bold",bg="black",fg="red",bd=5,width=15,relief=GROOVE,justify="center")
yas.place(x=75,y=80)


x=IntVar()
photoK = PhotoImage(file="karacı.png")
K_photo = photoK.subsample(2, 2)
def karacı():
    Frame(window,bg="red",height=200,width=200).place(x=360, y=180)
    Label(window, image=K_photo,bg="black").place(x=360, y=180)
photoD = PhotoImage(file="denizci.png")
D_photo = photoD.subsample(2, 2)
def denizci():
    Frame(window, bg="red", height=200,width=200).place(x=360, y=180)
    Label(window, image=D_photo,bg="black").place(x=360, y=180)
photoH = PhotoImage(file="havacı.png")
H_photo = photoH.subsample(2, 2)
def havacı():
    Frame(window, bg="red", height=200,width=200).place(x=360, y=180)
    Label(window, image=H_photo,bg="black").place(x=360, y=180)
kara=Radiobutton(window,bg="red",text="Karacı",font="times 12 bold",variable=x,value=1,activebackground="red",command=karacı)
kara.place(x=10,y=120)
deniz=Radiobutton(window,bg="red",text="Denizci",font="times 12 bold",variable=x,value=2,activebackground="red",command=denizci)
deniz.place(x=100,y=120)
hava=Radiobutton(window,bg="red",text="Havacı",font="times 12 bold",variable=x,value=3,activebackground="red",command=havacı)
hava.place(x=190,y=120)


from tkinter import messagebox
var1=IntVar()
var2=IntVar()
var3=IntVar()
def health():
    x=messagebox.askyesno("Sağlık sorunu", "Eğer bir sağlık sorunun varsa 'Evet' basın, yoksa 'Hayır' basın")
    if x==True:
        a=Checkbutton(window, text="Sağlık Durumu", command=health, bg="red", activebackground="red",
                font="times 12 bold", variable=var1, onvalue=1,offvalue=0)
        a.place(x=10, y=150)
        a.select()
    else:
        b=Checkbutton(window, text="Sağlık Durumu", command=health, bg="red",activebackground="red",
                    font="times 12 bold", variable=var2,offvalue=1,onvalue=0)
        b.place(x=10, y=150)
        b.deselect()
Checkbutton(window,text="Sağlık Durumu",command=health,bg="red",activebackground="red",
            font="times 12 bold",variable=var3,onvalue=1,offvalue=0).place(x=10,y=150)


photo=PhotoImage(file="Türk Bayrağı.png")
Label(window,image=photo,bg="black").place(x=300,y=10)


def clicked_button():
    cur.execute("SELECT * FROM asker WHERE isim=? AND soyad=?", (isim.get(), soyad.get()))
    result = cur.fetchone()

    if result:
        Label(window, text="{} {}\ndoğrulamanız başarılı".format(isim.get(), soyad.get()), font="times 15 bold",
              bg="red", width=20, borderwidth=5, relief=RAISED).place(x=200, y=350)
    else:
        Label(window, text="Doğrulama başarısız. Asker bulunamadı.", font="times 15 bold",
              bg="red", width=30, borderwidth=5, relief=RAISED).place(x=150, y=350)

Button(window, text="Doğrula", font="times 15 bold", bg="red", activebackground="black", activeforeground="red",
       command=clicked_button).place(x=75, y=190)



Label(window,text="1. Gerekli boşlukları doldurun.",bg="red",font="times 12 bold").place(x=10,y=500)
Label(window,text="2. Sol üst sekmedeki 'Ekleme' bölümüne gelin ve bilginizi ekleyin.",bg="red",font="times 12 bold").place(x=10,y=525)
Label(window,text="3. Doğrula butonuna tıklayın ve işleminiz bitmiştir.",bg="red",font="times 12 bold").place(x=10,y=550)


window.config(menu=menubar)
window.mainloop()
