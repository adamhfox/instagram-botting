from instabot import Bot
import schedule
import time


def upload_photo(username1, password1, photo, the_caption):
    bot = Bot()
    bot.login(username=username1,password=password1)
    bot.upload_photo(photo, the_caption)






schedule.every().day.at("16:17").do(upload_photo, )

while True:
    schedule.run_pending()
    time.sleep(60) 