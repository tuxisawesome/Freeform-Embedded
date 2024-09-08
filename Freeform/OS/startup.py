import sys
from time import sleep
# caution: path[0] is reserved for script path (or '' in REPL)
print("Import display driver")
sys.path.insert(1, 'sys/drv/')
import wave_2in13_v3

wave_2in13_v3.print_screen("Hello world!")
sleep(5)
wave_2in13_v3.clock_demo()
sleep(2)
wave_2in13_v3.init_clear()
wave_2in13_v3.sleep()