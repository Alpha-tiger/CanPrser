import os


#C:\\Users\\thomas\\Documents\\Workspace Tom\\HEMS\\OLY-GEP-165K-2011.csv

currentWorkingDir = os.getcwd()

# location of the Canlog files
LogFilesDir = currentWorkingDir + "\\CanLogFiles"

# location to where the parsed files should be placed
ParsedFilesDir = currentWorkingDir + "\\Parsed"

#create a parsed Dir to place the file in
if not os.path.exists(ParsedFilesDir):
    os.makedirs(ParsedFilesDir)



# iterate through all the files

for filename in os.listdir(LogFilesDir):
    try:

        file = open(LogFilesDir+"\\"+filename, 'r', errors='replace')
        #lno is used to keep the line numbers
        newfile_flag=1

        filename=filename.split('.')
        print('Parsing {}'.format(filename[0]))
        lno=0
        for line in file:
            if lno>0 :
                spaceremovedline =line.replace(" ","")
                splitline = spaceremovedline.split("\t")
                if (len(splitline)>2) and splitline[0].isdigit():
                    #print (splitline)
                    with open(ParsedFilesDir+"\\"+filename[0]+"Raw.txt", "a") as text_file:
                        data = splitline[0]+","+splitline[2]+","+splitline[6]+","+splitline[7]+","+splitline[9]+","+splitline[10]+splitline[11]+splitline[12]+splitline[13]+splitline[14]+splitline[15]+splitline[16]+splitline[17]
                        print(data, file=text_file)
                        #print(data)
                        #newfile = 1 Indicates a new canlog file has been opened for parsing.

            lno = lno+1
            newfile_flag=0

    except  Exception:
       print (filename[0] +" could not be parsed")
