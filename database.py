# 𝙳𝚘𝚗'𝚝 𝚁𝚎𝚖𝚘𝚟𝚎 𝙲𝚛𝚎𝚍𝚒𝚝 @ASHWANI10
# 𝚂𝚞𝚋𝚜𝚌𝚛𝚒𝚋𝚎 Telegram 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 𝙵𝚘𝚛 𝙰𝚖𝚊𝚣𝚒𝚗𝚐 𝙱𝚘𝚝 @Quantabots
# 𝙰𝚜𝚔 𝙳𝚘𝚞𝚋𝚝 𝚘𝚗 𝚝𝚎𝚕𝚎𝚐𝚛𝚊𝚖 @OGsnx

from pymongo import MongoClient
from configs import cfg

client = MongoClient(cfg.MONGO_URI)

users = client['main']['users']
groups = client['main']['groups']

def already_db(user_id):
        user = users.find_one({"user_id" : str(user_id)})
        if not user:
            return False
        return True

def already_dbg(chat_id):
        group = groups.find_one({"chat_id" : str(chat_id)})
        if not group:
            return False
        return True

def add_user(user_id):
    in_db = already_db(user_id)
    if in_db:
        return
    return users.insert_one({"user_id": str(user_id)}) 

def remove_user(user_id):
    in_db = already_db(user_id)
    if not in_db:
        return 
    return users.delete_one({"user_id": str(user_id)})
    
def add_group(chat_id):
    in_db = already_dbg(chat_id)
    if in_db:
        return
    return groups.insert_one({"chat_id": str(chat_id)})

def all_users():
    user = users.find({})
    usrs = len(list(user))
    return usrs

def all_groups():
    group = groups.find({})
    grps = len(list(group))
    return grps
