import glob
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.backends.backend_pdf import PdfPages

folder_path = 'D:\Sensoria Biocare\Docs\\21- Report con medias\Audios'  #Put your folder path
valsPerSec = 44100    #Sampling rate of your records (Samples/s)

frec = '1000'    #Put your desired frecuency here
gain = '0.30'   #Put your desired gain here

avgDataY = np.zeros([])
avgDataY_1 =  np.zeros([])
avgDataY_2 =  np.zeros([])
avgDataY_3 =  np.zeros([])
avgDataY_4 =  np.zeros([])
avgDataY_5 =  np.zeros([])
####Nothing here
counter = 0
first_ = 0
second_ = 0
counter_2 = 0

Y = 0
Y_1 = 0
Y_2= 0
Y_3 = 0
Y_4 = 0
Y_5 = 0

for filename in glob.glob(os.path.join(folder_path, '*.RAW')):      #Search all Raw files on folder
    file_real_name = filename[len(folder_path) + 1:len(filename)]   #Extract file name
    print(file_real_name)
    k = 0
    for i in range(0, len(file_real_name)):  # Search a xx_xx_xx_xxx structure in the string (R/L_500_25_0.04)
        if file_real_name[i] == "_":
            k += 1
            if k == 1:
                lado = file_real_name[i - 1]
                first_ = i
            if k == 2:
                file_frec = file_real_name[first_ + 1:i]
                second_ = i
                print(file_frec)
            if k == 3:
                pulse = file_real_name[second_ + 1:i]
                print(pulse)
                file_gain = file_real_name[i + 1: i+5] #len(file_real_name) - 4
                print(file_gain)
                break
    if file_frec == frec and gain == file_gain:
        print("NICE")
        print(pulse)
        if pulse == "25":
            pulse_1 = pulse
            dataY = np.memmap(filename, dtype='h', mode='r')
            dataY = dataY[int((0.5 + int(pulse) / 1000) * valsPerSec): int((0.6 + int(pulse) / 1000) * valsPerSec)] / 20
            avgDataY = (dataY + avgDataY)
            Y += 1
            dataX = np.arange(len(dataY)) / (valsPerSec / 1000)  # time axis from 0 to 60
            #data_2= np.sin(dataX/5)*15

        if pulse == "50":
            pulse_2 = pulse
            dataY_1 = np.memmap(filename, dtype='h', mode='r')
            dataY_1 = dataY_1[
                      int((0.5 + int(pulse) / 1000) * valsPerSec): int((0.6 + int(pulse) / 1000) * valsPerSec)] / 20
            avgDataY_1 = (dataY_1 + avgDataY_1)
            Y_1 += 1
            dataX_1 = np.arange(len(dataY_1)) / (valsPerSec / 1000)  # time axis from 0 to 60
        if pulse == "100":
            pulse_3 = pulse
            dataY_2 = np.memmap(filename, dtype='h', mode='r')
            dataY_2 = dataY_2[
                      int((0.5 + int(pulse) / 1000) * valsPerSec): int((0.6 + int(pulse) / 1000) * valsPerSec)] / 20
            avgDataY_2 = (dataY_2 + avgDataY_2)
            Y_2 += 1
            dataX_2 = np.arange(len(dataY_2)) / (valsPerSec / 1000)  # time axis from 0 to 60
        if pulse == "150":
            pulse_4 = pulse
            dataY_3 = np.memmap(filename, dtype='h', mode='r')
            dataY_3 = dataY_3[
                      int((0.5 + int(pulse) / 1000) * valsPerSec): int((0.6 + int(pulse) / 1000) * valsPerSec)] / 20
            avgDataY_3 = (dataY_3 + avgDataY_3)
            Y_3 += 1
            dataX_3 = np.arange(len(dataY_3)) / (valsPerSec / 1000)  # time axis from 0 to 60
        if pulse == "200":
            pulse_5 = pulse
            dataY_4 = np.memmap(filename, dtype='h', mode='r')
            dataY_4 = dataY_4[
                      int((0.5 + int(pulse) / 1000) * valsPerSec): int((0.6 + int(pulse) / 1000) * valsPerSec)] / 20
            avgDataY_4 = (dataY_4+ avgDataY_4)
            Y_4 += 1
            dataX_4 = np.arange(len(dataY_4)) / (valsPerSec / 1000)  # time axis from 0 to 60
        if pulse == "300":
            pulse_6 = pulse
            dataY_5 = np.memmap(filename, dtype='h', mode='r')
            dataY_5 = dataY_5[
                      int((0.5 + int(pulse) / 1000) * valsPerSec): int((0.6 + int(pulse) / 1000) * valsPerSec)] / 20
            avgDataY_5= (dataY_5 + avgDataY_5)
            Y_5 += 1
            dataX_5 = np.arange(len(dataY_5)) / (valsPerSec / 1000)  # time axis from 0 to 60

avgDataY = avgDataY/Y
avgDataY_1 = avgDataY_1/Y_1
avgDataY_2 = avgDataY_2/Y_2
avgDataY_3 = avgDataY_3/Y_3
avgDataY_4 = avgDataY_4/Y_4
avgDataY_5 = avgDataY_5/Y_5

print("HI")
print(Y_2)
with PdfPages(folder_path + '\%sHz_%sGain.pdf' % (frec, gain)) as pdf:  # Create a pdf file with variable name as
    # function of frec & gain

    # Initialise the subplot function using number of rows and columns
    figure, axis = plt.subplots(3, 1, figsize=(8.27, 11.69))
    figure.suptitle('Eco recording of %d samples while generating %s Hz  with gain %s ' % (Y, frec, gain), fontsize=16, y=0.965)

    # First Page, First plot
    axis[0].plot(dataX, avgDataY)
    axis[0].set_title("%s ms Pulse" % (pulse_1))
    axis[0].grid(color='black', linestyle='--', linewidth=1)
    axis[0].set_xlabel("Time (ms)")
    axis[0].set_ylabel("Amplitud")
    # axis[0].plot(dataX, data_2)
    # First Page, Second plot
    axis[1].plot(dataX_1, avgDataY_1)
    axis[1].set_title("%s ms Pulse" % (pulse_2))
    axis[1].grid(color='black', linestyle='--', linewidth=1)
    axis[1].set_xlabel("Time (ms)")
    axis[1].set_ylabel("Amplitud")
    # axis[1].plot(dataX, data_2)
    # First Page, Third plot
    axis[2].plot(dataX_2, avgDataY_2)
    axis[2].set_title("%s ms Pulse" % (pulse_3))
    axis[2].grid(color='black', linestyle='--', linewidth=1)
    axis[2].set_xlabel("Time (ms)")
    axis[2].set_ylabel("Amplitude (mV)")
    # axis[2].plot(dataX, data_2)
    #Margin stuff
    plt.subplots_adjust(left=0.15,
                        bottom=0.1,
                        right=0.9,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.4)

    pdf.savefig()
    plt.close()

    # Second Page, First plot
    figure, axis = plt.subplots(3, 1, figsize=(8.27, 11.69))
    axis[0].plot(dataX_3, avgDataY_3)
    axis[0].set_title("%s ms Pulse" % (pulse_4))
    axis[0].grid(color='black', linestyle='--', linewidth=1)
    axis[0].set_xlabel("Time (ms)")
    axis[0].set_ylabel("Amplitud")

    # Second Page, Second plot
    axis[1].plot(dataX_4, avgDataY_4)
    axis[1].set_title("%s ms Pulse" % (pulse_5))
    axis[1].grid(color='black', linestyle='--', linewidth=1)
    axis[1].set_xlabel("Time (ms)")
    axis[1].set_ylabel("Amplitud")

    # Second Page, Third plot
    axis[2].plot(dataX_5, avgDataY_5)
    axis[2].set_title("%s ms Pulse" % (pulse_6))
    axis[2].grid(color='black', linestyle='--', linewidth=1)
    axis[2].set_xlabel("Time (ms)")
    axis[2].set_ylabel("Amplitude (mV)")

    #Margin Stuff again
    plt.subplots_adjust(left=0.15,
                        bottom=0.1,
                        right=0.9,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.4)
    pdf.savefig()
    plt.close()
