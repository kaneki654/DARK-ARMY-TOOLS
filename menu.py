import os
import random
import sys
import time
import pyfiglet
from functionality.drkrmydnction import clear

class colors:
    RAWR = '\033[91m'
    TAE = '\033[92m'

print(colors.RAWR + "WAIT MO LANG YA, BILANG KA SAMPO..")
time.sleep(10)
clear()

ascii_banner = pyfiglet.figlet_format("DARK-ARMY-DDOS-TOOLS")
print(ascii_banner)

print(colors.TAE + '[1]DDOSit')
print(colors.RAWR + '[2]C2')
print(colors.TAE + '[3]BYPASSES')
print(colors.TAE + '[4]CRYPTOR')

user_input = int(input('PILI KA ISA YA: '))


if user_input == 1:
    from GRAA import *
    import subprocess

    cmd = 'python GRAA.py'
    p=subprocess.Popen(cmd,shell=True)
    NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
    print(BOBO_ERROR_HAHAHAH_KAWAWA)
    print(NAG_OUT_TANGINANG_YAN)

if user_input == 2:
    from POWPOW import *
    import subprocess

    cmd = 'python POWPOW.py'
    p=subprocess.Popen(cmd,shell=True)
    NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
    print(BOBO_ERROR_HAHAHAH_KAWAWA)
    print(NAG_OUT_TANGINANG_YAN)

if user_input == 4:
    clear()

    ascii_banner = pyfiglet.figlet_format('CRYPTOR')
    print(ascii_banner)

    print('[1]C2 CRYPTOR')
    
    user_input = int(input('PILI KA PA DITO BAI: '))

    if user_input == 1:
        from CRYPTOR.simulan import *
        import subprocess

        cmd = 'python simulan.py'
        p=subprocess.Popen(cmd,shell=True)
        NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
        print(BOBO_ERROR_HAHAHAH_KAWAWA)
        print(NAG_OUT_TANGINANG_YAN)
    
    else:
        clear()
        print('PARANG MAY KULANG??')
        time.sleep(7)
        clear()
        print('BYE MUNA:> (run mo nlng ako ulit kapag okay na)')
        time.sleep(7)
        quit()
        
if user_input == 3:
    clear()

    ascii_banner = pyfiglet.figlet_format('BYPASS TOOL')
    print(ascii_banner)

    print('[1]ddosgaurd')
    print('[2]PythoBYPASS')
    print('[3]OVH')

    user_input = int(input('PILI KA PA DITO ISA: '))

    if user_input == 1:
        import subprocess

        cmd = 'node functions.js'
        p=subprocess.Popen(cmd,shell=True)
        NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
        print(BOBO_ERROR_HAHAHAH_KAWAWA)
        print(NAG_OUT_TANGINANG_YAN)
    
    else:
        print('NAGKULANG KA:<')
        quit()
    
    if user_input == 2:
        from grooming import *
        import subprocess

        cmd = 'python grooming.py'
        p=subprocess.Popen(cmd,shell=True)
        NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
        print(BOBO_ERROR_HAHAHAH_KAWAWA)
        print(NAG_OUT_TANGINANG_YAN)
    else:
        print('NAGKULANG KA:<')
        quit()

    if user_input == 3:
        import subprocess

        cmd = 'node need.js'
        p=subprocess.Popen(cmd,shell=True)
        NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
        print(BOBO_ERROR_HAHAHAH_KAWAWA)
        print(NAG_OUT_TANGINANG_YAN)
    else:
        print('NAGKULANG KA:<')
        quit()