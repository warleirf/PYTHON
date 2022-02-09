from imap_tools import MailBox, AND 

usuario = "warlei.info@gmail.com"
senha = "Wrf@201201036917"

meu_email = MailBox("imap.gmail.com").login(usuario, senha)

# pegar email que foram enviadors por um remetente especifíco.

lista_email = meu_email.fetch(AND(subject="OLX"))
print(len(list(lista_email)))