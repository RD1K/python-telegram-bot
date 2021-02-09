'''
This program is used to get user input from the Telegram messaging platform,
in the form of different commands which have different functions. In some
cases, the user has to input arguments after the command, and this input is processed
and used to make memes based on pre-defined images and pre-defined coordinates
(which determine the placement of text). The completed meme is saved locally, and
then sent via Telegram in the same place (group chat/direct messages) where it was
requested. There are other commands that are entirely text-based, and gather input
from the user, and use this in conjunction with a randomly generated number to
"determine the chance" of an event out of 100%, or rate someone in a category out of 100%.
'''

## Enter Telegram token here
TOKEN = ""
HOME_DIRECTORY = ""

from telegram.ext import Updater, CommandHandler, Filters
import logging, pythonimaging
from random import randint
from os import system

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

class inputToMeme:
    def __init__(self,update,context,template):
        try:
            userInput = " ".join(context.args)
            userInput = userInput.split(",")
            if template == 1:
                pythonimaging.domino_template.make_meme(userInput)
            context.bot.send_photo(chat_id=update.effective_chat.id,photo=open((HOME_DIRECTORY + "/sample-out.jpg"), 'rb'), reply_to_message_id=update.message.message_id)
            print("Sent photo!")
        except:
            context.bot.send_message(chat_id = update.effective_chat.id, text = "What are you doing??", reply_to_message_id=update.message.message_id)

def start_callback(update, context):
    update.message.reply_text("Yup, I'm here!")

def help(update, context):
    helpMessage = "I create memes based on templates and text provided to me by you. These are the available templates right now:\n - Dominoes, accepts 2 arguments (/domino)\nAlso, the /rate command allows you to rate something out of 100% and accepts 2 arguments (person, topic).\nThe /chance command allows you to rate the chance of an event, with 1 argument, being the event.\nThe /say command echoes what the user says."
    context.bot.send_message(chat_id=update.effective_chat.id,text=helpMessage, reply_to_message_id=update.message.message_id)

def domino(update, context):
    domino = inputToMeme(update, context, 1)

def rate(update, context):
    try:
        userInput = " ".join(context.args)
        userInput = userInput.split(",")
        percent = randint(0,100)
        input1 = userInput[0].strip()
        input2 = userInput[1].strip()
        message = "%s is %s percent %s." % (input1,percent,input2)
        context.bot.send_message(chat_id=update.effective_chat.id,text=message, reply_to_message_id=update.message.message_id)
        print("Sent message!")
    except:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "What are you doing??", reply_to_message_id=update.message.message_id)

def chance(update, context):
    try:
        userInput = " ".join(context.args)
        userInput.strip()
        percent = randint(0,100)
        message = "There is a %s percent chance that %s." % (percent, userInput)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_to_message_id=update.message.message_id)
        print("Sent message!")
    except:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "What are you doing??", reply_to_message_id=update.message.message_id)

def say(update,context):
    try:
        userInput = " ".join(context.args)
        userInput.strip()
        message = userInput
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_to_message_id=update.message.message_id)
        print("Sent message!")
    except:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "What are you doing??", reply_to_message_id=update.message.message_id)

dispatcher.add_handler(CommandHandler('start', start_callback))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('domino', domino))
dispatcher.add_handler(CommandHandler('rate', rate))
dispatcher.add_handler(CommandHandler('chance', chance))
dispatcher.add_handler(CommandHandler('say', say))

updater.start_polling()
