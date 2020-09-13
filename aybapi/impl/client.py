import typing

# Importing implemented models
from .bot import Bot
from .category import Category

# Importing helper methods and utils
from ..utils.endpoints import *
from ..utils.fetch import fetch

# Importing base class of Client model
from ..base.client import Client as ClientBase


class Client(ClientBase):
    def fetch_stats(self) -> typing.Optional[dict]:
        """Fetches the overall site status available to the public

        Returns
        -------
        API response: typing.Dict
                The API response containing the site status information.
        """
        data = fetch(BASE_URL + STATS)
        return data

    def fetch_bot(self, id) -> Bot:
        """Fetches a specific bot according to it's ID

        Returns
        -------
        bot: aybapi.Bot
                AYBAPI bot object containing bot information from API response.
        """
        data = fetch(BASE_URL + BOT.format(id))
        return Bot(self, data)

    def fetch_category(self, id) -> Category:
        """Fetches a specific category according to it's ID

        Returns
        -------
        category: aybapi.Category
                AYBAPI category object containing bot information from API response.
        """
        data = fetch(BASE_URL + CATEGORY.format(id))
        return Category(data)
