import argparse
import sys
import os
import re


def _find_numbered_directories():
    return [ dir for dir in os.listdir() if re.match(r'\d+[a-z]?-', dir) ]

def _determine_renames(dirs):
    def aux(index, dir):
        match = re.match(r'\d+[a-z]?(-.*)$', dir)
        rest = match.group(1)
        return f'{str(index + 1).rjust(2, "0")}{rest}'

    renames = [ (dir, aux(index, dir)) for index, dir in enumerate(dirs) ]

    return [ (old, new) for (old, new) in renames if old != new ]


def _perform_renames(renames):
    for old, new in renames:
        print(f'Renaming {old} to {new}')
        os.rename(old, new)


def _show_renames(renames):
    if renames:
        longest = max(len(x) for x, _ in renames)

        for (old, new) in renames:
            print(f'{old.rjust(longest)} -> {new}')
    else:
        print('no renames necessary')


def shell_entry_point():
    parser = argparse.ArgumentParser(prog='renumber')
    parser.add_argument('-f', '--force', help='Actually perform renames', action='store_true')
    args = parser.parse_args(sys.argv[1:])

    directories = _find_numbered_directories()
    directories.sort()
    renames = _determine_renames(directories)

    if args.force:
        _perform_renames(renames)
    else:
        _show_renames(renames)