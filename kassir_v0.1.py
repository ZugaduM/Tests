from datetime import datetime
import time
import os
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
#-----------------------------------------------------------------
global open_time
global close_time
global cart
open_time = datetime.now()
close_time = datetime.now()
cart = {}
#-----------------------------------------------------------------


def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')


#-----------------------------------------------------------------


def add_product():
  global cart
  product_name = Prompt.ask("Введите название продукта")

  if product_name in cart:
    print(
        f'Продукт {product_name} уже есть в корзине. Количество: {cart[product_name]["quantity"]}'
    )
    ask = Prompt.ask('Изменить количество?', choices=['Да', 'Нет'])
    if ask == 'Да':
      product_quantity = Prompt.ask("Введите количество продукта")
      cart[product_name]["quantity"] = product_quantity
    else:
      pass
  else:
    product_price = Prompt.ask("Введите цену продукта")
    product_quantity = Prompt.ask("Введите количество продукта")
    cart[product_name] = {"price": product_price, "quantity": product_quantity}

  smena_open()


#-----------------------------------------------------------------


def show_cart():
  global cart
  clear()
  if cart != {}:
    cart_text = Text()
    cart_text.append("Корзина:\n\n")
    for keys, values in cart.items():
      cart_text.append(
          f"{keys} - {values['quantity']} шт. - {values['price']} руб.\n\n")
    cart_text.append("1. Оплатить.\n")
    cart_text.append("2. Очистить корзину.\n")
    cart_text.append("3. Назад.")
    print(Panel(cart_text, title="Касса вер. 0.1", style="grey66 on black"))
    ask = Prompt.ask('Выберите действие')
    if ask == '1':
      oplata()
    if ask == '2':
      clear_cart()
    if ask == '3':
      smena_open()
  else:
    print('Корзина пуста!')
    time.sleep(3)
    smena_open()


#-----------------------------------------------------------------


def clear_cart():
  global cart
  cart.clear()
  print('Корзина очищена!')
  time.sleep(3)
  smena_open()


#-----------------------------------------------------------------


def oplata():
  global cart
  clear()
  sum_ = 0
  oplata_text = Text()
  oplata_text.append("Ваш чек составил:\n\n")
  for keys, values in cart.items():
    oplata_text.append(
        f"{keys} - {values['quantity']} шт. - {values['price']} руб.\n\n")
    sum_ += int(values['price']) * int(values['quantity'])
  oplata_text.append(f"Итого: {sum_} руб.\n")
  print(Panel(oplata_text, title="Касса вер. 0.1", style="grey66 on black"))
  clear_cart()
  Prompt.ask("Нажмите <Enter> для возврата...")


#-----------------------------------------------------------------


def smena_close():
  global open_time, close_time
  clear()
  cart.clear()
  close_time = datetime.now()
  total_time = str(close_time - open_time)
  close_text = Text()
  close_text.append("Смена закрыта!\n\n")
  close_text.append("Время работы составило " +
                    total_time[:len(total_time) - 7])
  print(Panel(close_text, title="Касса вер. 0.1", style="grey66 on black"))
  Prompt.ask("Нажмите <Enter> для завершения...")
  exit()


#-----------------------------------------------------------------


def smena_open():
  global open_time
  clear()
  if open_time == '':
    open_time = datetime.now()
  smena_text = Text()
  smena_text.append("Смена открыта " +
                    datetime.strftime(open_time, "%d.%m.%Y г. %X") + "\n\n")
  smena_text.append("1. Добавить товар в корзину\n")
  smena_text.append("2. Показать корзину\n")
  smena_text.append("3. Очистить корзину\n")
  smena_text.append("4. Закрыть смену")
  print(Panel(smena_text, title="Касса вер. 0.1", style="grey66 on black"))
  smena_choice = Prompt.ask("Выберите действие")
  if smena_choice == "1":
    add_product()
  if smena_choice == "2":
    show_cart()
  if smena_choice == "3":
    clear_cart()
  if smena_choice == "4":
    smena_close()
  else:
    main_function()


#-----------------------------------------------------------------


def main_function():
  clear()
  main_text = Text()
  main_text.append("Добро пожаловать!\n\n")
  main_text.append("1. Открыть смену\n")
  main_text.append("2. Выйти из программы")
  print(Panel(main_text, title="Касса вер. 0.1", style="grey66 on black"))
  main_choice = Prompt.ask("Выберите действие")
  if main_choice == "2":
    exit()
  else:
    smena_open()


#-----------------------------------------------------------------

main_function()
