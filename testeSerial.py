#!/usr/bin/python

import time, serial, io

i=4480

ser = serial.Serial('/dev/ttyUSB0', 2000000, timeout=30, rtscts=True)
ser.flush()
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding='ascii', newline='\r')

# Open a file
fo = open('string', 'r')
string = fo.read();

# Close opend file
fo.close()

stringLen = len(string)
print '\nInput file size: %d Bytes' % stringLen
print 'SDcard file size: %d Bytes' % (stringLen*i)

try:
	for y in range (9):

		timeNameFile=str(int(time.time()))[2:10]

		print '\nOPW %s' % timeNameFile
		ser.write('OPW %s\r' % timeNameFile)
		print sio.readline()

		print 'WRF %d' % (stringLen*i)
		ser.write('WRF %d\r' % (stringLen*i))
		for x in range(i):
			ser.write(string)
		print sio.readline()

		print 'CLF %s' % timeNameFile
		ser.write('CLF %s\r' % timeNameFile)
		print sio.readline()

	print str(int(time.time()))[2:10]+'\n'

except KeyboardInterrupt:
	print('cancelled')
	ser.close()

ser.close()

