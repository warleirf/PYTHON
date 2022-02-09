import imaplib
import email
import os
import base64   

#login e senha para conectar na conta de email
objCon = imaplib.IMAP4_SSL("imap.gmail.com")
login = "warlei.info@gmail.com"
senha = "Wrf@201201036917"

objCon.login(login,senha)

#loopar a caixa de entrada
(objCon.select(mailbox='inbox', readonly=True))
resposta,idDosEmails = objCon.search(None,'All')

for num in idDosEmails[0].split():
    resultado,dados = objCon.fetch(num,('RFC822'))
    texto_do_email = dados[0][1]
    texto_do_email = texto_do_email.decode('utf-8')
    texto_do_email = email.message_from_string(texto_do_email)
    print(texto_do_email)