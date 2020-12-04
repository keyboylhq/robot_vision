from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("myBot")
chatbot.set_trainer(ChatterBotCorpusTrainer)

# 使用英文语料库训练它
chatbot.train("chatterbot.corpus.english")

# 开始对话
chatbot.get_response("Hello, how are you today?")