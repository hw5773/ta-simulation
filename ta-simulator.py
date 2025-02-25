import os, sys, argparse, logging

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", default="INFO", type=str)
    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

if __name__ == "__main__":
    main()
