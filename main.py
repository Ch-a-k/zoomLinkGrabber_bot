import os
from zoom_links_resend_bot import ZoomLinksTelegramBot


if __name__ == '__main__':
    TOKEN = '2004159121:AAGsV2jqucjxjVxL_5ToT_DJAiJmiKwr2GY'
    REDIRECT_TO_CHAT_ID = "@zoomgrabber_group"
    INTERVAL = float("1")

    tg_bot = ZoomLinksTelegramBot(
        token=TOKEN,
        redirect_to_chat_id=REDIRECT_TO_CHAT_ID,
    )
    tg_bot.run(interval=INTERVAL)
