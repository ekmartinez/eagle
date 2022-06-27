import os
import sys
import nmap
import psutil
import pandas as pd
from ipwhois import IPWhois

class Eagle:
    def __init__(self, target):
        self.target = target
        
    def setter(self):
        new_target = input("Enter new target: ")
        self.target = new_target

    def dialog(self):
        input('\n' + 'Press any key to return to menu >>\n')
        os.system('cls') 

    def flying(self):
        print("\nEagle is flying & assessing situation. \nJust a moment.....")

    def pin_point(self):
        """Identifies connected computers in the local network"""
        self.flying()
        nm = nmap.PortScanner()
        nm.scan(hosts=f"{self.target}/24", arguments="-n -sP")
        
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

        for host, status in hosts_list:
            print(host + ' ' + status)

    def open_ports(self):
        """Shows open ports"""
        pass

    def connectionsWho(self):
        """Displays local processes connected to the outside"""
        print('\nGetting information, please wait......\n')   
        tempConnect = pd.DataFrame(psutil.net_connections())
        connects = pd.DataFrame(tempConnect.loc[tempConnect['status'] == "ESTABLISHED"])
        
        processName = []
        for process in connects['pid']:
            p = psutil.Process(process)
            processName.append(p.name())
            
        localAddress, localPort = [], []
        for ip in connects['laddr']:
            localAddress.append(ip[0])
            localPort.append(ip[1])
            
        remoteAddress,remotePort = [], []
        for ip in connects['raddr']:
            remoteAddress.append(ip[0])
            remotePort.append(ip[1])
        
        d = {
            'Local' : localAddress, 
            'lport' : localPort, 
            'Remote': remoteAddress, 
            'rport' : remotePort, 
            'Process' : processName
            }
            
        tempMoment = pd.DataFrame(d)
        moment = pd.DataFrame(tempMoment.loc[tempMoment['Remote'] != "127.0.0.1"])
        
        entity = []
        for ent in moment['Remote']:
            obj = IPWhois(ent)
            who = obj.lookup_whois()
            entity.append(who['asn_description'])
            
        moment['Entity'] = entity
        moment.reset_index(drop=True, inplace=True)
        print(moment)
        print(('-' * 100) + '\n')
        
        
        
    def fly(self):
        os.system('cls')
        while(True):    
            print('\n' + '-'*115)
            print(('*'*47) + '  `````\Eagle/`````  ' + ('*'*47))
            print(('-'*115) + '\n')
            option = input(f'''

        Options for {self.target}:

            (1)  -  Pin devices connected to my network.
            (2)  -  View connections to the outside.
            (3)  -  Perform a basic nmap port scan.
            (4)  -  Enter a new target.
            (5)  -  Exit.

        Choose an option >>> ''')        

            if option == '1':
                print(self.pin_point())
                self.dialog()
            elif option == '2':
                self.connectionsWho()
                self.dialog()
            elif option == '3':
                pass
            elif option == '4':
                self.setter()
                os.system('cls')
            elif option == '5':
                os.system('cls')
                sys.exit()


def target():
    os.system("cls")
    target = input("\n`````\__Eagle__/`````: To begin enter target address for recon: ")
    return target

if __name__ == '__main__':
    eagle = Eagle(target())
    eagle.fly()

