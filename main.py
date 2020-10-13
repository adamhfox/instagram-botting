from instabot import Bot
import schedule
import time


def upload_photo(username1, password1, photo_dir, the_caption):
    bot = Bot()
    bot.login(username=username1,password=password1)
    bot.upload_photo(photo_dir, the_caption)

def convert24(str1): 
     
    
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2]
        
       
    elif str1[-2:] == "AM": 
        return str1[:-2] 
        
    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2]
        
    else: 
        return str(int(str1[:2]) + 12) + str1[2:8] 


username = ' username here '
username = ' password here '

#post 1 content
img_1 = 'image filename for post'
caption_1 = 'caption for your #POST'
time_1 = "11:35"

#post 1 content
img_2 = 'image filename for post'
caption_2 = 'caption for your #POST'
time_2 = "19:35"

''''''
schedule.every().day.at(time_1).do(upload_photo, username, password, img_1, caption_1)
schedule.every().day.at(time_2).do(upload_photo, username, password, img_2, caption_2)



while True:
    
    schedule.run_pending()
    time.sleep(45) 
    
    """
    # uncomment box and comment up functions above to get military time conversion
    print(convert24("07:56:00 PM"))
    break
    """