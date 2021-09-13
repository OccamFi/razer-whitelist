import numpy as np
import csv
import sys

initialListPath = sys.argv[1]
blockHashPath = sys.argv[2]

print(sys.argv)

initialList = np.loadtxt(initialListPath, dtype='str', delimiter=',', skiprows=1, usecols=(0, 1, 2, 3)) #Loading of the list before randomization
blockHash = open(blockHashPath, 'r').read()

seed = np.frombuffer(str.encode(blockHash), dtype='uint32') #preparing the seed from block hash

np.random.seed(seed) #setting the seed

np.random.shuffle(initialList); #randomizing the list

randomList = np.insert(initialList, 0, ['ETH Address','Stake','Tier','Participation Weight'], axis=0)

with open('randomList.csv', 'w', newline='') as file: #Saving randomized list
    writer = csv.writer(file)
    writer.writerows(randomList)
