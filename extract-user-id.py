import re
import json
# Variables
infilename = "user_id_new.txt"
outfilename = "user_id_new_1.txt"
verbose = False
# Argument parser to help programs become more flexible.
import argparse
parser = argparse.ArgumentParser()


# Adds arguments
parser.add_argument('-o', action="store", dest='outfilename', help='Output the result to a filename specified.')
parser.add_argument('-v', action="store_true", default=False, dest='verbose', help='Verbose output.')

import time
startTime = time.time()
from os import listdir
from os.path import isfile, join
mypath = "./"


fout = open(infilename, "a", encoding='UTF8')
for file in listdir(mypath):
    if isfile(join(mypath, file)) and file.endswith('.html'):
        with open(file, "r", encoding="utf-8") as f:
            fin = f.read()

            output = re.findall("data-user-id=\"(.*?)\"", fin)
            usertag = re.findall("class=\"chatlog__author-name\" title=\"(.*?)\"", fin)

            new_obj = list(zip(output, usertag))

            if verbose == True:
                print(new_obj)
        for item in new_obj:
            if verbose == True:
                print("Writing to file...")
            fout.write(item[0])
            fout.write(":")
            fout.write(item[1])
            fout.write("\n")
fout.close()


# Display JSON data
json_obj = json.dumps(new_obj, indent=4)
print(json_obj)
# Print total running time
print("It took {0:2f} seconds to finish running.".format(time.time() - startTime))
