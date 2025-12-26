# TencleOS Shell v2.1 - Directory Navigation
# Supports cd and run commands

use os

# Get current directory by checking marker files
<< ! >func> if os.path.exists(".current_Apps") {
    var current_dir = "T:\\TencleOS\\Apps"
} elif os.path.exists(".current_Games") {
    var current_dir = "T:\\TencleOS\\Games"
} elif os.path.exists(".current_System") {
    var current_dir = "T:\\TencleOS\\System"
} >> func << else {
    var current_dir = "T:\\TencleOS"
}

# Build prompt and get command
<< ! >func> if current_dir == "T:\\TencleOS" {
    var command = input("T:/TencleOS> ")
} elif current_dir == "T:\\TencleOS\\Apps" {
    var command = input("T:/TencleOS/Apps> ")
} elif current_dir == "T:\\TencleOS\\Games" {
    var command = input("T:/TencleOS/Games> ")
} >> func << else {
    var command = input("T:/TencleOS/System> ")
}

# Parse command for arguments using simple string operations
<< ! >func> if command.startswith("cd ") {
    var cmd = "cd"
    var arg = command.replace("cd ", "", 1)
} elif command.startswith("run ") {
    var cmd = "run"
    var arg = command.replace("run ", "", 1)
} elif command.startswith("echo ") {
    var cmd = "echo"
    var arg = command.replace("echo ", "", 1)
} >> func << else {
    var cmd = command
    var arg = ""
}

<< ! >func> if cmd == "help" {
    int << func >> ("")
    int << func >> ("TencleOS Shell v2.1 - Available Commands")
    int << func >> ("========================================")
    int << func >> ("SYSTEM")
    int << func >> ("  help        - Show this help")
    int << func >> ("  ver         - Show version")
    int << func >> ("  sysinfo     - System information")
    int << func >> ("  about       - About TencleOS")
    int << func >> ("  cls/clear   - Clear screen")
    int << func >> ("  exit/quit   - Exit shell")
    int << func >> ("")
    int << func >> ("NAVIGATION")
    int << func >> ("  cd <dir>    - Change directory (Apps, Games, System)")
    int << func >> ("  cd ..       - Go to parent directory")
    int << func >> ("  dir/ls      - List files in current directory")
    int << func >> ("  pwd         - Show current directory")
    int << func >> ("  tree        - Directory tree")
    int << func >> ("")
    int << func >> ("APPLICATIONS")
    int << func >> ("  run <app>   - Run application in current directory")
    int << func >> ("  apps        - List all apps")
    int << func >> ("")
    int << func >> ("UTILITIES")
    int << func >> ("  echo <text> - Print text")
    int << func >> ("  credits     - Show credits")
    int << func >> ("========================================")
    int << func >> ("")
    
} elif cmd == "ver" {
    int << func >> ("")
    int << func >> ("TencleOS Shell v2.1 [Build 1.2.0]")
    int << func >> ("TLang Interpreter v1.1")
    int << func >> ("(c) 2025 CostaTech Corporation")
    int << func >> ("")
    
} elif cmd == "sysinfo" {
    int << func >> ("")
    int << func >> ("System Information")
    int << func >> ("  OS - TencleOS v2.1")
    int << func >> ("  Kernel - TLang v1.1")
    int << func >> ("  Shell - DOS-style Terminal")
    int << func >> ("  Applications - 12 installed")
    int << func >> ("  Current Directory - " + current_dir)
    int << func >> ("")
    
} elif cmd == "about" {
    int << func >> ("")
    int << func >> ("TencleOS - The TLang Operating System")
    int << func >> ("Version 2.1 [Build 1.2.0]")
    int << func >> ("")
    int << func >> ("A custom operating system built with TLang,")
    int << func >> ("featuring a DOS-style shell with directory navigation")
    int << func >> ("and 12 integrated applications.")
    int << func >> ("")
    int << func >> ("Developed by CostaTech - 2025")
    int << func >> ("")
    
} elif cmd == "cls" {
    int << func >> ("[Screen cleared]")
    
} elif cmd == "clear" {
    int << func >> ("[Screen cleared]")
    
} elif cmd == "cd" {
    << ! >func> if arg == "" {
        int << func >> ("Usage - cd <directory>")
        int << func >> ("Available - Apps, Games, System, ..")
    } >> func << else {
        var target = arg
        
        << ! >func> if target == ".." {
            launch("cd_root")
        } elif target == "Apps" {
            launch("cd_Apps")
        } elif target == "Games" {
            launch("cd_Games")
        } elif target == "System" {
            launch("cd_System")
        } >> func << else {
            int << func >> ("Directory not found - " + target)
        }
    }
    
} elif cmd == "dir" {
    int << func >> ("")
    int << func >> ("Directory of " + current_dir)
    int << func >> ("========================================")
    
    << ! >func> if current_dir == "T:\\TencleOS" {
        int << func >> ("  <DIR>  Apps          - Applications")
        int << func >> ("  <DIR>  Games         - Games")
        int << func >> ("  <DIR>  System        - System files")
        int << func >> ("========================================")
        int << func >> ("  3 folder(s)")
        
    } elif current_dir == "T:\\TencleOS\\Apps" {
        int << func >> ("  TLangIDE.exe         - Code editor")
        int << func >> ("  calculator.tl        - Calculator app")
        int << func >> ("  browser.pyw          - Web browser")
        int << func >> ("  notepad.pyw          - Text editor")
        int << func >> ("  explorer.pyw         - File manager")
        int << func >> ("  time.tl              - Clock")
        int << func >> ("========================================")
        int << func >> ("  6 file(s)")
        
    } elif current_dir == "T:\\TencleOS\\Games" {
        int << func >> ("  snake.tl             - Snake game")
        int << func >> ("  flappybird.tl        - Flappy Bird")
        int << func >> ("  minecraft.py         - Minecraft clone")
        int << func >> ("  slam dunk.py         - Basketball game")
        int << func >> ("========================================")
        int << func >> ("  4 file(s)")
        
    } elif current_dir == "T:\\TencleOS\\System" {
        int << func >> ("  <DIR>  tlang         - TLang interpreter")
        int << func >> ("  os.tl                - Shell script")
        int << func >> ("========================================")
        int << func >> ("  1 folder(s), 1 file(s)")
    }
    
    int << func >> ("")
    
} elif cmd == "ls" {
    int << func >> ("")
    
    << ! >func> if current_dir == "T:\\TencleOS" {
        int << func >> ("Apps/  Games/  System/")
    } elif current_dir == "T:\\TencleOS\\Apps" {
        int << func >> ("TLangIDE.exe  calculator.tl  browser.pyw  notepad.pyw  explorer.pyw  time.tl")
    } elif current_dir == "T:\\TencleOS\\Games" {
        int << func >> ("snake.tl  flappybird.tl  minecraft.py  slam dunk.py")
    } elif current_dir == "T:\\TencleOS\\System" {
        int << func >> ("tlang/  os.tl")
    }
    
    int << func >> ("")
    
} elif cmd == "pwd" {
    int << func >> ("")
    int << func >> (current_dir)
    int << func >> ("")
    
} elif cmd == "tree" {
    int << func >> ("")
    int << func >> ("T:\\TencleOS")
    int << func >> ("|-- Apps/")
    int << func >> ("|   |-- TLangIDE.exe")
    int << func >> ("|   |-- calculator.tl")
    int << func >> ("|   |-- browser.pyw")
    int << func >> ("|   |-- notepad.pyw")
    int << func >> ("|   |-- explorer.pyw")
    int << func >> ("|   |-- time.tl")
    int << func >> ("|-- Games/")
    int << func >> ("|   |-- snake.tl")
    int << func >> ("|   |-- flappybird.tl")
    int << func >> ("|   |-- minecraft.py")
    int << func >> ("|   |-- slam dunk.py")
    int << func >> ("|-- System/")
    int << func >> ("|   |-- tlang/")
    int << func >> ("|   |-- os.tl")
    int << func >> ("")
    
} elif cmd == "apps" {
    int << func >> ("")
    int << func >> ("Installed Applications")
    int << func >> ("========================================")
    int << func >> ("Apps Folder")
    int << func >> ("  - TLangIDE      (Code editor)")
    int << func >> ("  - calculator    (Math operations)")
    int << func >> ("  - browser       (Web browsing)")
    int << func >> ("  - notepad       (Text editing)")
    int << func >> ("  - explorer      (File management)")
    int << func >> ("  - time          (Clock)")
    int << func >> ("")
    int << func >> ("Games Folder")
    int << func >> ("  - snake         (Classic game)")
    int << func >> ("  - flappybird    (Arcade game)")
    int << func >> ("  - minecraft     (Block building)")
    int << func >> ("  - slamdunk      (Basketball game)")
    int << func >> ("========================================")
    int << func >> ("Navigate with - cd Apps / cd Games")
    int << func >> ("Then run with - run <appname>")
    int << func >> ("")
    
} elif cmd == "run" {
    << ! >func> if arg == "" {
        int << func >> ("Usage - run <application>")
        int << func >> ("Type 'apps' to see available applications")
    } >> func << else {
        var app = arg
        
        # Check if in Apps folder
        << ! >func> if current_dir == "T:\\TencleOS\\Apps" {
            << ! >func> if app == "studio" or app == "TLangIDE" {
                int << func >> ("[Launching TLang IDE...]")
                launch("studio")
            } elif app == "calc" or app == "calculator" {
                int << func >> ("[Launching Calculator...]")
                launch("calc")
            } elif app == "browser" {
                int << func >> ("[Launching Browser...]")
                launch("browser")
            } elif app == "notepad" {
                int << func >> ("[Launching Notepad...]")
                launch("notepad")
            } elif app == "explorer" {
                int << func >> ("[Launching Explorer...]")
                launch("explorer")
            } elif app == "time" {
                int << func >> ("[Launching Clock...]")
                launch("time")
            } >> func << else {
                int << func >> ("Application '" + app + "' not found in Apps folder")
            }
            
        # Check if in Games folder
        } elif current_dir == "T:\\TencleOS\\Games" {
            << ! >func> if app == "snake" {
                int << func >> ("[Launching Snake Game...]")
                launch("snake")
            } elif app == "flappybird" {
                int << func >> ("[Launching Flappy Bird...]")
                launch("flappybird")
            } elif app == "minecraft" {
                int << func >> ("[Launching Minecraft...]")
                launch("minecraft")
            } elif app == "slamdunk" {
                int << func >> ("[Launching Slam Dunk...]")
                launch("slamdunk")
            } >> func << else {
                int << func >> ("Game '" + app + "' not found in Games folder")
            }
            
        } >> func << else {
            int << func >> ("Cannot run applications from " + current_dir)
            int << func >> ("Navigate to Apps or Games folder first")
            int << func >> ("Use - cd Apps  or  cd Games")
        }
    }
    
} elif cmd == "credits" {
    int << func >> ("")
    int << func >> ("TencleOS Credits")
    int << func >> ("========================================")
    int << func >> ("Developer - CostaTech")
    int << func >> ("Language - TLang v1.1")
    int << func >> ("Year - 2025")
    int << func >> ("")
    int << func >> ("Special thanks to")
    int << func >> ("  - TLang Community")
    int << func >> ("  - All beta testers")
    int << func >> ("========================================")
    int << func >> ("")
    
} elif cmd == "exit" {
    int << func >> ("")
    int << func >> ("Goodbye!")
    launch("exit")
    
} elif cmd == "quit" {
    int << func >> ("")
    int << func >> ("Goodbye!")
    launch("exit")
    
} elif cmd == "" {
    # Empty command - do nothing
    
} >> func << else {
    var msg = "'" + command + "' not recognized. Type 'help'"
    int << func >> (msg)
}
