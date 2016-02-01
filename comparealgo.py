f9000= file('C:\Users\Kimia\Desktop\Algo_Results_9000_analysed.csv', 'r')
f300= file('C:\Users\Kimia\Desktop\Algo_Loc_300.csv', 'r')
fcomp= file('C:\Users\Kimia\Desktop\Py_Compare.csv', 'w')

c9000 = csv.reader(f9000)
c300 = csv.reader(f300)
ccomp = csv.writer(fcomp)


masterlist = list(c9000)

for loc_row in c300:
	row = 1
	found = False 
	for master_row in masterlist:
		results_row = loc_row
		if loc_row[6] == master_row[1] and loc_row[1] == master_row[6]:
			score = master_row[2]
			results_row.append(score)
			found = True
			break
		row = row+1
	if not found:
		results_row.append('ERROR, not found in master')
	ccomp.writerow(results_row)
f9000.close()
f300.close()
fcomp.close()
	

