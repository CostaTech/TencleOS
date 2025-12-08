# TencleOS Login System
# Simplified PIN-based login (input() string comparison not supported)

use os
use sys
use datetime
use time

int << func >> ("      ")
int << func >> ("████████╗███████╗███╗   ██╗ ██████╗██╗     ███████╗ ██████╗ ███████╗")
int << func >> ("╚══██╔══╝██╔════╝████╗  ██║██╔════╝██║     ██╔════╝██╔═══██╗██╔════╝")
int << func >> ("   ██║   █████╗  ██╔██╗ ██║██║     ██║     █████╗  ██║   ██║███████╗")
int << func >> ("   ██║   ██╔══╝  ██║╚██╗██║██║     ██║     ██╔══╝  ██║   ██║╚════██║")
int << func >> ("   ██║   ███████╗██║ ╚████║╚██████╗███████╗███████╗╚██████╔╝███████║")
int << func >> ("   ╚═╝   ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝")
int << func >> ("")

int << func >> ("Login to TencleOS")
int << func >> ("Enter PIN code (default: 1234)")
int << func >> ("")

var pin = input("PIN: ")

<< ! >func> if pin == 1234 {
    int << func >> ("")
    int << func >> ("Login successful! Starting TencleOS...")
    int << func >> ("")

# Note: TLang does not support file I/O yet
# Username and password are hardcoded
l_n = "Costantino"
l_p = "123456"

int << func >> ("")
int << func >> ("========================================")
int << func >> ("           T E N C L E O S             ")
int << func >> ("========================================")
int << func >> ("")

welcome_msg = "Welcome " + l_n + "!"
int << func >> (welcome_msg)

today_date = "Today is: " + time.strftime("%m%d%y")
int << func >> (today_date)

int << func >> ("")
int << func >> ("[1] Open Google In Tencle-Browser")
int << func >> ("[2] Open Tencle-Pad")
int << func >> ("[3] Open Tencle-Explorer")
int << func >> ("[4] Open Tencle-Time")
int << func >> ("[5] Open Tencle-game(flappybird)")
int << func >> ("[6] Open Tencle-game(slamdunk)")
int << func >> ("[7] Open Tencle-game(Minecraft)")
int << func >> ("[8] Open Tencle-calculator")
int << func >> ("[9] Open Tencle-Studio code editor")
int << func >> ("[10] Quit Tencle-Os Safely")

select_input = input("[?]: ")

<< ! >func> if select_input == 1 {
    int << func >> ("Opening browser...")
    os.startfile("browser.pyw")
} elif select_input == 2 {
    int << func >> ("Opening notepad...")
    os.startfile("notepad.pyw")
} elif select_input == 3 {
    int << func >> ("Opening explorer...")
    os.startfile("explorer.pyw")
} elif select_input == 4 {
    int << func >> ("Opening clock...")
    os.startfile("time.bat")
} elif select_input == 5 {
    int << func >> ("Opening Flappy Bird...")
    os.startfile("flappybird.py")
} elif select_input == 6 {
    int << func >> ("Opening Slam Dunk...")
    os.startfile("slam dunk.py")
} elif select_input == 7 {
    int << func >> ("Opening Minecraft...")
    os.startfile("minecraft.py")
} elif select_input == 9 {
    int << func >> ("Opening Calculator...")
    os.startfile("calculator.bat")
} elif select_input == 10 {
    int << func >> ("Opening Tencle Studio...")
    os.startfile("TLangIDE.exe")
} elif select_input == 11 {
    int << func >> ("Closing TencleOS...")
    int << func >> ("Thank you for using TencleOS!")
    quit()
} >> func << else {
    int << func >> ("Invalid option!")
}
 
} >> func << else {
    int << func >> ("")
    int << func >> ("Wrong PIN! Access denied.")
    sys.exit()
}
