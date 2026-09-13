#!/usr/bin/env python3
_H='Error. Is your input a valid text? Or it your output_input path?'
_G='cipher.sh'
_F='Error. Perhaps you forgot to specify an output path?'
_E='decipher.sh'
_D='Contact me to gain Full-Access (FA) to use this program without waiting.'
_C='bin'
_B=None
_A='store_true'
VER='hexinator v.0.0.4 LA'
import argparse,subprocess,time,os
BASE=os.path.dirname(os.path.abspath(__file__))
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
		print(_D);time.sleep(10)
		if args.output and args.output_input is not _B:
			with open(args.output_input+'.txt','w')as f:res=subprocess.run([os.path.join(BASE,_C,_E),args.output_input],stdout=f)
			if res.returncode!=0:print('Error. Is your output_input a valid hex?');exit(res.returncode)
		elif args.output:print(_F)
		else:
			result=subprocess.run([os.path.join(BASE,_C,_E),args.input])
			if result.returncode!=0:print('Error. Is your input a valid hex? Or it your output_input path?');exit(result.returncode)
	elif args.text and args.input is not _B:
		print(_D);time.sleep(10)
		if args.output and args.output_input is not _B:
			with open(args.output_input+'.txt','w')as f:res=subprocess.run([os.path.join(BASE,_C,_G),args.output_input],stdout=f)
			if res.returncode!=0:print(_H);exit(res.returncode)
		elif args.output:print(_F)
		else:
			result=subprocess.run([os.path.join(BASE,_C,_G),args.input])
			if result.returncode!=0:print(_H);exit(result.returncode)
	else:print("There was an error. Try filling the input argument if you're not using -h or -v")
except KeyboardInterrupt:print('\nQuitting hexinator...\nThank you for using my tool.');exit(0)
