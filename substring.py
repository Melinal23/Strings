def main():

    string = "laboratory"

    sub = "rat"

    if sub in string:
        print(True)
    else:
        print(False)

    #OR

    print(string.find(sub))

if __name__ == '__main__':
    main()
