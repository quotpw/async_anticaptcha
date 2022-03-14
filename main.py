import asyncio

import anti_captcha


async def main():
    obj = anti_captcha.AntiCaptcha('wrong_key')
    try:
        print(await obj.get_balance())
    except anti_captcha.exceptions.AntiCaptchaError as err:
        print(err.response)

    await obj.session.close()


if __name__ == '__main__':
    asyncio.run(main())
