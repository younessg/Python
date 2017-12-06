import argparse
import sys

def main():
    print "Constructor called!"

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-i',
	nargs='+',
	#action='store', default is store
	dest='filename',
	metavar='Expected file name1',
	help='file to search')

    parser.add_argument(
        '--i',
	nargs=1,
	#action='store', default is store
	dest='filename2',
	metavar='Expected file name2',
	help='file to search 2')

    args = parser.parse_args()
    print args.filename
    print args.filename2
    #options = parser.parse_args(rgs)

    if not sys.stdin.isatty(): # not part of the pipe no terminal attached to standard in
        print "part of pipe"
        input_file = sys.stdin # expecting something from the sys in
        print "reading from sys in".join(input_file)
    else:
        print "Not part of pipe"

    return "Terminate!"

if __name__ == "__main__":
    print "Running from python"
    sys.exit(main())
else:
    print "Running from import"
