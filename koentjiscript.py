import argparse

import koentjiparse.parser as kparse

parser = argparse.ArgumentParser(prog='KoentjiScript v1.0', description='Solusi nomor satu untuk segala keperluan parsing-parsingan koentjiscript (Node.js) Anda.')
parser.add_argument('filename', type=str)

if __name__ == '__main__':
    args = parser.parse_args()

    # Pass filename ke parser untuk dibuka dan diproses
    print(f'Memproses file {args.filename}...')
    kparse.get(args.filename)
