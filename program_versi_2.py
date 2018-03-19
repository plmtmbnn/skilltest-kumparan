import pandas as pd
import time

start_time = time.time()

total_amount_money = 0
first_two_digit = {}
highest = {}
id_file = 0
while (id_file < 40):
    num = "%02d" % (id_file,)
    filename = 'data/MichaelJackson_'+ num + '.csv'
    readcsv = pd.read_csv(filename, iterator=True, chunksize=3000000)
    df = pd.DataFrame(pd.concat(readcsv, ignore_index=True))
    
    for line in df.itertuples():
        total_amount_money += line[2]
        if(line[1][:2] in first_two_digit != False):
            first_two_digit[line[1][:2]] += line[2]
        else:
            first_two_digit[line[1][:2]] = line[2]
        if(len(highest) != 1000000):
            highest[line[1]] = line[2]        
        if(len(highest) == 1000000 and line[2] > highest[min(highest,key=highest.get)]):
            highest[line[1]] = highest[min(highest,key=highest.get)]
            del highest[min(highest,key=highest.get)]
            highest[line[1]] = line[2]
    id_file += 1       
    del readcsv
    del df

# "#Task1"
#----Calculate the sum of money from all accounts----"
#print sum(frequency.values())
f = open('output/task_1/total_wealth.txt','w')
f.write(str(total_amount_money))
f.close()




print("\n--- %s seconds ---" % (time.time() - start_time))