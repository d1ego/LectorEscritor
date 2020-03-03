import time
import threading
from threading import Thread
import inspect

class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()

contador=0
f = open("texto.txt", "r")
b = open("texto.txt", "r")

a = open("texto.txt", "a")

lock = threading.Lock()

def conteo():
    global contador
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    with lock:
        print
        "Lock Acquired"
        contador += 1
        time.sleep(2)

def lector1():
    while contador<5:
        print("Hola soy el lector 1 y el archivo de texto dice:")
        print(f.read())
        conteo()
        escritor1()

def lector2():
    while contador <5:
        print("Hola soy el lector 2 y el archivo de texto dice:")
        print(b.read())
        conteo()
        escritor2()

def escritor1():
    while contador <5:
        print("Hola soy el escritor 1 y agregue texto al libro:")
        a.write("\n+++++++Esta linea ha sido escrita por el escritor 1\n")
        conteo()
        lector2()

def escritor2():
    while contador <5:
        print("Hola soy el escritor 2 y agregue texto al libro:")
        a.write("\n-------Esta linea ha sido escrita por el escritor 2\n")
        conteo()
        lector1()


def main():
    Lector1=Thread(lector1())


main()
