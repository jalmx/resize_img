#!e
_A='extension'
from os.path import sep,isdir,isfile
from os import listdir
from pathlib import Path
from sys import argv,exit
from PIL import Image
import fnmatch
HELP='\nScript to resize images to 1000px height, from folder or one file, support PNG, JPEG\n\nHOW TO USE:\n\n    rsize image.png\n    rsize .\n    rsize /home/user/Pictures \n    \nIf you want to change something, you have to modify the script\n\n'
def get_path_abs(path_raw):
	A=Path(path_raw)or Path('.')
	if not A.is_absolute():return A.absolute()
	return A
def get_name(full_path):'\n    ';A=full_path.split(sep)[-1];return{'name':A.split('.')[0],_A:A.split('.')[-1]}
def search_type(name_file):
	A=['png','jpeg','jpg']
	for B in A:
		if fnmatch.fnmatch(name_file,f"*.{B}"):return True
	return False
def read_files_from_folder(path):
	B=listdir(path)
	for A in B:
		if search_type(A):rsize(A)
def rsize(path,height_base=1000):
	D=height_base;B=path;G=get_path_abs(B);A=Image.open(G)
	if A.height>D:C=D/A.height;H=int(A.height*C);I=int(A.width*C);E=A.resize((I,H));F=f"{get_name(B)['name']}_r.{get_name(B)[_A]}";E.save(F);print(f"Factor: {C}");print(f"File saved: {get_path_abs(F)}");return E
	return A
def cli():
	if len(argv)<2 or len(argv)>2:print(HELP);exit(1)
	A=argv[1]
	if A=='--help':print(HELP);exit(0)
	try:
		if isdir(A):print(get_path_abs(A));read_files_from_folder(A)
		else:rsize(A)
	except Exception as B:print(B);print(HELP);exit(1)
	exit(0)
def main():cli()
if __name__=='__main__':main()