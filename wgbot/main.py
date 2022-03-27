from flask import Flask, request
#from flask_sqlalchemy import SQLAlchemy
from tokens import Tokens, app, db
from get_info import user_tokens


@app.route('/')
def first():
    return "Hello"


@app.route('/done/tg/<int:tg_id>', methods=['GET', 'POST'])
def done_tg(tg_id):
    status = request.args.get("status")
    access_token = request.args.get("access_token")
    nickname = request.args.get("nickname")
    account_id = request.args.get("account_id")
    expires_at = request.args.get("expires_at")
    telegram_id = tg_id

    if status == "ok":

        if str(account_id) == user_tokens(account_id)[1]:
            Tokens.query.filter_by(account_id=str(account_id)).update(
                dict(telegram_id=str(telegram_id)))
            db.session.commit()

        else:
            try:
                token = Tokens(account_id=account_id, status=status, access_token=access_token, nickname=nickname,
                               expires_at=expires_at, telegram_id=telegram_id)
                db.session.add(token)
                db.session.commit()
                answer = str("Done! Your nickname is {}".format(nickname))
                return answer

            except:
                return "Error! Try again!"
    else:
        return "Error! Try again!"


@app.route('/done/vk/<int:vk_id>', methods=['GET', 'POST'])
def done_vk(vk_id):
    status = request.args.get("status")
    access_token = request.args.get("access_token")
    nickname = request.args.get("nickname")
    account_id = request.args.get("account_id")
    expires_at = request.args.get("expires_at")
    vk_id = vk_id

    if status == "ok":
        try:
            token = Tokens(account_id=account_id, status=status, access_token=access_token, nickname=nickname,
                           expires_at=expires_at, vk_id=vk_id)
            db.session.add(token)
            db.session.commit()
            answer = str("Done! Your nickname is {}".format(nickname))
            return answer

        except:
            return "Error! Try again!"
    else:
        return "Error! Try again!"

#тестовая вычитка токена для тг
def testdata(tg_id):
    testid = Tokens.query.filter_by(telegram_id=tg_id).first()
    mass = []
    mass.append(testid.access_token)
    mass.append(testid.account_id)

    return mass

#тестовая вычитка токена VK
def vk_tokn(vk_id):
    try:
        db.session.commit()
        testid = Tokens.query.filter_by(vk_id=vk_id).first()
        return testid.vk_id
    except:
        error = "error"
        return error


def tg_tokn(tg_id):
    try:
        testid = Tokens.query.filter_by(tg_id=tg_id).first()
        return testid.tg_id
    except:
        error = "error"
        return error



if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=80)
