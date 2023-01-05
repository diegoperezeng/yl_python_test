def calc_from_days(days,unity):
  wc_number = 0
  wc_def = ""
  if unity == "h":
    wc_number = 24
    wc_def = "horas"
  elif unity == "m":
    wc_number = 24 * 60
    wc_def = "minutos"
  elif unity == "s":
    wc_number = 24 * 60 * 60
    wc_def = "segundos"
  if unity == "h" or unity == "m" or unity == "s":    
    return print(f"{days} dias são {days * wc_number} {wc_def}.")
  else:
    return print("Utilize 'h' para hora\nUtilize 'm' para minutos\nUtilize 's' para segundos\n")
    

def begin_prog():
  days = input("Digite a quantidade de dias:\n")
  unity = ""
  while unity != "h" and unity != "m" and unity != "s":
    unity = input("Digite 'h' para calculo de horas, 'm' para minutos e 's' para segundos:\n")
    print(unity.casefold()) and print("\n")
    print(unity.center(30,"-")) and print("\n")
    print(unity.capitalize()) and print("\n")
    
  calc_from_days(int(days),unity)


begin_prog()

