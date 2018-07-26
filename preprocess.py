from multiprocessing import Pool
import re
import string
import sys

translator=str.maketrans('','',string.punctuation)

def processline(line):
    line = line.strip().lower()
    line=line.translate(translator)
    line = re.sub('“|”', ' ', line)
    line = re.sub(' +', ' ', line)

    spaceline = line
    line = re.sub(' ', '', line)
    return line +','+ spaceline

if __name__ == '__main__':
    fin = sys.argv[1]
    fout = sys.argv[2]

    fin = open(fin)
    lines = fin.readlines()

    p = Pool(5)
    lines = p.map(processline, lines)

    fout = open(fout, 'w')
    fout.write('\n'.join(lines))
