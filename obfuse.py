import os
import sys

def alter(filename, algorithm):
	with open(filename, 'rb+') as file:
		file_bytes = file.read()
		file.seek(0)
		altered_bytes = bytes([algorithm(byte) for byte in file_bytes])
		file.write(altered_bytes)

def obfuscate(filename):
	alter(filename, lambda byte: (byte+1)%256)

def clarify(filename):
	alter(filename, lambda byte: (byte-1)%256)

mode = sys.argv[1]
names = sys.argv[2:]

if mode == "obfuscate":
	method = obfuscate
elif mode == "clarify":
	method = clarify

def alter_dir(dirname):
	for root, dirs, files in os.walk(dirname, topdown=False):
		for filename in files:
			method(os.path.join(root, filename))
		for dirname in dirs:
			alter_dir(os.path.join(root, dirname))

for name in names:
	if os.path.isfile(name):
		method(name)
	elif os.path.isdir(name):
		alter_dir(name)