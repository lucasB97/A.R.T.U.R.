from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot(
    'A.R.T.U.R.',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Me desculpe, mas eu não entendi. Ainda estou aprendendo :(',
            'maximum_similarity_threshold': 0.90
        }
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training with Personal Ques & Ans
training_data = open('training/ques_ans.txt').read().splitlines()


trainer = ListTrainer(chatbot)
trainer.train(training_data)

# Training with Portugues Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    "chatterbot.corpus.portuguese",
    "chatterbot.corpus.portuguese.greetings",
    "chatterbot.corpus.portuguese.conversations",
    "chatterbot.corpus.portuguese.linguistic_knowledge"
)
