import os
import sys
import json
import openai
import argparse

from dotenv import load_dotenv
from chatgpt import *


parser = argparse.ArgumentParser(description='ChatGPT API interface')

parser.add_argument(
    '--with_context', '-c', 
    action='store_const', 
    const=True, 
    default=False, 
    required=False
)

# input params
parser.add_argument(
    '--from_file', '-f',
    type=str,
    default=None,
    required=False
)

parser.add_argument(
    '--interactive', '-i',
    action='store_const',
    const=True,
    default=False,
    required=False
)

# output params
parser.add_argument(
    '--output_file', '-o',
    type=str,
    default=None,
    required=False
)

parser.add_argument(
    '--output_terminal', '-p', 
    action='store_const', 
    const=True, 
    default=False, 
    required=False
)

# model
parser.add_argument(
    '--model', '-m', 
    default='gpt-3.5-turbo', 
    required=False, 
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

    if args.from_file:
        gpt_from_file(
            apply_context=args.apply_context,
            output_terminal=args.output_terminal
        )

    elif args.interactive:
        gpt_interactive(
            apply_context=args.apply_context,
            output_file=args.output_file
        )