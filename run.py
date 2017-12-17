import argparse
from tsbench.adjust import adjust
from tsbench.runner import Runner


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('algorithm_name', help='name of algorithm to run')
    parser.add_argument('proportion', type=float, help='training dataset proportion')
    args = parser.parse_args()
    assert 0.0 < args.proportion < 1.0

    adjust()

    r = Runner(args.algorithm_name, args.proportion)
    r.execute()
    print 'successfully done'
