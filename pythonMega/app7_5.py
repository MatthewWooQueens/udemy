import os

def main():
    if not os.path.exists('./members.txt'):
        open('members.txt','x')
    file = open('members.txt', 'a')
    name = input('Add a new member: ')
    file.write(f"{name}\n")
    file.close()
if __name__ == '__main__':
    main()
