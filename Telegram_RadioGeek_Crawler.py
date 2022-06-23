import asyncio
from telethon import TelegramClient
import os

api_id = "2421227"
api_hash = "5cfbdb99e4477b828bf06a9cd1efeead"

client = TelegramClient('YOUR_SESSION_NAME', api_id, api_hash)
client.start()

try:
    # remove old Readme.md file
    os.remove("./README.md")
except:
    pass

# add new Readme file and title
with open("./README.md", "w") as f:
    readme_title = """
# Latest RadioGeek | آخرین آپدیت پادکست رادیو گیک


    """

    f.write(readme_title)
    f.close()


def update_readme(title, caption, msg_url):
    readme_format = """
#### - [TITLE](LINK) 
 <details> <p>\n\nCAPTION\n\n</p> <p><br></p>
 </details> 
 <hr />\n\n"""

    with open("./README.md", "a") as f:
        text = readme_format.replace(
            "TITLE",
            title
        ).replace(
            "LINK",
            msg_url
        ).replace(
            "CAPTION",
            caption
        )
        f.write(text)
        f.close()


async def main():
    channel = await client.get_entity('jadiradio')
    async for message in client.iter_messages(channel):

        msg_url = f"https://t.me/{channel.username}/{message.id}"
        is_title = True
        title = ""
        caption = message.text

        if (message.media):
            try:
                title = message.media.document.attributes[0].title
                if title is None:
                    is_title = False

            except AttributeError:
                is_title = False

            if not is_title:
                try:
                    title = message.media.document.attributes[-1].file_name
                except:
                    continue

        try:
            title = title.replace(
                ".mp3", "").replace("-", " ").replace("_", " ")
        except:
            pass

        if title == "":
            continue

        update_readme(title, caption, msg_url)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
