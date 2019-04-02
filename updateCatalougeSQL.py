import csv

print("***BIP Catalouge Update Tool***")

catNum = str(input("Please Enter Catalouge Number: "))                #catalouge number

#ipfile = str(input("Please Enter Full Path To CSV Input File: "))
#opfile = str(input("Please Enter Full Path To TXT Output File: "))

ipfile = r"C:\Users\lubhayan\Documents\Clients\Internal\BIP Scripts\CSV Edit of AF M3 to IFS Parts Codes.csv"                   #r = raw string, don't need to escape charachters
opfile = r"C:\Users\lubhayan\Documents\Clients\Internal\BIP Scripts\SQL_Output.txt"


with open(ipfile, 'r') as csv_file:                     #open file to read from (with auto closes files)
    csv_reader = csv.reader(csv_file)                   #read as csv

    next(csv_reader)                                    #ignore header line

    with open(opfile,'w') as new_file:                  #open output file

        for line in csv_reader:                         #loop through lines
            old_id1 = line[0]                        #first value from left
            new_id1 = line[1]                        #second value from left
            new_descr = line[2]                      #third value from left

            #print(old_id1 + "|" + new_id1 + "|" + new_descr)

            statement = "UPDATE ctlg_obj SET ID1='" + new_id1 + "', " + "DESCR='" + new_descr + "' WHERE CTLG_NR='" + catNum + "' AND ID1 = '" + old_id1 + "';\n"
            #print(statement)
            new_file.write(statement)

print("***Complete***")
