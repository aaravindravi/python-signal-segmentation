'''
Similar to the buffer function of matlab

Parameters:
sampleRate = sampling rate of the signal
windowLen = window size in seconds
duration = number of samples based on sampling rate
shiftLen = shift time in seconds
dataOverlap = computes the number of samples based on sampling rate
data = is a 1-D array of values/ signal you want segment

Usage:
bufOut = buffer(data,duration,dataOverlap)
'''
import math
import numpy as np

def buffer(data,duration,dataOverlap):
    numberOfSegments = int(math.ceil((len(data)-dataOverlap)/(duration-dataOverlap)))
    #print(data.shape)
    tempBuf = [data[i:i+duration] for i in range(0,len(data),(duration-int(dataOverlap)))]
    tempBuf[numberOfSegments-1] = np.pad(tempBuf[numberOfSegments-1],(0,duration-tempBuf[numberOfSegments-1].shape[0]),'constant')
    tempBuf2 = np.vstack(tempBuf[0:numberOfSegments])
    return tempBuf2
	

def main():

    sampleRate=250
    windowLen=2
    shiftLen=0.5

    duration=int(windowLen*sampleRate)
    dataOverlap = (windowLen-shiftLen)*sampleRate
# Example Sin Waveform for 4s long and 10 Hz
    t=np.linspace(0,4,4*sampleRate)
    data=np.sin(2*np.pi*10*t)
    #print("python main function")
    #print(numberOfSegments)

    bufOut=buffer(data,duration,dataOverlap)
    print(bufOut.shape)
	
	
	
if __name__ == '__main__':
    main()