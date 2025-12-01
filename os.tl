use os
use time

os.system("pip install PyQt5 PyQtWebEngine")

int << func >> ("      ")
int << func >> ("████████╗███████╗███╗   ██╗ ██████╗██╗     ███████╗ ██████╗ ███████╗")
int << func >> ("╚══██╔══╝██╔════╝████╗  ██║██╔════╝██║     ██╔════╝██╔═══██╗██╔════╝")
int << func >> ("   ██║   █████╗  ██╔██╗ ██║██║     ██║     █████╗  ██║   ██║███████╗")
int << func >> ("   ██║   ██╔══╝  ██║╚██╗██║██║     ██║     ██╔══╝  ██║   ██║╚════██║")
int << func >> ("   ██║   ███████╗██║ ╚████║╚██████╗███████╗███████╗╚██████╔╝███████║")
int << func >> ("   ╚═╝   ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝")
int << func >> ("")

int << func >> ("")
int << func >> ("[1] Continue with the setup.")
int << func >> ("[2] I've Already Done The Setup.")
int << func >> ("")

var setup = input("[?]: ")

<< ! >func> if setup == "1" {
    var name = input("Please enter your Username: ")
    var pas = input("Please enter your password to login: ")
    
    var f = open("user/username.txt", "w")
    f.write(name)
    f.close()
    
    var f2 = open("user/password.txt", "w")
    f2.write(pas)
    f2.close()
    
    int << func >> ("Setup Complete!")
    os.startfile("main-os.py")
    time.sleep(3)
    quit()
    
} elif setup == "2" {
    var login_pass = open("user/password.txt", "r")
    var l_p = login_pass.read()
    login_pass.close()
    
    var login_name = open("user/username.txt", "r")
    var l_n = login_name.read()
    login_name.close()
    
    var running = on
    <<While>>! running <on> {
        var login = input("Please enter the password for " + l_n + " Username: ")
        << ! >func> if login == l_p {
            os.startfile("main-os.py")
            quit()
        } >> func << else {
            int << func >> ("Wrong Password!")
        }
    }
    
} >> func << else {
    int << func >> ("Invalid option selected. Exiting.")
    quit()
}
