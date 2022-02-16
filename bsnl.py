def main():
    dataBase=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
              't', 'u', 'v', 'w', 'x', 'y', 'z']
    for a in dataBase:
        for b in dataBase:
            for x in range(0,10) :
                for y in range(0,10):
                    for z in range(0, 10):
                        print(f'{a}{b}@BSNL{x}{y}{z}')



main()
