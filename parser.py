import optparse
from sendingUDP import *
from receivingUDP import *

#parse arguments supplied
parser = optparse.OptionParser()
parser.add_option('-s', help='run as server (mandatory option)', dest='s',
    default=False, action='store_true')
parser.add_option('-r', help='run as receiver (mandatory option)', dest='r',
    default=False, action='store_true')
parser.add_option('-i', help='input file (-s required)', dest='i',
    action='store', type='string')
parser.add_option('-T', help='target host of receiver (-s required)', 
    dest='hostname', action='store', type='string')
parser.add_option('-o', help='output file (-r required)', dest='o',
    action='store', type='string')
parser.add_option('-w', help='window size (mandatory option)', dest='wsize',
    action='store', type='int')
parser.add_option('-t', help='timeout value (milliseconds, default[%default])',
    dest='timeout', action='store', type='int', default=20)
parser.add_option('-m', help='payload size (bytes, default[%default])', dest='payload',
    action='store', type='int', default=256)
    
(opts, args) = parser.parse_args()
#determines mandatory arguments
#determines dependencies of arguments
if opts.s and opts.r:
	print "you may only run as server or reciever\n"
	parser.print_help()
	exit(-1)
if not opts.s and not opts.r:
	print "you must select either to run as server or reciever\n"
	parser.print_help()
	exit(-1)
if not opts.wsize:
	print "missing options"
	parser.print_help()
	exit(-1)
if opts.s and not opts.hostname:
	print "missing options"
	parser.print_help()
	exit(-1)
if opts.s and not opts.i:
	print "missing options"
	parser.print_help()
	exit(-1)
if opts.r and not opts.o:
	print "you must select the output file\n"
	parser.print_help()
	exit(-1)
	
if opts.r:
	areceiver = Receiver(4483, opts.o, opts.wsize)
	
if opts.s:
	asender = Sender(opts.hostname, 4483, opts.i, opts.wsize, opts.payload)
