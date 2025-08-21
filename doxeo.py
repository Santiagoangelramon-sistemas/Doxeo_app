#---------------------------------
# Desktop app Doxeo-automatico
#---------------------------------

# a continuacion le vamos a compartir nuestra cuenta bancaria e informacion personal privada al profesor
from tkinter import *
from tkinter import messagebox

# Se declara una variable llamada ventana_principal, que adquiere la caracteristicas de un objeto de tipo Tk()

ventana = Tk()

ventana.title("Dr.Ramon")

ventana.geometry("800x550")

ventana.resizable(0,0)

ventana.config(bg="white")

# -------------------------
# Frame principal
# -------------------------
frame_juego = Frame(ventana)
frame_juego.config(bg="Black", width=780, height=440, bd=5, relief="solid")
frame_juego.place(x=10, y=10)

# Título y subtítulos
titulo = Label(frame_juego, text="Santiago Angel Ramon", fg="White",bg="Black", font=("Arial", 30, "bold"))
titulo.place(x=260, y=5)

# Título y subtítulos
titulo = Label(frame_juego, text="Fecha de Nacimiento: 17 de abril 2009", fg="White",bg="Black", font=("Arial", 15, "bold"))
titulo.place(x=220, y=70)

# Título y subtítulos
titulo = Label(frame_juego, text="Edad: 16 años", fg="White",bg="Black", font=("Arial", 15, "bold"))
titulo.place(x=220, y=96)

# Título y subtítulos
titulo = Label(frame_juego, text="Pais: Colombia", fg="White",bg="Black", font=("Arial", 15, "bold"))
titulo.place(x=220, y=124)

# Título y subtítulos
titulo = Label(frame_juego, text="Lugar de origen: San Gil - Santander", fg="White",bg="Black", font=("Arial", 15, "bold"))
titulo.place(x=220, y=155)

# Título y subtítulos
titulo = Label(frame_juego, text="Estatura: 1.73m", fg="White",bg="Black", font=("Arial", 15, "bold"))
titulo.place(x=220, y=180)

# Título y subtítulos
titulo = Label(frame_juego, text="Peso: 90 kg", fg="White",bg="Black", font=("Arial", 15, "bold"))
titulo.place(x=220, y=205)

logo = PhotoImage(file="empanadas.png")
lb_logo = Label(frame_juego, image=logo, bg="Black")
lb_logo.place(x=20, y=40)

logo_2 = PhotoImage(file="Papurris.png")
lb_logo = Label(frame_juego, image=logo_2, bg="Black")
lb_logo.place(x=20, y=250)

logo_2 = PhotoImage(file="Kangelox.png")
lb_logo = Label(frame_juego, image=logo_2, bg="Black")
lb_logo.place(x=20, y=250)


def familia():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("familia")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("600x500")
    toplevel_centigrados.config(bg="white")

def Animes():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("Animes Favoritos")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("600x500")
    toplevel_centigrados.config(bg="white")

def Videojuegos():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("Videojuegos Favoritos")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("600x500")
    toplevel_centigrados.config(bg="white")

def Personajes():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("Personajes")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("600x500")
    toplevel_centigrados.config(bg="white")

def educacion():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("educacion")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("600x500")
    toplevel_centigrados.config(bg="white")

def amigos():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("amigos")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("600x500")
    toplevel_centigrados.config(bg="white")

def hobbies():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("hobbies")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("600x500")
    toplevel_centigrados.config(bg="white")

def horario():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("horario")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("600x500")
    toplevel_centigrados.config(bg="white")

def preparacion():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("preparacion para el icfes 11")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("600x500")
    toplevel_centigrados.config(bg="black")

def proyecto():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("proyecto de vida")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("600x500")
    toplevel_centigrados.config(bg="white")

bt_familia = Button(ventana,text="familia", command=familia)    
bt_familia.place(x=130, y=460, width=100, height=30)

bt_Animes = Button(ventana,text="Animes", command=Animes)    
bt_Animes.place(x=110, y=500, width=100, height=30)

bt_Personajes = Button(ventana,text="Personajes", command=Personajes)    
bt_Personajes.place(x=340, y=500, width=120, height=30)

bt_Videojuegos = Button(ventana,text="Videojuegos", command=Videojuegos)    
bt_Videojuegos.place(x=230, y=500, width=100, height=30)

bt_educacion = Button(ventana, text="educacion", command= educacion)
bt_educacion.place(x=240, y=460, width=100, height=30)

bt_amigos = Button(ventana, text="amigos", command=amigos)
bt_amigos.place(x=350, y=460, width=100, height=30)

bt_hobbies = Button(ventana,text="hobbies", command=hobbies)    
bt_hobbies.place(x=460, y=460, width=100, height=30)

bt_horario= Button(ventana,text="horario", command=horario)    
bt_horario.place(x=570, y=460, width=100, height=30)

bt_preparacion = Button(ventana, text="preparacion", command= preparacion)
bt_preparacion.place(x=680, y=460, width=100, height=30)

bt_proyecto = Button(ventana, text="proyecto", command=proyecto)
bt_proyecto.place(x=20, y=460, width=100, height=30)


# Metodo principal que despliega la ventana en pantalla
ventana.mainloop()