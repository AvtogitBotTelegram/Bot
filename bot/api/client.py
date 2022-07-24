from bot.api.details import DetailsApi
from bot.config import config


class ApiClient:

    def __init__(self, url: str) -> None:
        self.details = DetailsApi(url)


client = ApiClient(config.url)
