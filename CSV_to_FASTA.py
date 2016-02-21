# PROGRAM TITLE: CSV_to_FASTA.py
# AUTHOR: 		   KESHAV DIAL
# USAGE:		     First, use Excel to generate your random genetic sequences
#				         in three seperate csv files. Place this file in the same
#				         directory as the csv files. Run this script and select the
#				         three csv files sequentially. This program will export the
#				         sequences in a single FASTA file named "local_blast.fasta".

import csv
import re
for i in ['FASTA1','FASTA2','FASTA3']:
	statment = 'Enter a CSV filename for '+i+": "
	filename = raw_input(statment)
	with open(filename, 'rb') as csvfile:
    		csv_temp = csv.reader(csvfile, delimiter=' ', quotechar='|')
    		temp = list(csv_temp)
	csvfile.close()
	FASTA = []
	map(FASTA.extend, temp)
	FASTA = ''.join(FASTA)
	FASTA = FASTA.replace(',', '')
	file = open("local_blast.fasta","a+")
	file.write('>'+i+'\n')
	file.write(re.sub("(.{80})", "\\1\n",FASTA, 0, re.DOTALL))
	if (i == 'FASTA1') or(i =='FASTA2'):
		file.write('\n')
