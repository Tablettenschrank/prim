import multiprocessing
import time

start_time = time.time()

processes = 7
limit1 = 100_000_000
chunksize=20_000_000

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
    for i in range(2, int(zahl ** 0.5) + 1):
        if zahl % i == 0:
            return
    return zahl

if __name__ == "__main__":
    limit = range(2,limit1)
    with multiprocessing.Pool(processes) as p:
        ergebnis = p.map(primZahl,limit,chunksize)

    with open("prim.txt","a") as f:
                f.write(str(ergebnis).replace("None, ",""))
                f.close()
    
    end_time = time.time()
    with open("prim.txt","r") as f:
        a = f.read().split()
        b = a[-2].replace(",","")
        f.close()
        b = int(b)

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
