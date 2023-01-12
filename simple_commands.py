#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from telegram import ParseMode, Update
from telegram.ext import CommandHandler, CallbackContext

from user_setting import UserSetting
from utils import send_async
from shared_vars import dispatcher
from internationalization import _, user_locale

@user_locale
def help_handler(update: Update, context: CallbackContext):
    """Handler for the /help command"""
    help_text = _("[Halo](https://graph.org/file/5f411c75dc9672ac6515b.jpg)\n\n"
  "⚠️ Ikuti langkah ini:\n\n"
      "1. Tambahkan bot ini ke grup\n"
      "2. Di grup, memulai permainan baru dengan /new atau bergabung sudah"
      " menjalankan permainan dengan /join\n"
      "3. Setelah setidaknya dua pemain bergabung, mulailah permainan dengan"
      " /start\n"
      "4. Jenis <code>@unobot</code> ke dalam kotak obrolan Anda dan tekan "
      "<b>space</b>, or click the <code>via @unobot</code> text "
      "next to messages. You will see your cards (some greyed out), "
      "any extra options like drawing, and a <b>?</b> to see the "
      "current game state. The <b>greyed out cards</b> are those you "
      "<b>can not play</b> at the moment. Tap an option to execute "
      "the selected action.\n"
      "Players can join the game at any time. To leave a game, "
      "gunakan /leave. Jika seorang pemain membutuhkan waktu lebih dari 90 detik untuk bermain, "
      "kamu bisa memakai /skip untuk melewati pemain itu. gunakan /notify_me to "
      "menerima pesan pribadi saat permainan baru dimulai.\n\n"
      "<b>Language</b> dan pengaturan lainnya: /settings\n"
      "Perintah lainnya (hanya untuk pembuat game):\n"
      "/close - Tutup lobi\n"
      "/open - Buka lobi\n"
      "/kill - Hentikan permainan\n"
      "/kick - Pilih pemain untuk ditendang "
      "dengan membalas kepesan pengguna\n"
      "/enable_translations - Terjemahkan teks yang relevan ke semua "
      "bahasa yang digunakan dalam permainan\n"
      "/disable_translations - Use English for those texts\n\n"
      "<b>Experimental:</b> Play in multiple groups at the same time. "
      "Press the <code>Current game: ...</code> button and select the "
      "group you want to play a card in.\n"
      "• Jika ingin melihat Daftar Bot lainnya Klik :\n"
      "<a href=\"https://t.me/tirexgugel\">"
      "Klik Disini</a>, Join Group :\n"
      "• Group :\n"
      "<a href=\"https://telegram.me/rexaprivateroom\">Klik Disini</a>"
      "👑 Owner :\n"
      "<a href=\"https://telegram.me/JustRex\">Rexa</a>"
      "enjoy the game 😊.")

    send_async(context.bot, update.message.chat_id, text=help_text,
               parse_mode=ParseMode.HTML, disable_web_page_preview=True)

@user_locale
def modes(update: Update, context: CallbackContext):
    """Handler for the /help command"""
    modes_explanation = _("This UNO bot has four game modes: Classic, Sanic, Wild and Text.\n\n"
      " 🎻 The Classic mode uses the conventional UNO deck and there is no auto skip.\n"
      " 🚀 The Sanic mode uses the conventional UNO deck and the bot automatically skips a player if he/she takes too long to play its turn\n"
      " 🐉 The Wild mode uses a deck with more special cards, less number variety and no auto skip.\n"
      " ✍️ The Text mode uses the conventional UNO deck but instead of stickers it uses the text.\n\n"
      "To change the game mode, the GAME CREATOR has to type the bot nickname and a space, "
      "just like when playing a card, and all gamemode options should appear.")
    send_async(context.bot, update.message.chat_id, text=modes_explanation,
               parse_mode=ParseMode.HTML, disable_web_page_preview=True)

@user_locale
def source(update: Update, context: CallbackContext):
    """Handler for the /help command"""
    source_text = _("Bot ini adalah Perangkat Lunak Bebas dan dilisensikan di bawah AGPL. "
      "Kode tersedia di sini: \n"
      "https://github.com/jh0ker/mau_mau_bot")
    attributions = _("Attributions:\n"
      'Draw icon by '
      '<a href="http://www.faithtoken.com/">Faithtoken</a>\n'
      'Pass icon by '
      '<a href="http://delapouite.com/">Delapouite</a>\n'
      "Originals available on http://game-icons.net\n"
      "Icons edited by ɳick")

    send_async(context.bot, update.message.chat_id, text=source_text + '\n' +
                                                 attributions,
               parse_mode=ParseMode.HTML, disable_web_page_preview=True)


@user_locale
def news(update: Update, context: CallbackContext):
    """Handler for the /news command"""
    send_async(context.bot, update.message.chat_id,
               text=_("All news here: https://telegram.me/unobotupdates"),
               disable_web_page_preview=True)


@user_locale
def stats(update: Update, context: CallbackContext):
    user = update.message.from_user
    us = UserSetting.get(id=user.id)
    if not us or not us.stats:
        send_async(context.bot, update.message.chat_id,
                   text=_("You did not enable statistics. Use /settings in "
                          "a private chat with the bot to enable them."))
    else:
        stats_text = list()

        n = us.games_played
        stats_text.append(
            _("{number} game played",
              "{number} games played",
              n).format(number=n)
        )

        n = us.first_places
        m = round((us.first_places / us.games_played) * 100) if us.games_played else 0
        stats_text.append(
            _("{number} first place ({percent}%)",
              "{number} first places ({percent}%)",
              n).format(number=n, percent=m)
        )

        n = us.cards_played
        stats_text.append(
            _("{number} card played",
              "{number} cards played",
              n).format(number=n)
        )

        send_async(context.bot, update.message.chat_id,
                   text='\n'.join(stats_text))


def register():
    dispatcher.add_handler(CommandHandler('help', help_handler))
    dispatcher.add_handler(CommandHandler('source', source))
    dispatcher.add_handler(CommandHandler('news', news))
    dispatcher.add_handler(CommandHandler('stats', stats))
    dispatcher.add_handler(CommandHandler('modes', modes))
