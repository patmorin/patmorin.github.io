#!/usr/bin/python3
import sys
import subprocess
import re

def warn(msg):
    sys.stderr.write(msg + "\n")
    sys.stderr.flush()

def process_ipe_file(filename):
    try:
        fp = open(filename, "r")
    except:
        warn("Unable to read input file {}".format(filename))
        return None
    xml = open(filename).read()
    nviews = len(re.findall(r'^<view', xml, re.M))
    print("{} has {} views".format(filename, nviews))
    outfile = re.sub(r'(\.(xml|ipe))?$', ".svg", filename)
    print("{} => {}".format(filename, outfile))
    subprocess.call(["iperender", "-svg", filename, outfile])
    for v in range(1, nviews+1):
        suffix = "-{}.svg".format(v)
        outfile = re.sub(r'(\.(xml|ipe))?$', suffix, filename)
        print("{} (view {}) => {}".format(filename, v, outfile))
        subprocess.call(["iperender", "-svg", "-view", str(v), filename, outfile])


if __name__ == "__main__":
        files = sys.argv[1:]
        for filename in files:
            process_ipe_file(filename)
