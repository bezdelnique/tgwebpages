import asyncio

import yaml
from telethon import TelegramClient

f = open('config.yaml')
config = yaml.load(f, yaml.Loader)
f.close()

api_id = config['api_id']
api_hash = config['api_hash']
phone = config['phone']


async def main():
    client = TelegramClient(phone, api_id, api_hash, system_version="4.16.30-vxCUSTOM")
    await client.connect()
    if not await client.is_user_authorized():
        result = await client.send_code_request(phone)
        phone_hash = result.phone_code_hash
        await client.sign_in(phone, input('Please quize: '), phone_code_hash=phone_hash)
    # pp((await client.get_me()).stringify())
    print(await client.get_me())

    # Попугай глаголет has ID -1001614074953
    # async for dialog in client.iter_dialogs():
    #     # print(dialog.name, 'has ID', dialog.id)
    #     pass

    async for dialog in client.iter_dialogs():
        # print(dialog.name, 'has ID', dialog.id)
        if dialog.name == "Попугай глаголет":
            print(dialog.name, dialog.id)
            async for message in client.iter_messages(dialog, limit=3, offset_id=99):
                print(message)

    # # You can send messages to yourself...
    # await client.send_message('me', 'Hello, myself!')
    #
    # # You can, of course, use markdown in your messages:
    # message = await client.send_message(
    #     'me',
    #     'This message has **bold**, `code`, __italics__ and '
    #     'a [nice website](https://pornhub.com)!',
    #     link_preview=False
    # )
    #
    # # Sending a message returns the sent message object, which you can use
    # print(message.raw_text)
    #
    # # You can reply to messages directly if you have a message object
    # await message.reply('Cool!')


asyncio.run(main())
