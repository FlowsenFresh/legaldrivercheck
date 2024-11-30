def get_user_age():
  """
  Funktion wo der Bediener sein Alter eingeben kann und der Wert zurück gegeben wird
  """
  while True:
    try:
      user_age = int(input('Gib hier dein Alter ein: '))
      if user_age < 0:
        print('Dein Alter kann nicht weniger als 0 betragen')
      else:
        return user_age
    except ValueError:
      print('Ungültige Eingabe. Gib bitte eine gültige Zahl ein!')

def check_driving_eligibility(user_age):
  """
  Funktion um zu checken was für das eingegebene Alter die richtige Wahl ist
  """
  if user_age >= 18:
    return 'alleine fahren'
  elif user_age == 17:
    return 'begleitetes fahren'
  else:
    return 'warten'

def display_driving_result(msg):
  """
  Funktion für die Ausgabe des Ergebnises von check_driving_eligibility()
  """
  if msg == 'alleine fahren':
    print('Du bist alt genug um alleine zu fahren!')
  elif msg == 'begleitetes fahren':
    print('Du bist noch zu Jung um alleine zu fahren und brauchst somit eine Begleitperson')
  else:
    print('Du musst noch ein bisschen warten weil du noch etwas zu jung bist für den Führerschein')

def main():
  """
  Main Funktion die das Programm steuert.
  """
  user_age = get_user_age()
  driving_eligibility_msg = check_driving_eligibility(user_age)
  display_driving_result(driving_eligibility_msg)

if __name__ == '__main__':
  main()

