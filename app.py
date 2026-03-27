
from fastapi import FastAPI, Request
import requests
from difflib import get_close_matches
from products import PRODUCTS

app = FastAPI()

VERIFY_TOKEN = "mytoken123"
PAGE_ACCESS_TOKEN =("EAAiIIUv6rFkBRAykdp0PJJIbA0prHZCgelQsrpafdnow0k2Nxf1HWfNUFtl3HmMKkkKzwATajdMDXheUWDzokMwtelv6wdebnXuDoZC0XS2HBOon9JVBAJfWhRlHDZCxlWr7X7NGHDSrCWVAaRZBJ0IrulZCAiaqlYLe0WV1mrqtbUdMfVQZCof9FR3gqGHzLTZBgdJlQZDZD")
@app.get("/")
def home():
    return {"message": "Bot is LIVE 🚀"}


from fastapi.responses import PlainTextResponse

@app.get("/webhook")
async def verify_webhook(request: Request):
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")
    
    if token == VERIFY_TOKEN and challenge:
        return PlainTextResponse(content=challenge, status_code=200)
    return PlainTextResponse(content="Verification failed", status_code=403)
@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()

    try:
        for entry in data.get("entry", []):
            for messaging in entry.get("messaging", []):

                sender_id = messaging["sender"]["id"]

                if "message" in messaging and "text" in messaging["message"]:
                    user_msg = messaging["message"]["text"]

                    reply = smart_ai_reply(user_msg)

                    if reply:  # spam filter
                        send_message(sender_id, reply)

    except Exception as e:
        print("Error:", e)

    return {"status": "ok"}


# 🔥 AI ENGINE
def smart_ai_reply(message):
    msg = message.lower()

    # ❌ SPAM FILTER
    spam_words = ["beautiful", "sexy", "love you", "hot", "nice pic"]
    if any(word in msg for word in spam_words):
        return None

    # ❤️ EMOJI REPLY
    if any(emoji in msg for emoji in ["😍", "😘", "🥰", "❤️"]):
        return "❤️ Thank you! Aap product dekhna chahte ho?\n\n1️⃣ Hoodie\n2️⃣ T-shirt\n3️⃣ Offers"

    # 👋 GREETING
    if any(x in msg for x in ["hi", "hello", "hey", "kaise ho", "how are you"]):
        return "😊 Namaste! Aap kya dekhna chahte ho?\n\n1️⃣ Hoodie\n2️⃣ T-shirt\n3️⃣ Offers"

    # 🔍 PRODUCT MATCH (keyword + fuzzy)
    for product in PRODUCTS:
        for keyword in product["keywords"]:
            if keyword in msg:
                return format_product(product)

    # fuzzy match
    names = [p["name"].lower() for p in PRODUCTS]
    match = get_close_matches(msg, names, n=1, cutoff=0.3)

    if match:
        for p in PRODUCTS:
            if p["name"].lower() == match[0]:
                return format_product(p)

    return "🙏 Samajh nahi aaya\n\nTry: hoodie, tshirt"


# 📦 PRODUCT FORMAT
def format_product(p):
    return f"""🛍️ {p['name']}
💰 Price: {p['price']}
📏 Sizes: {p['sizes']}
📄 {p['description']}
🚚 Free Delivery Available"""


# 📤 SEND MESSAGE
def send_message(recipient_id, message_text):
    url = "https://graph.facebook.com/v18.0/me/messages"

    params = {"access_token": PAGE_ACCESS_TOKEN}

    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }

    requests.post(url, params=params, json=payload)