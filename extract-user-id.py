import re 

file = "*.html"

infilename = "user_id_new.txt"
outfilename = "user_id_new_1.txt"

with open(file, "r", encoding="utf-8") as f:
    fin = f.read()
    output = re.findall("data-user-id=\"(.*?)\"", fin)
    print(output)

fout = open(infilename, "a", encoding='utf-8')
for item in output:
    fout.write(item)
    fout.write("\n")

fout.close()

lines_seen = set()
outfile = open(outfilename, "w")
for line in open(infilename, "r"):
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

count = len(open(outfilename).readlines(  ))
print("Number of user IDs are {}".format(count))
