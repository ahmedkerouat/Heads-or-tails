from colorama import Fore , Style
import random
language = input(Fore.YELLOW +"You can choose your language between French and English \n" +Style.RESET_ALL)
def heads_or_tails_fr() :
  times = float(input(Fore.YELLOW +"Combien de fois voulez vous jouer ? \n" + Style.RESET_ALL))
  player_choice = input(Fore.YELLOW + "Pile ou face ? \n" + Style.RESET_ALL)
  times2 = times
  percentage = input(Fore.YELLOW +"Voulez vous voir la probabilité de chaque possibilité ?  (Oui ou non) \n"+ Style.RESET_ALL)
  vizualise = input(Fore.YELLOW +"Voulez vous voir chaque tour ?  (Oui ou non) \n"+ Style.RESET_ALL)

  possibility = [1 , 0]
  tails = 0
  heads = 0

  while times != 0 :
      times = times - 1
        
      result = random.choice(possibility)
      if result == 1:
        tails = tails + 1

        if vizualise =="oui":
            print(Fore.YELLOW +"Le résultat était face"+ Style.RESET_ALL)
            if player_choice == "face":
              print(Fore.GREEN +"Vous avez gagner !"+ Style.RESET_ALL)
            else:
              print(Fore.RED +"Vous avez perdu.."+ Style.RESET_ALL)

          
        else:
          heads = heads + 1
          if vizualise == "oui":
            print(Fore.YELLOW +"Le résultat était pile"+ Style.RESET_ALL)
            if player_choice == "face" :
              print(Fore.RED +"Vous avez perdu.."+ Style.RESET_ALL)
            else:
              print(Fore.GREEN +"Vous avez gagner !"+ Style.RESET_ALL)

            
  if player_choice == "face" :
      print(Fore.GREEN +"Sur", times2, "fois, vous avez gagner", tails,"fois." )
  else:
      print(Fore.GREEN +"Sur", times2, "fois, vous avez gagner", heads,"fois.")
  if percentage == "oui" or "Oui":
      division1 = tails / times2
      division2 = heads / times2
      print(Fore.YELLOW +"La probabilité d'avoir face est", division1 * 100 ,"%"+ Style.RESET_ALL)
      print(Fore.YELLOW +"La probabilité d'avoir pile est", division2 * 100 ,"%"+ Style.RESET_ALL)
  restart = input(Fore.YELLOW +"Voulez vous refaire ? (Oui ou non) \n"+ Style.RESET_ALL)
  if restart == "oui":
      heads_or_tails_eng()
  else:
      print(Fore.YELLOW +"A bientôt ! \n"+ Style.RESET_ALL)

def heads_or_tails_eng() :


    times = float(input(Fore.YELLOW +"How many times do you want to play \n" + Style.RESET_ALL))
    player_choice = input(Fore.YELLOW +"Heads or tails ? \n" +Style.RESET_ALL)
    times2 = times
    percentage = input(Fore.YELLOW +"Do you want to see the probabilty of each possibility ? (Yes or No) \n"+ Style.RESET_ALL)
    vizualise = input(Fore.YELLOW +"Do you want to see each flip ? (Yes or No) \n"+ Style.RESET_ALL)

    possibility = [1 , 0]
    tails = 0
    heads = 0

    while times != 0 :
        times = times - 1
        
        result = random.choice(possibility)
        if result == 1:
          tails = tails + 1

          if vizualise =="yes":
              print(Fore.YELLOW +"The result was tails"+ Style.RESET_ALL)
              if player_choice == "tails":
                print(Fore.GREEN +"You have won !"+ Style.RESET_ALL)
              else:
                print(Fore.RED +"You have lost.."+ Style.RESET_ALL)

          
        else:
          heads = heads + 1
          if vizualise == "yes":
            print(Fore.YELLOW +"The result was heads"+ Style.RESET_ALL)
            if player_choice == "tails" :
              print(Fore.RED +"You have lost.."+ Style.RESET_ALL)
            else:
              print(Fore.GREEN +"You have won !"+ Style.RESET_ALL)

            
    if player_choice == "tails" :
        print(Fore.GREEN +"Out of", times2, "times, you have won", tails,"times." )
    else:
        print(Fore.GREEN +"Out of", times2, "times, you have won", heads,"times.")
    if percentage == "Yes" or "yes":
        division1 = tails / times2
        division2 = heads / times2
        print(Fore.YELLOW +"The probability of getting tails is", division1 * 100 , "%"+ Style.RESET_ALL)
        print(Fore.YELLOW +"The probability of getting heads is", division2 * 100 ,"%"+ Style.RESET_ALL)
    restart = input(Fore.YELLOW +"Do you want to restart ? (Yes or no) \n"+ Style.RESET_ALL)
    if restart == "yes":
        heads_or_tails_eng()
    else:
        print(Fore.YELLOW +"See you soon \n"+ Style.RESET_ALL)
if language == "english":
  heads_or_tails_eng()
else:
  heads_or_tails_fr()   

