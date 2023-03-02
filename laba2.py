#задача 1
# par1 = input("")
# par2 = input("")
# if par1 == par2:
#     print("Пароль принят!")
# else:
#     print("Повторите попытку! Пароли не совпадают!")
#

#задача2
# mesto = int(input(""))
# if mesto in range(1,36):
#     if mesto % 2 == 0:
#         print("Место верхнее, в купе")
#     else:
#         print("Место нижнее, в купе")
# if mesto in range(38,53):
#     if mesto % 2 == 0:
#         print("Место верхнее боковое")
#     else:
#         print("Место нижнее боковое")


#задача3
# year = int(input(""))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Год", year, "- високосеный.")
# else:
#     print("Год", year, "- НЕ високосеный.")

#задача4
# vvod1 = input("")
# vvod2 = input("")
# if (vvod1 == "красный" and vvod2 == "синий") or (vvod2 == "красный" and vvod1 == "синий"):
#     print("фиолетовый")
# if (vvod1 == "красный" and vvod2 == "желтый") or (vvod2 == "красный" and vvod1 == "желтый"):
#     print("оранжевый")
# if (vvod1 == "синий" and vvod2 == "желтый") or (vvod2 == "синий" and vvod1 == "желтый"):
#     print("зеленый")
# if vvod1 or vvod2 != "красный" or "синий" or "желтый":
#     print("Не правильный цвет!")


#задача5
# n = int(input("Введите N"))
# res = ''
# for i in range(n):
#     s = input()
#     res = res + s + ''
# print(res)