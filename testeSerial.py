import time, serial, io

i=3200*60*7
testStr='123456789012345678901234567890123456789012'
print '\nFile size: %d Bytes' % (i*len(testStr))

ser = serial.Serial('/dev/ttyUSB0', 2000000, timeout=10, rtscts=True)
ser.flush()

sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding='ascii', newline='\r')

for y in range (0, 9):

	timeNameFile=str(int(time.time()))[2:10]

	print '\nOPW %s' % timeNameFile
	ser.write('OPW %s\r' % timeNameFile)
	print sio.readline()

	print '\nWRF %d' % (i*len(testStr))
	ser.write('WRF %d\r' % (i*len(testStr)))
	for x in range(0, i):
		start_time = time.time()
		ser.write(testStr)
		print time.time() - start_time
	print sio.readline()

	print '\nCLF %s' % timeNameFile
	ser.write('CLF %s\r' % timeNameFile)
	print sio.readline()
	print '\n'



ser.close()

