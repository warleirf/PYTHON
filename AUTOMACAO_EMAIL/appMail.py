from imp_tools import MailBox, AND

usuario = "warlei.info@gmail.com"
senha = "Wrf@201201036917"

meu_email = MailBox("imap.gmail.com").login(usuario, senha)

#pegar email que foi enviado por um remetente especifico

lista_email = meu_email.