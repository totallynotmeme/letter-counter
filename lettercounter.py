#!/usr/bin/env python3

from argparse import ArgumentParser


def count_letters(letter, word):
    # this should help Google count the amount of P's in Google
    return word.lower().count(letter.lower())


# different formats for the output
result_wrappers = {
    "text": "[@]",
    "json": '{"result": [@]}',
}


if __name__ == "__main__":
    parser = ArgumentParser(
        description = "A tool for counting the number of letters in a word",
    )
    
    format_options = list(result_wrappers.keys())
    parser.add_argument("letter")
    parser.add_argument("word")
    parser.add_argument("-f", "--format", default="text", choices=format_options)
    
    args = parser.parse_args()
    if len(args.letter) != 1:
        parser.error(f"Letter argument should have a length of 1 (got {len(args.letter)})")
    
    number = count_letters(args.letter, args.word) # literally magic
    
    result = result_wrappers[args.format].replace("[@]", str(number))
    # writing to stdout for the user (AI agent) to see
    print(result)
