import csv
f = open('guns.csv')
data = list(csv.reader(f))
print(data[:5])

headers = data[0]
data = data[1:]
print(headers)
print(data[:5])

years = []
for row in data:
    years.append(row[1])
    
    
years_counts = {}
for year in years:
    if year in years_counts:
        years_counts[year] += 1
    else:
        years_counts[year] = 1
        
print(years_counts)

import datetime
dates = []

for row in data:
    year = int(row[1])
    month = int(row[2])
    dates.append(datetime.datetime(year = year, month = month, day = 1))
    

print(dates[:5])

date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1
        
print(date_counts)
    

sexes = []
for row in data:
    sexes.append(row[5])


sex_counts = {}
for sex in sexes:
    if sex in sex_counts:
        sex_counts[sex] += 1
    else:
        sex_counts[sex] = 1
        
        
races = []
for row in data:
    races.append(row[7])


race_counts = {}
for race in races:
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1
        
print(sex_counts)
print(race_counts)

c = open('census.csv')
census = list(csv.reader(c))

print(census)

mapping = {'White':197318956, 'Hispanic':44618105, 'Black':40250635, 'Native American/Native Alaskan':3739506,'Asian/Pacific Islander': 15159516+ 674625}

race_per_hundredk = {}

for race in race_counts:
    race_per_hundredk[race] = race_counts[race]/mapping[race]*100000

print(race_per_hundredk)



intents = []
for row in data:
    intents.append(row[3])
    
homicide_race_counts = {}

for i, race in enumerate(races):
    if intents[i] == "Homicide":
        if race in homicide_race_counts:
            homicide_race_counts[race] += 1
        else:
            homicide_race_counts[race] = 1
            
for race in homicide_race_counts:
    homicide_race_counts[race] = homicide_race_counts[race]/mapping[race]*100000
    
    
print(homicide_race_counts)
