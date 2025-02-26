import os, sys, argparse, logging

def supply(fname, one, half):
    ret = {}
    with open(fname, "r") as f:
        f.readline()
        for line in f:
            tmp = line.strip().split(",")
            if "2025-1" not in tmp[0]:
                continue
            students = int(tmp[-2])
            ctype = tmp[1]
            if ctype not in ret:
                ret[ctype] = 0
            if students >= one:
                ret[ctype] += 1
            elif students >= half:
                ret[ctype] += 0.5
    total = 0
    for k in ret:
        total += ret[k]
    return ret, total

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Class prediction", type=str, required=True)
    parser.add_argument("-p", "--one", help="Mininum number of students for 1 TA", type=int, required=True)
    parser.add_argument("-q", "--half", help="Mininum number of students for 0.5 TA", type=int, required=True)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", default="INFO", type=str)
    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    if not os.path.exists(args.input):
        logging.error("File not exist: {}".format(args.input))
        sys.exit(1)

    s, t = supply(args.input, args.one, args.half)
    logging.info("supply: {}".format(s))
    logging.info("total: {}".format(t))

if __name__ == "__main__":
    main()
