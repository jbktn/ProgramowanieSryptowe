import argparse
from grep import grep
from cut import cut
from skrypt1 import ops
import sys

def main():
    parser = argparse.ArgumentParser(prog="skrypt3.py", description="skrypt3")
    
    subprasers = parser.add_subparsers(dest='command')

    parser_cut = subprasers.add_parser('cut')
    parser_cut.add_argument('-d', dest='delimit')
    parser_cut.add_argument('-f', dest='number', type=int)

    parser_grep = subprasers.add_parser('grep')
    parser_grep.add_argument('-i', dest='case', action='store_true')
    parser_grep.add_argument('-w', dest='word', action='store_true')
    parser_grep.add_argument('pattern')

    parser_string = subprasers.add_parser('string')
    parser_string.add_argument('str', type=str)

    args = parser.parse_args()

    if args.command == 'cut':
        input_lines = sys.stdin.read()
        cut(input_lines, args.delimit, args.number)
    elif args.command == 'grep':
        input_lines = sys.stdin.read()
        grep(args.pattern, input_lines, args.case, args.word)
    elif args.command == 'string':
        ops(args.str)
        
    

if __name__ == "__main__":
    main()