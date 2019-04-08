import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re
import telepot
import schedule

bot = telepot.Bot('879354760:AAF4JiZOadBOx4cLg3O2CstEui2SAE0h1-A')

campeonato_pernambucano = "https://www.bet365.com/#/AC/B1/C1/D13/E40253096/F2/"
campeonato_paulista = "https://www.bet365.com/#/AC/B1/C1/D13/E40251259/F2/"
campeonato_gaucho = "https://www.bet365.com/#/AC/B1/C1/D13/E40158263/F2/"
campeonato_geral = "https://www.bet365.com/#/AC/B1/C1/D13/E102/F16/"

def principal():

    data = time.strftime("%d/%m/%Y - %H:%M:%S")
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)  # seu path do driver
    driver.get("https://www.bet365.com/")
    print('Site acessado...')
    time.sleep(2)

    driver.find_element_by_xpath("/html/body/form/div[3]/center/div/div[3]/div/div[1]/div/div/a/div[2]/div[1]/div").click()
    print('Site burlado!')
    time.sleep(5)


    #---------------NÃO MEXER NO CÓDIGO ACIMA DESSA LINHA---------------------

    driver.get(campeonato_geral)
    print('Site acessado: Jogos Brasileiros - Geral')
    time.sleep(5)

    txt_sport = open('sport.txt', "r").read()
    txt_nautico = open('nautico.txt', "r").read()
    txt_santa = open('santa.txt', "r").read()

    src = driver.page_source
    achou_sport = re.search(r'Sport Recife', src)
    achou_nautico = re.search(r'Náutico', src)
    achou_santa = re.search(r'Santa Cruz', src)

    write_sport = open('sport.txt', "w")
    write_nautico = open('nautico.txt', "w")
    write_santa = open('santa.txt', "w")

    driver.get_screenshot_as_file('partidas.png')

    if achou_sport != None:
        print('Valor encontrado: Sport Recife')

        if 'ACHOU' in txt_sport:
            print('[' + data + '] Notifcação já enviada antes - Sport')

        else:

            write_sport.write('ACHOU')
            bot.sendMessage(999999999, 'O jogo do Sport Recife abriu!')
            bot.sendMessage(999999999, 'CAMPEONATO PERNAMBUCANO.PNG: ')
            bot.sendPhoto(999999999, open('partidas.png', 'rb'))

            bot.sendMessage(999999999, 'O jogo do Sport Recife abriu!')
            bot.sendMessage(999999999, 'CAMPEONATO PERNAMBUCANO.PNG: ')
            bot.sendPhoto(999999999, open('partidas.png', 'rb'))

            print('[' + data + '] Telegram enviado! - Sport')

    else:
        print('Não encontrado - Sport Recife')
        erase_sport = open('sport.txt', "w")
        erase_sport.write('')

    if achou_nautico != None:
        print('Valor encontrado: Nãutico')

        if 'ACHOU' in txt_nautico:
            print('[' + data + '] Notifcação já enviada antes - Náutico')

        else:

            write_nautico.write('ACHOU')
            bot.sendMessage(999999999, 'O jogo do Náutico abriu!') 			# 999999999 = your chat id
            bot.sendMessage(999999999, 'CAMPEONATO PERNAMBUCANO.PNG: ')		# 999999999 = your chat id
            bot.sendPhoto(999999999, open('partidas.png', 'rb'))			# 999999999 = your chat id

            bot.sendMessage(999999999, 'O jogo do Náutico abriu!')			# 999999999 = your chat id
            bot.sendMessage(999999999, 'CAMPEONATO PERNAMBUCANO.PNG: ')		# 999999999 = your chat id
            bot.sendPhoto(999999999, open('partidas.png', 'rb'))			# 999999999 = your chat id

            print('[' + data + '] Telegram enviado! - Náutico')


    else:
        print('Não encontrado - Náutico')
        erase_naut = open('nautico.txt', "w")
        erase_naut.write('')

    if achou_santa != None:
        print('Valor encontrado: Santa Cruz')

        if 'ACHOU' in txt_santa:
            print('[' + data + '] Notifcação já enviada antes - Santa Cruz')

        else:

            write_santa.write('ACHOU')
            bot.sendMessage(999999999, 'O jogo do Santa Cruz abriu!')		# 999999999 = your chat id
            bot.sendMessage(999999999, 'CAMPEONATO PERNAMBUCANO.PNG: ')		# 999999999 = your chat id
            bot.sendPhoto(999999999, open('partidas.png', 'rb'))			# 999999999 = your chat id

            bot.sendMessage(999999999, 'O jogo do Santa Cruz abriu!')		# 999999999 = your chat id
            bot.sendMessage(999999999, 'CAMPEONATO PERNAMBUCANO.PNG: ')		# 999999999 = your chat id
            bot.sendPhoto(999999999, open('partidas.png', 'rb'))			# 999999999 = your chat id

            print('[' + data + '] Telegram enviado! - Santa Cruz')


    else:
        print('Não encontrado - Santa Cruz')
        erase_santa = open('santa.txt', "w")
        erase_santa.write('')


#================ ADICIONAR NOVO TIME---------

########################################################
##################### CORINTHIANS ######################
########################################################

    txt_cor = open('cor.txt', "r").read()
    achou_cor = re.search(r'Corinthians', src)
    write_cor = open('cor.txt', "w")

    driver.get_screenshot_as_file('partidas_paulista.png')


    if achou_cor != None:
        print('Valor encontrado: Corinthians')

        if 'ACHOU' in txt_cor:
            print('[' + data + '] Notifcação já enviada antes - Corinthians')

        else:

            write_cor.write('ACHOU')
            bot.sendMessage(999999999, 'O jogo do Corinthians abriu!')
            bot.sendMessage(999999999, 'CAMPEONATO PAULISTA.PNG: ')
            bot.sendPhoto(999999999, open('partidas_paulista.png', 'rb'))

            bot.sendMessage(999999999, 'O jogo do Corinthians abriu!')
            bot.sendMessage(999999999, 'CAMPEONATO PAULISTA.PNG: ')
            bot.sendPhoto(999999999, open('partidas_paulista.png', 'rb'))

            print('[' + data + '] Telegram enviado! - Corinthians')

    else:
        print('Não encontrado - Corinthians')
        erase_cor = open('cor.txt', "w")
        erase_cor.write('')


########################################################
##################### PALMEIRAS ######################
########################################################

    txt_palm = open('palm.txt', "r").read()

    achou_palm = re.search(r'Palmeiras', src)  ### TROCAR O NOME DO TIME

    write_palm = open('palm.txt', "w")

    driver.get_screenshot_as_file('partidas_paulista.png')  ### TIRA SCREENSHOT


    if achou_palm != None:
        print('Valor encontrado: Palmeiras')

        if 'ACHOU' in txt_palm:
            print('[' + data + '] Notifcação já enviada antes - Palmeiras')

        else:

            write_palm.write('ACHOU')
            bot.sendMessage(999999999, 'O jogo do Palmeiras abriu!')
            bot.sendMessage(999999999, 'CAMPEONATO PAULISTA.PNG: ')
            bot.sendPhoto(999999999, open('partidas_paulista.png', 'rb')) ###   ENVIA .PNG

            bot.sendMessage(999999999, 'O jogo do Corinthians abriu!')
            bot.sendMessage(999999999, 'CAMPEONATO PAULISTA.PNG: ')
            bot.sendPhoto(999999999, open('partidas_paulista.png', 'rb')) ### ENVIA .PNG

            print('[' + data + '] Telegram enviado! - Palmeiras')

    else:
        print('Não encontrado - Palmeiras')
        erase_palm = open('palm.txt', "w")
        erase_palm.write('')


########################################################
##################### GRÊMIO ######################
########################################################

    txt_gremio = open('gremio.txt', "r").read()

    achou_gremio = re.search(r'Grêmio', src)  ### TROCAR O NOME DO TIME

    write_gremio = open('gremio.txt', "w")

    driver.get_screenshot_as_file('partidas_gaucho.png')  ### TIRA SCREENSHOT


    if achou_gremio != None:
        print('Valor encontrado: Grêmio')

        if 'ACHOU' in txt_gremio:
            print('[' + data + '] Notifcação já enviada antes - Grêmio')

        else:

            write_gremio.write('ACHOU')
            bot.sendMessage(999999999, 'O jogo do Grêmio abriu!')
            bot.sendMessage(999999999, 'CAMPEONATO GAÚCHO.PNG: ')
            bot.sendPhoto(999999999, open('partidas_gaucho.png', 'rb')) ###   ENVIA .PNG

            bot.sendMessage(999999999, 'O jogo do Grêmio abriu!')
            bot.sendMessage(999999999, 'CAMPEONATO GAÚCHO.PNG: ')
            bot.sendPhoto(999999999, open('partidas_gaucho.png', 'rb')) ### ENVIA .PNG

            print('[' + data + '] Telegram enviado! - Grêmio')

    else:
        print('Não encontrado - Grêmio')
        erase_gremio = open('gremio.txt', "w")
        erase_gremio.write('')


#----------NÃO MEXER ABAIXO DESSA LINHA-----------

    time.sleep(10)

    driver.quit()

principal()

#schedule.every(2).minutes.do(principal)

#while True:
#    schedule.run_pending()
