import os
import sys
import json
import openai
import argparse

from dotenv import load_dotenv
from src.chatgpt_utils import *
from src.colors import Colors


parser = argparse.ArgumentParser(description='ChatGPT API interface')

parser.add_argument(
    '--with_context', '-c', 
    action='store_const',
    const=True,
    default=True
)

# input params
parser.add_argument(
    '--from_file', '-f',
    type=str,
    default=None
)

parser.add_argument(
    '--interactive', '-i',
    action='store_const',
    const=True,
    default=False
)

# output params
parser.add_argument(
    '--output_file', '-o',
    type=str,
    default=None
)

parser.add_argument(
    '--output_terminal', '-p', 
    action='store_const', 
    const=True, 
    default=False
)

# model
parser.add_argument(
    '--model', '-m', 
    default='gpt-3.5-turbo', 
    required=False
)

# [-c] (context)
# [-f | -i] (input)
# [-o, -p] (output)
# [-m] (model)

args = parser.parse_args()


if __name__ == '__main__':
    load_dotenv()
    openai.api_key = os.environ['GPT_API_KEY']

    # print logo
    with open('./assets/logo.txt', 'r') as f:
        print(f'{Colors.OKGREEN}{f.read()}{Colors.ENDC}\n')

    if args.from_file:
        gpt_from_file(
            apply_context=args.with_context,
            output_terminal=args.output_terminal
        )

    elif args.interactive:
        gpt_interactive(
            apply_context=args.with_context,
            output_file=args.output_file
        )
