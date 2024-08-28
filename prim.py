import multiprocessing
import time
import math
from numba import njit

start_time = time.time()

processes = 7
limit0 = 3 # 3 is default
limit1 = 50_000_000
chunksize=100_000

with open("prim.txt","w") as f:
    f.write("")
    f.close()

@njit
def primZahl(zahl:int):
    if zahl <= 1:
        return
    for i in range(3, int(math.sqrt(zahl)) + 1,2):
        if zahl % i == 0:
            return
    return zahl    

if __name__ == "__main__":
    limit = range(limit0,limit1,2)
    with multiprocessing.Pool(processes) as p:
        ergebnis = list(filter(None,p.map(primZahl,limit,chunksize)))
    
    with open("prim.txt","a") as f:
                ergebnis2 = str(ergebnis)
                ergebnis2 = ergebnis2.replace("[","")
                ergebnis2 = ergebnis2.replace("]","")
                f.write(ergebnis2)
                f.close()
    ergebnis3 = ergebnis
    end_time = time.time()
    with open("prim.txt","r") as f:
        a = f.read()
        f.close()
        b = ergebnis3[-1]

        c = f"{b:_}"
        c = c.replace("_",".")
        
        d = len(ergebnis)
        e = f"{d:_}"
        e = e.replace("_",".")

        limit1txt = f"{limit1:_}"
        limit1txt = limit1txt.replace("_",".")

        limit0txt = f"{limit0:_}"
        limit0txt = limit0txt.replace("_",".")

        chunksize = f"{chunksize:_}"
        chunksize = chunksize.replace("_",".")
        

    print("---------------------------------")
    print(limit0,"-",limit1txt)
    print("")
    print("Last Number: ",c)
    print("Calculatet Prim's: ",e)
    print("chunksize: ",chunksize )
    print("")
    runtime = end_time - start_time
    print(f"{runtime:.3f}","Seconds")
    print(f"{runtime/60:.3f}","Minutes")
    print("---------------------------------")
