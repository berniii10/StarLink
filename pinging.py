import re
import time 
import datetime
import threading
import subprocess as sb

def f1():
    ip = input("To which IP: ")
    print()
    print(sb.check_output(['ping', ip, '-c', '1']).decode())

def f2():
    print()
    print(sb.check_output(['speedtest-cli', '--simple']).decode())

def f3():
    ip = input("To which IP: ")
    print()
    print(sb.check_output(['traceroute', ip]).decode())

def f4():
    ip = input("\nTo whom do you want to execute the test? ")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = current_date + ".txt"

    with open(filename, "a") as file:
        s = int(input("For how many seconds do you want to execute the test? "))
        end_time = time.time() + s

        print("Starting test:")
        while end_time > time.time():
            out = sb.check_output(['ping', ip, '-c', '1']).decode()
            delay = re.search("time=(\d+\.\d+)", str(out))
            print(delay.group(0))

            file.write(out)
            file.write("\n")
            time.sleep(0.5)
    print()
    
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


def f5():
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
        print("5. Run iperf test")

        selected_functionality = int(input("Choose functionality: "))

        if selected_functionality == 0:
            print("Exiting program")
            break
        elif selected_functionality == 1:
            f1()
        elif selected_functionality == 2:
            f2()
        elif selected_functionality == 3:
            f4()
        elif selected_functionality == 4:
            f4()
        elif selected_functionality == 5:
            f5()
            print("Remember that you need to restart to execute again this.")


if __name__ == '__main__':
    main()
