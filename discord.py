

import requests 

# Vlož sem svůj webhook URL z Discordu
webhook_url = "https://discord.com/api/webhooks/1361599673282068614/BlA5HyxD3_o1gtCUNkSMyXwjHVH4tgBWxHP91q4eI1vzxoafGDNv49WfJioVJao0L0Pv"

# Text zprávy
message = {
    "content": "meowmeow uaaaaaah"
}

# Odeslání zprávy
response = requests.post(webhook_url, json=message)

# Kontrola výsledku
if response.status_code == 204:
    print("Zpráva úspěšně odeslána!")
else:
    print(f"Chyba při odesílání zprávy: {response.status_code}")
