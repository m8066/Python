testVar = raw_input("Enter something:")
print testVar

cnt1=0
for k in testVar:
	if k in 'iaueo':
		cnt1=cnt1+1

print cnt1

