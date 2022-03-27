import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from main import vk_tokn
from get_info import garage_info_10, user_tokens, online, update_tokens
import requests
import time
from threading import Thread


def vk():
    try:
        vk_session = vk_api.VkApi(
            token='')
        longpoll = VkBotLongPoll(vk_session, '179146714')

        def sender(id, text):
            vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})

        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.from_chat:
                    id = event.chat_id
                    msg = event.object.message['text'].lower()
                    rtm = event.object.message['conversation_message_id']
                    if msg == '/auth':
                        if event.message.from_id == vk_tokn(event.message.from_id):
                            sender(id, "Привет, ты чо охуел второй раз тыцать? А?")
                        else:
                            link = "https://api.worldoftanks.ru/wot/auth/login/?application_id=ad94d0414fe22f0f13a5a99201bb3359" \
                                   "&display=page&nofollow=0&redirect_uri=http://oymelnyk.com/done/vk/" + str(
                                event.message.from_id)
                            sender(id, "Перейди по ссылке и авторизуйся - " + str(link))
                            print(link)

                    if msg == '/start':
                        text = "Привет! Я бот клана [4M0K] ЧМОК В ПУПОК!\nДля авторизации напиши в чат /auth и перейди по " \
                               "ссылке.\n Список команд: /commands"

                        sender(id, text)

                    if msg == '/commands':
                        text = "/start - Начать работу с ботом\n" \
                               "/auth - авторизоваться\n" \
                               "/commands - список команд\n" \
                               "/squads - списки рот\n" \
                               "/garage - список техники в ангаре (нужна авторизация)\n" \
                               "/ts - ссылка на наш ТимСпик\n" \
                               "/rules - правила роты\n" \
                               "/schedule - расписание\n" \
                               "/online - онлайн\n" \
                               "пососи ок?"

                        sender(id, text)

                    if msg == '/squads':
                        text = "Рота 1\n" \
                               "🍋 KucJIbIu_AcKoP6uH - половой"\
                                "CJlADENbKUY\n" \
                                "_Schtil_\n", \
                               "ANGER1978\n" \
                               "euthanasia_\n" \
                               "_Admiral_Odessit_\n"\
                               "CoBeTcKuu__TaHKucT_\n" \
                               "MuHcKoE_Ka3uHo\n" \
                               "al14na300597\n"
                        sender(id, text)

                    if msg == 'сосать':
                        text = "чмок чмок чмок"

                        sender(id, text)

                    if msg == '/garage':
                        try:
                            user_inf = user_tokens(event.message.from_id)
                            print(event.message.from_id)
                            data = garage_info_10(str(user_inf[0]), str(user_inf[1]))
                            text = ''
                            fire_tanks = ['Объект 907', 'T95/FV4201 Chieftain', 'Объект 279 ранний',
                                          'Carro da Combattimento 45 t', 'M60', 'VK 72.01 (K)', 'T95E6', 'Т-22 ср.']
                            comet_tanks = ['Conqueror Gun Carriage', 'Bat.-Châtillon 155 58', 'T92 HMC', 'G.W. E 100', 'Объект 261']
                            light_tanks = ['Panhard EBR 105', 'Т-100 ЛТ', 'Rheinmetall Panzerwagen', 'Manticore',
                                           'XM551 Sheridan']
                            label_tanks_fire = ''
                            label_tanks_comet = ''
                            label_tanks_light = ''
                            for i in data:
                                if str(i) in fire_tanks:
                                    label_tanks_fire += "🔥 " + str(i) + '\n'
                                elif str(i) in comet_tanks:
                                    label_tanks_comet += "☄ " + str(i) + '\n'
                                elif str(i) in light_tanks:
                                    label_tanks_light += "🚦 " + str(i) + '\n'
                                else:
                                    text += str(i) + '\n'
                            sender(id, str(
                                user_inf[2] + "\n\n") + label_tanks_fire + label_tanks_comet + label_tanks_light + text)
                        except:
                            sender(id, 'Ошибка блять! А не попробовать ли тебе авторизоваться? А? Команда /auth')

                    if msg == '/ts':
                        text_ts = "TS - 4M0K.ts-3.su"
                        sender(id, text_ts)

                    if msg == 'какой тс':
                        text_ts = "TS - 4M0K.ts-3.su"
                        sender(id, text_ts)

                    if msg == 'киньте тс':
                        text_ts = "TS - 4M0K.ts-3.su"
                        sender(id, text_ts)

                    if msg == '/rules':
                        rules = 'Правила роты "Черный тюльпан":\n\n' \
                                '1. Всегда твердая пися.\n' \
                                '2. Все тупые, но за то красивые.\n' \
                                '3. Кто ссыт - тот гибнет.\n' \
                                '4. Проблемы негра не ебут никого.\n' \
                                '5. Если хочешь кого-то подпереть, подопри свою мамку.\n' \
                                '6. Самое главное написать - "Сорри".\n' \
                                '7. Полевой - неадекват.\n' \
                                '8. Хейтер хуже пидораса, но лучше Олега.\n' \
                                '9. Олег хуже всех!!!'
                        sender(id, rules)

                    if msg == '/schedule':
                        schedule = 'Расписание боев:\n\n' \
                                   'Понедельник - 20:00 - 22:00 МСК\n' \
                                   'Вторник - 20:00 - 22:00 МСК\n' \
                                   'Среда - выходной\n' \
                                   'Четверг - 20:00 - 22:00 МСК\n' \
                                   'Пятница - выходной\n' \
                                   'Суббота - по онлайну\n' \
                                   'Восскресение - по онлайну'

                        sender(id, schedule)

                    if msg == '/online':
                        try:
                            user_inf = user_tokens(event.message.from_id)
                            link = 'https://api.worldoftanks.ru/wot/account/info/?application_id=ad94d0414fe22f0f13a5a99201bb3359&account_id=' + str(
                                user_inf[1]) + '&fields=clan_id'
                            api_request = requests.get(link)
                            api_request = api_request.json()
                            clan_id = api_request['data'][str(user_inf[1])]['clan_id']
                            online_now = online(str(user_inf[0]), str(clan_id))
                            ot = ''
                            kucjiuhka = ['KucJIbIu_AcKoP6uH', 'CJlADENbKUY', '_Schtil_', 'ANGER1978', 'euthanasia_',
                                         '_Admiral_Odessit_', 'CoBeTcKuu__TaHKucT_', 'MuHcKoE_Ka3uHo', 'al14na300597']
                            kucjiuhka_online = ''
                            kucjiuhka_online_mass = []

                            stop_kick = ['_VaN4iK_OsTrOv', 'ANGER1978', 'BuKyJIbKa_Ta_caMa9', 'Mertvii', 'ubiyca1129',
                                         'PAK_I3_XEPCOHA', 'Neon85', 'Agent_XXX', '_VaN4iK_OsTrOv', 'malish178']
                            stop_kick_online = ''
                            stop_kick_online_mass = []

                            for i in online_now[1]:
                                if i in kucjiuhka:

                                    kucjiuhka_online += str(i) + '\n'
                                    kucjiuhka_online_mass.append(str(i))

                                elif i in stop_kick:
                                    stop_kick_online += str(i) + '\n'
                                    stop_kick_online_mass.append(str(i))

                                else:
                                    ot += str(i) + '\n'

                            propaganda_msg = 'Кого нет в списке роты выполните команду /auth'
                            online_text = 'Сейчас онлайн: ' + str(
                                online_now[0]) + '\n' + 'Онлайн кого не кикать: ' + str(
                                len(stop_kick_online_mass)) + '\nОнлайн тюльпэнов ' + str(
                                len(kucjiuhka_online_mass)) + '\n\n' + '🛑Не кикать🛑\n' + stop_kick_online + '\n' + '🌷Рота Верни тюльпан🌷\n' + str(
                                kucjiuhka_online) + '\n' + str(ot) + '\n\n' + propaganda_msg

                            sender(id, online_text)


                        except:
                            sender(id, "Авторизуйся командой /auth")
    except requests.exceptions.ReadTimeout:
        print("\n Переподключение к серверам ВК \n")
        #th1.start()
        time.sleep(5)
vk()

#th1 = Thread(target=vk)
#th2 = Thread(target=update_tokens)

#th1.start()
#x = 0
#while x == 0:
#    print("start update")
#    th2.start()
#    time.sleep(604800)
