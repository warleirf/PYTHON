from cmath import log
from datetime import date
import email
from fileinput import filename
import imaplib
from re import search

#Conectar ao servidor de email gmail com IMAP
objCon = imaplib.IMAP4_SSL("imap.gmail.com")

#Informações de login e senha para acessar a conta gmail.
login = "warlei.info@gmail.com"
senha = "Wrf@789100"

objCon.login(login, senha)

#loopar a caixa de entrada
objCon.list()
objCon.select(mailbox='inbox', readonly=True)
respostas,idDosEmails = objCon.search(None,'ALL')

#lopando cada ID de email na caixa de email
for num in idDosEmails[0].split():
    #decodificando o email e jogando em uma variavel as partes do email
    resultado,dados = objCon.fetch(num,'RFC822')
    texto_do_email = dados[0][1]
    texto_do_email = texto_do_email.decode('latin-1')
    texto_do_email = email.message_from_string(texto_do_email)

#lopando as partes do email
for part in texto_do_email.walk():
    #condição: se tiver anexo pegar o nome do anexo
    if part.get_content_maintype() == 'multipart':
        continue
    if part.get('Content-Disposition') is None:
        continue
    #pegar o nome do arquivo em anexo
    filename = part.get_filename()
    #Criamos um arquivo com o mesmo nome na pasta local
    arquivo = open(filename,'wb')
    #escrevemos o binario do anexo no arquivo
    arquivo.write(part.get_payload(decode=True))
    arquivo.close()