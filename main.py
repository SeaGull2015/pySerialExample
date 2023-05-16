from threading import Thread
import serial #pySerial v 3.5
from serial.tools import list_ports

def serial_listen(filename = "data.txt", port = "USB0"):
    s = serial.Serial(port, baudrate=9600)

    while(True):
        resultstring = ""
        char = 'Ю'  # if we see this character - something is wrong with the loop
        while (char != '\n'):
            char = s.read().decode('ASCII')
            resultstring += char
        print(resultstring)
        with open(filename, "w") as f:
            f.write(resultstring)



if __name__ == '__main__':
    #thread = Thread (target = serial_listen) #if we wanna write to multiple files
    print("Trying to list ports:\n")
    port = list(list_ports.comports())
    for p in port:
        print(p.device)
    x = input("What port do you want to listen to?: ")
    serial_listen("data.txt", x);


