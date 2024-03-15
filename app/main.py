import utils
import read_csv
import charts

def run():
  data=read_csv.read_csv('./data.csv')
  user_country=input(f'Type the country => ')
  #user_country='colombia'
  result=utils.data_by_country(data,user_country)
  if len(result)>0:
    country=result[0]
    keys,values=utils.get_population_of_country(country)
    print(list(keys))
    print(list(values))
    title='Población por año'
    suptitle='Población de '+user_country.title()
    xlabel='Año'
    ylabel='Población en millones'
    charts.set_yaxis_funtion_ticker_FuncFormatter(lambda x,pos:f'{x/1000000:.0f} mill.')
    charts.generate_bar_chart(country['Country/Territory'],keys,values,title,suptitle,xlabel,ylabel)
    #charts.generate_line_chart(keys,values,title,suptitle,xlabel,ylabel)

  #result=utils.get_percentage_population_of_world(data)
  #otra solucion 
  result=utils.get_percentage_population_of_world_v2(data)
  if len(result)>0:
    '''
    Resume el top 10 donde el 10 el la suma del resto de paises
    Tambien formatea las Etiquetass
    '''
    result=utils.get_topX_sum_others_percentage_population_of_world(result,12)
    #Formatea las Etiquetas
    #result=utils.format_key_whit_value(result)
    
    keys=result.keys()
    values=result.values()
    #print(list(keys))
    #print(list(values))
    
    title='Población Mundial'
    suptitle='Top 12 de Porcentaje de Población Mundial'
    xlabel='Porcentaje de Población por pais'
    charts.generate_pie_chart('population_of_world',keys,values,title,suptitle,xlabel)

if __name__=='__main__':
  run()