import getopt
import sys
from random import randint

import pandas as pd
from pandas import concat

from util import snake_case
from vars import headers
from factories import generate_rows

from util import insert_row


def get_options(argv):
    rows = 0
    white_rows = 0
    output_file = 'output.xlsx'
    help_text = 'python generate.py -r <number of rows> -w <number of white rows> -o <output path>'

    try:
        opts, args = getopt.getopt(argv, "hr:w:", ["rows=", "white-rows=", "output-file="])
    except getopt.GetoptError:
        print(help_text)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-r", "--rows"):
            rows = arg
        elif opt in ("-w", "--white-rows"):
            white_rows = arg
        elif opt in ("-o", "--output-file"):
            output_file = arg
        else:
            print(help_text)
            sys.exit()
    return output_file, rows, white_rows


def main(argv):
    output_file, rows, white_rows = get_options(argv)
    df = pd.DataFrame(columns=headers)
    rows_list = generate_rows(rows)

    for object_dict in rows_list:
        aux_dict = {}
        for h in headers:
            aux_dict.update({h, object_dict.get(snake_case(h), '')})
        df.append(aux_dict)

    for i in range(int(white_rows) + 1):
        index = randint(0, len(df))
        df = insert_row(index, df, pd.Series())


    df = df.sort_index().reset_index(drop=True)
    df.to_excel(output_file)
    print('File written to', output_file)

if __name__ == "__main__":
    main(sys.argv[1:])