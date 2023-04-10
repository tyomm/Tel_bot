from distutils import command
import telebot
from constants import API_KEY
# from sqlite import *
import sqlite3

bot = telebot.TeleBot(API_KEY, parse_mode = None)


#===================1 /start COMMAND 1====================
start1 = "Ողջույն սիրելի "
start2 = " ջան😊 "
start3 = "ես ստեղծվել եմ Արտյոմի կողմից և պատրաստ եմ Ձեզ օգնել սովորել գերմաներեն: Եթե ուզում եք իմանալ ավելին, ապա մուտքագրեք՝ /help\n"
start4 = "Ինչպե՞ս է Ձեր անունը:😊"

@bot.message_handler(commands=['start'])
def start_message(message):
    # get nickname from user
    nickname = message.from_user.username or (message.from_user.first_name + " " + message.from_user.last_name if message.from_user.first_name and message.from_user.last_name else None)
    bot.forward_message(1159606389, message.chat.id, message.message_id) # Forward message to me ('/start' command)

    if (nickname):
        bot.send_message(message.chat.id, start1 + nickname + start2 + start3)
    else:
        ask_user(message)
#====================0 /start COMMAND 0=========================

#================1 Get user's Name 1============
def ask_user(message):
    bot.send_message(message.chat.id, start4)
    bot.register_next_step_handler(message, process_name_step)

def process_name_step(message):
    name = message.text
    bot.send_message(message.chat.id, start1 + name + start2 + start3)
#================0 Get user's Name 0============

#===================1 /help command 1====================
help = "Բայերը գերմաներենում` /verbs\n"
@bot.message_handler(commands=['help'])
def help_center(message):
    bot.send_message(message.chat.id, help)
#====================0 /help command 0====================


#====================1 /verbs command 1====================
verbs = "1) Ո՞րն է բայի հոլովը գերմաներենում` /q1\n2) Որո՞նք են փոփոխվող(stem-changing) բայերը գերմաներենում` /q2"
@bot.message_handler(commands=['verbs'])
def Verbs(message):
    bot.send_message(message.chat.id, verbs)

q1 = """Բայի հոլովը բայի հիմնական ձևն է, որը սովորաբար մնում է անփոփոխ, երբ դուք խոնարհում եք բայը: Գերմաներենում բայերի 
        մեծ մասն ունի -en/n վերջավորությունը՝ spielen, sagen, wandern, liefern: Երբ հեռացնեք -en/n վերջավորությունը, 
        դուք կստանաք բայի հոլովը՝ բայի հիմնական մասը՝ spielen, sagen, wandern, liefern: Երբ դուք խոնարհում եք այս բայերը, 
        պարզապես անհրաժեշտ է ավելացնել ճիշտ բայական վերջավորությունը՝ կախված անձից. Ich spiele, du spielst, er/sie/es spielt; wir liefern, ihr liefert, sie/Sie liefern."""
@bot.message_handler(commands=['q1'])
def Q1(message):
    bot.send_message(message.chat.id, q1)

q2 = """Փոփոխվող բայերը անկանոն բայեր են, որոնք փոփոխության են ենթարկվում ներկա ժամանակով (Präsens) բայերի ձայնավորի մեջ։ 
        Ձայնավորների այս փոփոխությունը տեղի է ունենում միայն երկրորդ դեմքի եզակի (du) և երրորդ դեմքի եզակի (er/sie/es) ձևերում:"""
@bot.message_handler(commands=['q2'])
def Q2(message):
    bot.send_message(message.chat.id, q2)
#====================0 /verbs command 0====================



#==============1 Save Telegram DataBase 1================
closed = False
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    global closed
    if message.text.lower() == '/':  # '/finish' 
        print(message.text)
        closed = True
        bot.send_message(1159606389, "Closed the DataBase   /")
        with open("File_DataBase.txt", "rb") as file1:
            bot.send_document(1159606389, file1)
        with open("File_DataBase.txt", "w") as file: # for delete file content
            file.truncate() # for delete file content

    elif message.text.lower() == '//':  # '/continue'
        bot.send_message(1159606389, "Opend the DataBase  //")
        closed = False

    elif message.text.lower() != '' and not closed:
        print(message.text)
        with open("File_DataBase.txt", "a", encoding="utf-8") as file:
            file.write(message.text)
            file.write("\n\n")
#===============0 Save Telegram DataBase 0================




bot.polling(none_stop = True)

