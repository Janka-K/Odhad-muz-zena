#Vytvoř funkci, která dostane jako argument příjmení a zkusí podle něj uhodnout #pohlaví. Funkce bude vracet řetězec "žena" nebo "muž". Funkce bude součástí #programu, který se na příjmení zeptá a následně vypíše odhad pohlaví uživatele.

prijmeni = input("Napiste Vase prijmeni: ")



def pohlavi(prijmeni):
  if prijmeni[-3:].lower() == "ova" or prijmeni[-3:].lower() == "ová":
    return "zena"
  else:
    return "muz"

print(f"Vase pohlavi na zaklade prijmeni {prijmeni} je {pohlavi(prijmeni)}")




    