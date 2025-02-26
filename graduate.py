import os, sys, argparse, logging

def analysis(fname):
    with open(fname, "r") as f:
        header = f.readline().strip()
        tmp = header.split(",")
        sidx, pidx, ridx = 0, 0, 0
        for i in range(len(tmp)):
            if tmp[i] == "rest":
                ridx = i
            if tmp[i] == "program":
                pidx = i
            if tmp[i] == "status":
                sidx = i
        rest = 0
        integrated = 0
        phd = 0

        for line in f:
            tmp = line.strip().split(",")
            try:
                program = tmp[pidx]
                status = tmp[sidx]
                if "통합" in program and "재학" in status:
                    integrated += 1
                    rest += float(tmp[ridx])
                elif "박사" in program and "재학" in status:
                    phd += 1
                    rest += float(tmp[ridx])
            except:
                logging.error("error line: {}".format(line))

    logging.info("Rest TA: {}".format(rest))
    logging.info("Integrated: {}".format(integrated))
    logging.info("Ph D: {}".format(phd))

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Class prediction", required=True)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", default="INFO", type=str)
    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    if not os.path.exists(args.input):
        logging.error("File not exist: {}".format(args.input))
        sys.exit(1)

    analysis(args.input)    

if __name__ == "__main__":
    main()
