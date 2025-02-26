import os, sys, argparse, logging
import freshmen as fp
import course as co

def simulation(interval, init, fresh, courses, number, one, half, gsupply, must, semester):
    X, y = fp.preprocessing(fresh)
    model = fp.generate_model(X, y)
    output = fp.predict(model, X, interval)
    expect = must / semester

    prev_supply = 0
    for i in range(interval):
        #integrated = output[i][0]
        #phd = output[i][1]
        integrated = 10
        phd = 7
        demand = init + (integrated + phd + number) * 2 - prev_supply
        supplies, total = co.supply(courses, one, half)

        supply = total + gsupply
        esemesters = demand / supply
        logging.info("{} (total)> esemesters: {}, goal: {} (fine: {})".format(i, esemesters, semester, esemesters < semester))
        prev_supply = supply

    prev_supply = 0
    for i in range(interval):
        #integrated = output[i][0]
        #phd = output[i][1]
        integrated = 10
        phd = 7
        demand = init + (integrated + phd + number) * 2 - prev_supply
        supplies, total = co.supply(courses, one, half)

        supply = supplies["el"] + gsupply
        esemesters = demand / supply
        logging.info("{} (total)> esemesters: {}, goal: {} (fine: {})".format(i, esemesters, semester, esemesters < semester))
        prev_supply = supply

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fresh", help="Freshmen data", type=str, required=True)
    parser.add_argument("-c", "--course", help="Course data", type=str, required=True)
    parser.add_argument("-n", "--number", help="KENTECH students", type=int, required=True)
    parser.add_argument("-g", "--grad", help="TA numbers in graduate courses", type=int, required=True)
    parser.add_argument("-i", "--init", help="Initial value", type=float, required=True)
    parser.add_argument("-y", "--interval", help="Number of intervals", type=int, required=True)
    parser.add_argument("-p", "--one", help="Minimum number of students for 1 TA", type=int, required=True)
    parser.add_argument("-q", "--half", help="Minimum number of students for 0.5 TA", type=int, required=True)
    parser.add_argument("-m", "--must", help="Number of TAs", type=int, required=True)
    parser.add_argument("-s", "--semester", help="Number of semesters", type=int, required=True)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", default="INFO", type=str)
    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    if not os.path.exists(args.fresh):
        logging.error("File does not exist: {}".format(args.fresh))
        sys.exit(1)

    simulation(args.interval, args.init, args.fresh, args.course, args.number, args.one, args.half, args.grad, args.must, args.semester)

if __name__ == "__main__":
    main()
