import os
import time

terminal_start_message = "──────────────Script Start──────────────"
terminal_end_message = "───────────────Script End───────────────"

print(terminal_start_message)

__currentscript__ = os.path.basename(__file__)
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

print("write 'quit' to quit, write 'list' to get content")

def get_content(shutdown_timer):
    loop = True
    while loop == True:
        file = input("file-name: ").lower()
        if file == "ls" or file == "list" or file =="dir":
            os.system("cd " + __location__)
            print("────DIRECTORY────")
            for i in os.listdir(__location__):
                if i == __currentscript__:
                    continue
                print(i)
            print("─────────────────")
        else:
            os.system(os.path.join(__location__, file))
        if file == "quit" or file == "exit":
            loop = False
            print("Quitting Script..")
            time.sleep(shutdown_timer)
            print(terminal_end_message)

get_content(1)