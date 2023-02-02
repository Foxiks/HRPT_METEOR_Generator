import bitstring, os, sys
import numpy as np
sync='0000001000011000101001111010001110010010110111011001101010111111'
time = '0000000000000000000000000000000000101111'
sp_info=''.join(str(x) for x in np.random.randint(low=0, high=2, size=(176)))
calib=str('0'*120)
last=str('0'*80)
n = 0
lines = int(os.path.getsize("out.hrpt")*8)/94320
file_mixed = open('out.hrpt', 'rb').read()
mixed = bitstring.ConstBitStream(file_mixed)
while(int(lines)>=int(n)):
    try:
        img_c1= mixed.read(94320).bin
    except bitstring.ReadError:
        sys.exit()
    sp_info=''.join(str(x) for x in np.random.randint(low=0, high=2, size=(176)))
    fr1 = sync+time+sp_info+calib+img_c1+last
    with open('out.hrpt_mn2', 'ab') as file:
        bitstring.BitArray(bin=str(fr1)).tofile(file)
    n+=1
    print('Lines: '+ str(n), end='\r')