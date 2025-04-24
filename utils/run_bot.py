import os, json, random
from utils.instagram_following_bot import InstagramFollowerBot
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("INSTAGRAM_USERNAME")
USER_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")


def run_bot():
    retry = 3
    with open("data/accounts.json", "r") as file:
        accounts = json.load(file)
    account_choice = str(random.randint(1, 10))
    account_url = accounts[account_choice]["url"]
    account_name = accounts[account_choice]["handle"]
    while retry != 0:
        bot = InstagramFollowerBot(username=USERNAME, password=USER_PASSWORD)
        bot.navigate_to_account(account_url=account_url, account_name=account_name)
        try:
            bot.navigate_to_account(account_url=account_url, account_name=account_name)
            bot.follow_accounts()
        except Exception as e:
            bot.send_email(account_name, e)
            retry -= 1
        else:
            bot.send_email(account_name)
            break

