import abc
import typing
from ..impl.bot import Bot
from ..impl.category import Category


class Client(abc.ABC):

    @abc.abstractmethod
    def fetch_stats(self) -> typing.Optional[dict]:
        """Fetches the overall site status available to the public

        Returns
        -------
        API response: typing.Dict
                The API response containing the site status information.
        """

    @abc.abstractmethod
    def fetch_bot(self, id) -> Bot:
        """Fetches a specific bot according to it's ID

        Returns
        -------
        bot: aybapi.Bot
                AYBAPI bot object containing bot information from API response.
        """

    def fetch_category(self, id) -> Category:
        """Fetches a specific category according to it's ID

        Returns
        -------
        category: aybapi.Category
                AYBAPI category object containing bot information from API response.
        """
