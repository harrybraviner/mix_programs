import argparse

mix_chars = [
    ' ',    # 00
    'A',    # 01
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',    # 09
    'Δ',    # 10
    'J',    # 11
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',    # 19
    'Σ',    # 20
    'Π',    # 21
    'S',    # 22
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',    # 29
    '0',    # 30
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',    # 39
    '.',    # 40
    ',',    # 41
    '(',    # 42
    ')',    # 43
    '+',    # 44
    '-',    # 45
    '*',    # 46
    '/',    # 47
    '=',    # 48
    '$',    # 49
    '<',    # 50
    '>',    # 51,
    '@',    # 52
    ';',    # 53
    ':',    # 54
    '\'',   # 55
]

char_lookup_dict = {c: i for i, c in enumerate(mix_chars)}

def convert_alf_to_word(word_as_str):
    if len(word_as_str) != 5:
        raise ValueError('Mix words must be 5 alphanumeric characters long!')
    acc = 0
    for ch in word_as_str:
        acc <<= 6
        if ch not in char_lookup_dict:
            raise ValueError('Character {} is not recognized!'.format(ch))
        acc += char_lookup_dict[ch]
    return acc

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['read', 'write'])
    parser.add_argument('filename', type=str)
    parser.add_argument('--skip-blanks', action='store_true',
                       help='If reading a file, does not print trailing blanks to the screen')
    args = parser.parse_args()

    filename = args.filename

    if args.mode == 'write':
        if args.skip_blanks:
            print('Warning: --skip-blanks option ignored for mode = write')

        done = False
        words = []
        while True:
            try:
                word_as_str = input('Enter a 5 character mix word: ')
            except KeyboardInterrupt:
                break

            word_as_mix = convert_alf_to_word(word_as_str)
            words.append(word_as_mix)

            if len(words) == 100:
                break
        if len(words) < 100:
            words = words + ([0] * (100 - len(words)))

        print('\nWriting to file {}'.format(filename))

        with open(filename, 'wb') as f:
            for word in words:
                f.write(word.to_bytes(length=4, byteorder='big'))
    elif args.mode == 'read':
        raise NotImplementedError
