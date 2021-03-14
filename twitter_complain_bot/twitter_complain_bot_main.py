from twitter_complain_bot import InternetSpeedTwitterBot

isp_speed_twitter_bot = InternetSpeedTwitterBot()

# get the internet speed and tweet the provider if the speed is less than what was promised
# by the internet provider
isp_speed_twitter_bot.get_internet_speed()


# FUTURE FUNCTIONALITY:
# - ADD A FUNCTIONALITY WHERE A USER CAN TYPE IN THEIR ISP LIKE SPECTRUM OR AT&T
# AND THEN THEY CAN GET INFO ON THE PROMISED DOWNLOAD AND UPLOAD SPEED AND THEN WE
# CAN USE THOSE VALUES REAL TIME TO SEE IF WE HAVE THE PROMISED SPEEDS AVAILABLE