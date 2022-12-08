import argparse
import subprocess as sb

def parseArg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, nargs=1)
    args = parser.parse_args()
    return args

def ping(n):
    outs = []
    for i in range(n):
        out = sb.check_output(['ping', '13.93.48.10', '-c', '1'])
        print(out)
        outs.append(out)
    

def main():
    n_pings = 5 # Default number of pings
    
    args = parseArg()
    if args.n:
        ping(args.n)
    else:
        ping(n_pings)


if __name__ == '__main__':
    main()
