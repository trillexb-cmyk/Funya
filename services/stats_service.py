import time

start_time = time.time()
users = set()
chats = set()

def update(m):
    users.add(m.from_user.id)
    chats.add(m.chat.id)

def get():
    return {
        "users": len(users),
        "chats": len(chats),
        "uptime": int(time.time() - start_time)
    }
