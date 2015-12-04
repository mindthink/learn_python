def add(a,b):
	print "adding %d +%d" %(a,b)	
        return a+b

def substract(a,b):
	print "subtracting %d -%d "%(a,b)
	return a-b

def multiply(a,b):
	print "MULTIPLAYING %d * %d"%(a,b)
	return a*b

def divide(a,b):
	print "DIVISSION %d / %d" %(a,b)
	return a/b

print "lets's do some with just functions!"

age=add(30,50)
height=substract(78,4)
weight=multiply(90,2)
ip=divide(100,2)

print "Age: %d,height:%d,weight:%d,iq:%d"%(age,height,weight,ip)

print "here is a puzzle"

what =add(age,substract(height,multiply(weight,divide(ip,2))))

print "that become:",what,"can you do it by hand?"

