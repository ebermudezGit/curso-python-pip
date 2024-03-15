import csv
import re

data=[]

def read_csv_dict(path):
  with open(path,'r') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    header=next(reader)
    data.clear()
    for row in reader:
      data.append({key:value for key,value in zip(header,row)})

def get_population_contry(Country):
  country=list(filter(lambda item:item['Country/Territory']=='Colombia',data))
  dict_population={}
  for key,value in country[0].items():
    if re.search('[0-9]+ Population$',key):
      #print(key,value)
      dict_population[key.replace(' Population','')]=int(value)
  return dict_population
  
if __name__=='__main__':
  read_csv_dict('./app/data.csv')
  print(get_population_contry('Colombia'))