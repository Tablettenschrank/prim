import multiprocessing
import time
import math
from numba import njit, cuda

# Configuration variables
processes = 3  # Number of CPU cores to use
begin = 3  # Starting number for primality check
end = 50_000_000  # Ending number for primality check
chunksize = 10_000  # Chunk size for CPU processing
use_gpu = True  # Use GPU for calculations (True) or CPU (False)
gpu_threads_per_block = 128  # Number of threads per block for GPU processing
#RTX 2060 Super (256)

start_time = time.time()

with open("prim.txt", "w") as f:
    f.write("")
    f.close()

def Format(string1: str) -> str:
    string2 = f"{string1:_}"
    string2 = string2.replace("_", ".")
    return string2

@njit
def primZahlCPU(zahl: int):
    if zahl <= 1:
        return
    for i in range(3, int(math.sqrt(zahl)) + 1, 2):
        if zahl % i == 0:
            return
    return zahl

@cuda.jit
def primZahlGPU(arr, results):
    idx = cuda.grid(1)
    if idx < arr.shape[0]:
        zahl = arr[idx]
        if zahl <= 1:
            results[idx] = 0
        else:
            is_prime = True
            for i in range(3, int(math.sqrt(zahl)) + 1, 2):
                if zahl % i == 0:
                    is_prime = False
                    break
            results[idx] = zahl if is_prime else 0

if __name__ == "__main__":
    limit = range(begin, end, 2)
    if use_gpu:
        # Create a CUDA device array
        arr = cuda.to_device(list(limit))
        results = cuda.device_array_like(arr)
        blocks = (arr.shape[0] + gpu_threads_per_block - 1) // gpu_threads_per_block
        primZahlGPU[blocks, gpu_threads_per_block](arr, results)
        ergebniss = results.copy_to_host()
        ergebniss = list(filter(None, ergebniss))
    else:
        with multiprocessing.Pool(processes) as p:
            ergebniss = list(filter(None, p.map(primZahlCPU, limit, chunksize)))

    end_time = time.time()
    with open("prim.txt", "a") as f:
        weg = ", ".join(map(str, ergebniss))
        f.write(weg)
        f.close()
    ergebnissAmount = len(ergebniss)
    lastNumber = ergebniss[-1]

    print("---------------------------------")
    print(Format(begin), "-", Format(end))
    print("")
    print("Last Number: ", Format(lastNumber))
    print("Calculatet Prim's: ", Format(ergebnissAmount))
    print("chunksize: ", Format(chunksize))
    print("")
    runtime = end_time - start_time
    print(f"{runtime:.3f}", "Seconds")
    print(f"{runtime/60:.3f}", "Minutes")
    print("---------------------------------")