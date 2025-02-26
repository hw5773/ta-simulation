import os, sys, argparse, logging
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten

TIMESTEPS = 5
FEATURES = 3

def preprocessing(fname):
    X, y = [], []
    dataset = []
    with open(fname, "r") as f:
        f.readline()
        for line in f:
            tmp = line.strip().split(",")
            dataset.append([int(tmp[1]), int(tmp[2]), int(tmp[3])])

    for i in range(len(dataset) - TIMESTEPS):
        X.append(dataset[i:i+TIMESTEPS])
        y.append(dataset[i+TIMESTEPS])

    X = np.array(X)
    y = np.array(y)

    return X, y

def generate_model(X, y):
    model = Sequential()
    model.add(Flatten(input_shape=(TIMESTEPS, FEATURES)))
    model.add(Dense(128, activation="relu", input_shape=(TIMESTEPS, FEATURES)))
    model.add(Dense(128, activation="relu"))
    model.add(Dense(128, activation="relu"))
    model.add(Dense(64, activation="relu"))
    model.add(Dense(32, activation="relu"))
    model.add(Dense(16, activation="relu"))
    model.add(Dense(8, activation="relu"))
    model.add(Dense(FEATURES))

    model.compile(optimizer="adam", loss="mse")
    model.fit(X, y, epochs=300, verbose=1)

    return model

def predict(model, X, num):
    ret = []

    for i in range(num):
        val = [X[-1]]
        pred = model.predict(np.array(val))
        pred = list(map(int, list(pred[0])))
        ret.append(pred)
        add = []
        for idx in range(len(X[-1])):
            if idx == 0:
                continue
            add.append(list(X[-1][idx]))
        add.append(pred)
        X = list(X)
        X.append(add)
        X = np.array(X)
        logging.debug("X: {}".format(X))
    
    logging.debug("ret: {}".format(ret))
    return ret

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Freshmen prediction", required=True)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", default="INFO", type=str)
    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    if not os.path.exists(args.input):
        logging.error("File not exist: {}".format(args.input))
        sys.exit(1)

    X, y = preprocessing(args.input)
    logging.info("X: {}".format(X))
    logging.info("y: {}".format(y))
    model = generate_model(X, y)
    output = predict(model, X, 10)
    logging.info("output: {}".format(output))

if __name__ == "__main__":
    main()
