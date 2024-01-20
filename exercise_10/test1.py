import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Example script to demonstrate argparse usage.')

# Add arguments
parser.add_argument('--input', type=str, help='Input file path')
parser.add_argument('--output', type=str, help='Output file path')
parser.add_argument('--verbose', action='store_true', help='Increase output verbosity')

# Parse arguments
args = parser.parse_args()

# Use the arguments
if args.verbose:
    print("Verbose mode is on.")

if args.input:
    print(f"Input file: {args.input}")

if args.output:
    print(f"Output file: {args.output}")
