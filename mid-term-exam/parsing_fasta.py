# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file)
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght
# Use separate functions for the input and the output


'''
Pseudo-code:
-parse the fasta records using on the '>' sign
-return only the records that do not contain the string 'OS=Homo sapiens'

-save those record in a new file
-using regular expressions find the organism name in those records (after OS before GN)
-concatenate the strings of the sequence and compute length
-print organism and sequence length
'''
import re

def parsing_fasta():
    records = get_fasta_records()
    #empty element at the beginning because of
    records.pop(0)

    with open("no_sapiens.fasta","w") as f:
        for r in records:
            f.write(">" + r) #re-insert the > sign at the beginning

    for r in records:
        #split lines on \n to separate header and sequence
        x = r.split("\n")

        # find organism in header, reads from "OS=" to the next value "GN"
        org = re.search("OS=*([^GN]+)",x[0]).group(0)

        # concatenate sequence and compute lenght
        seq = ""
        for i in range(1,len(x)):
            seq = seq + x[i]

        print("source organism: %s, sequence length: %d" % (org, len(seq)) )

def get_fasta_records():
    # read records and split them on each header (> sign)
    with open('sprot_prot.fasta.txt') as f:
        records = f.read()
        records = records.split(">")
    # create list of non sapiens records
    no_sapiens = []
    for r in records:
        # -1 means string not found
        if(r.find("OS=Homo sapiens") == -1):
            no_sapiens.append(r)
    return no_sapiens
