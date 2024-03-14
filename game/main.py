import random

def choose_options():
  options=('piedra','papel','tijera')
  user_opcion = input('piedra, papel o tijera => ')
  user_opcion=user_opcion.lower()

  if user_opcion not in options:
    print('Esa opcion no es valida')
    #continue
    return None,None

  computer_opcion = random.choice(options)

  print('User option => ',user_opcion)
  print('Computer option => ',computer_opcion)
  return user_opcion,computer_opcion

def check_rules(user_opcion,computer_opcion,user_wins,computer_wins):
  if user_opcion == computer_opcion:
    print(f'Empate! ambos eligieron {user_opcion}')
  elif user_opcion == 'piedra':
    if computer_opcion == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      user_wins+=1
    else:
      print('papel gana a piedra')
      print('computer gano')
      computer_wins+=1
  elif user_opcion == 'papel':
    if computer_opcion == 'piedra':
      print('papel gana a piedra')
      print('user gano!')
      user_wins+=1
    else:
      print('tijera gana a papel')
      print('computer gano')
      computer_wins+=1
  elif user_opcion == 'tijera':
    if computer_opcion == 'papel':
      print('tijera gana a papel')
      print('user gano!')
      user_wins+=1
    else:
      print('piedra gana a tijera')
      print('computer gano')
      computer_wins+=1
  return user_wins,computer_wins

def run_game():
  computer_wins=0
  user_wins=0
  rounds=0
  while computer_wins<2 and user_wins<2:
  
    print('*' * 10)
    print('ROUND',rounds+1)
    print('*' * 10)
    print('🤖cumputadora',computer_wins)
    print('🙋usuario',user_wins)
    print('*' * 10)
  
    user_opcion,computer_opcion= choose_options()
    if user_opcion is None:
      continue
    user_wins,computer_wins=check_rules(user_opcion,computer_opcion,user_wins,computer_wins)
    rounds+=1
  
  print('*' * 10)
  print('Final')
  print('Numero de Rondas:',rounds)
  print('*' * 10)
  print('🤖cumputadora',computer_wins)
  print('🙋usuario',user_wins)
  print('*' * 10)
  if user_wins>computer_wins:
    print('🎖️ Se acabo Ganador 🙋 User')
  else:
    print('🎖️ Se acabo Ganador 🤖 Computer')
  print('*' * 10)

run_game()
