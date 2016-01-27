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

    letters['a'] = '2'
    letters['b'] = '22'
    letters['c'] = '222'
    letters['d'] = '3'
    letters['e'] = '33'
    letters['f'] = '333'
    letters['g'] = '4'
    letters['h'] = '44'
    letters['i'] = '444'
    letters['j'] = '5'
    letters['k'] = '55'
    letters['l'] = '555'
    letters['m'] = '6'
    letters['n'] = '66'
    letters['o'] = '666'
    letters['p'] = '7'
    letters['q'] = '77'
    letters['r'] = '777'
    letters['s'] = '7777'
    letters['t'] = '8'
    letters['u'] = '88'
    letters['v'] = '888'
    letters['w'] = '9'
    letters['x'] = '99'
    letters['y'] = '999'
    letters['z'] = '9999'
    letters[' '] = '0'

    for line in fileinput.input():
        if not fileinput.isfirstline():
            for character in line:
                if character not in letters:
                    pass
                elif len(message) > 0 and letters[character][:1] == message[-1:]:
                    message += " " + letters[character]
                else:
                    message += letters[character]
                    
            print("Case #%d: %s" % (case, message))

            message = ""
            case += 1

    fileinput.close()

if __name__ == '__main__':
    main()
