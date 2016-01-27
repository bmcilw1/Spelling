#!/usr/bin/env python

from __future__ import absolute_import, division, print_function, unicode_literals
import fileinput

def main():
    '''
    The strategy used to solve this problem will be simple hashing with the characters being
    the keys and the digit sequence being the value.
    '''
    words = {}
    letters = {}
    message = ""
    cases = int(0)
    case = int(1)

    letters['a'] = 2
    letters['b'] = 2
    letters['c'] = 2
    letters['d'] = 3
    letters['e'] = 3
    letters['f'] = 3
    letters['g'] = 4
    letters['h'] = 4
    letters['i'] = 4
    letters['j'] = 5
    letters['k'] = 5
    letters['l'] = 5
    letters['m'] = 6
    letters['n'] = 6
    letters['o'] = 6
    letters['p'] = 7
    letters['q'] = 7
    letters['r'] = 7
    letters['s'] = 7
    letters['t'] = 8
    letters['u'] = 8
    letters['v'] = 8
    letters['w'] = 9
    letters['x'] = 9
    letters['y'] = 9
    letters['z'] = 9
    letters[' '] = 0

    for line in fileinput.input():
        if not fileinput.isfirstline():
            for character in line:
                if character not in letters:
                    pass
                elif len(message) > 0 and letters[character] == message[-1:]:
                    message += " " + str(letters[character])
                else:
                    message += str(letters[character])
                    
            print("Case #%d: %s" % (case, message))

            message = ""
            case += 1

    fileinput.close()

if __name__ == '__main__':
    main()
