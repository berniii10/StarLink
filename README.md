# StarLink

--- Testbed script description: ---
The code defines several functions that use Python's subprocess module to execute command-line programs such as ping, traceroute, and speedtest-cli to gather data and write them to CSV files. The code is essentially a network monitoring tool that can perform various tests and store the results in CSV files for analysis.

The code defines the following functions:

    newDataInFile(file): This function appends a row of seven dashes to the end of the CSV file specified by the file parameter.
    saveFile(file, data): This function saves the list of data values to the CSV file specified by the file parameter. The current date and time are added to the beginning of the list before it is saved.
    f1(): This function prompts the user to enter an IP address or host name, executes the ping command, parses the output to extract the ping time, and saves the results to the "pings.csv" file.
    f2(): This function executes the speedtest-cli command, parses the output to extract the ping time, download speed, and upload speed, and saves the results to the "speedtests.csv" file.
    f3(): This function prompts the user to enter an IP address, the maximum number of hops, executes the traceroute command, parses the output to extract the hops and IP addresses, and saves the results to the "traceroutes.csv" file.
    f4(): This function prompts the user to enter an IP address or host name, the duration of the test, and the interval between pings. It then executes the ping command and writes the results to a text file named with the current date and time.
    f4_csv(): This function is similar to f4() but saves the results to the "pingtests.csv" file in CSV format.
    f5(): This function prompts the user to enter the duration of the test and the gateway IP address. It then executes the speedtest-cli command and writes the results to the "speedtests_s.csv" file in CSV format.

Note that the functions use the path variable to specify the directory where the CSV files are stored.

--- Processor script description: ---
This code is a Python script that imports several libraries: csv, matplotlib.pyplot, pandas, and datetime. It defines two functions, speedtest() and pingtests(), which both read data from CSV files and plot the data using matplotlib.pyplot.

The speedtest() function reads data from a CSV file located at SPEEDTESTS_SPLOT_FILE_PATH and extracts the ping, download, and upload speeds, along with the time of each measurement. It then plots the ping versus time, and then the download and upload speeds versus time. The x-axis of both plots represents the time of the measurement, and the y-axis represents the value of the corresponding metric (ping, download, or upload speed). The time values are converted to seconds and set so that the first measurement is at time zero. The plots are displayed using plt.show().

The pingtests() function reads data from a CSV file located at PING_TEST_FILE_PATH and extracts the time and round-trip time (RTT) of each ping test. It then plots the RTT versus time. The x-axis represents the time of the measurement, and the y-axis represents the RTT in seconds. The time values are converted to seconds and set so that the first measurement is at time zero. The plot is displayed using plt.show().

The main() function prompts the user to choose a functionality from a menu. If the user selects 1, it calls speedtest(), if the user selects 2, it calls pingtests(), and if the user selects 0, it exits the program.
