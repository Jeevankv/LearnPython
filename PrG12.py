
#deleting word in file
infile = "messy_data_file.txt"
outfile = "cleaned_file.txt"

delete_list = ["word_1", "word_2", "word_n"]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()