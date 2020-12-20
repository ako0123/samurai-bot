import telebot # pyTelegramBotAPI 
from telebot import types
token = '1289131326:AAGXIawwewqt70_8M535p22mjnQXQE03mYc'# bot father token telegram
bot = telebot.TeleBot(token) #creat a bot 
markup = types.InlineKeyboardMarkup(row_width=2) # inline клавиратура МЕНЮ
food1 = types.InlineKeyboardButton("Филадельфия", callback_data='food1') # кнопки 
food2 = types.InlineKeyboardButton("Цезарь ролл", callback_data='food2') # кнопки 
food3 = types.InlineKeyboardButton("Суши унаги", callback_data='food3') # кнопки 
food4 = types.InlineKeyboardButton("Футомаки ясай", callback_data='food4')
food5 = types.InlineKeyboardButton("Сет Куранты", callback_data='food5')
food6 = types.InlineKeyboardButton("Сет Сета-Клаус", callback_data='food6')
food7 = types.InlineKeyboardButton("Сет Алматы - любовь моя", callback_data='food7')
food8 = types.InlineKeyboardButton("Сет Горячая штучка", callback_data='food8')
markup.add(food1, food2, food3, food4, food5, food6, food7, food8)
@bot.message_handler(commands=['myorder'])  # работает если вызвали команду myorder
def order(message):
    bot.send_message(message.chat.id, text='Рахмет за ваш заказ, отправьте пожалуйста ваш адрес и мы отправим к вам курьера')# отправка сообщение
@bot.message_handler(commands=['start'])# работает если вызвали команду start'
def mes(message):
    bot.send_message(message.chat.id, text="Добро пожаловать в наш суши бар<b> Суши Мастер </b>.Меня зовут,{0.first_name}. Я ваш виртуальный менеджер.\nПосле того как ознакомтесь с меню, нажмите на сделать заказ, чтобы узнать ваш заказ вызовите команду /myorder ".format(bot.get_me()), parse_mode='html')
    bot.send_message(message.chat.id,text='<b> Меню </b>', parse_mode='html', reply_markup=markup) # вызов клавиратуры Меню
markup1=types.InlineKeyboardMarkup(row_width=2)
but1=types.InlineKeyboardButton('Сделать заказ', callback_data='add1')
but2 = types.InlineKeyboardButton('Меню', callback_data='add2')
markup1.add(but1,but2)
@bot.callback_query_handler(func=lambda call: True)# работают если нажали на какую-то кнопку 
def data (call):
    if call.message:
        if call.data == 'food1':# если нажали на кнопку в меню Филадельфия
            bot.send_message(call.message.chat.id, text='Филадельфия \n 1399 тг')# отправка инфо про суши как сообщение 
            food1=open('food1.jpg', 'rb')# открываем картинку 
            bot.send_photo(call.message.chat.id,food1)
            bot.send_message(call.message.chat.id, text='Лосось, сыр сливочный, огурец, нори, рис.', reply_markup=markup1)# отправляем картинку
        elif call.data == 'food2':
            bot.send_message(call.message.chat.id, text='Цезарь ролл \n 999 тг')
            food2 = open('foo.jpg', 'rb')
            bot.send_photo(call.message.chat.id, food2)
            bot.send_message(call.message.chat.id, text='(запеч) Курица терияки, сыр сливочный, помидор, салат айсберг, замес монако, нори, рис.',
                             reply_markup=markup1)
        elif call.data == 'food4':
            bot.send_message(call.message.chat.id, text='Футомаки ясай \n 869 тг')
            food4 = open('foo4.jpg', 'rb')
            bot.send_photo(call.message.chat.id, food4)
            bot.send_message(call.message.chat.id,text='Прмидор, салат айсберг, огурец, перец болгарский,авокадо, нори, рис.',
                             reply_markup=markup1)
        elif call.data == 'food3':
            bot.send_message(call.message.chat.id, text='Суши унаги \n 399 тг')
            food3 = open('food3.jpg', 'rb')
            bot.send_photo(call.message.chat.id, food3)
            bot.send_message(call.message.chat.id,text='Угорь, рис, нори.',
                             reply_markup=markup1)
        elif call.data == 'food5':
            bot.send_message(call.message.chat.id, text='Сет Куранты \n 5299 тг')
            food5 = open('food5.jpg', 'rb')
            bot.send_photo(call.message.chat.id, food5)
            bot.send_message(call.message.chat.id,text='Филадельфия 8шт, Калифорния каппа маки 8шт, Футомаки чикен 8шт, Сяке хот в кунжуте(запеч) 8шт, Калифорния(темпура) 8шт',
                             reply_markup=markup1)
        elif call.data == 'food6':
            bot.send_message(call.message.chat.id, text='Сет Сета-Клаус \n 6699 тг')
            food6 = open('food6.jpg', 'rb')
            bot.send_photo(call.message.chat.id, food6)
            bot.send_message(call.message.chat.id,text='Филадельфия 8шт, Калифорния в кунжуте эби хот 8 шт, Чикен спайси(запеч) 8шт, Аррива(темпура) 8шт, Калифорния каппа маки с икрой 8шт, Чеддер 8шт, Лава с крабом 8шт.',
                             reply_markup=markup1)
        elif call.data == 'food7':
            bot.send_message(call.message.chat.id, text='Сет Алматы - любовь моя \n 4890тг')
            food7 = open('food7.jpg', 'rb')
            bot.send_photo(call.message.chat.id, food7)
            bot.send_message(call.message.chat.id,text='Нежный с курицей (запеч) 8шт, Цезарь ролл (запеч) 8шт, Лава с лососем 8шт, Калифорния каппа маки с икрой 8шт, Аррива (темпура) 8 шт, Филадельфия 8шт, Каппа маки 8шт, Филадельфия (темпура) 8шт.',
                             reply_markup=markup1)
        elif call.data == 'food8':
            bot.send_message(call.message.chat.id, text='Сет Горячая штучка \n 4999 тг')
            food8 = open('food8.jpg', 'rb')
            bot.send_photo(call.message.chat.id, food8)
            bot.send_message(call.message.chat.id,text='Сет Горячая штучка',
                             reply_markup=markup1)
        elif call.data == 'add2':
            bot.send_message(call.message.chat.id, text='<b> Меню </b>', parse_mode='html', reply_markup=markup)# если нажали на кнопку меню в Inline
        elif call.data == 'add1': 
            mark=types.ReplyKeyboardMarkup(resize_keyboard=True)# если нажали сделать заказ, создается клавиратура 
            food1 = types.KeyboardButton("Филадельфия")# кнопки который при нажатии отправляет текст кнопки
            food2 = types.KeyboardButton("Цезарь ролл")
            food3 = types.KeyboardButton("Суши унаги")
            food4 = types.KeyboardButton("Футомаки ясай")
            food5 = types.KeyboardButton("Сет Куранты")
            food6 = types.KeyboardButton("Сет Сета-Клаус")
            food7 = types.KeyboardButton("Сет Алматы - любовь моя")
            food8 = types.KeyboardButton("Сет Горячая штучка")
            final=types.KeyboardButton("все")
            mark.add(food1, food2, food3, food4, food5, food6, food7, food8,final)

            bot.send_message(call.message.chat.id, text='Нажмите на то что хотите заказть, когда закончите с выбором нажмите на кнопку все', parse_mode='html', reply_markup=mark)
from collections import defaultdict
order = defaultdict(lambda: {}) # создается словарь

def update_order(user_id, key, value):      # добавляется заказы от людей
   order[user_id][key] = value          #{'ako':{'sushi':'234', 'cola':'150'}, 'kazybek':{'set':'1200'}}

def get_order(user_id):
    return order[user_id]    # закзаз юзера order['ako'] return {'sushi':234, 'cola':150}

def get_bill(user_id):      
    price=order[user_id].values()# внутри price сохраняем из юзера все значении  это у нас  234 и 150. Потому что у нас вложенный словарь   {'ako':{'sushi':'234', 'cola':'150'},
    sum=0 
    for i in price:
        sum=int(i)+sum
    return sum # возвращает сумму заказа 


@bot.message_handler(content_types=['location'])#если отправляет локацию выполняется
def loc(message):
    bot.send_message(message.chat.id,text='Спасибо, ожидайте ваш заказ')
    bot.send_message(message.chat.id, text='Курьер: Аслан, 877745464')
@bot.message_handler(content_types=['text'])
def message(message):
    if message.text=="Филадельфия":#если написали "Филадельфия"
        update_order(message.chat.id, "Филадельфия",'1399') #вызывается функция update_order и добавляет в словарь 
    elif message.text=="Цезарь ролл":
        update_order(message.chat.id,"Цезарь ролл",'999')
    elif message.text=="Футомаки ясай":
        update_order(message.chat.id,"Футомаки ясай",'869')
    elif message.text=="Суши унаги":
        update_order(message.chat.id,"Суши унаги",'399')
    elif message.text=="Сет Куранты":
        update_order(message.chat.id, "Сет Куранты",'5299')
    elif message.text=="Сет Сета-Клаус":
        update_order(message.chat.id,"Сет Сета-Клаус",'6699')
    elif message.text=="Сет Алматы - любовь моя":
        update_order(message.chat.id, "Сет Алматы - любовь моя",'4890')
    elif message.text=="Сет Горячая штучка":
        update_order(message.chat.id,"Сет Горячая штучка",'4990')
    elif message.text=="все":
        bot.send_message(message.chat.id,text='Ваш заказ{}, ваш счет {}'.format(get_order(message.chat.id),get_bill(message.chat.id))) #если нажали все отправляет чек 


bot.polling()
