from sys import argv

script ,input_file=argv

#print all file 
def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

#print one line
def print_a_line(line_count,f):
	print line_count,f.readline()

#open a file
current_file=open(input_file)

#carry on the print_all()
print_all(current_file)

print "Now let's rewind,kind of like a tape."

rewind(current_file)

print "Lets' print three lines:"

current_line =1

print_a_line(current_line,current_file)

current_line+=1
print_a_line(current_line,current_file)

current_line+=1
print_a_line(current_line,current_file)

