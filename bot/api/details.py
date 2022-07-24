import httpx

from bot.api.schemas import ModelDetails


class DetailsApi:

    def __init__(self, url: str) -> None:
        self.url = url

    def get_bad_details(self) -> list[ModelDetails]:
        files = {'upload-file': open('excelfile/ris.xlsx', 'rb')}
        response = httpx.post(f'{self.url}/api/v1/detail/expired-details', files=files)
        response.raise_for_status()
        return [ModelDetails(**detail) for detail in response.json()]
