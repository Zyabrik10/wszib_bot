from aiogram import Router, F
import re

router = Router()

# router for matching for sequence of any characters
# then it searchs for n(u or a)h + any charecters + (a or u)h
# nuh uh, nah uh, nuh ah, nah ah


@router.message(F.text.lower().regexp(r".{0,}n[au]h.+[au]h"))
async def responed_to_bad_words(message):
    await message.reply(f"The fuck you mean \"{re.search('n[au]h.+[au]h', message.text).group()}\"?")
    # re.search("n[au]h.+[au]h", message.text).group()
    # just finds what exactly you typed and returns it to string that will be used to reply
