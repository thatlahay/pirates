import sys,os,re,socket
import colorama,math
from time import sleep
colorama.init()
"""
"""
1.This program can be change at the member only
2.You can create your own member by coding
3.PirateS_OS
"""
def clear(self):
    os.system('cls' if os.name == 'nt' else 'clear')
#THE BOAT (Can update)
class boat():
    """
    1.This class can make we can swim  in the internet
    2.This is very important (Can keep in mind this is main_code)
    """
    def __init__(self):
        self.destination = ""
        self.port = 0
    def set_destinaton(self,destination):
        """
        1.This will set destination for our boat
        """
        self.destination = input("[?] Where  you want to go: ")
        self.port = input("[?] Port: ")
    def connect(self, ip,port):
        """
        1.This will make our boat go to the destination use socket library
        2.Always need set_destination
        """
        s = socket.socket()
        s.connect((ip,port))
class binary():
    """
    1.This class can help we about binary_code
    """
    def __init__(self):
        self.code = ""
    def decrypt(self):
        """
        1.This can decrypt binary code to decimal
        """
        self.code = str(input("[?] Please enter binary code: "))
        nummu = 0
        result = []
        for char in self.code[::-1]:
            num  = int(char)
            numa = math.pow(2,nummu)
            nummu = nummu + 1
            if num == 0:
                numa = 0
            result.append(int(numa))
        plus = sum(result)
        print(plus)
class coding_smart():
    """
    1.This class make coding is easy than
    """
    def __init__(self):
        print("[coding_smart] You cannot use this at now")
        self.text = "NONE"
    def smart_print(self,text):
        """
        1.This need param "text"
        2.This is beta and will complete soon
        """
        text = self.text
        return text
#We always need trust montain.
#She soure_code is rather intersting
#We need contruct
class command_main():
    def __init__(self):
        self.command = ""
    def bg(self,color):
        if color == "RED":
            print("\033[31m")
class montain():
    """
    1.This is an manager for our boar
    2.She is work for free
    3.She can check_status
    4.She do manager better than any member on this boat
    5.She can checking very nice
    6.She is secondary member in boat
    """
    def __init__(self):
        self.data = []
        self.name = "\033[32m[Montain-> My name is Montain ^-^!"

        print("\033[32m[Montain with happy react]-> Welcome Aboar captain ! ^-^ !\033[37m")
    #Checknet 
    def check_network(self):
        """
        1.Montain check network funcition
        2.Very nice
        """
        try:
            s = socket.socket()
            s.connect(("google.com",80))
            s.close()
            print("Network\t\tONLINE\033[37m")
            return True
        except:
            print("Network\t\t\033[31mOFFLINE\033[37m")
            return False
    def answer(self):
        return self.name
    def check_status(self):

        """
        1.This define will check status of our boar
        2.This will be usefully
        """
        print("\033[32mNAME\t\tSTATUS")
        self.check_network()
        print("\033[32mComputer\t\033[31mAT RISK")
#ALERT_BAT
class alert_bat():
    def __init__(self):
        self.name = "alert_bat"
        print("[alert_bat.exe with sad react]-> I only want you marry me.")
    def calculate(self,math_problem):
        result = math_problem
        return result
#Captain
class captain():
    """
    1.This can make we taught with member
    2.This will make our boat happy
    """
    def __init__(self):
        """
        1.WE NEED THIS GUY
        """
        self.command = ""

    def hello(self,members):
        """
        1.Make we can Hello members
        """
        print("[YOU] say hello to "+members)
    def make_command(self):
        """
        1.This will make you can make_command on your ship
        """
        command = input("[supire@captain] ")
        return command
    def arugamunt(self):
        #DO SOMETHING
        print('DO SOMETHING')
#IMPORT MEMBER FOR EACH JOB    
manager = montain()
tactician = alert_bat()
captain = captain()
#MAKE CHOICE FOR CAPTAIN
while True:
    command = captain.make_command()
    try:
        if command == "OK":
            print("[OK WHAT?] ")
        elif command == "checkship":
            print("[Montain] There is some information:")
            manager.check_status()
        elif command == "checknet":
            print("[Montain] There is some information")
        elif command == "bg":
            print('LOL')
        elif command == "ship":
            print("""
            Pirates_OS
            V_SHIP: 1.0
            S_FOR_USE: 12311
            OR WHERE FOR  SQL INJECTION
            """)
        elif command == "whatos":
            print('''
            This is an ship, not os
            ''')
        elif command == "map":
            """
            1.This will check map of network or something like the sea
            """
            print("MAP")
        elif command == "ifconfig":
            try:
                print("PUBLIC_IP: "+socket.gethostbyname(socket.gethostname()))
                print("NAME: "+socket.getfqdn())            
            except:
                print("Notwork now")
        elif command == "cls":
            print(chr(27) + "[2J",end="")
        else:   
            print("",end="")
    except:
        print("LAZY")
def main(asd):
    print("asd")
