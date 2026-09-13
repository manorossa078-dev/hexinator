#!/usr/bin/env python3
_D='Error. Perhaps you forgot to specify an output path?'
_C='Contact me to gain Full-Access (FA) to use this program without waiting.'
_B=None
_A='store_true'
VER='hexinator v.0.0.3 LA'
import argparse,subprocess,time
parser=argparse.ArgumentParser(description="This is a tool for all the lazy or workaholic Linux users. It makes you cipher and decipher hex-encoded lines with ease in a very lightweight tool. You're currently on LA (Limited Access), so you'll have a delay of 10 seconds.")
parser.add_argument('input',help='The input field for your hex/text',nargs='?')
parser.add_argument('output_input',help='The output input field is used only if you choose to write the results to a file',nargs='?')
parser.add_argument('-v','--version',help='Gives user current version',action=_A)
parser.add_argument('-x','--hex',help='Used to specify an hex for the input argument\nhex->text',action=_A)
parser.add_argument('-t','--text',help='Used to specify a text for the input argument\ntext->hex',action=_A)
parser.add_argument('-o','--output',help="Saves output to file. We'll append the .txt extension ourselves",action=_A)
args=parser.parse_args()
try:
	if args.version:print(VER)
	elif args.hex and args.input is not _B:
		print(_C);time.sleep(10)
		if args.output and args.output_input is not _B:
			with open(args.output+'.txt','w')as f:subprocess.run(['./bin/decipher.sh',args.input],stdout=f)
		else:print(_D)
	elif args.text and args.input is not _B:
		print(_C);time.sleep(10)
		if args.output and args.output_input is not _B:
			with open(args.output+'.txt','w')as f:subprocess.run(['./bin/cipher.sh',args.input],stdout=f)
		else:print(_D)
	else:print("There was an error... Try filling the input argument if you're not using -h or -v")
except KeyboardInterrupt:print('\nQuitting hexinator...\nThanks you for using my tool.');exit(0)
