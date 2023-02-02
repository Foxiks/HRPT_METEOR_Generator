import binascii, time
from manchester_code import encode
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input binary CADU file")
parser.add_argument("-o", "--output", help="Output binary CADU file with manchester code")
parser.add_argument("-c", "--chunk", help="Chunk size (1 Chunk = 4 bits)")
args = parser.parse_args()

inputfile = args.input
outfile = args.output
line = int(args.chunk)
line2 = int(args.chunk)
backline = 0
size = os.path.getsize(inputfile)
p1 = size/100
with open(outfile, 'w') as f1:
    f1.write('')
k = 0
start_time = time.time()
print("-------------------------------------------------")
print("                                                 ")
print("            Binary Manchester encoder            ")
print("                 by Egor UB1QBJ                  ")
print("                                                 ")
print("-------------------------------------------------")
print("Reading input")
with open(inputfile, 'rb') as f:
    x = f.read()
print("Encoding")
while True:
    if(line <= size*2):
        x1 = x[backline:line]
        backline = line
        line += line2
        manchester_code = encode(x1)
        nman = (''.join(f'{m:08b}' for m in manchester_code))
        try:
            data = '%08X' % int(nman, 2)
        except ValueError:
            print("")
            print("Done!", end='\r')
            print(str(time.time()-start_time))
            break
        progress = os.path.getsize(outfile)
        print("Writing output. Progress: " + str(int((progress/p1)/2)) + "%", end='\r')
        with open(outfile, 'ab') as f:
            binstr = binascii.unhexlify(data)
            f.write(binstr)

