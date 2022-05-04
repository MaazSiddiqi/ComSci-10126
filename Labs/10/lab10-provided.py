def readPitchers():
    all_pitchers = []
    with open('pitchers.txt','r') as pit:

        for p in pit:
            data = p.split('\t')
            pObj = Pitcher(data[0],data[1],int(data[2]),int(data[3]),float(data[4]))
            all_pitchers.append(pObj)

    return all_pitchers

def readBatters():
    all_batters = []
    with open('batters.txt','r') as bat:
        for b in bat:
            data = b.split('\t')
            bObj = Batter(data[0],data[1],int(data[2]),int(data[3]),float(data[4]))
            all_batters.append(bObj)

    return all_batters
