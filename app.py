import requests

# Token e ID del gruppo Telegram
telegram_token = '7390613815:AAFZzCFSMnfomMqRXHkKzEqsrPo7Rh_0Yf4'
group_id = '-1001771715212'
topic_id = '79558'  # ID del topic per il thread di Telegram

# Funzione per inviare un messaggio su Telegram
def send_telegram_message(message, chat_id, topic_id):
    url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'
    
    payload = {
        'chat_id': chat_id,
        'text': message,
        'message_thread_id': topic_id,
        'parse_mode': 'Markdown',  # Usa MarkdownV2 per supporto caratteri
        'disable_web_page_preview': True
    }
    
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Se il codice di stato non è 200, solleva un'eccezione
        print(f"Messaggio inviato con successo: {message}")
    except requests.exceptions.RequestException as e:
        print(f"Errore nell'invio del messaggio a Telegram: {e}")

if __name__ == "__main__":
    send_telegram_message("TEST IN CORSO", group_id, topic_id)