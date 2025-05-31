
while True:
    print("------------------------------------")
    signal = input("\nEnter the traffic signal (red/yellow/green/quit): \n")

    if (signal == 'red'):
        print("stop")

    elif (signal == 'yellow'):
        print("ready")
    elif (signal == 'green'):
        print("go")

    elif (signal == 'quit'):
        print("************closing************")
        print("------------------------------------")

        break
    else:
        print("invalid signal")
