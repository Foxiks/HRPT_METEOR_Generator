import bitstring, os, sys
import numpy as np
sync='0000001000011000101001111010001110010010110111011001101010111111'
time = '0000000000000000000000000000000000101111'
sp_info=''.join(str(x) for x in np.random.randint(low=0, high=2, size=(176)))
calib=str('0'*120)
last=str('0'*80)
n = 0
print('Convert ch 1 to 10-bit pattern...')
file1 = open('ch1.bmp', 'rb').read()
b = bitstring.BitStream(file1).bin[9296:]
chunks = [b[i:i+8] for i in range(0, len(b), 8)]
chunks = [str+'00' for str in chunks]
print('Convert ch 2 to 10-bit pattern...')
file2 = open('ch2.bmp', 'rb').read()
b1 = bitstring.BitStream(file2).bin[9296:]
chunks1 = [b1[i:i+8] for i in range(0, len(b1), 8)]
chunks1 = [str+'00' for str in chunks1]
print('Convert ch 3 to 10-bit pattern...')
file3 = open('ch3.bmp', 'rb').read()
b2 = bitstring.BitStream(file3).bin[9296:]
chunks2 = [b2[i:i+8] for i in range(0, len(b2), 8)]
chunks2 = [str+'00' for str in chunks2]
print('Convert ch 4 to 10-bit pattern...')
file4 = open('ch4.bmp', 'rb').read()
b3 = bitstring.BitStream(file4).bin[9296:]
chunks3 = [b3[i:i+8] for i in range(0, len(b3), 8)]
chunks3 = [str+'00' for str in chunks3]
print('Convert ch 5 to 10-bit pattern...')
file5 = open('ch5.bmp', 'rb').read()
b5 = bitstring.BitStream(file5).bin[9296:]
chunks5 = [b5[i:i+8] for i in range(0, len(b5), 8)]
chunks5 = [str+'00' for str in chunks5]
print('Convert ch 6 to 10-bit pattern...')
file6 = open('ch6.bmp', 'rb').read()
b6 = bitstring.BitStream(file6).bin[9296:]
chunks6 = [b6[i:i+8] for i in range(0, len(b6), 8)]
chunks6 = [str+'00' for str in chunks6]
print('Mixing Channels...')
res = [x for y in zip(chunks, chunks1, chunks2, chunks3, chunks5, chunks6) for x in y]
with open('data.mixed', 'wb') as file:
    bitstring.BitArray(bin=''.join(res)).tofile(file)
lines = int(os.path.getsize("data.mixed"))
file_mixed = open('data.mixed', 'rb').read()
mixed = bitstring.ConstBitStream(file_mixed)
while(int(lines)>=int(n)):
    try:
        img_c11= mixed.read(10).bin
        img_c21= mixed.read(10).bin
        img_c31= mixed.read(10).bin
        img_c41= mixed.read(10).bin
        img_c51= mixed.read(10).bin
        img_c61= mixed.read(10).bin
        img_c12= mixed.read(10).bin
        img_c22= mixed.read(10).bin
        img_c32= mixed.read(10).bin
        img_c42= mixed.read(10).bin
        img_c52= mixed.read(10).bin
        img_c62= mixed.read(10).bin
        img_c13= mixed.read(10).bin
        img_c23= mixed.read(10).bin
        img_c33= mixed.read(10).bin
        img_c43= mixed.read(10).bin
        img_c53= mixed.read(10).bin
        img_c63= mixed.read(10).bin
        img_c14= mixed.read(10).bin
        img_c24= mixed.read(10).bin
        img_c34= mixed.read(10).bin
        img_c44= mixed.read(10).bin
        img_c54= mixed.read(10).bin
        img_c64= mixed.read(10).bin
    except bitstring.ReadError:
        os.remove('data.mixed')
        sys.exit()    
    fr1 = img_c11+img_c12+img_c13+img_c14+img_c21+img_c22+img_c23+img_c24+img_c31+img_c32+img_c33+img_c34+img_c41+img_c42+img_c43+img_c44+img_c51+img_c52+img_c53+img_c54+img_c61+img_c62+img_c63+img_c64
    with open('out.hrpt', 'ab') as file:
        bitstring.BitArray(bin=str(fr1)).tofile(file)
    n+=24
    print('Bytes: '+ str(n), end='\r')