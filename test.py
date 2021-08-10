import bcrypt

password = bcrypt.hashpw(b"zayyad1", bcrypt.gensalt())

print (password)

def verify_password():
    user = bcrypt.checkpw(b"zayyad1", password)
    return user