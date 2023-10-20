Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import time
starttime = time.time()
lasttime = starttime
lapnum = 1
print("Press ENTER to count laps. \nPress CTRL+C to stop")
Press ENTER to count laps. 
Press CTRL+C to stop
try:
    while True:
        input()
        laptime = round((time.time() - lasttime), 2)
        totaltime = round((time.time() - starttime), 2)
        print("Lap No. "+str(lapnum))
        print("Total Time: "+str(totaltime))
        print("Lap Time: "+str(laptime))
        print("*"*20)
        lasttime = time.time()
        lapnum += 1
except KeyboardInterrupt:
    print("Done")

    

''
Lap No. 1
Total Time: 214.37
Lap Time: 214.37
********************

''
Lap No. 2
Total Time: 216.37
Lap Time: 1.98
********************

''
Lap No. 3
Total Time: 219.57
Lap Time: 3.19
********************

''
Lap No. 4
Total Time: 221.34
Lap Time: 1.74
********************

''
Lap No. 5
Total Time: 222.55
Lap Time: 1.18
********************

''
Lap No. 6
Total Time: 224.56
Lap Time: 1.99
********************

''
Lap No. 7
Total Time: 225.12
Lap Time: 0.54
********************

''
Lap No. 8
Total Time: 226.39
Lap Time: 1.26
********************

''
Lap No. 9
Total Time: 226.88
Lap Time: 0.47
********************

''
Lap No. 10
Total Time: 227.54
Lap Time: 0.65
********************

''
Lap No. 11
Total Time: 230.52
Lap Time: 2.96
********************

''
Lap No. 12
Total Time: 231.71
Lap Time: 1.17
********************

''
Lap No. 13
Total Time: 233.18
Lap Time: 1.45
********************

''
Lap No. 14
Total Time: 233.56
Lap Time: 0.37
********************

''
Lap No. 15
Total Time: 234.12
Lap Time: 0.55
********************
