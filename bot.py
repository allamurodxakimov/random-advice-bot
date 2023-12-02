from settings import url
import requests
from time import sleep
from bored.main import Bored

welcome_msg = '''
    <b>Hello there!</b>

🌟 Welcome to the Random Advice Bot! 🌟

Get ready to receive a dose of wisdom and guidance tailored just for you. Here's a quick guide on how to make the most out of this bot:

1. /start: Use this command to receive a warm welcome message and get instructions on how to interact with the bot.

2. /random: Feeling spontaneous? Use this command for a random piece of advice that might just be what you need at the moment.

3. /sport: Need advice related to sports? Type this command, and let the bot serve you some sports-related wisdom.

4. /education: If you're seeking guidance on matters of education, use this command to receive valuable advice.

5. /recreational: For advice on leisure and recreational activities, simply type this command and enjoy some thoughtful suggestions.

6. /social: Looking for tips on social interactions? Use this command to receive advice that could enhance your social experiences.

7. /diy: Planning a DIY project? Type this command to get some helpful advice for your do-it-yourself endeavors.

8. /cooking: Ready to whip up a delicious meal? Use this command for cooking advice that might just make your culinary experience even better.

9. /relaxation: Feeling stressed? Type this command for advice on relaxation techniques that could help you unwind.

10. /music: Choose the music you want from the activity.

11. /busywork: Need something to keep yourself occupied? Use this command for advice on productive and engaging tasks.
Remember, if you enter any other text, the bot will provide an error message to guide you back to the available commands.
'''

def echobot_update(url:str):
    endpoint = "/getUpdates"
    url+=endpoint
    respons = requests.get(url)
    if respons.status_code==200:
        result = respons.json()['result']
        if len(result)!=0:
            return result[-1]
        else :
            return 404
    else:
        return respons.status_code

def send_massage(url:str,chat_id:int,text:str):
        endpoint = '/sendMessage'
        url+=endpoint
        payload = {
            'chat_id': chat_id,
            'text': text,
            "parse_mode":"HTML"
        }
        requests.get(url, params=payload)
def main(url:str):
    last_update_id = -1
    bored = Bored()
    while True:
        crr_update = echobot_update(url)
        if crr_update['update_id']!=last_update_id:
            user = crr_update['message']['from']
            text = crr_update['message'].get("text")

            if text is None:
                send_massage(url,user['id'],"Menga text yuboring iltimos!")
            elif text=="/start":
                send_massage(url,user['id'],welcome_msg) 
            elif text=="/random":
                advice = bored.get_activity()['activity']
                send_massage(url,user['id'],advice)
            elif text=='/education':
                act_type = bored.get_activity_by_type('education')['activity']
                send_massage(url,user['id'],act_type)
            elif text == "/recreational":
                advic_rec = bored.get_activity_by_type("recreational")['activity']
                send_massage(url,user['id'],advic_rec)
            elif text== "/social":
                advic_soc = bored.get_activity_by_type("social")['activity']
                send_massage(url,user['id'],advic_soc)
            elif text == "/diy":
                advic_diy = bored.get_activity_by_type("diy")['activity']
                send_massage(url,user['id'],advic_diy)
            elif text == "/cooking":
                advic_cook = bored.get_activity_by_type("cooking")['activity']
                send_massage(url,user['id'],advic_cook)
            elif text == "/relaxation":
                advic_rel = bored.get_activity_by_type("relaxation")['activity']
                send_massage(url,user['id'],advic_rel)
            elif text == "/music":
                advic_music = bored.get_activity_by_type("music")['activity']
                send_massage(url,user['id'],advic_music)
            elif text == "/busywork":
                advic_bus = bored.get_activity_by_type("busywork")['activity']
                send_massage(url,user['id'],advic_bus)
            else:
                advic = "To'g'ri ma'lumot kelmadi :("
                send_massage(url,user['id'],advic)
            last_update_id=crr_update['update_id']
        sleep(0.4)

main(url)
                
