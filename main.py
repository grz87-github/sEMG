
# Importing Libraries
import datetime as dt
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

def loop():
    i = 0
    data=[]
    while(True):

        #fig = plt.figure()
        #ax = fig.add_subplot(1, 1, 1)
        #xs = []
        #ys = []
        print(arduino.readline().decode('UTF-8').strip())
        row = arduino.readline().decode('UTF-8').strip()
        if row !="": data.append([row])
        i=i+1
        if(i==100):
            save('/tmp/test1.txt', data)
            i=0
            data=[]

# def animate(i, xs, ys):
#
#     # Read temperature (Celsius) from TMP102
#     line = arduino.readline().decode("utf-8").rstrip()
#
#     # Add x and y to lists
#     xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
#     ys.append(line)
#
#     # Limit x and y lists to 20 items
#     xs = xs[-20:]
#     ys = ys[-20:]
#
#     # Draw x and y lists
#     ax.clear()
#     ax.plot(xs, ys)
#
#     # Format plot
#     plt.xticks(rotation=45, ha='right')
#     plt.subplots_adjust(bottom=0.30)
#     plt.title('TMP102 Temperature over Time')
#     plt.ylabel('Temperature (deg C)')

def save(file,data):
    # open the file in the write mode
    f = open(file, 'a', encoding='UTF8')

    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerows(data)

    # close the file
    f.close()
#save('/tmp/test1.txt',[["test"],["test2"]] )
data=[]
arduino = serial.Serial(port='/dev/cu.usbmodem142201', baudrate=115200, timeout=.001)
arduino.flush()
loop()

#ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
#plt.show()


