import serial
import sys
from SerialList import serial_ports
from datetime import datetime
# added comment
avaliblePorts = serial_ports()

if len(avaliblePorts) == 0:
    print('No avalible ports')
    exit()
 
print('Avalible ports :- ')
for port_i in range(len(avaliblePorts)):
    print(str(port_i + 1) + ')' + avaliblePorts[port_i])

ind = input('Choose port number : ')

try:
    indint = int(ind)
    avaliblePorts[indint-1]
except:
    print('Wrong Input')
    exit()

baud = int(input("Enter BaudRate : "))

s = serial.Serial(avaliblePorts[indint-1] ,baud  )


file = open('log.txt' , 'w')

while 1:    
    serial_data = s.readline().decode('ascii','replace')
    timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S.%f")
    file.write(timestamp + ' > ' + serial_data)
    sys.stdout.write(timestamp + ' > ' + serial_data)




