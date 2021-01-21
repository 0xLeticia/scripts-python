
import requests
import re
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print('Automação iniciada...')
time.sleep(2)
print('')

print('Acessando site INDEED vagas de emprego...')
time.sleep(3)
print('')

print('Iniciando captura de emails...')
print('')
print('')

x = 0

with open('lista-de-emails.txt','w') as arquivo:#CRIANDO O ARQUIVO TXT PARA SALVAR OS EMAILS
    
    for i in range(0,51):#QUANTIDADE DE PAGINAS A PERCORRER
        url = (f"https://br.indeed.com/empregos?q=E+Mail+Para+Curriculo&l=Nova+Odessa,+SP&fromage=last&start={x}")

        html_page = requests.get(url)
        html_source = html_page.text
        
        emails = re.findall('\w+@\w+\.{1}\w+', html_source)

        for email in emails:
            if email in lista:
                pass
            
            elif email == '0252655a41544fd28ae41f8b8ff36917@sentry.indeed':
                pass
            
            else:
                lista.append(email)
                print(email)
                print(email,file=arquivo)

        x = x+10
valor = len(list)        
print('')
print('')
print(f'{valor} emails capturados e salvos...')
time.sleep(2)
print('')

print('Acessando a lista de emails...')
time.sleep(2)
print('')

#NÃO ESQUEÇA DE ATIVAR 'AUTORIZAR PROGRAMAS MENOS SEGUROS' NA SUA CONTA GMAIL!
#O GMAIL SÓ AUTORIZA 500 EMAILS POR DIA...NÃO ABUSE!

with open('curriculo.txt','r',encoding='utf-8') as arquivo2:
    curriculo = arquivo2.read()

print('Iniciando o envio de emails para empresas...')
time.sleep(2)
print('')
print('.')
print('.')
print('.')
print('')

for i in range(1, valor):#QUANTIDADE DE EMAILS A ENVIAR
    fromaddr = "seuemail@gmail.com"#INSIRA SEU EMAIL AQUI
    toaddr = lista[i]
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "CURRICULO"

    body = curriculo

    msg.attach(MIMEText(body, 'plain'))

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "senha-do-seu-gmail")#INSIRA A SENHA DO SEU GMAIL AQUI
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

    print(f'Email {i}/{valor} enviado com sucesso!')
    #time.sleep(30)
            
print('')
print('.')
print('.')
print('.')
print('')
print('Automação concluida com sucesso!')
