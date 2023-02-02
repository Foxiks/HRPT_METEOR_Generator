import bitstring, os, sys
n = 0
k = 0
l = 0
lines = int(os.path.getsize("out.hrpt_mn2")*8)/7584
file_mixed = open('out.hrpt_mn2', 'rb').read()
mixed = bitstring.ConstBitStream(file_mixed)
while(int(lines)>=int(k)):
    mtvza=str('0'*1952)
    '11111011001110000110101001000101'
    with open('mtvza.pattern', 'ab') as file:
        bitstring.BitArray(bin=str('11111011001110000110101001000101'+mtvza)).tofile(file)
    k+=1
while(int(l)<=1500):
    with open('cadu.hrpt_mn2', 'ab') as file:
        tlm='00000000'
        bism='0000000000000000000000000000000000000000'
        sspd='00000000000000000000000000000000'
        mtvza='0000000000000000000000000000000000000000000000000000000000000000'
        data = '00011010110011111111110000011101'+tlm+bism+sspd+mtvza+str('0'*1904)+tlm+bism+sspd+mtvza+str('0'*1904)+tlm+bism+sspd+mtvza+str('0'*1904)+tlm+bism+sspd+mtvza+str('0'*1872)
        bitstring.BitArray(bin=str(data)).tofile(file)
    l+=1
file_mtvza = open('mtvza.pattern', 'rb').read()
mtvza = bitstring.ConstBitStream(file_mtvza)

while(int(lines)>=int(n)):
    try:
        img_c1= mixed.read(1904).bin
    except bitstring.ReadError:
        sys.exit()
    try:
        mtvza_c1= mtvza.read(64).bin
    except bitstring.ReadError:
        sys.exit()
    asm='00011010110011111111110000011101'
    fr1 = asm+tlm+bism+sspd+mtvza_c1+img_c1
    try:
        img_c2= mixed.read(1904).bin
    except bitstring.ReadError:
        sys.exit()
    try:
        mtvza_c2= mtvza.read(64).bin
    except bitstring.ReadError:
        sys.exit()
    fr2 = tlm+bism+sspd+mtvza_c2+img_c2
    try:
        img_c3= mixed.read(1904).bin
    except bitstring.ReadError:
        sys.exit()
    try:
        mtvza_c3= mtvza.read(64).bin
    except bitstring.ReadError:
        sys.exit()
    fr3 = tlm+bism+sspd+mtvza_c3+img_c3
    try:
        img_c4= mixed.read(1872).bin
    except bitstring.ReadError:
        sys.exit()
    try:
        mtvza_c4= mtvza.read(64).bin
    except bitstring.ReadError:
        sys.exit()
    fr4 = tlm+bism+sspd+mtvza_c4+img_c4
    with open('cadu.hrpt_mn2', 'ab') as file:
        bitstring.BitArray(bin=str(str(fr1)+str(fr2)+str(fr3)+str(fr4))).tofile(file)
    n+=1
    print('Lines: '+ str(n), end='\r')