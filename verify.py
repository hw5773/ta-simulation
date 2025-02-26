with open("class-revised.csv", "w") as of:
    with open("class.csv", "r") as f:
        header = f.readline()
        of.write(header)

        for line in f:
            tmp = line.strip().split(",")
            students = int(tmp[-2])

            if students >= 20:
                tmp[-1] = "1"
            elif students >= 10:
                tmp[-1] = "0.5"
            else:
                tmp[-1] = "0"

            of.write("{}\n".format(','.join(tmp)))
