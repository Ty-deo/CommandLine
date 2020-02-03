import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=argparse.FileType('r'),
                    help="Enter the file name of the SAA hole data(.txt) to be prepared for AutoCAD")
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()
print(args.filename)
fileName = args.filename.name
if args.verbosity >= 1:
    print("The file to be prepared for AutoCAD is {}".format(args.filename, fileName))
else:
    print(fileName)