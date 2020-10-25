
import os 
import shutil
path='/home/ogichi/Downloads'  
list_ = os.listdir(path)
for file_ in list_: 
	name, ext = os.path.splitext(file_) 
	ext = ext[1:] 
	if ext == '': 
        	continue 
	elif  ext=='jpg' or ext=='mp4' or ext=='mov':
		shutil.move('/home/ogichi/Downloads/'+name+'.'+ext, '/home/ogichi/Pictures')
	elif ext =='zip' or ext=='img' or ext=='AppImage':
		shutil.move('/home/ogichi/Downloads/'+name+'.'+ext, '/home/ogichi/software')
	elif  ext=='py':
		shutil.move('/home/ogichi/Downloads/'+name+'.'+ext, '/home/ogichi/pythonprojects')
	elif ext=='html':
		shutil.move('/home/ogichi/Downloads/'+name+'.'+ext, 'home/ogichi/htmlprojects')


