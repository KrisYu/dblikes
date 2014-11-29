import os
import re

infile = open('time.txt')
outfile = open('timedeal.txt','w')

outfile.write('date')
outfile.write(',')
outfile.write('time')
outfile.write('\n')

for line in infile.readlines():
	line = line.strip()
	try:
		date, time = line.split()
		if not '年' in date:
			date = str('2014年') + date
		
		#提取出来
		date = re.findall('[0-9]{4}\u5e74.*[0-9]*.\u6708',date)[0]
		date = date.replace('年','/')
		date = date.replace('月','')
		outfile.write(date)
		outfile.write(',')
		
		outfile.write(time)
		outfile.write('\n')
	except:
		outfile.write(line)






