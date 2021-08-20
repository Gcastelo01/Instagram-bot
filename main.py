import src.botImplement as bot


link = str(input('Cole o link da postagem aqui: '))
username = str(input("Digite seu  e-mail do instagram: "))
password = str(input('Digite sua senha: '))
caminho = str(input('Cole o caminho para o arquivo .txt com os termos a serem comentados: '))

commentBot = bot.InstaBot(username, password, link, caminho)
commentBot.comment()
