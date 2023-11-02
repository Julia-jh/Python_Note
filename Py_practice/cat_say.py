"""
import this module and promptly take input from user and display a cat and saying.
"""
def cat_say(saying):
    length = len(saying)

    print(' ' * 12, '_' * length) # 12
    print(' ' * 10, '< {} >'.format(saying)) # 10
    print(' ' * 12, '-' * length) # 12
    print('           /') # 11
    print(' /\\_/\\    /') # 10
    print('( o.o )')
    print(' > ^ <')


def main():
    saying = input("What would you like the cat to say? ")
    cat_say(saying)

if __name__ == '__main__':
    main()