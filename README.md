# HRPT METEOR Signal Generator
A collection of utilities for creating your own HRPT signal for transmitting images as on the Meteor-M2 satellite at a frequency of 1700 MHz!
## How to use
### 1. Preparing your images. 
Images must be in: 8-bit Grayscale and 1572px wide (Please make sure your images are the same length. Otherwise, your signal will only be effective for sending the shortest photo. Other, longer photos, will be cut).
This is easy to do with [Gimp](https://www.gimp.org).
#### Steps:
1. Open your image
2. Set the grayscale mode (Image -> Mode -> Grayscale)
3. Set the 8-bit mode (Image -> Precision -> 8 bit)
4. Invert your photo horizontally (Image -> Transformation -> Flip Horizontally)
5. Export image (File -> Export As -> ch1.bmp (So you need to prepare 6 channels. File names should be: ch1.bmp ch2.bmp ch3.bmp ch4.bmp ch5.bmp ch6.bmp))
### 2. Convert your photos into a load for HRPT MSU-MR transport frame.
Run the following code (Note that your photos must be in the folder with this utility):
```
1_Image_Mixer.exe
```
or
```
python3 1_Image_Mixer.py
```
After running the program, you will receive a file: ```out.hrpt``` (The program may take some time (several minutes))

### 3. Create MSU-MR transport frames with your photos!
Run the following code (File ```out.hrpt``` must be in the folder with the utility):
```
2_MSU-TS_Generator.exe
```
or
```
python3 2_MSU-TS_Generator.py
```
After running the program, you will receive a file: ```out.hrpt_mn2```

### 4. Create a (M)HRPT CADU for Data Transfer.
Run the following code (File ```out.hrpt_mn2``` must be in the folder with the utility):
```
3_HRPT_Generator.exe
```
or
```
python3 3_HRPT_Generator.py
```
After running the program, you will receive a file: ```cadu.hrpt_mn2```

### 5. Use Manchester encoding for your data To ensure frequent switching of your BPSK modulator.
Run the following code (File ```cadu.hrpt_mn2``` must be in the folder with the utility):
```
4_Manchester_Encoder.exe -i cadu.hrpt_mn2 -o cadu.hrpt_mn2_man -c 8192
```
or
```
python3 4_Manchester_Encoder.py -i cadu.hrpt_mn2 -o cadu.hrpt_mn2_man -c 8192
```
After running the program, you will receive a file: ```cadu.hrpt_mn2_man```

### 6. Send your data with GNURadio and SDR Transceiver!
If you want to generate an I/Q Waveform File use ```Meteor-HRPT-IQ.grc```
In the File Source block, specify your file after the Manchester encoder. In the WAV File Sink block, specify the file in which the IQ file will be saved. 

To send a signal via SDR, use the Osmocomm Sink block or another block for your SDR, instead of the Wav File Sink block. Also remove the Noise Generator block and the Add block that mixes the generator noise with the signal.
