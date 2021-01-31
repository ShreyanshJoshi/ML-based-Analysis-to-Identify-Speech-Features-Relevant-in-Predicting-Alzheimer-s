file1 = open("files.txt","r")
csvfile=open("sentence.csv",'a')
csvfile.write('File,N,V,Q,S\n')
for i in file1:
	final = open('sentence/'+i[:-1],"r")
	a=i[:5]+'.cha,'
	for x in final.readlines()[-6:-2]:
		a+=x[4:-1] + ','
	a=a[:-1]+'\n'
	csvfile.write(a)
