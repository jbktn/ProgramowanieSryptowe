import argparse
from grep import grep
from cut import cut
from skrypt1 import ops
import sys

def main():
    parser = argparse.ArgumentParser(description="skrypt3")
    parser.add_argument('command', type=str, help='grep, cut lub skrypt1')
    parser.add_argument('-d', dest='delimiter')
    parser.add_argument('-f', dest='field_number', type=int)
    parser.add_argument('-i', dest='ignore_case', action='store_true')
    parser.add_argument('-w', dest='whole_word', action='store_true')
    parser.add_argument('pattern', type=str)

    args = parser.parse_args()

    if args.command == 'cut':
        input_lines = sys.stdin.read()
        result = cut(input_lines, args.delimiter, args.field_number)
    elif args.command == 'grep':
        input_lines = sys.stdin.read()
        result = grep(args.pattern, input_lines, args.ignore_case, args.whole_word)
    else:
        ops(args.command)
        
    

if __name__ == "__main__":
    main()