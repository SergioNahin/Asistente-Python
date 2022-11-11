#L I B R E R I A S
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia 
import smtplib      # enviar mail
import webbrowser as wb #buscar chrome
import os 
import pyautogui 
import psutil 
import pyjokes

# INICIALIZACION
engine = pyttsx3.init()
voces = engine.getProperty("voices")
engine.setProperty("voice", voces[0].id) #voces[1].id de 0 a 5, existen diferentes voces
newVoiceRate = 150  #Velocidad al hablar
engine.setProperty("rate", newVoiceRate)

def hablar(audio):
    engine.say(audio)
    engine.runAndWait()

def tiempo():       #Esta funcion sirve para leer la hora con todo y segundos
    time = datetime.datetime.now().strftime("%I:%M:%S")
    hablar("Son las")
    hablar(time)

def fecha():
    año = int(datetime.datetime.now().year)
    mes = int(datetime.datetime.now().month)
    dia = int(datetime.datetime.now().day)
    hablar("El dia de hoy es")
    hablar(dia)
    hablar("Del mes ")
    hablar(mes)
    hablar("Del año")
    hablar(año)

def deseo():
    hablar("Bienvenido Señor!")
    hora = datetime.datetime.now().hour
    if hora >= 6 and hora < 12:
        hablar("Buenos Dias Alegria!!")
        hablar("Romeo esta a tus servicios en esta bonita mañana. ¿Como puedo ayudarte?")
    elif hora >= 12 and hora < 18:
        hablar("Buenas Tardes, no olvides comer")
        hablar("Romeo esta a tus servicios. ¿Como puedo ayudarte?")
    elif hora >= 18  and hora < 22:
        hablar("Buenas noches")
        hablar("No duerma tan tarde,Romeo esta a tus servicios, ¿Como puedo ayudarte?")
    else:
        hablar("Trabajando hasta tarde otra vez señor...")
        hablar("En que puedo servirle")
    

def comando():
    r = sr.Recognizer()
    with    sr.Microphone() as source:
        print("Escuchando...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconociendo...")
        consulta = r.recognize_google(audio)
        print("Tu dijiste: {}".format(consulta))
    except Exception as e:
        print(e)
        hablar("Lo lamento podrias repetirlo...")
        return "None"
    return consulta

def enviarmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("sergiontr280@gmail.com","Mario280100")
    server.sendmail("sergiontr280@gmail.com ",to,content) #Envio de correo a
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/HP/Desktop/img/ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    hablar("CPU esta en" + usage)

   # bateria = psutil.sensors_battery
    #hablar("La bateria esta en")
    #hablar(bateria.percent())

def bromas():
    hablar(pyjokes.get_joke())

if __name__ == "__main__":
    
    deseo()
    while True:
        consulta = comando().lower()
        print(consulta)
        
        if "tiempo" in consulta:
            tiempo()

        elif "dia"  in consulta:
            fecha()

        elif "bye" in consulta:
            hablar("Hasta luego señor espero haberlo ayudado")
            quit()

        elif "busca" in consulta:
            hablar("buscando...")
            consulta = consulta.replace("busca","")
            resultado = wikipedia.summary(consulta, sentences = 2)
            hablar(resultado)

        elif "manda mensaje" in consulta: 
            try: 
                hablar("Dime el mensaje a enviar")
                contenido = comando()
                to = "trinidad.ramirez.sergio.nahin@gmail.com "
                enviarmail(to,contenido)
                hablar("El mensaje se envio con Exito!!")
            except Exception as e:
                print(e)
                hablar("No se pudo enviar el mensaje hay un error")

        elif "internet" in consulta:
            hablar("Que deseas buscar en internet?")
            busqueda = comando()
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            wb.get(chromepath).open_new_tab(busqueda+".com")

        elif "cierra sesion" in consulta: 
            os.system("shutdown -l")

        elif "apagar" in consulta: 
            os.system("shutdown /s /t 1")

        elif "restart" in consulta: 
            os.system("shutdown /r /t 1")

        elif "poner musica" in consulta:
            try:
                musica_dir = "C:/Users/HP/Desktop/musica"
                canciones = os.listdir(musica_dir)
                os.startfile(os.path.join(musica_dir,canciones[0]))
            except Exception as e:
                print(e)
                hablar("Hay un error, verifique")

        elif "escribe" in consulta: 
            hablar("Que quiere que recuerde por usted señor?")
            recordar = comando()
            hablar("Usted quiere que le recuerde "+ recordar)
            recordatorio = open("recordar.txt","w")
            recordatorio.write(recordar)
            recordatorio.close()

        elif "recuerdame" in consulta: 
            recordatorio = open("recordar.txt","r")
            hablar("Me dijiste que te recordara esto "+ recordatorio.read())

        elif "screenshot" in consulta:
            screenshot()
            hablar("Esta hecho!!")

        elif "estado" in consulta: 
            cpu()

        elif "joke" in consulta: 
            bromas()


