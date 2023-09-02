import json

from telegram import Update
from telegram.ext import CallbackContext

from bot.inline_keyboards import products_keyboard
from bot.keyboards import main_markup, categories_markup
from bot.make_image import get_gr_photo
from redis_connection import redis_connection as redconn
from bot.api import bot_login


def start(update: Update, context: CallbackContext):
    # user_json = redconn.get(f'{update.message.from_user.id}')
    # if user_json:
    #     user_data = json.loads(user_json)
    #     if user_data:
    #         token = user_data.get('token', None)
    #         if token:
    #             context.bot.send_message(
    #                 chat_id=update.effective_chat.id,
    #                 text="Salom, bot ishga tushdi!",
    #                 reply_markup=main_markup
    #             )
    redconn.delete(f'{update.message.from_user.id}')
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Salom, bot ishga tushdi!\nOnline do'konimizning imkoniyatlaridan to'liq foydalana olishingiz uchun tizimga kirishingiz zarur,\ntelefon raqam:",
    )


def text_message(update: Update, context: CallbackContext):
    message = update.message.text
    print('user id:', update.message.from_user.id)
    try:
        user_json = redconn.get(f'{update.message.from_user.id}')
        print('user_json:',user_json)
        if user_json:
            user_data = json.loads(user_json)
            token = user_data.get('token', None)
            phone_number = user_data.get('phone_number', None)
            if token:
                if message == 'Kategoriyalar':
                    context.bot.send_message(
                        chat_id=update.effective_chat.id,
                        text=f"Kategoriyalar",
                        reply_markup=categories_markup
                    )
                elif message == 'Ortga':
                    context.bot.send_message(
                        chat_id=update.effective_chat.id,
                        text=f"Bosh sahifa..",
                        reply_markup=main_markup
                    )
                elif message == '🛒Savatcha':
                    context.bot.send_message(
                        chat_id=update.effective_chat.id,
                        text=f"Bosh sahifa..",
                        # reply_markup=main_markup
                    )

                else:
                    pkeyboard, keys = products_keyboard(message, page=1)
                    context.bot.send_photo(
                        chat_id=update.effective_chat.id,
                        photo=open(get_gr_photo(keys), 'rb'),
                        caption="Raqami bo'yicha tanlang:",
                        reply_markup=pkeyboard
                    )

            elif phone_number:
                status_code,response_data = bot_login(
                    phone_number=phone_number,
                    password=message
                )
                if status_code == 200:
                    redconn.mset({f'{update.message.from_user.id}': json.dumps({
                        'phone_number': message,
                        'token': response_data['token']
                    })})
                    context.bot.send_message(
                                    chat_id=update.effective_chat.id,
                                    text="Tizimga kirdingiz!",
                                    reply_markup=main_markup
                                )
                else:
                    context.bot.send_message(
                        chat_id=update.effective_chat.id,
                        text=f"password:",
                    )
            else:
                redconn.mset({f'{update.message.from_user.id}': {
                    'phone_number': message
                }})
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=f"Online do'konimizning imkoniyatlaridan to'liq foydalana olishingiz uchun tizimga kirishingiz zarur,\ntelefon raqam:",
                    # reply_markup=categories_markup
                )
        else:
            redconn.mset({
                f'{update.message.from_user.id}': json.dumps({
                    'phone_number': message
                })
            })
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"password:",
                # reply_markup=categories_markup
            )
    except Exception as error:
        print('error:', error)

def photo_message(update: Update, context: CallbackContext):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('1.jpg', 'rb'))
