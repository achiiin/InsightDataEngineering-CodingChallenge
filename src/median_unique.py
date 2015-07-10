import argparse
import bisect  # Maintains a list in sorted order without having to call sort 
               # each time an item is added to the list.

parser = argparse.ArgumentParser(description="")

parser.add_argument("inputfile", type=str, help="the path of input file")
parser.add_argument("outputfile", type=str, help="the path of output file")

args = parser.parse_args()
#args = parser.parse_args('./tweet_input/tweets.txt ./tweet_output/ft2.txt'.split())
###===================================================================================###
SCRIPT_NAME = "IDS_challange_2"
SCRIPT_VERSION = "v1.0"
REVISION_DATE = "2015-07-08"
AUTHOR = "Ching-Yen (chingyen@buffalo.edu)"
DESCRIPTION = ""
## Input ##
file_input = args.inputfile
## Output ##
directory_output = "../tweet_output"
file_output_1 = "ft1.txt"  # Calculate the total number of times each word has been tweeted.
file_output_2 = "ft2.txt"  # Calculate the median number of unique words per tweet, and update
                           # this median as tweets come in.

###===================================================================================###



def median(num_1,list_1):
    if num_1 % 2 == 0:
        index = int(num_1/2)
        return list_1[index]
    else:
        index = int((num_1 - 1)/2)
        num_2 = (list_1[index]+list_1[index+1]) / 2.0
        str_1 = str(num_2)
        return float(str_1[:str_1.find('.')+3])
        
txt_out = open(args.outputfile, 'a')   
    
with open(file_input) as f:
    list_number = []
    num_line = 0
    for line in f:  
        Words = set(line.split(" "))
        bisect.insort(list_number, len(Words))
        txt_out.write("%.2f \n"%(median(num_line,list_number)))
        num_line += 1
        
txt_out.close()