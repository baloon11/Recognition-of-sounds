# coding: utf-8
import alsaaudio, numpy, scipy.io.wavfile
from matplotlib import pyplot, mlab
import sys, os, time, wave

SAMPLE_RATE = 44100 # Hz

if os.path.isfile('standart.wav'):
    os.remove('standart.wav')

def record_wav(file_name, sec):
        # recording audio
    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
    inp.setchannels(1)
    inp.setrate(SAMPLE_RATE)
    inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    inp.setperiodsize(2048)#1024

    w = wave.open(file_name, 'w')
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(SAMPLE_RATE)

    start_time=time.time()
    end_time=0.0
    while True:
        if end_time-start_time<=sec:
            l, data = inp.read()
            w.writeframes(data)
        else:
            break
        end_time=time.time()
    w.close()

def get_wave_data(wave_filename):
    sample_rate, wave_data = scipy.io.wavfile.read(wave_filename)
    return wave_data

def get_fingerprint(wave_data):
    pxx, _, _ = mlab.specgram(wave_data, NFFT=2048, noverlap=500, Fs=SAMPLE_RATE)
    band = pxx[15:250]  # the most interesting frequency from 60 to 1000 Hz
    return numpy.argmax(band.transpose(), 1)  # max in each part of time

def frequency_to_list_from_file():
    i_str=""
    i_list=[]
    for i in open("frequency_list_etalon","r"):
        if "\n" in i[-1]:
            i=i[:-1]+str(i[-1])[:-2]
            i=i.strip()
        i_str+=i
    for i in i_str.split():
        i_list.append(int(i))
    return i_list

if 'etalon' == sys.argv[1]:
    record_wav('etalon.wav', 3.0)
    wave_data = get_wave_data('etalon.wav')
    frequency_list_etalon= open("frequency_list_etalon","w")
    frequency_list_etalon.write( str(get_fingerprint(wave_data))[1:-1].strip() )
    frequency_list_etalon.close()

if 'standart' == sys.argv[1]:
    stream_list=[]
    etalon_list=frequency_to_list_from_file()
    while True:
        match=0
        record_wav('standart.wav', 0.5)
        wave_data = get_wave_data('standart.wav')
        os.remove('standart.wav')
        stream_list+=list(get_fingerprint(wave_data))
        len_etalon_list=len(etalon_list)

        while True:
            if len(stream_list)>len_etalon_list:

                for i in xrange(len_etalon_list-1):
                    if int(stream_list[i])==int(etalon_list[i]):
                        match+=1

                if float(match)/float(len_etalon_list)>=0.8:# 80%
                    print "Yes, it is work"
                    os.system('/usr/bin/firefox')
                    stream_list=stream_list[len_etalon_list-1:]
                    continue
                else:
                    stream_list=stream_list[1:]
                    continue
            else:
                break




