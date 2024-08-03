cmd = ""
isStarted = False;

while True:
    cmd = input("=> ").lower()
    if cmd == "help":
        print("""
start - to start the car
stop  - to stop the car
quit  - to exit                            
""")
    elif cmd == "start":
        if isStarted:
            print("Car is already running..")
        else:
            isStarted = True
            print("Car started..")
    elif cmd == "stop":
        if not isStarted:
            print("Car is already stopped..")
        else:
            isStarted = False
            print("Car stopped.!")
    elif cmd == "quit":
        print("Exit!")
        break
    else:
        print("You're enter a wrong command!!")    
