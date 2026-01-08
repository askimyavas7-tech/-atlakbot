_memory = {}

def remember(user_id, text):
    # Kullanıcının mesajlarını kaydederek kişiselleştirilmiş bir deneyim oluşturur
    _memory.setdefault(user_id, []).append(text)
    print(f"Remembered message for user {user_id}: {text}")

def recall(user_id):
    # Kullanıcının geçmiş mesajlarını alarak bağlamı korur
    return _memory.get(user_id, [])
