import can #module used to enable and virtualise CAN communications
from textwrap import wrap #wrap function used to split string
import json #formats data correctly
import base64 #convert data to base64 format and back
import time
from cryptography.fernet import Fernet
def encrypt():                    #the message intended to be sent on the
	#encode to binary
	message = msg
	encoded = message.encode()
	print (encoded)

	#encrypt
	f = Fernet(tkey)
	encrypt.result = f.encrypt(encoded)
	#return encrypted
def implement():
	recvd = "" #declare string
	data = [] #declare list
	for i in range(len(thelist)): #for-loop gets the groups of 8 bytes till it has pulled all data from the list
		inputt = (thelist[i]) #the 8 bytes are stored in the variable ready to be sent
		asciii = list(map(ord,str(inputt))) #the string is converted to ascii values to be sent on the bus
		send = str(asciii) #formats the data to be able to then convert to byte data type
		msg = bytes(send, 'utf-8') #message is converted to byte data type to be sent on the bus
		msg1 = can.Message(arbitration_id=0x12345, data = msg, is_extended_id=False) #generates the CAN-bus message.
		try: #this tries to send the message and returns if it is successful
			bus1.send(msg1)
			#print ("message sent on {}".format(bus1.channel_info))
			continue
		except can.CanError:
			#print("Error, message not sent")
			continue
		msg2 = bus2.recv() #the message is received on the second bus
		recvd = (msg2.data) #the data portion of the message is extracted
		fixed = json.loads(recvd) #the message's formatting is fixed using json
		letters = "".join([chr(c) for c in fixed]) #the ascii values are converted back to ascii characters
		data.append(str(letters)) #each 8 byte message that comes through the for loop is added to a list
	implement.string = "".join(data) #the list of 8 bytes are reconnected to one whole string

def decrypt():
	f2 = Fernet(key)
	help = encrypt.result
	#encoded = help.encode('ascii')
	decrypted = f2.decrypt(help)
	print (decrypted)
	decrypt.msg= decrypted.decode()
	
	
if __name__ == "__main__":
	begin_time = time.process_time() #gets the current time in ms
	bus1 = can.interface.Bus(bustype='virtual', bitrate=1000000) #defines the virtual CAN-buses
	bus2 = can.interface.Bus(bustype='virtual', bitrate=1000000) #bitrate = 1mbps
	msg = "1CF#80050000003C" #an example of a typical message that might be sent on a CAN-bus
	#key = "zfz" #the key used in cryptographic functions
	key = Fernet.generate_key()
	#print (key)

	file = open('key.txt', 'wb')
	file.write(key)
	file.close()

	file = open('key.txt', 'rb')
	tkey = file.read()
	file.close()
	#print (tkey)
	encrypt() #calls the encrypt function
	encrypted = str(msg) #converts the data to string under a new variable name ##encrypt.result
	thelist = wrap(encrypted, 8) #this imported function splits the data into groups of 8 characters per list element.
	#print (thelist)
	#print(encrypted)
	implement() #calls the main function passing messages on the bus/
	#print (implement.string)
	decrypt() #calls the decrypt function
	#print (decrypt.msg)
	print (time.process_time() - begin_time) #gets the time in ms and takes it away from the time at the beginning 
						#this determines how long it took for the entire program to execute




