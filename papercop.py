import tempfile, os, shutil, zipfile, re, pickle

def execute(years, roll):
	#If there already exists a file with the same name.
	try:
		os.remove(' temp.zip ')
	except:
		pass
	#roll = raw_input()

	#Processing the Roll Number
	if int(roll[0:2]) == 14:
		k = 0
	else:
		k = (14-int(roll[0:2]))*2-1
	inp = roll[2:4]
	ext = ''
	if int(roll[4]) == 1:
		ext = ''
	elif int(roll[4]) == 3:
		ext = '1'
	inp = inp+ext

	#After processing the roll number, retrieving the required Pickle File 
	#with all the corresponding subject numbers.
	with open("./Pickle/"+inp+'.pickle','rb') as restoremydata:
	    a_list = pickle.load(restoremydata)

	#Looping over all the subjects
	for x in range(len(a_list[k])):
	    a_list[k][x] = a_list[k][x]+".pdf"
	#make a temporary directory to store the files
	dirpath = tempfile.mkdtemp()
	pattern = re.compile("\d{4}")
	years_lop = []

	#as the string is unicode, its difficult to read, hence a if else for 
	#everything to make the requried array of required years.
	if '2011' in years:
		years_lop.append('2011')

	if '2010' in years:
		years_lop.append('2010')

	if '2012' in years:
		years_lop.append('2012')

	if '2013' in years:
		years_lop.append('2013')

	#looping over the required folders
	for key in years_lop:
		for lookfor in a_list[k]:
			for root, dirs, files in os.walk( './Files/peqp/'+key+'/'):
			    if lookfor in files :
				pat=os.pathjoin(root,lookfor)
				shutil.copy(pat,dirpath)
				head,tail=os.path.split(pat)
				match=re.search(pattern,pat)
				rname=pat[match.start():match.end()]
				os.rename(dirpath+'/'+tail,dirpath+"/"+rname+'_'+tail)

	#add files to the zipfile
	zf = zipfile.ZipFile('temp.zip', mode = 'a')
	for root1,dirs1,files1 in os.walk(dirpath):
	    for f in files1:
		zf.write(os.path.join(root1,f),os.path.basename(os.path.join(root1,f)))
	zf.close()

	#close the remporary directory
	shutil.rmtree(dirpath)

	#Complete the process by returning the required zipfile.
	return os.path.abspath('temp.zip')



