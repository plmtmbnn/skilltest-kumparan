#Polma E. Tambunan

import csv
import time

frequency = {}
freq_first_two_digit = {}

start_time = time.time()
datas = 0
id_file = 0

while (id_file < 40):
    data = 0
    i = 0
    num = "%02d" % (id_file,)
    filename = 'data/MichaelJackson_'+ num + '.csv'
    file = open(filename)
    with file as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(i > 100000):
                break
            data = data + int(row['num'])
            frequency[row['id']] = int(row['num'])
            flag = row['id'][:2] in freq_first_two_digit
            if(flag != False):
                freq_first_two_digit[row['id'][:2]] += long(row['num'])
            else:
                freq_first_two_digit[row['id'][:2]] = long(row['num'])
            i = i + 1
    datas = datas + data
    id_file = id_file + 1 
    file.close()

print "\n#Task1"
print "\n----Calculate the sum of money from all accounts----"
print sum(frequency.values())
f = open('output/task_1/total_wealth.txt','w')
f.write(str(sum(frequency.values())))
f.close()


print "\n#Task2"
print "\n----Group the account based on the first two character on the id, then calculate the sum of money for each group----"
f = open('output/task_2/grouped_wealth.csv','w')
column_name = "group,sum\n"
f.write(column_name)
for c in freq_first_two_digit:
    print c,freq_first_two_digit[c]
    row = ''+c+','+str(freq_first_two_digit[c])+'\n'
    f.write(row)
f.close()

#task 3a
top100 = sorted(frequency.items(),key=lambda kv : kv[1],reverse=True)
print "\n#Task3 [a]"
print "\n----TOP 10 : The most biggest amount of money----"
sumtop100 = []
f = open('output/task_3/richest.csv','w')
column_name = "group,sum\n"
f.write(column_name)

for a,b in top100[:100]:
    print a,b
    row = ''+a+','+str(a)+'\n'
    f.write(row)
    sumtop100.append(b)
print "\n#Task3 [b]"
print "\nRatio"
a = float(sum(int(i) for i in sumtop100))
b = float(sum(frequency.values()))
c = a/b
print 'richest_sum = {} richest_percentage={}'.format(a,c)
text = 'richest_sum = {} richest_percentage={}'.format(a,c)
f = open('output/task_3/richest_stats.txt','w')
f.write(text)
f.close()

print("\n--- %s seconds ---" % (time.time() - start_time))