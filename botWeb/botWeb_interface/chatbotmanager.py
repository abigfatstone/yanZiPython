from django.conf import settings
from django.apps import AppConfig
import logging
import sys
import os

chatbotPath = "/".join(settings.BASE_DIR.split('/')[:-1])
sys.path.append(chatbotPath)
print('====================')
print(chatbotPath)
from firstScript import Chatbot

logger = logging.getLogger(__name__)


class ChatbotManager(AppConfig):
    name = 'botWeb_interface'
    verbose_name = 'Chatbot Interface'

    bot = None

    def ready(self):
        if (os.environ.get(
                'RUN_MAIN') == 'true' and  # HACK: Avoid the autoreloader executing the startup code twice (could also use: python manage.py runserver --noreload) (see http://stackoverflow.com/questions/28489863/why-is-run-called-twice-in-the-django-dev-server)
                not any(x in sys.argv for x in
                        ['makemigrations', 'migrate'])):  # HACK: Avoid initialisation while migrate
            ChatbotManager.initBot()

    @staticmethod
    def initBot():
        if not ChatbotManager.bot:
            logger.info('Initializing bot...')
            ChatbotManager.bot = Chatbot()
        else:
            logger.info('Bot already initialized.')

    @staticmethod
    def callBot(user_input):
        if ChatbotManager.bot:
            return ChatbotManager.bot.daemonPredict(user_input)
        else:
            logger.error('Error: Bot not initialized!')


if __name__ == '__main__':
    c = ChatbotManager()
    aa = c.callBot({'message':'hello','session_id':'yangzi'})

