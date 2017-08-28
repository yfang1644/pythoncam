# MFCRecorder

This is script to automate the recording of public webcam shows from myfreecams. 


## Requirements

I have only tested this on debian(7+8) and Mac OS X (10.10.4), but it should run on other OSs

Requires python3.5 or newer. You can grab python3.5.2 from https://www.python.org/downloads/release/python-352/
and mfcauto.py (https://github.com/ZombieAlex/mfcauto.py)

to install required modules, run:
```
python3.5 -m pip install livestreamer
python3.5 -m pip install --upgrade git+https://github.com/ZombieAlex/mfcauto.py@master
```

## Setup

edit lines 6 and 8 to set the path for the directory to save the videos to, and to set the location of the "wanted.txt" file.

Add models UID (user ID) to the "wanted.txt" file (only one model per line). This uses the UID instead of the name becaue the models can change their name at anytime, but their UID always stays the same. There is a number of ways to get the models UID, but the easiest would probably be to get it from the URL for their profile image. The profile image URL is formatted as (or similar to):
```
https://img.mfcimg.com/photos2/###/{uid}/avatar.90x90.jpg
```
"{uid}" is the models UID which is the number you will want to add to the "wanted.txt" file. the "###" is the first 3 digits of the models UID. For example, if the models UID is "123456789" the URL for their profile picture will be:
```
https://img.mfcimg.com/photos2/123/123456789/avatar.90x90.jpg
```

alternatively, you can add a model with the "add.py" script (must be ran with python3.5 or newer).

Its usage is as follows:
add.py {models_display_name}

ie:
```
add.py AspenRae
```


## Additional options

you can now set a custom "completed" directory where the videos will be moved when the stream ends. The variables which can be used in the naming are as follows:

{path} = the value set to "save directory"

{model} = the display name of the model

{uid} = the uid (user id) or broadcasters id as its often reffered in MFCs code which is a static number for the model

{year} = the current 4 digit year (ie:2017)

{month} = the current two digit month (ie: 01 for January)

{day} = the two digit day of the month

{hour} = the two digit hour in 24 hour format (ie: 1pm = 13)

{minute} = the current minute value in two digit format (ie: 1:28 = 28)

{seconds} = the current times seconds value in 2 digit format

For example, if a made up model named "hannah" who has the uid 208562, and the "save_directory" in the config file == "/Users/Joe/MFC/": {path}/{uid}/{year}/{year}.{month}.{day}_{hour}.{minutes}.{seconds}_{model}.mp4 = "/Users/Joe/MFC/208562/2017/2017.07.26_19.34.47_hannah.mp4"


You can create your own "post processing" script which can be called at the end of the stream. The parameters which will be passed to the script are as follows:

1 = full file path (ie: /Users/Joe/MFC/208562/2017/2017.07.26_19.34.47_hannah.mp4)

2 = filename (ie : 2017.07.26_19.34.47_hannah.mp4)

3 = directory (ie : /Users/Joe/MFC/208562/hannah/2017/)

4 = models name (ie: hannah)

5 = uid (ie: 208562 as given in the directory/file naming structure example above)
