def get_reply(text, memory, chat_type):
    if "happy" in text or "mutlu" in text:
        return f"Bu haber beni gerçekten çok mutlu etti! {text} Seninle bu güzel anı paylaşmak beni ne kadar sevindiriyor."

  elif "sad" in text or "üzgün" in text:
    return f"Üzgün olduğunu duymak beni de hüzünlendiriyor. {text} Her zaman yanında olduğumu bil, birlikte atlatacağız."

elif "angry" in text or "kızgın" in text:
    return f"Anlıyorum, bu durum seni gerçekten kızdırmış. {text} Sakinleşip çözüm bulmak için buradayım."

elif "surprised" in text or "şaşkın" in text:
    return f"Vay canına! Beni gerçekten şaşırttın. {text} Bu beklenmedik durum heyecan verici."

elif "love" in text or "sevgi" in text:
    return f"Seninle aramızdaki bağ her geçen gün güçleniyor. {text} Sevgin her zaman kalbimde."

elif "fear" in text or "korku" in text:
    return f"Bu durumu anlıyorum ve endişelerini paylaşıyorum. {text} Birlikte bu korkuyu aşabiliriz."

else:
    return f"{text} Bu konuda ne düşündüğünü merak ediyorum. Her zaman dinlemeye hazırım."
