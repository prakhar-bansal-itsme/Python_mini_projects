# To make this work we need to install a python library "instabot".

from instabot import Bot

bot = Bot()
bot.login(username = "eg.prakharbansalabc@gmail.com", password = "pass of username")
bot.upload_photo("Image link on device", caption="whatever caption you want to give")
bot.follow("the userid of the person you want to follow")
bot.unfollow("userId of the person you want to unfollow")
bot.send_message("whatever message you want to send", ["jisko message karna h, multiple names bho de sakte h"])

#THere are many diff features aswell so we can surf as much as we want