# Cindy Hsin-Liu Kao, Media lab
# completed begineer and intermediate problem set.
from electiondata import ElectionResults

#test case
import unittest

def cmp_stats(csv_lines, new_csv_lines ):

	obama = [line.split(",")[3] for line in csv_lines]
	romney = [line.split(",")[5] for line in csv_lines]
	obama_percent = [line.split(",")[4] for line in csv_lines]
	romney_percent = [line.split(",")[6] for line in csv_lines]
	state_name = [line.split(",")[1] for line in csv_lines]

	total_state_name = [line.split(",")[4] for line in new_csv_lines]
	total_pop = [line.split(",")[9] for line in new_csv_lines]

	for i in state_name:
		for j in total_state_name:
			if i == j:
				pop_index =  total_state_name.index(j)
				percent_index = state_name.index(i) 
				new_obama_percent = round(float(obama[percent_index]) / float(total_pop[pop_index]), 3)	
				#print  romney[percent_index] + " " + total_pop[pop_index]	
				new_romney_percent = round(float(romney[percent_index]) / float(total_pop[pop_index]), 3)
				print "[" + j + "] " + "Obama new/old: " + str(new_obama_percent*100) + "/" + str(obama_percent[percent_index]) + ", Romney new/old: " + str(new_romney_percent*100) + "/" + str(romney_percent[percent_index])
	return obama[1]


def countLine(obama):
	return obama[0];

#opening '2012_US_election_state.csv'
f = open('2012_US_election_state.csv', 'r')
print "Opened file '2012_US_election_state.csv'"
all_lines = f.readlines()

def opensuccess(f):
	return f != ""

obama = [line.split(",")[3] for line in all_lines]
romney = [line.split(",")[5] for line in all_lines]

#opening 'NST_EST2012_ALLDATA.csv'
f2 = open('NST_EST2012_ALLDATA.csv', 'r')
print "Opened file 'NST_EST2012_ALLDATA.csv'"
f2_all_lines = f2.readlines()


#function for intermediate problem set
cmp_stats(all_lines, f2_all_lines)


# code for begineers problem set
obama_total = 0
romney_total = 0

import string

for o in obama:
	if o == "Obama vote": #skip
		oo = o
	else:
		o_int = int(o, 10)
		# print o_int
		obama_total = obama_total + o_int

for r in romney:
	if r == "Romney vote": #skip
		rr = r	
	else:
		r_int = int(r, 10)
		romney_total = romney_total + r_int
	
print "Obama total votes:" + str(obama_total) + " Romney total votes: " + str(romney_total)


def obama(obama_total):
	return obama_total

# import to json
import json

#create a dictionary
votes_result = {'Obama total vote' :  obama_total, 'Romney total vote' : romney_total}

with open('json_out.txt', 'w') as outfile:
	json.dump(votes_result, outfile)

print "done"
 

class ResultTest(unittest.TestCase):
	def test_Case(self):
		o_num = obama(obama_total)
		assert o_num == 51958250

# if this file is run directly, run the tests
if __name__ == "__main__":	
	unittest.main()
