import telebot
from telebot import *

api = '5358224842:AAExGY1ZLDzZa6APL1xBH1OIWjuQ66pqj0Q'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	print(message.chat.id)
	bot.reply_to(message,"Halo syng. Ada yang bisa di bantu?🥰")
	markup = types.ReplyKeyboardMarkup()
	item1 = types.KeyboardButton('/start')
	item2 = types.KeyboardButton('/info')
	item3 = types.KeyboardButton('/testimoni')
	item4 = types.KeyboardButton('/Hubungi_Mimin')
	
	#assign inline keyboard
	markup.row(item1)
	markup.row(item2)
	markup.row(item3, item4)
	bot.send_message(message.chat.id, 'Silahkan Pilih beb🥰', reply_markup=markup)

@bot.message_handler(commands=['info'])
def send_welcome(message):
	bot.reply_to(message, '''
💢Join Grup Video Porn Barat dengan💢
Grup Video Resolusi SD 360p : 150k💵
Grup Video Resolusi HD 720p : 350k💵

Video berdurasi minimal ±20 menit (dengan ukuran file yang besar, tergantung resolusi video).
					SD 360p : ±100MB
					HD 720p : ±200MB
Jadi, silahkan siapkan paket data yang besar yahh atau pakai koneksi WiFi.

💸Tersedia pembayaran VIA:💸
					📌 DANA
					📌 OVO
					📌 DLL. (note:jika tersedia)

Tentang Grup:
Setiap 1 minggu, mimin akan upload 10 video terbaru di masing - masing grup yah.
Untuk member baru, tetap bisa nonton video yang sudah mimin upload sebelumnya, jadi tidak perlu menunggu sampai minggu depan.

Q&A:
🗣:Min, mau nanya, kalau sudah pernah join terus keluar terus mau join lagi, gimana min? harus transfer lagi kah?
👱‍♀️:Enggak kok, kamu cukup kirim bukti kalau kamu sudah pernah join atau sudah pernah transfer, jadi tidak perlu khawatir.
🗣:Min, mau liat testimoni nya dong.
👱‍♀️:Untuk testi nya, bisa di liat di /testimoni yahh

Untuk lebih lanjut bisa /Hubungi_Mimin
	''')

@bot.message_handler(commands=['testimoni'])
def send_welcome(message):
	markup = types.InlineKeyboardMarkup()
	itema = types.InlineKeyboardButton('Cek Testimoni', url='https://t.me/+R9tOdMAKcAA3NzNl')

	#assign inline keyboard
	markup.row(itema)
	bot.send_message(message.chat.id, '''
Belum yakin dengan mimin?
Penipuan?
Nggak ppa kok, mimin ngerti. 
Yuk Cek Testimoninya🤗''', reply_markup=markup)

@bot.message_handler(commands=['Hubungi_Mimin'])
def send_welcome(message):
	markup = types.InlineKeyboardMarkup()
	itema = types.InlineKeyboardButton("Hubungi Mimin", url='https://t.me/Eva_Putrii')

	#assign inline keyboard
	markup.row(itema)
	bot.send_message(message.chat.id, "Kontak Mimin", reply_markup=markup)

print('Bot is Running')
while True:
    try:
        bot.polling()
    except:
        pass
