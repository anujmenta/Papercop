import sys,re, os, shutil
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from cStringIO import StringIO


#Parses the PDF
def pdfparser(data,filed):
    fp = file(pat, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue()

    #Regular expression to compile strings of type 11FF11001
    pattern = re.compile('[A-Z]{2}\s*\d{5}')
    match = re.search(pattern, data)

    #try-except in case there is no such string
    try:
		s=match.start()
		e=match.end()
		return data[s:e].replace(' ','')
    except:
		return False
   

#main function
if __name__ == '__main__':
	#folders you want to span
    Arry=range(2013,2015)

    for xi in Arry:
	    rootdir="./Files/peqp/"#+str(xi)+"/"
	    count_rename=0
	    count_bad=0
	    #looping over the folders 
	    for root,dirsa,files in os.walk(rootdir):
			for name in files:
				pat=os.path.join(root,name)
				head,tail=os.path.split(pat)
				if name.endswith(".pdf"):
					#(for testing)print name
					rep = pdfparser(sys.argv[0],name)
					if rep:
						#(for testing)print rep
						#renames the file
						os.rename(pat,head+"/"+rep+".pdf")
						count_rename+=1
					else:
						try:
							count_bad+=1
							print "Bad File"						
							#(If you want to move the bad files somewhere else)
							#shutil.move(pat,"/home/kira/ThreeMasters/Exceptions/"+str(xi)+"/")
						except:
							pass
	    #just to keep track of numbers
	    print count_rename
	    print count_bad	
