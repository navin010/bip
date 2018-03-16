import csv

print("***BIP Catalouge Translation Tool***")

cat1 = str(input("Please Enter Catalouge Number 1: "))                #catalouge 1
cat2 = str(input("Please Enter Catalouge Number 2: "))                #catalouge 2
dict = str(input("Please Enter Translation Dictionary Number: "))     #dictionary

ipfile = str(input("Please Enter Full Path To CSV Input File: "))
opfile = str(input("Please Enter Full Path To TXT Output File: "))

#ipfile = r"C:\PyCharm\Projects\BIP\conversion.csv"                   #r = raw string, don't need to escape charachters
#opfile = r"C:\PyCharm\Projects\BIP\SQL_Output.txt"


with open(ipfile, 'r') as csv_file:                     #open file to read from (with auto closes files)
    csv_reader = csv.reader(csv_file)                   #read as csv

    next(csv_reader)                                    #ignore header line

    with open(opfile,'w') as new_file:                  #open output file

        for line in csv_reader:                         #loop through lines
            cat1_value = line[0]                        #left value
            cat2_value = line[1]                        #right value

            new_file.write("insert into cor_obj values(SQ_COR_OBJ_NR.nextval, " + cat1 + ", " + cat2 + ", " + dict + ", " "(select nr from ctlg_obj where ctlg_nr = " + cat1 + " and id1 = '" + cat1_value + "'), (select nr from ctlg_obj where ctlg_nr = " + cat2 + " and id1 = '" + cat2_value + "'));" + "\n")             #write sql statement out followed by line feed

