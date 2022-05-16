from argparse import *
from stegano import lsb
from PIL import Image
import base64
import base58
import pyfiglet



ascii_banner=pyfiglet.figlet_format("crypStego\n")
print(ascii_banner)

print(f'Author ---> Pr4bin Sigd3l\n.........................\n')



example_text = '''example:

 python3 crypStego.py -d -b64 -i "jshdksdshdhsjhd"
 '''
parser=ArgumentParser(description='Encoding ,decoding and steganography of given input......',epilog=example_text)

group=parser.add_mutually_exclusive_group()

group.add_argument('-e','--encode', action='store_true', help='encode')
group.add_argument('-d','--decode', action='store_true', help='decode ')
group.add_argument('-s','--steg', action='store_true', help='steganography ')


form=parser.add_mutually_exclusive_group()
form.add_argument('-b64','--base64',action='store_true', help=' to/from base64')
form.add_argument('-b58','--base58',action='store_true', help='to/from base658')
form.add_argument('-hx','--hex',action='store_true', help=' to/from hex')
form.add_argument('-r13','--rot13',action='store_true', help=' to/from rot13')
form.add_argument('-H','--hide',action='store_true', help=' hide data in image')
form.add_argument('-ex','--extract',action='store_true', help='extract data from image')

parser.add_argument('-i','--input',metavar='',type=str,help='Any input to decode/encode')
parser.add_argument('-I','--image',metavar='',help='Any image ')


args=parser.parse_args()


def base64_encode(text):
	byte_srt=text.encode("ASCII")
	b64_val=base64.b64encode(byte_srt)
	b64_str=b64_val.decode("ASCII")
	print(text +" : "+b64_str)

def base64_decode(text):
	byte_srt=text.encode("ASCII")
	b64_val=base64.b64decode(byte_srt)
	b64_str=b64_val.decode("ASCII")
	print(text +" : "+b64_str)


def base58_encode(text):
	byte_srt=text.encode("ASCII")
	b58_val=base58.b58encode(byte_srt)
	b58_str=b58_val.decode("ASCII")
	print(text +" : "+b58_str)

def base58_decode(text):
	byte_srt=text.encode("ASCII")
	b58_val=base58.b58decode(byte_srt)
	b58_str=b58_val.decode("ASCII")
	print(text +" : "+b58_str)


def hex_decode(hex_string):
	byt=bytes.fromhex(hex_string).decode("ASCII")
	print(hex_string + ": " +byt)

def hex_encode(text):
	hex_string=text.encode('utf-8').hex()
	print(text+" : "+hex_string)


def rot13_encode(text):
	dic1={'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4,
		'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9,
		'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14,
		'P' : 15, 'Q' : 16, 'R' : 17, 'S' : 18, 'T' :19,
		'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25}

	dic2={0 : 'N', 1 : 'O', 2 : 'P', 3 : 'Q', 4 : 'R', 5 : 'S',
		6 : 'T', 7 : 'U', 8 : 'V', 9 : 'W', 10 : 'X',
		11 : 'Y', 12 : 'Z', 13 : 'A', 14 : 'B', 15 : 'C',
		16 : 'D', 17 : 'E', 18 : 'F', 19 : 'G', 20 : 'H',
		21 : 'I', 22 : 'J', 23 : 'K', 24 : 'L', 25 : 'M'}  
	
	if text!='':
		s=text.replace(" ","").upper()
		ls=list(s)
		ci=""
		for n in ls:
			num=dic1[n]
			cipher_text=dic2[num]
			ci+=cipher_text
		cipher=ci.lower()
		print(cipher)	
		

def rot13_decode(txt):
	rot13_encode(txt)

def hide_steg(data,img1):
	img=Image.open(img1)
	img=img.convert("RGB")
	secret=lsb.hide(img,data)
	secret.save("./secret.png")
	print("[+]........successfully done")


def extract_steg(img2):
	img=Image.open(img2)
	img=img.convert("RGB")
	message=lsb.reveal(img)
	print("[+]........successfully done")
	print(f'secret message is :>{message}')


if __name__=='__main__':
	if args.decode:
		if args.base64:
			base64_decode(args.input)
		elif args.hex:
			hex_decode(args.input)
		elif args.rot13:
			rot13_decode(args.input)
		elif args.base58:
			base58_decode(args.input)	
	elif args.encode:
		if args.base64:
			base64_encode(args.input)
		elif args.hex:
			hex_encode(args.input)
		elif args.rot13:
			rot13_encode(args.input)
		elif args.base58:
			base58_encode(args.input)	


	if args.steg:
		if args.hide:
			hide_steg(args.input,args.image)
		elif args.extract:
			extract_steg(args.image)


















