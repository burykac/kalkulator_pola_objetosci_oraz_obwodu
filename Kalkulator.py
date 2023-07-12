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
                  a = float(input("Wprowadź a: "))
                  b = float(input("Wprowadź b: "))
                  print(Wzory.P_prostokat(a, b))
            case 5:
                  a = float(input("Wprowadź a: "))
                  b = float(input("Wprowadź h: "))
                  print(Wzory.P_prostokat(a, b))
            case 6:
                  a = float(input("Wprowadź a: "))
                  b = float(input("Wprowadź b: "))
                  print(Wzory.Ob_prostokat(a, b))
            case 7:
                  a = float(input("Wprowadź a: "))
                  b = float(input("Wprowadź b: "))
                  h = float(input("Wprowadź h: "))
                  print(Wzory.P_trapez(a, b, h))
            case 8:
                  a = float(input("Wprowadź a: "))
                  b = float(input("Wprowadź b: "))
                  c = float(input("Wprowadź c: "))
                  d = float(input("Wprowadź d: "))
                  print(Wzory.Ob_trapez(a, b, c, d))
            case 9:
                  a = float(input("Wprowadź a: "))
                  b = float(input("Wprowadź h: "))
                  print(Wzory.P_prostokat(a, b))
            case 10:
                  d = float(input("Wprowadź d: "))
                  p = float(input("Wprowadź p: "))
                  print(Wzory.P_romb_przekatne(d, p))
            case 11:
                  a = float(input("Wprowadź a: "))
                  h = float(input("Wprowadź h: "))
                  print(Wzory.P_trojkat(a, h))
            case 12:
                  a = float(input("Wprowadź a: "))
                  print(Wzory.P_t_rownobocznego(a))
            case 13:
                  a = float(input("Wprowadź a: "))
                  print(Wzory.Wysokosc_t_rownobocznego(a))
            case 14:
                  r = float(input("Wprowadź r: "))
                  print(Wzory.P_kola(r))
            case 15:
                  r = float(input("Wprowadź r: "))
                  print(Wzory.V_kuli(r))
            case 16:
                  