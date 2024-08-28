import multiprocessing
import time
import math
from numba import njit

start_time = time.time()

processes = 7
limit1 = 10_000_000
chunksize=2_000_000

#print('IMPORTANT! You need a "prim.txt" file!')
#print('IMPORTANT! You need a "prim.txt" file!')
#print('IMPORTANT! You need a "prim.txt" file!')
#print('IMPORTANT! You need a "prim.txt" file!')

with open("prim.txt","w") as f:
    f.write("")
    f.close()

def primZahl(zahl):
    if zahl <= 1:
        return
    if zahl % 2 == 0:
        return
    for i in range(2, int(zahl ** 0.5) + 1):
        if zahl % i == 0:
            return
    return zahl    

if __name__ == "__main__":
    limit = range(3,limit1,2)
    with multiprocessing.Pool(processes) as p:
        ergebnis = list(filter(None,p.map(primZahl,limit,chunksize)))
        ergebnis3 = ergebnis
    # print(ergebnis)
    # print(ergebnis)
    with open("prim.txt","a") as f:
                ergebnis2 = str(ergebnis)
                ergebnis2 = ergebnis2.replace("[","")
                ergebnis2 = ergebnis2.replace("]","")
                # print(ergebnis2)
                f.write(ergebnis2)
                f.close()
    
    end_time = time.time()
    with open("prim.txt","r") as f:
        a = f.read()
        f.close()
        b = ergebnis3[-1]

        c = f"{b:_}"
        c = c.replace("_",".")

        d = len(a)
        e = f"{d:_}"
        e = e.replace("_",".")

        limit1txt = f"{limit1:_}"
        limit1txt = limit1txt.replace("_",".")

        chunksize = f"{chunksize:_}"
        chunksize = chunksize.replace("_",".")


    # print("---------------------------------")
    # print(len(ergebnis),"Prim's")
    # print(a)
    print("---------------------------------")
    print("0","-",limit1txt)
    print("")
    print("Last Number: ",c)
    print("Calculatet Prim's: ",e)
    print("chunksize: ",chunksize )
    runtime = end_time - start_time
    print(f"{runtime:.3f}","Seconds")
    print(f"{runtime/60:.3f}","Minutes")
    print("---------------------------------")
