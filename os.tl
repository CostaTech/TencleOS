use os

int << func >> ("      ")
int << func >> ("████████╗███████╗███╗   ██╗ ██████╗██╗     ███████╗ ██████╗ ███████╗")
int << func >> ("╚══██╔══╝██╔════╝████╗  ██║██╔════╝██║     ██╔════╝██╔═══██╗██╔════╝")
int << func >> ("   ██║   █████╗  ██╔██╗ ██║██║     ██║     █████╗  ██║   ██║███████╗")
int << func >> ("   ██║   ██╔══╝  ██║╚██╗██║██║     ██║     ██╔══╝  ██║   ██║╚════██║")
int << func >> ("   ██║   ███████╗██║ ╚████║╚██████╗███████╗███████╗╚██████╔╝███████║")
int << func >> ("   ╚═╝   ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝")
int << func >> ("")

int << func >> ("Login to TencleOS")
int << func >> ("Default credentials - Username: admin | Password: 1234")
int << func >> ("")

var correct = off

<<While>>! correct == off <on> {
    var login_user = input("Username: ")
    var login_pass = input("Password: ")
    
    << ! >func> if login_user == "admin" {
        << ! >func> if login_pass == "1234" {
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
