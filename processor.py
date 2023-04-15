import csv
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

SPEEDTESTS_SPLOT_FILE_PATH = "data/spt_plot.csv"
PING_TEST_FILE_PATH = "data/pt_plot.csv"

def speedtest():

    time = []
    ping = []
    download = []
    upload = []

    with open(SPEEDTESTS_SPLOT_FILE_PATH) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # skip header row
        for row in csv_reader:
            time_str = row[0]
            time.append(datetime.strptime(time_str, '%d-%m-%Y-%H-%M-%S'))
            ping_val = float(row[1].replace('ms', ''))
            download_val = float(row[2].replace('Mbit/s', ''))
            upload_val = float(row[3].replace('Mbit/s', ''))
            ping.append(ping_val)
            download.append(download_val)
            upload.append(upload_val)

    # calculate time range in seconds
    time_range = (time[-1] - time[0]).total_seconds()

    # convert time to seconds and set first sample as 0 seconds
    time_sec = [(t - time[0]).total_seconds() for t in time]

    # plot the data
    plt.plot(time_sec, ping)

    # set the axis labels and title
    plt.xlabel('Time (seconds)')
    plt.ylabel('Ping (ms)')
    plt.title('Ping vs. Time')

    # set the x-axis range to span the entire time period of the data
    plt.xlim(0, time_range)
    plt.ylim(0, max(ping))
    plt.xticks(rotation=45)

    # display the plot
    plt.show()

    # plot the download and upload speeds
    plt.plot(time_sec, download, label='Download')
    plt.plot(time_sec, upload, label='Upload')

    # set the axis labels and title
    plt.xlabel('Time (seconds)')
    plt.ylabel('Speed (Mbit/s)')
    plt.title('Download and Upload Speeds vs. Time')

    # set the x-axis range to span the entire time period of the data
    plt.xlim(0, time_range)
    plt.ylim(0, max(max(download), max(upload)))
    plt.xticks(rotation=45)

    # display the legend and the plot
    plt.legend()
    plt.show()

def pingtests():

    time_values = []
    rtt_values = []

    # open CSV file and read in data
    with open(PING_TEST_FILE_PATH, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        for row in reader:
            try:
                # parse time value from string
                time_str = row[0]
                time_obj = datetime.strptime(time_str, '%d-%m-%Y-%H-%M-%S')

                # extract rtt value from string
                rtt_str = row[5]
                rtt_val = float(rtt_str.replace("time=", ""))

                # add values to lists
                time_values.append(time_obj)
                rtt_values.append(rtt_val)
            except (ValueError, IndexError):
                # skip rows that cannot be parsed
                continue

    # calculate time differences in seconds
    time_diffs = [(t - time_values[0]).total_seconds() for t in time_values]

    # create a new figure
    fig, ax = plt.subplots()

    # set x-axis label
    ax.set_xlabel('Time (s)')

    # set y-axis label
    ax.set_ylabel('RTT')

    # plot RTT versus time
    ax.plot(time_diffs, rtt_values)

    # show the plot
    plt.show()



def main():
    selected_functionality = -1

    while True:
        print("Choose a functionality:")
        print("0. Exit")
        print("1. Plot Speed Test")
        print("2. Plot Ping Test")
        print("3. To Implement")
        print("4. To Implement")
        print("5. To Implement")
        print("6. To Implement")

        selected_functionality = int(input("Choose functionality: "))

        if selected_functionality == 0:
            print("Exiting program")
            break
        elif selected_functionality == 1:
            speedtest()
        elif selected_functionality == 2:
            pingtests()
        elif selected_functionality == 3:
            pass
        elif selected_functionality == 4:
            pass
        elif selected_functionality == 5:
            pass
        elif selected_functionality == 6:
            pass

if __name__ == '__main__':
    main()