import multiprocessing
import time
import math
from numba import njit

start_time = time.time()

processes = 3 # Cores
begin = 3 # 3 is default
end = 500_000_000   
chunksize=10_000

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
    limit = range(begin,end,2)
    with multiprocessing.Pool(processes) as p:
        ergebniss = list(filter(None,p.map(primZahl,limit,chunksize)))
    
    end_time = time.time()
    with open("prim.txt","a") as f:
        weg = ", ".join(map(str,ergebniss))
        f.write(weg)
        f.close()
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
