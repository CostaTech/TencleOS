# TencleOS Digital Clock - TLang Version
# Console version (TLang doesn't support tkinter GUI)
# Original: time.pyw - Tkinter GUI with digital clock display

use time
use os
use sys

int << func >> ("========================================")
int << func >> ("      TENCLEOS DIGITAL CLOCK          ")
int << func >> ("========================================")
int << func >> ("")
int << func >> ("Hours : Minutes : Seconds")
int << func >> ("")

# Display time 10 times (simulating clock updates)
for i in 10 {
    current_time = time.strftime("%H:%M:%S")
    int << func >> ("     " + current_time)
    time.sleep(1)
}

int << func >> ("")
int << func >> ("========================================")
int << func >> ("Thank you for using TencleOS Clock!")
int << func >> ("Press Enter to close...")
var wait = input()


