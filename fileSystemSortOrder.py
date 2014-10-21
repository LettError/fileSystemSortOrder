
"""

	For the rare occasion you'd like to test how your
	file system sorts unicode names.

	It will generate a file for each character between
	the minValue and maxValue. 

	Needless to say, if you tell this script to make
	a lot of files, your filesystem might reach some
	sort of implementation limit and tell you it did
	not like it.


"""
import unicodedata
import os

skip = [47, 127]

r = os.getcwd()
p = os.path.join(r, "sortOrderTestFiles")
if not os.path.exists(p):
	os.makedirs(p)

minValue = 32
maxValue = 500	# edit these for more / fewer files
for i in range(minValue, maxValue):
	if i in skip:
		continue
	c = unichr(i)
	try:
		name = unicodedata.name(c)
	except ValueError:
		name = "?"

	filename = u"%s\t%d\t0x%x\t%s"%(c, i, i, name)
	#print name
	f = open(os.path.join(p, filename), 'w')
	f.write(name)
	f.close()