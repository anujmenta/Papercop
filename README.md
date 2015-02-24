# Papercop
The Question Paper portal of IIT Kharagpur

#How it all happened

Step 1 :
- Dump all the papers from the library site. ( Simply mirror the site)
- Rename all the papers with the subject numbers for uniformity and search purposes. ( Using the script "threemasters.py" )
- Manually rename some papers which are left out because of exceptions

Step 2:
- Make encoded data to be used to determine the subjects in a particular semester of particular department.
- We used pickle files to store data.
- Each pickle files contains a list of lists corresponding to every department.

#How it works
- It processes the input ( Roll number) for all the requred fields i.e Department and Semester number.
- Uses this information to load the corresponding pickle file.
- Use the semester number to obtain the list of subjects in that semester.
- Call "papercop.py" to do the rest.
- Rest: copy requred files into temporary directory, zip it and output it to the user as an attachment. 


#Example:
- Input: "12MA20007"
- Pickle file required : "MA2.pickle"
- Semester number =  (14-(12))*2 + 2(Spring Semster)
- Obtains list = ['Subject 1.pdf', 'Subject 2.pdf']
Do the rest.
