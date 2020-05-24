import logging
from django.conf import settings
from django.apps import AppConfig
import sys
import os
import base64

from .formatHtml import format_html,format_file,save_file

# load first script
chatbotPath = "/".join(settings.BASE_DIR.split('/')[:-1])
sys.path.append(chatbotPath)
from firstScript import Chatbot

logger = logging.getLogger(__name__)


class ChatbotManager(AppConfig):
    name = 'chatBot'
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
        answer = {}
        if ChatbotManager.bot:
            print(user_input)
            client_type = user_input['client_type']
            if user_input['question_type'] == 'text':
                question = {'message': user_input['message'],
                            'callback_key': user_input['callback_key'],
                            'session_id':  user_input['session_id']}            
                answer = ChatbotManager.bot.daemonPredict(question)

                if answer['message'].split(':')[0] == '文件地址':
                    file_path = answer['message'].split(':')[1]
                    ai_message,ai_message_type = format_file(file_path,client_type)
                    answer['message'] = ai_message
                    answer['answer_type'] = ai_message_type  
                else:  
                    answer['answer_type'] = 'text'   
                    answer['message'] = format_html(answer['message'] ,client_type)

            elif user_input['question_type'] == 'image':
                save_file(user_input['message'])
                answer['answer_type'] = 'text'
                answer['message'] = 'image save in resource file.'

            answer['client_type'] = user_input['client_type'] 
        else:
            error_message = 'Error: Bot not initialized!'
            logger.error(error_message)
            answer['message'] = error_message
        return answer


if __name__ == '__main__':
    c = ChatbotManager()
    aa = c.callBot({'message': 'hello', 'session_id': 'yangzi'})
