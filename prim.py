import multiprocessing
import time
import math
from numba import njit

start_time = time.time()

processes = 7
limit0 = 3 # 3 is default
limit1 = 50_000_00
chunksize=100_00

with open("prim.txt","w") as f:
    f.write("")
    f.close()

def Format(string1:str)-> str:
    string2 = f"{string1:_}"
    string2 = string2.replace("_",".")
    return string2

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
        ergebniss = list(filter(None,p.map(primZahl,limit,chunksize)))
    
    end_time = time.time()
    with open("prim.txt","a") as f:
                ergebniss2 = str(ergebniss)
                ergebniss2 = ergebniss2.replace("[","")
                ergebniss2 = ergebniss2.replace("]","")
                f.write(ergebniss2)
                f.close()
    with open("prim.txt","r") as f:
        a = f.read()
        f.close()
    ergebnissAmount = len(ergebniss)
    lastNumber = ergebniss[-1]
        
    print("---------------------------------")
    print(Format(limit0),"-",Format(limit1))
    print("")
    print("Last Number: ",Format(lastNumber))
    print("Calculatet Prim's: ",Format(ergebnissAmount))
    print("chunksize: ",Format(chunksize))
    print("")
    runtime = end_time - start_time
    print(f"{runtime:.3f}","Seconds")
    print(f"{runtime/60:.3f}","Minutes")
    print("---------------------------------")
