import logging


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def weather_forecast(bot, update):
    query = ' '.join(update.message.text.split(' ')[1:])

    import requests, bs4

    s = requests.get('https://sinoptik.com.ru/погода-%s' % query.lower())
    b = bs4.BeautifulSoup(s.text, "html.parser")
    p3 = b.select('.temperature .p3')
    pogoda1 = p3[0].getText()
    p4 = b.select('.temperature .p4')
    pogoda2 = p4[0].getText()
    p5 = b.select('.temperature .p5')
    pogoda3 = p5[0].getText()
    p6 = b.select('.temperature .p6')
    pogoda4 = p6[0].getText()
    p = b.select('.rSide .description')
    pogoda = p[0].getText()
    result = 'Утром :{0} {1}\nДнём :{2} {3}\n{4}'.format(pogoda1, pogoda2, pogoda3, pogoda4, pogoda)

    update.message.reply_text(result.strip())
    # bot.send_photo(chat_id=update.message.chat_id, photo=photo_url)
