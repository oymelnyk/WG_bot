import datetime

from tanks import Tanks
from tokens import Tokens, db
import requests
#from datetime import datetime



#WG API
application_id = ''


def user_tokens(user_id):
    try:
        # Find access_token + account_id by telegram_id
        try:
            temp_id = Tokens.query.filter_by(telegram_id=user_id).first()
            mass = [temp_id.access_token, temp_id.account_id, temp_id.nickname]
            return mass
        except:
            pass

        # Find access_token + account_id by vk_id
        try:
            temp_id = Tokens.query.filter_by(vk_id=user_id).first()
            mass = [temp_id.access_token, temp_id.account_id, temp_id.nickname]
            return mass
        except:
            pass

        try:
            temp_id = Tokens.query.filter_by(account_id=user_id).first()
            mass = [temp_id.access_token, temp_id.account_id, temp_id.nickname]
            return mass
        except:
            pass
    except:
        return "Error garage_list(" + str(user_id) + ")"


def garage_info_10(access_token, account_id):
    link = 'https://api.worldoftanks.ru/wot/account/info/?application_id='+str(application_id)+'&account_id='+str(account_id)+'&access_token='+str(access_token)+'&extra=private.garage'

    api_request = requests.get(link)
    api_request = api_request.json()

    #updated_time = datetime.utcfromtimestamp(api_request['data'][account_id]['updated_at']).strftime('%Y-%m-%d %H:%M:%S')
    garage = api_request['data'][account_id]['private']['garage']

    tanks = []
    for i in garage:
        try:
            tank = Tanks.query.filter_by(tank_id=i).first()
            tanks.append(str(tank.tank_name))
            #print(tank.tank_name)
        except:
            pass
    return tanks




def online(access_token, clan_id):
    link = 'https://api.worldoftanks.ru/wot/clans/info/?application_id='+str(application_id)+'&access_token='+str(access_token)+'&clan_id='+clan_id+'&extra=private.online_members'
    api_request = requests.get(link)
    api_request = api_request.json()
    json_online = api_request['data'][str(clan_id)]['private']['online_members']
    len_json_online = len(json_online)
    #print(json_online)
    #print(len_json_online)

    members_count = api_request['data'][clan_id]['members_count']
    members_mass = {}

    for i in range(0, members_count):
        members_mass[api_request['data'][clan_id]['members'][i]['account_id']] = api_request['data'][clan_id]['members'][i]['account_name']
    online_now = []
    for i in members_mass:
        for ii in json_online:
            if i == ii:
                online_now.append(members_mass[i])

    return len_json_online, online_now

def update_tokens():
    link = 'https://api.worldoftanks.ru/wot/auth/prolongate/'
    token = Tokens.query.all()
    for i in token:
        try:
            print(i.access_token)
            api_request = requests.request('POST', link, data={'application_id': str(application_id), 'access_token': str(i.access_token)})
            api_request = api_request.json()
            print(api_request)
            access_token = api_request['data']['access_token']
            print(access_token)
            expires_at = api_request['data']['expires_at']
            print(expires_at)
            Tokens.query.filter_by(access_token=str(i.access_token)).update(dict(access_token=str(access_token), expires_at=str(expires_at)))
            db.session.commit()
        except:
            print("Error - "+str(i))
    txt = 'Update tokens - '+str(datetime.datetime.now())
    print(txt)
    return txt


