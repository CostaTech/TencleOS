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

var login_user = input("Username: ")
var login_pass = input("Password: ")

<< ! >func> if login_user == "admin" {
    << ! >func> if login_pass == "1234" {
        int << func >> ("")
        int << func >> ("Login successful! Starting TencleOS...")
        int << func >> ("")
        os.startfile("main-os.bat")
    } >> func << else {
        int << func >> ("")
        int << func >> ("Wrong password! Access denied.")
    }
} >> func << else {
    int << func >> ("")
    int << func >> ("Username not found! Access denied.")
}
