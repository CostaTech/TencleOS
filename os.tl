use os

int << func >> ("      ")
int << func >> ("████████╗███████╗███╗   ██╗ ██████╗██╗     ███████╗ ██████╗ ███████╗")
int << func >> ("╚══██╔══╝██╔════╝████╗  ██║██╔════╝██║     ██╔════╝██╔═══██╗██╔════╝")
int << func >> ("   ██║   █████╗  ██╔██╗ ██║██║     ██║     █████╗  ██║   ██║███████╗")
int << func >> ("   ██║   ██╔══╝  ██║╚██╗██║██║     ██║     ██╔══╝  ██║   ██║╚════██║")
int << func >> ("   ██║   ███████╗██║ ╚████║╚██████╗███████╗███████╗╚██████╔╝███████║")
int << func >> ("   ╚═╝   ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝")
int << func >> ("")

var username = "admin"
var password = "1234"

int << func >> ("Login to TencleOS")
int << func >> ("")

var correct = off

<<While>>! correct == off <on> {
    var login_user = input("Username: ")
    var login_pass = input("Password: ")
    
    << ! >func> if login_user == username {
        << ! >func> if login_pass == password {
            int << func >> ("")
            int << func >> ("Login successful! Starting TencleOS...")
            int << func >> ("")
            os.startfile("main-os.bat")
            correct = on
        } >> func << else {
            int << func >> ("Wrong password! Try again.")
            int << func >> ("")
        }
    } >> func << else {
        int << func >> ("Username not found! Try again.")
        int << func >> ("")
    }
}
