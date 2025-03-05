import os, sys, argparse, logging
import freshmen as fp
import course as co

def simulation(interval, init, fresh, prediction, courses, number, one, half, additional, must):
    X, y = fp.preprocessing(fresh)
    model = fp.generate_model(X, y)
    output = fp.predict(model, X, interval)
    if prediction:
        integrated = output[i][0]
        phd = output[i][1]
    else:
        integrated = 10
        phd = 7
 
    prev_supply = 0
    for i in range(interval):
        demand = (integrated + phd + number) * must - prev_supply
        supplies, total = co.supply(courses, one, half)

        supply = total + additional
        if supply > demand:
            rest = init / (supply - demand)
        else:
            rest = -1
        logging.info("{} (total)> demand: {}, supply: {}, required month: {} (fine: {})".format(i, demand, supply, rest, demand > supply * 0.8 and demand < supply))
        prev_supply = supply

    prev_supply = 0
    for i in range(interval):
        demand = (integrated + phd + number) * must - prev_supply
        supplies, total = co.supply(courses, one, half)

        supply = supplies["el"] + additional
        if supply > demand:
            rest = init / (supply - demand)
        else:
            rest = -1
        logging.info("{} (EL)> demand: {}, supply: {}, required month: {} (fine: {})".format(i, demand, supply, rest, demand > supply * 0.8 and demand < supply))
        prev_supply = supply

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fresh", help="Freshmen data", type=str, required=True)
    parser.add_argument("-z", "--prediction", help="Prediction (yes/no)", default=False, action="store_true")
    parser.add_argument("-c", "--course", help="Course data", type=str, required=True)
    parser.add_argument("-n", "--number", help="KENTECH students", type=int, required=True)
    parser.add_argument("-a", "--additional", help="Additional TA numbers (IR, capstone, or graduate courses)", type=int, required=True)
    parser.add_argument("-i", "--init", help="Initial value", type=float, required=True)
    parser.add_argument("-y", "--interval", help="Number of intervals", type=int, required=True)
    parser.add_argument("-p", "--one", help="Minimum number of students for 1 TA", type=int, required=True)
    parser.add_argument("-q", "--half", help="Minimum number of students for 0.5 TA", type=int, required=True)
    parser.add_argument("-m", "--must", help="Number of TAs", type=int, required=True)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", default="INFO", type=str)
    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    if not os.path.exists(args.fresh):
        logging.error("File does not exist: {}".format(args.fresh))
        sys.exit(1)

    simulation(args.interval, args.init, args.fresh, args.course, args.number, args.one, args.half, args.additional, args.must)

if __name__ == "__main__":
    main()
