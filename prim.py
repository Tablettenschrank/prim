import multiprocessing
import time
import math
from numba import njit

@njit
def primZahl(zahl:int):
    if zahl <= 1:
        return
    for i in range(3, int(math.sqrt(zahl)) + 1,2):
        if zahl % i == 0:
            return
    return zahl    

if __name__ == "__main__":

    def Format(string1:str)-> str:
        string2 = f"{string1:_}"
        string2 = string2.replace("_",".")
        return string2

    def updateTmp(lastNumber:str):
        with open("tmp.txt","w") as f:
            f.write(str(lastNumber))
            f.close()
        return 


    start_time = time.time()

    resetFile = False
    more = True #if true and reset file = False, then it's calculate the mew diffrience between begin and end
    processes = 7 # Cores
    begin = 3 # 3 is default
    end = 500_0_0
    chunksize=10_00

    if resetFile:
        with open("prim.txt","w") as f:
            f.write("")
            f.close()
    else:
        with open("tmp.txt","r") as f:
            begin = f.readline()
            print(begin)
            f.close()
            print(begin)
            begin = int(begin)
        if more:
            end = end + begin
            print("more!!!")

    
  
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

    updateTmp(str(lastNumber))
        
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

