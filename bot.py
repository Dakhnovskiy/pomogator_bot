import bot.bot_helpers as bot_helpers


if __name__ == '__main__':
    updater = bot_helpers.get_configured_updater()
    bot_helpers.start_bot(updater)
