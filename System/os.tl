# TencleOS Shell - Single Command Mode
# The .bat file handles the loop

var command = input("T:\\TencleOS> ")

<< ! >func> if command == "help" {
    int << func >> ("")
    int << func >> ("TencleOS Shell v2.0 - Available Commands:")
    int << func >> ("========================================")
    int << func >> ("SYSTEM:")
    int << func >> ("  help        - Show this help")
    int << func >> ("  ver         - Show version")
    int << func >> ("  time        - Show date and time")
    int << func >> ("  sysinfo     - System information")
    int << func >> ("  about       - About TencleOS")
    int << func >> ("  cls/clear   - Clear screen")
    int << func >> ("  exit/quit   - Exit shell")
    int << func >> ("")
    int << func >> ("FILES:")
    int << func >> ("  dir/ls      - List files")
    int << func >> ("  pwd         - Current directory")
    int << func >> ("  tree        - Directory tree")
    int << func >> ("")
    int << func >> ("APPS:")
    int << func >> ("  apps        - List all apps")
    int << func >> ("  run <app>   - Run application")
    int << func >> ("  studio      - TLang IDE")
    int << func >> ("  calc        - Calculator")
    int << func >> ("  snake       - Snake game")
    int << func >> ("  browser     - Web browser")
    int << func >> ("  notepad     - Text editor")
    int << func >> ("")
    int << func >> ("UTILITIES:")
    int << func >> ("  echo <text> - Print text")
    int << func >> ("  color       - Color info")
    int << func >> ("  credits     - Show credits")
    int << func >> ("========================================")
    int << func >> ("")
    
} elif command == "ver" {
    int << func >> ("")
    int << func >> ("TencleOS Shell v2.0 [Build 1.1.0]")
    int << func >> ("TLang Interpreter v1.1")
    int << func >> ("(c) 2025 CostaTech Corporation")
    int << func >> ("")
    
} elif command == "time" {
    int << func >> ("")
    int << func >> ("[TIME COMMAND - Not yet implemented]")
    int << func >> ("Current time feature coming soon!")
    int << func >> ("")
    
} elif command == "sysinfo" {
    int << func >> ("")
    int << func >> ("System Information:")
    int << func >> ("  OS: TencleOS v2.0")
    int << func >> ("  Kernel: TLang v1.1")
    int << func >> ("  Shell: DOS-style Terminal")
    int << func >> ("  Applications: 12 installed")
    int << func >> ("")
    
} elif command == "about" {
    int << func >> ("")
    int << func >> ("TencleOS - The TLang Operating System")
    int << func >> ("Version 2.0 [Build 1.1.0]")
    int << func >> ("")
    int << func >> ("A custom operating system built with TLang,")
    int << func >> ("featuring a DOS-style shell interface and")
    int << func >> ("12 integrated applications.")
    int << func >> ("")
    int << func >> ("Developed by CostaTech - 2025")
    int << func >> ("")
    
} elif command == "cls" {
    int << func >> ("[Screen cleared]")
    
} elif command == "clear" {
    int << func >> ("[Screen cleared]")
    
} elif command == "dir" {
    int << func >> ("")
    int << func >> ("Directory of T:\\TencleOS")
    int << func >> ("========================================")
    int << func >> ("  <DIR>  Apps          - Applications")
    int << func >> ("  <DIR>  Games         - Games")
    int << func >> ("  <DIR>  System        - System files")
    int << func >> ("========================================")
    int << func >> ("  3 folder(s), 12 application(s)")
    int << func >> ("")
    
} elif command == "ls" {
    int << func >> ("")
    int << func >> ("Apps/  Games/  System/")
    int << func >> ("")
    
} elif command == "pwd" {
    int << func >> ("")
    int << func >> ("T:\\TencleOS")
    int << func >> ("")
    
} elif command == "tree" {
    int << func >> ("")
    int << func >> ("T:\\TencleOS")
    int << func >> ("|-- Apps/")
    int << func >> ("|   |-- TLangIDE.exe")
    int << func >> ("|   |-- calculator.bat")
    int << func >> ("|   |-- browser.pyw")
    int << func >> ("|   |-- notepad.pyw")
    int << func >> ("|-- Games/")
    int << func >> ("|   |-- snake.bat")
    int << func >> ("|   |-- minecraft.bat")
    int << func >> ("|   |-- slamdunk.bat")
    int << func >> ("|   |-- flappybird.tl")
    int << func >> ("|-- System/")
    int << func >> ("|   |-- tlang/")
    int << func >> ("|   |-- os.tl")
    int << func >> ("|   |-- os.bat")
    int << func >> ("")
    
} elif command == "apps" {
    int << func >> ("")
    int << func >> ("Installed Applications:")
    int << func >> ("========================================")
    int << func >> ("  1. Tencle-Browser    - Web browsing")
    int << func >> ("  2. Tencle-Pad        - Text editing")
    int << func >> ("  3. Tencle-Explorer   - File management")
    int << func >> ("  4. Snake             - Classic game")
    int << func >> ("  5. Calculator        - Math operations")
    int << func >> ("  6. Minecraft         - Block building")
    int << func >> ("  7. Slam Dunk         - Basketball game")
    int << func >> ("  8. Flappy Bird       - Arcade game")
    int << func >> ("  9. Tencle-Time       - Clock")
    int << func >> (" 10. TLang IDE         - Code editor")
    int << func >> ("========================================")
    int << func >> ("Type 'run <app>' or app name to launch")
    int << func >> ("")
    
} elif command == "studio" {
    int << func >> ("")
    int << func >> ("[Launching TLang IDE...]")
    launch("studio")
    
} elif command == "calc" {
    int << func >> ("")
    int << func >> ("[Launching Calculator...]")
    launch("calc")
    
} elif command == "snake" {
    int << func >> ("")
    int << func >> ("[Launching Snake Game...]")
    launch("snake")

} elif command == "flappybird" {
    int << func >> ("")
    int << func >> ("[Launching Flappy Bird...]")
    launch("flappybird")

} elif command == "minecraft" {
    int << func >> ("")
    int << func >> ("[Launching Minecraft...]")
    launch("minecraft")

} elif command == "slamdunk" {
    int << func >> ("")
    int << func >> ("[Launching Slam Dunk...]")
    launch("slamdunk")
    
} elif command == "browser" {
    int << func >> ("")
    int << func >> ("[Launching Browser...]")
    launch("browser")
    
} elif command == "notepad" {
    int << func >> ("")
    int << func >> ("[Launching Notepad...]")
    launch("notepad")
    
} elif command == "color" {
    int << func >> ("")
    int << func >> ("Terminal Color Codes:")
    int << func >> ("  Default console colors")
    int << func >> ("  TencleOS uses standard DOS palette")
    int << func >> ("")
    
} elif command == "credits" {
    int << func >> ("")
    int << func >> ("TencleOS Credits")
    int << func >> ("========================================")
    int << func >> ("Developer: CostaTech")
    int << func >> ("Language: TLang v1.1")
    int << func >> ("Year: 2025")
    int << func >> ("")
    int << func >> ("Special thanks to:")
    int << func >> ("  - TLang Community")
    int << func >> ("  - All beta testers")
    int << func >> ("========================================")
    int << func >> ("")
    
} elif command == "exit" {
    int << func >> ("")
    int << func >> ("Goodbye!")
    
} elif command == "quit" {
    int << func >> ("")
    int << func >> ("Goodbye!")
    
} elif command == "" {
    # Empty command
    
} >> func << else {
    msg = "'" + command + "' not recognized. Type 'help'"
    int << func >> (msg)
}
