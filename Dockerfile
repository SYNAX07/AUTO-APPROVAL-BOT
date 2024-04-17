# 𝙳𝚘𝚗'𝚝 𝚁𝚎𝚖𝚘𝚟𝚎 𝙲𝚛𝚎𝚍𝚒𝚝 @ASHWANI10
# 𝚂𝚞𝚋𝚜𝚌𝚛𝚒𝚋𝚎 Telegram 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 𝙵𝚘𝚛 𝙰𝚖𝚊𝚣𝚒𝚗𝚐 𝙱𝚘𝚝 @Quantabots
# 𝙰𝚜𝚔 𝙳𝚘𝚞𝚋𝚝 𝚘𝚗 𝚝𝚎𝚕𝚎𝚐𝚛𝚊𝚖 @OGsnx

FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app

CMD python3 bot.py
