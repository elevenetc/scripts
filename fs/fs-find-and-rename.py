import fnmatch
import os
import sys

from termcolor import colored

help = "\n" \
       "Required params:\n" \
       "  any search name/pattern (example: '*.mov', '*.*', 'hello')\n" \
       "  replace name\n" \
       "Optional params:\n" \
       "  'help'" \
       "\n"


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


if __name__ == '__main__':

    argsLen = len(sys.argv)

    if argsLen == 1 or (argsLen == 2 and sys.argv[1] == "help"):
        print colored(help, 'green')
    if argsLen <= 2:
        print colored('No required params are passed.', 'red')
        print colored(help, 'green')
    else:

        path = os.path.dirname(os.path.realpath(__file__))
        search = sys.argv[1]
        replace = sys.argv[2]
        result = find(search, './')

        print
        print('Path: ' + colored(path, 'yellow'))
        print('Search: ' + colored(search, 'yellow'))
        print('Replace: ' + colored(replace, 'yellow'))
        print

        print('Found files: ' + colored(result, 'magenta'))

        if len(result) == 0:
            print colored('No files found for "' + search + '"', 'red')
        else:
            for path in result:
                fileName = os.path.basename(path)
                newPath = path.replace(fileName, replace)
                os.rename(path, newPath)
                print 'Renamed From ' + colored(path, 'magenta') + ' to ' + colored(newPath, 'green')
