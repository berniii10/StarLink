import re
import csv
import time 
import datetime
import threading
import subprocess as sb

def newDataInFile(file):
    with open(file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(["-","-","-","-","-","-","-",])
def saveFile(file, data):
    data.insert(0, datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S"))
    with open(file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def f1():
    ip = input("To which IP or host: ")
    print()
    out = sb.check_output(['ping', ip, '-c', '1']).decode() 
    print(out)

    out = out.split()
    data = []
    data.append(out[1])
    data.append(out[2])
    data.append(out[14])

    print(data)
    print("---")
    
    saveFile("pings.csv", data)


def f2():
    print("Executing test...")
    print()
    out = sb.check_output(['speedtest-cli', '--simple']).decode()
    print(out)
    out = out.split()
    header =["Ping","Download","Upload"]
    data = []
    data.append(out[1] + out[2])
    data.append(out[4] + out[5])
    data.append(out[7] + out[8])
    print(data)

    saveFile("speedtests.csv", data)


def f3():
    ip = input("To which IP: ")
    h = input("Input the amount of hops that you want to do: ")
    print("Starting test...")
    print()
    out = sb.check_output(['traceroute', '-m', h, ip]).decode()
    print(out)
    out = out.split()
    # print(out)
    header = ["host", "ip", "max_hops", "hops"]
    data = []
    data.append(out[2])
    data.append(out[3])
    data.append(out[4])
    out = out[10:]
    # print(out)
    data.extend(out)
    # print(data)

    saveFile("traceroutes.csv", data)


def f4():
    ip = input("\nTo whom do you want to execute the test: ")
    current_date = datetime.datetime.now().strftime("%m-%d-%H-%M")
    filename = current_date + ".txt"

    with open(filename, "a") as file:
        s = int(input("For how many seconds do you want to execute the test? "))
        p_t = int(input("How often do you want to send pings? "))
        end_time = time.time() + s

        print("Starting test...")
        while end_time > time.time():
            print("Before ping")
            try: 
                out = sb.check_output(['ping', ip, '-c', '1']).decode()
            except sb.CalledProcessError as e:
                file.write("---\n")
                continue
            print(out)
            print("After ping")

            delay = re.search("time=(\d+\.\d+)", str(out))
            if delay == None: continue
            print(delay.group(0))

            file.write(delay.group(0))
            file.write(out)
            file.write("\n")
            time.sleep(p_t)
    print()


def f4_csv():
    ip = input("\nTo whom do you want to execute the test: ")

    newDataInFile("pingtests.csv")

    with open("pingtests.csv", "a") as file:
        s = int(input("For how many seconds do you want to execute the test? "))
        p_t = float(input("How often do you want to send pings? "))
        n_hops = input("Number of hops: ")
        end_time = time.time() + s
        
        header = ["host", "ip", "icmp", "ttl", "rtt", "trans_pack", "recv_pack", "pack_loss", "min/avg/max/mdev"]

        print("Starting test...")
        while end_time > time.time():
            data = []
            print("Before ping")
            try: 
                out = sb.check_output(['ping', ip, '-c', '1', '-i', n_hops]).decode()
            except sb.CalledProcessError as e:
                file.write("---\n")
                print("Error in ping. This will be written as ---")
                saveFile("pingtests.csv", ["E"])
                continue
            out = out.split()
            print(out)
            data.append(out[1])
            data.append(out[2])
            data.append(p_t)
            data.append(out[12])
            data.append(out[13])
            data.append(out[14])
            data.append(out[21])
            data.append(out[24])
            data.append(out[26])
            data.append(out[34])
            print(data)
            print("After ping")

            time.sleep(p_t)

            saveFile("pingtests.csv", data)
    print()
    

def f5():

    t = int(input("How long do you want to execute the test? (in seconds) "))
    ip = input("Gateway IP: ")
    end_t = time.time() + t

    newDataInFile("speedtests_s.csv")

    print("Executing test...")
    while time.time() < end_t:

        b = time.time()
        out = sb.check_output(['ping', ip, '-c', '1']).decode() 
        outping = out.split()[13].replace("time=", "")
        print(f"Ping to gateway {outping}")

        out = sb.check_output(['speedtest-cli', '--simple']).decode()


        while time.time() < b + 25:
            pass
        print(out)
        out = out.split()
        data = []
        out[1] = str(float(out[1])-float(outping))
        # print(out[1])

        data.append(out[1] + out[2])
        data.append(out[4] + out[5])
        data.append(out[7] + out[8])
        print(data)

        saveFile("speedtests_s.csv", data)


stop_thread = threading.Event()

def server():
    iperf3_process = sb.Popen(['iperf3', '-s'], stdout=sb.PIPE, stderr=sb.PIPE)
    while True:
        for line in iperf3_process.stdout:
            print(line.decode().strip())
            if stop_thread.is_set():
                iperf3_process.terminate()
                return
                break

thread = threading.Thread(target=server)
stop_thread_client = threading.Event()
server_host = '127.0.0.1'

def client(ip):
    iperf3_process = sb.Popen(['iperf3', '-c', ip], stdout=sb.PIPE, stderr=sb.PIPE)
    while True:
        for line in iperf3_process.stdout:
            print(line.decode().strip())
            if stop_thread.is_set():
                iperf3_process.terminate()
                return
                break

thread_client = threading.Thread(target=client, args=(server_host,))

def f6():
    s = input("Will you be the server or client? (c/s)")
    if s == 'c':
        # t = input("How long do you want to execute it? (seconds) ")
        # et = time.time() + t
        thread_client.start()
        while True:
            inp = input("Enter 'q' if you want to stop iperf3: ")
            if inp == 'q':
                stop_thread.set()
                break
        print("Exiting iperf3 execution on client.")

    elif s == 's':
        thread.start()
        while True:
            inp = input("Enter 'q' if you want to stop iperf3: ")
            if inp == 'q':
                stop_thread.set()
                break
        print("Exiting iperf3 execution on server.")
    
    return

def main():
    selected_functionality = -1

    while True:
        print("Choose a functionality:")
        print("0. Exit")
        print("1. Ping")
        print("2. Speed test")
        print("3. Traceroute")
        print("4. Execute Test")
        print("5. Execute Speed Test")
        print("6. Run iperf test")

        selected_functionality = int(input("Choose functionality: "))

        if selected_functionality == 0:
            print("Exiting program")
            break
        elif selected_functionality == 1:
            f1()
        elif selected_functionality == 2:
            f2()
        elif selected_functionality == 3:
            f3()
        elif selected_functionality == 4:
            f4_csv()
        elif selected_functionality == 5:
            f5()
        elif selected_functionality == 6:
            f6()
            print("Remember that you need to restart to execute again this.")


if __name__ == '__main__':
    main()
    """
    start_time = time.time()
    output = sb.check_output(['speedtest-cli', '--simple'])
    end_time = time.time()

    elapsed_time = end_time - start_time

    print(f"Command took {elapsed_time:.2f} seconds to execute")
    """