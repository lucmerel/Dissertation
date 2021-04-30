import can #module used to enable and virtualise CAN communications
from textwrap import wrap #wrap function used to split string
import json #formats data correctly
import base64 #convert data to base64 format and back
import time

def encrypt():                    #the message intended to be sent on the
	combo = (key + msg + key) #CAN-bus has a key added to it
	invert = combo[::-1] #the order of characters is flipped
	encoded = invert.encode('ascii') #the ascii is encoded to the byte data type
	b64_en = base64.b64encode(encoded) #this data is converted to base64
	b64_ = b64_en.decode('ascii') #base64 characters are converted back to a string
	asciii = (list(map(ord, b64_))) #the string is converted to their ascii character codes
	maths = [x+7 for x in asciii] # e.g. (0x97 = a). These ascii values have 7 added to them.
	encrypt.result = "".join([chr(a) for a in maths]) #This encryption is done now it is converted 
							#back to a string ready to be sent on a bus.
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
	asciii2 = (list(map(ord, implement.string))) #this converts the received can message to ascii values
	undo_maths = [x-7 for x in asciii2] #this is the opposite of the encryption
	b64_ = "".join([chr(a) for a in undo_maths]) #converts back to string
	b64_de = base64.b64decode(b64_) #this undoes the base64 encoding 
	decoded = b64_de.decode('ascii') #the data is converted from byte type to string
	revert = decoded[::-1] #the strings order must be reversed again
	decrypt.msg = revert[3:-3] #this removes the prepended and appended encryption key.
	
	
if __name__ == "__main__":
	begin_time = time.process_time() #gets the current time in ms
	bus1 = can.interface.Bus(bustype='virtual', bitrate=1000000) #defines the virtual CAN-buses
	bus2 = can.interface.Bus(bustype='virtual', bitrate=1000000) #bitrate = 1mbps
	msg = "1CF#80050000003C" #an example of a typical message that might be sent on a CAN-bus
	key = "zfz" #the key used in cryptographic functions
	#encrypt() #calls the encrypt function
	encrypted = str(msg) #converts the data to string under a new variable name ##encrypt.result
	thelist = wrap(encrypted, 8) #this imported function splits the data into groups of 8 characters per list element.
	#print (thelist)
	#print(encrypted)
	implement() #calls the main function passing messages on the bus/
	#print (implement.string)
	#decrypt() #calls the decrypt function
	#print (decrypt.msg)
	print (time.process_time() - begin_time) #gets the time in ms and takes it away from the time at the beginning 
						#this determines how long it took for the entire program to execute




