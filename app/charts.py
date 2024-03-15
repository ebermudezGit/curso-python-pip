import matplotlib.pyplot as plt
from matplotlib import ticker

yaxis_funtion_ticker_FuncFormatter=None

def set_yaxis_funtion_ticker_FuncFormatter(funct=lambda x,pos:f'{x}'):
  global yaxis_funtion_ticker_FuncFormatter
  yaxis_funtion_ticker_FuncFormatter=funct

def generate_bar_chart(image_name,labels,values,title,suptitle,xlabel,ylabel):
  fig,ax=plt.subplots()
  ax.bar(labels,values)
  #formato de los ejes, Eje y estilo plano, Evita notacion cientifica
  ax.ticklabel_format(axis='y',style='plain')
  #ax.yaxis.set_major_formatter(ticker.FuncFormatter(fn_millions))
  #ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.0f} mill."))
  #ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x,pos:f'{x/1000000:.0f} mill.'))
  if yaxis_funtion_ticker_FuncFormatter is not None:
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(yaxis_funtion_ticker_FuncFormatter))
  
  #Título
  plt.title(title,fontsize = 10,color = 'black',style = "italic")
  # Supertítulo del gráfico
  plt.suptitle(suptitle,size = 15,fontweight = 'bold',color = 'black')
  # Etiqueta del eje x
  plt.xlabel(xlabel)
  #Título del eje Y 
  plt.ylabel(ylabel)
  #Fuente del gráfico
  fig.text(0.8, 0.005,'Fuente: kaggle',ha='right',color = 'black',style = "italic",fontsize = 6)
  #Eliminar marco del gráfico
  plt.box(on=None)
  #Líneas horizontales en el gráfico
  ax.set_axisbelow(True)
  ax.yaxis.grid(True, color='#bdbdbd')

  #Etiquetas para las barras
  for bar in ax.patches:
    # Obtenemos la altura para las anotaciones.
    bar_value = bar.get_height()
    # Formato de números con separador de miles.
    text = f'{bar_value:,.0f}'
    # Centrar etiquetas de x-axis.
    text_x = bar.get_x() + bar.get_width() / 2
    # get_y() lugar donde empieza la barra y añadimos la altura.
    text_y = bar.get_y() + bar_value
    # Ubicación de las etiquetas de datos de las barras y color
    ax.text(text_x, text_y, text, ha='center',va='bottom', color="black",size=5)
  
  #plt.show()
  plt.savefig(f'./imgs/{image_name}.png')
  plt.close()

def generate_pie_chart(image_name,labels,values,title,suptitle,xlabel):
  fig,ax=plt.subplots()
    
  # Rotacion por el x-axis
  angle = -40
  #Mueestra los valores dentro de la revanada del Pie (2 formas)
  #ax.pie(values, labels=labels, autopct='%1.1f%%',startangle=angle)
  #wedges, *_ = ax.pie(values, autopct='%1.1f%%', startangle=angle,labels=labels)
  #Miestra solo el Pie
  ax.pie(values, labels=labels,startangle=angle)
  #Imprime las leyendas
  #ax.legend( labels, loc='center left', bbox_to_anchor=(1, 0))
  
  
  if yaxis_funtion_ticker_FuncFormatter is not None:
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(yaxis_funtion_ticker_FuncFormatter))

  #Título
  plt.title(title,fontsize = 10,color = 'black',style = "italic")
  # Supertítulo del gráfico
  plt.suptitle(suptitle,size = 15,fontweight = 'bold',color = 'black')
  # Etiqueta del eje x
  plt.xlabel(xlabel)
  
  #plt.show()
  plt.savefig(f'./imgs/{image_name}.png')
  plt.close()

def generate_scatter_chart(labels,values):
  fig,ax=plt.subplots()
  ax.scatter(labels,values)
  #plt.show()
  plt.savefig('scatter.png')
  plt.close()

def generate_line_chart(labels,values,title,suptitle,xlabel,ylabel):
  fig,ax=plt.subplots()
  ax.plot(labels,values)
  #formato de los ejes, Eje y estilo plano, Evita notacion cientifica
  ax.ticklabel_format(axis='y',style='plain')
  if yaxis_funtion_ticker_FuncFormatter is not None:
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(yaxis_funtion_ticker_FuncFormatter))
  #Título
  plt.title(title,fontsize = 10,color = 'black',style = "italic")
  # Supertítulo del gráfico
  plt.suptitle(suptitle,size = 15,fontweight = 'bold',color = 'black')
  # Etiqueta del eje x
  plt.xlabel(xlabel)
  #Título del eje Y 
  plt.ylabel(ylabel)
  #Fuente del gráfico
  fig.text(0.8, 0.005,'Fuente: kaggle',ha='right',color = 'black',style = "italic",fontsize = 6)
  #Eliminar marco del gráfico
  plt.box(on=None)
  #Líneas horizontales en el gráfico
  ax.set_axisbelow(True)
  ax.yaxis.grid(True, color='#bdbdbd')

  #Etiquetas para las barras
  for bar in ax.patches:
    # Obtenemos la altura para las anotaciones.
    bar_value = bar.get_height()
    # Formato de números con separador de miles.
    text = f'{bar_value:,.0f}'
    # Centrar etiquetas de x-axis.
    text_x = bar.get_x() + bar.get_width() / 2
    # get_y() lugar donde empieza la barra y añadimos la altura.
    text_y = bar.get_y() + bar_value
    # Ubicación de las etiquetas de datos de las barras y color
    ax.text(text_x, text_y, text, ha='center',va='bottom', color="black",size=6)
    
  #plt.show()
  plt.savefig('line.png')
  plt.close()

def generate_variuos_chart(labels,values):
  #fig,((ax,ax2),(ax3,ax4))=plt.subplots(2,2)
  fig,((ax,ax2),(ax3,ax4))=plt.subplots(nrows=2,ncols=2,facecolor='lightskyblue',layout='constrained')
  
  fig.suptitle('Varios graficos')
  
  ax.set_title('Gráfica de Pie')
  ax.pie(values,labels=labels)
  ax2.set_title('Gráfica de Lineas')
  ax2.plot(labels,values)
  ax3.set_title('Gráfica de Barras')
  ax3.bar(labels,values)
  ax4.set_title('Gráfica de Dispersión')
  ax4.scatter(labels,values)
  #plt.show()
  plt.savefig('variuos_chart.png')
  plt.close()

if __name__=='__main__':
  labels=['a','b','c']
  values=[100,200,80]
  #generate_bar_chart(labels,values,'','','','')
  #generate_pie_chart(labels,values)
  #generate_scatter_chart(labels,values)
  #generate_line_chart(labels,values,'','','','')
  generate_variuos_chart(labels,values)
  