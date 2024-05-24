import os

def main():
    print("hello world")
    file = open(r'garbage.txt', 'w') #Using a row string
    file.write('yolo')
    file.close()

if __name__ == '__main__':
    main()
