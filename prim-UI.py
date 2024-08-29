import multiprocessing
import time
import math
import threading
import FreeSimpleGUI as fsg
from numba import njit


layout = [
        [
            fsg.Text("Hallo",key="text",font="Any 24")
        ]
    ]
window = fsg.Window("Das Fenster",layout)
fsg.theme_global("DarkBrown")
def UI():

    
    
    while True:
        e, v = window.read()
        print(e, v)

        if e is None:
            window.close()
            break

        if e == "Event":
            window["text"](v["Event"])

def warte5Sekunden():
    time.sleep(5)
    window.write_event_value("Event","Ausgelöst")
    time.sleep(2)
    
start_time = time.time()

processes = 3 # Cores
begin = 3 # 3 is default
end = 5_000_000
chunksize=1_000

with open("prim.txt","w") as f:
    f.write("")
    f.close()

def Format(string1:str)-> str:
    string2 = f"{string1:_}"
    string2 = string2.replace("_",".")
    return string2

def Format2(ergebniss):
    with open("prim.txt","a") as f:
        weg = ", ".join(map(str,ergebniss))
        f.write(weg)
        f.close()
    return

def output(begin,end,chunksize,end_time,start_time,ergebniss):
    ergebnissAmount = len(ergebniss)
    lastNumber = ergebniss[-1]
    print("---------------------------------")
    print(Format(begin),"-",Format(end))
    print("")
    print("Last Number: ",Format(lastNumber))
    print("Calculatet Prim's: ",Format(ergebnissAmount))
    print("chunksize: ",Format(chunksize))
    print("")
    runtime = end_time - start_time
    print(f"{runtime:.3f}","Seconds")
    print(f"{runtime/60:.3f}","Minutes")
    print("---------------------------------")
    return


@njit
def primZahl(zahl:int)->int:
    if zahl <= 1:
        return
    for i in range(3, int(math.sqrt(zahl)) + 1,2):
        if zahl % i == 0:
            return
    return zahl    

limit = range(begin,end,2)

def ergebnissCalc(processes,limit,chunksize)->list:
    with multiprocessing.Pool(processes) as p:
        ergebniss = list(filter(None,p.map(primZahl,limit,chunksize)))
    return ergebniss

def lol():
    threading.Thread(target=warte5Sekunden,daemon=False).start()
    for i in range(0,5):
        print("lol")
        time.sleep(1)

def main():
    threading.Thread(target=UI,daemon=True).start()
    threading.Thread(target=lol,daemon=False).start()
    ergebniss = ergebnissCalc(processes,limit,chunksize)
    end_time = time.time()
    Format2(ergebniss)
    output(begin,end,chunksize,end_time,start_time,ergebniss)

##################################################################

if __name__ == "__main__":
    main()