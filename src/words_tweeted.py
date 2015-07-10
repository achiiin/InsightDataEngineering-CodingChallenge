import argparse
from functools import partial
import re
import collections
from collections import Counter

parser = argparse.ArgumentParser(description="")

parser.add_argument("inputfile", type=str, help="the path of input file")
parser.add_argument("outputfile", type=str, help="the path of output file")

args = parser.parse_args()
#args = parser.parse_args('./tweet_input/tweets.txt ./tweet_output/ft1.txt'.split())
###===================================================================================###
SCRIPT_NAME = "IDS_challange_1"
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

chunk_bytes = 524288000 # 500 Mb

###===================================================================================###



def read_in_chunks(size_in_bytes,list_1):
    with open(file_input) as f:
        text_prev = ''
        f_read = partial(f.read,size_in_bytes)
        for text in iter(f_read, ''):
            if not text.endswith('\n'):
                # if file contains a partial line at the end, then don't
                # use it when counting the substring count. 
                text, rest = text.rsplit('\n', 1)
                # pre-pend the previous partial line if any.
                text =  text_prev + text
                text_prev = rest
            else:
                # if the text ends with a '\n' then simple pre-pend the
                # previous partial line. 
                text =  text_prev + text
                text_prev = ''
            list_1.append(text)
        list_1.append(text_prev)
def fn_dic(list_1):
    dic_1 = {}
    for key in list_1:
        dic_1.setdefault(key,[]).append("1")
    return dic_1
def fn_len(dic_1):
    for key,value in dict.items(dic_1):
        dic_1[key] = len(value)
    return dic_1

list_split = []  
         
read_in_chunks(chunk_bytes,list_split) 

list_split = map(lambda x:re.split(" |\n",x),list_split)  # "|" is "or"
list_split = map(lambda x:fn_dic(x),list_split) # dictionaries in the list
list_split = map(lambda x:fn_len(x),list_split) # word and its number of occurances
list_split = reduce(lambda x,y:Counter(x)+Counter(y), list_split)

txt_out = open(args.outputfile, 'a')
list_split = collections.OrderedDict(sorted(list_split.items()))
for key,value in list_split.iteritems():
    txt_out.write("%s %s\n"%(key,value))
txt_out.close()

