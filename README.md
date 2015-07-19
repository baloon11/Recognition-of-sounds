# Recognition-of-sounds
This python-script performs the task of recognition sounds 
and run specific commands after detecting these sounds.

-------------------

Some technical details
----------------------

This script is based on the creation of sound fingerprint for
etalon .wav file.


(Etalon file is divided into parts
Then in each part we are looking for frequency
which corresponds to the max amplitude of sound.


We get a list of frequencies
(It will be store in the file: frequency_list_etalon )

when we run 
	python cts.py standart 


We run endless loop.
Each iteration of this loop does:

- create a sort .wav file (0.5 sec),
- make sound fingerprint of this short file,
- make list of frequencies for it
- save this data in in the general list
- delete this short file


(This loop is used for continuous listening microphone
and recording data, when the script is running)

So we get a list of which is constantly supplemented.

Then we compare etalon frequency list and general frequencies list.

When a match occurs lists (80%)
- Runs a command (run firefox)

For details --see code.

-------------------

Usage
------
create etalon .wav file (script will recognize the sounds of this file and run) 

	python cts.py etalon
	

Run script

	python cts.py standart

When the script is running,it waiting for the etalon sounds
to do the action (run firefox)



Requirements
------------
python 2.7

	sudo apt-get install python-alsaaudio

	pip install alsaaudio 
	pip install numpy
	pip install scipy
	pip install matplotlib 

---------------------------------------------------
The script is based on ideas and parts of the code from this article:
	http://habrahabr.ru/post/252937/

A short video how this script works:
	https://www.youtube.com/watch?v=hi8_oyXEssY&feature=youtu.be
