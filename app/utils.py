import re

def get_population_of_country(country_dict):
  population_dict={}
  for key,value in country_dict.items():
    if re.search('[0-9]+ Population$',key):
      #print(key,value)
      population_dict[key.replace(' Population','')]=int(value)
  population_dict=dict(sorted(population_dict.items()))
  keys=population_dict.keys()
  values=population_dict.values()
  return keys,values

def get_percentage_population_of_world_v2(data):
  countries=[x['Country/Territory'] for x in data]
  percentages=[float(x['World Population Percentage']) for x in data]
  return dict(sorted(dict(zip(countries,percentages)).items(),key=lambda x:x[1]))

def get_percentage_population_of_world(data):
  percentage_dict={}
  for countries in data:
    country=None
    percentage=0.0
    for key,value in countries.items():
      if 'Country' in key:
        country=value
      if 'Population Percentage' in key:
        percentage=float(value)
    if country is not None:
      percentage_dict[country]=percentage
  percentage_dict=dict(sorted(percentage_dict.items(),key=lambda x:x[1]))
  return percentage_dict                       

def func_format_label_with_value(label,value):
  return f'{label} - {value:.1f} %'
  
def get_topX_sum_others_percentage_population_of_world(percentage_dict,top):
  percentage_dict_top={}
  funcFormat=func_format_label_with_value
  percentage_dict=dict(sorted(percentage_dict.items(),key=lambda x:x[1],reverse=True))
  counter=1
  sum_others=0.0
  for key,value in percentage_dict.items():
    if counter<=top-1:
      percentage_dict_top[funcFormat(key,value)]=value
    elif value!=0:
      sum_others+=value
    counter+=1
  if sum_others>0:
    percentage_dict_top[funcFormat('Resto',sum_others)]=sum_others
  percentage_dict_top=dict(sorted(percentage_dict_top.items(),key=lambda x:x[1]))
  return percentage_dict_top
  
def format_key_whit_value(percentage_dict):
  funcFormat=func_format_label_with_value
  percentage_dict_formatted={funcFormat(k,v):v for k,v in percentage_dict.items()}
  return percentage_dict_formatted
  
A='Hola'

def data_by_country(data,country):
  result=list(filter(lambda item:item['Country/Territory'].upper()==country.upper(),data))
  return result
