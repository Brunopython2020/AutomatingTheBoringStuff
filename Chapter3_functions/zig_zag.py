
import time, sys


def zzag(simbol, width, step):
    
    step_zag = step

    for i in range(step_zag,0,-1):
        print(' '*(i-1),simbol*width,sep='')
        time.sleep(0.1)

    for i in range(0,(step_zag-1)):
        print(' '*(i+1),simbol*width,sep='')
        time.sleep(0.1)



while True:
    try:
        zzag('_|_', 20, 10)
    except KeyboardInterrupt:
        sys.exit()



