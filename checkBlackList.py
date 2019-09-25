def checkBlackList(licensePlate):
    try:
        fp = open('./blackLists/examplePlates.txt')
        line = fp.readline()
        while line:
            if line.strip().lower() == licensePlate.lower():
                return True
            line = fp.readline()
        return False
    except:
        print("An exception occurred")
    finally:
        fp.close()