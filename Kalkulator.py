import Wzory
print("Dostępne wybory: \n"
      "1. Pole kwadratu \n"
      "2. Pole kwadratu przy użyciu przekątnych \n"
      "3. Obwód kwadratu lub rombu \n"
      "4. Pole prostokąta \n"
      "5. Pole równoległoboku lub rombu \n"
      "6. Obwód prostokąta, równoległoboku lub deltoidu \n"
      "7. Pole trapezu \n"
      "8. Obwód trapezu \n"
      "9. Pole rombu \n"
      "10. Pole deltoidu lub romba przy użyciu przekątnych \n"
      "11. Pole trójkąta \n"
      "12. Pole trójkąta równobocznego \n"
      "13. Wysokość trójkąta równobocznego \n "
      "14. Pole koła \n"
      "15. Objętość kuli \n"
      "16. Pole kuli \n"
      "17. Objętość stożka \n"
      "18. Pole stożka \n"
      "19. Pole walca \n"
      "20. Objętość walca \n"
      "21. Pole sześcianu \n"
      "22. Objętość sześcianu \n"
      "Q. Quit")

while True:
    wybor = int(input("Co chcesz policzyć? "))
    match wybor:
            case 1:
                  a = float(input("Wprowadź a: "))
                  print(Wzory.P_kwadrat(a))
            case 2:
                  d = float(input("Wprowadź d: "))
                  print(Wzory.P_kwadrat_przekatne(d))
            case 3:
                  a = float(input("Wprowadź a: "))
                  print(Wzory.Ob_kwadrat(a))
            case 4:


