import can
import ast
from textwrap import wrap
import json

def implement():
	recvd = ""
	recvdlist = []
	for i in range(len(thelist)):
		inputt = (thelist[i])
		asciii = list(map(ord,str(inputt)))
		send = str(asciii)
		msg = bytes(send, 'utf-8')
		msg1 = can.Message(arbitration_id=0x12345, data = msg)
		try:
			bus1.send(msg1)
			print ("message sent on {}".format(bus1.channel_info))
		except can.CanError:
			print("Error, message not sent")
		msg2 = bus2.recv()
		recvd = (msg2.data)
		fixed = json.loads(recvd)
		letters = "".join([chr(c) for c in fixed])
		print (letters)
		recvdlist = recvdlist + [recvd]
	print (recvdlist)

if __name__ == "__main__":
	bus1 = can.interface.Bus(bustype='virtual', bitrate=1000000) #defines the virtual CAN-buses
	bus2 = can.interface.Bus(bustype='virtual', bitrate=1000000) #bitrate = 1mbps
	mesg = "XT~TKH~TKH8TKH;P7aKT_w=lq`V[j<TZ;~Ur~U[\<T[`" #example encrypted message.
	thelist = wrap(mesg, 8)	#wrap function splits the data to groups of 8 characters per list element
	print (thelist)	
	implement() #calls the function


