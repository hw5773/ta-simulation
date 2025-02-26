with open("2025-1-revised.csv", "w") as of:
    with open("2025-1.csv", "r") as f:
        for line in f:
            tmp = line.strip().split(",")
            lst = []
            lst.append("2025-1")
            ctype = tmp[2][0:2].lower()
            lst.append(ctype)
            code = tmp[2][2:]
            lst.append(code)
            lst.append(str(int(tmp[3])))
            students = int(tmp[8])
            lst.append(str(students))

            if students >= 20:
                lst.append("1")
            elif students >= 10:
                lst.append("0.5")
            else:
                lst.append("0")

            of.write("{}\n".format(','.join(lst)))
