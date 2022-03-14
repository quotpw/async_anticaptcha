import asyncio

from aiohttp import ClientSession, ClientResponse
from .exceptions import error_by_id


class AntiCaptcha:
    def __init__(self, api_key: str, base_url='https://api.anti-captcha.com', soft_id: int = None):
        self.api_key = api_key
        self.soft_id = None
        self.session = ClientSession(base_url)

    @staticmethod
    def check_on_errors(response: dict):
        if error_by_id.get(response['errorId']):
            error = error_by_id[response['errorId']](response.get('errorDescription'))
            error.response = response
            raise error

    @staticmethod
    async def prepare_response(response: ClientResponse):
        response = await response.json(content_type=None)
        AntiCaptcha.check_on_errors(response)
        return response

    async def post(self, url: str, data: dict = None):
        if data is None:
            data = {}
        else:
            for key in list(data):
                if data[key] is None:
                    data.pop(key)
        data['clientKey'] = self.api_key
        return await self.prepare_response(
            await self.session.post(url, json=data)
        )

    async def create_task(self, task: dict, language_pool: str = None, callback_url: str = None):
        return await self.post(
            '/createTask',
            {
                'task': task,
                'softId': self.soft_id,
                'languagePool': language_pool,
                'callbackUrl': callback_url
            }
        )

    async def get_task_result(self, task_id: int):
        return await self.post(
            '/getTaskResult',
            {
                'taskId': task_id
            }
        )

    async def wait_task_result(self, task_id: int, ping_every: int = 3):
        while True:
            result = await self.get_task_result(task_id)
            if result.get('status') == 'ready':
                return result
            await asyncio.sleep(ping_every)

    async def get_balance(self):
        return await self.post(
            '/getBalance'
        )

    async def get_queue_stats(self, queue_id: int):
        return await self.post(
            '/getQueueStats',
            {
                'queueId': queue_id
            }
        )

    async def report_incorrect_image_captcha(self, task_id: int):
        return await self.post(
            '/reportIncorrectImageCaptcha',
            {
                'taskId': task_id
            }
        )

    async def report_incorrect_recaptcha(self, task_id: int):
        return await self.post(
            '/reportIncorrectRecaptcha',
            {
                'taskId': task_id
            }
        )

    async def report_correct_recaptcha(self, task_id: int):
        return await self.post(
            '/reportCorrectRecaptcha',
            {
                'taskId': task_id
            }
        )

    async def get_spending_stats(self, timestamp: int = None, queue: str = None, ip: str = None):
        return await self.post(
            '/getSpendingStats',
            {
                'date': timestamp,
                'queue': queue,
                'softId': self.soft_id,
                'ip': ip
            }
        )

    async def get_app_stats(self, mode: str = None):
        return await self.post(
            '/getAppStats',
            {
                'softId': self.soft_id,
                'mode': mode
            }
        )

    async def solve_hcapthca(
            self, url: str, site_key: str,
            proxy_type: str = None, proxy_address: str = None, proxy_port: int = None,
            proxy_login: str = None, proxy_password: str = None, user_agent: str = None,
            **kwargs
    ):
        task_type = 'HCaptchaTaskProxyless'
        if None not in [proxy_type, proxy_address, proxy_port, user_agent]:
            task_type = 'HCaptchaTask'

        return await self.create_task(
            task={
                'type': task_type,
                'websiteURL': url,
                'websiteKey': site_key,
                'proxyType': proxy_type,
                'proxyAddress': proxy_address,
                'proxyPort': proxy_port,
                'proxyLogin': proxy_login,
                'proxyPassword': proxy_password,
                'userAgent': user_agent
            },
            **kwargs
        )
