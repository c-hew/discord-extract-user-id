 import time
startTime = time.time()
import re
from os import listdir
from os.path import isfile, join
mypath = "./"
infilename = "user_id_new.txt"
outfilename = "user_id_new_1.txt"
fout = open(infilename, "a", encoding='UTF8')
for file in listdir(mypath):
    if isfile(join(mypath, file)) and file.endswith('.html'):
        with open(file, "r", encoding="utf-8") as f:
            fin = f.read()
            output = re.findall("data-user-id=\"(.*?)\"", fin)
            usertag = re.findall("class=\"chatlog__author-name\" title=\"(.*?)\"", fin)
            new_obj = list(zip(output, usertag))
        for item in new_obj:
            fout.write(item[0])
            fout.write(":")
            fout.write(item[1])
            fout.write("\n")
fout.close()
print("It took {0:2f} seconds to finish running.".format(time.time() - startTime))
