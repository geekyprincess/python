#create a server file which in fixed interval of time, pings to check if internet is connected. And create a log file 
#which will save the datetime with status(0/1) and another status file with (0/1) for other programs to refer
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<      This project has been coded by geekyprincess(aka Ashima)     >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#


import urllib.request, time, os
from os import path

#get status fo internet connection 

def getStatus(url=''):
    if not url:
        url = 'http://www.google.com'
    try: 
        #check connection 
        with urllib.request.urlopen(url) as response:
            code = response.getcode()  
        #to handle no connection situation 
    except urllib.error.URLError:
        return 0
    else:
        #if no exception, connection present
        if code==200 : return 1
    #other situations return 0
    return 0

#get time in format
def getTime():
    timetuple = time.localtime()
    full_time = time.strftime("%Y-%m-%d %H:%M:%S", timetuple)
    day = time.strftime("%Y%m%d", timetuple)
    return full_time, day
    
#write log
def writeToLog(full_time, day, status):
    f_path = path.relpath("data/"+day+'_internet.txt')
    with open(f_path, 'a') as fo:
        line = full_time+","+str(status)+'\n'
        fo.write(line)

#write status file 
def writeStatus(status):
    with open('status', 'w') as fo:
        fo.write(str(status))

#main
dir_status = os.path.exists("data")
if not dir_status : os.mkdir('data')

i = 1
while i > 0:
    status = getStatus('')
    full_time, day = getTime()
    writeToLog(full_time,day,status)
    writeStatus(status)
    time.sleep( 10 )


