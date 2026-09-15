#!/usr/bin/env python3
_J='Error. Is your input a valid text? Or it your output_input path?'
_I='cipher.sh'
_H='Deciphrated message shown to screen.'
_G='Error. Perhaps you forgot to specify an output path?'
_F='decipher.sh'
_E='Contact me to gain Full-Access (FA) to use this program without waiting.'
_D='--output'
_C='bin'
_B=None
_A='store_true'
VER=' hexinator v.0.0.5 LA'
import argparse,subprocess,time,os
BASE=os.path.dirname(os.path.abspath(__file__))
parser=argparse.ArgumentParser(description="Copyright (C) 2026. This is a tool for all the lazy or workaholic Linux users. It makes you cipher and decipher hex-encoded lines with ease in a very lightweight tool. You're currently on LA (Limited Access), so you'll have a delay of 10 seconds.")
parser.add_argument('input',help='The input field for your hex/text',nargs='?')
parser.add_argument('output_input',help='The input field for your -o flag',nargs='?')
parser.add_argument('-o',_D,help='The output input field is used only if you choose to write the results to a file',nargs='?')
parser.add_argument('-v','--version',help='Gives user current version',action=_A)
parser.add_argument('-x','--hex',help='Used to specify an hex for the input argument\nhex->text',action=_A)
parser.add_argument('-t','--text',help='Used to specify a text for the input argument\ntext->hex',action=_A)
parser.add_argument('-s',_D,help="Saves output to file. We'll append the .txt extension ourselves",action=_A)
parser.add_argument('-e','--verbose',help='Documentated output',action=_A)
args=parser.parse_args()
try:
	if args.version:print(VER)
	elif args.hex and args.input is not _B:
		print(_E);time.sleep(10)
		if args.output and args.output_input is not _B:
			if args.verbose:print(f"Saving {args.input} to {args.output_input}...")
			with open(args.output_input+'.txt','w')as f:res=subprocess.run([os.path.join(BASE,_C,_F),args.input],stdout=f)
			if res.returncode!=0:print('Error. Is your output_input a valid hex?');exit(res.returncode)
			if args.verbose:print(f"File {args.output_input} saved successfully.")
		elif args.output:print(_G)
		else:
			if args.verbose:print(f"Printing {args.input}'s translation...")
			result=subprocess.run([os.path.join(BASE,_C,_F),args.input])
			if result.returncode!=0:print('Error. Is your input a valid hex? Or it your output_input path?');exit(result.returncode)
			if args.verbose:print(_H)
	elif args.text and args.input is not _B:
		print(_E);time.sleep(10)
		if args.output and args.output_input is not _B:
			if args.verbose:print(f"Saving {args.input} to {args.output_input}...")
			with open(args.output_input+'.txt','w')as f:res=subprocess.run([os.path.join(BASE,_C,_I),args.input],stdout=f)
			if res.returncode!=0:print(_J);exit(res.returncode)
			if args.verbose:print(f"File {args.output_input} saved successfully.")
		elif args.output:print(_G)
		else:
			if args.verbose:print(f"Deciphering {args.input}...")
			result=subprocess.run([os.path.join(BASE,_C,_I),args.input])
			if result.returncode!=0:print(_J);exit(result.returncode)
			if args.verbose:print(_H)
	else:print("There was an error. Try filling the input argument if you're not using -h or -v")
except KeyboardInterrupt:print('\nQuitting hexinator...\nThank you for using my tool.');exit(0)
