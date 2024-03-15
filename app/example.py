import main

print('Desde Example =>',main.data)

print('Desde main =>')
#Dualidad entre modulos usando if __name__=='__main__': en main.py
main.run()

print(main.utils.get_population())