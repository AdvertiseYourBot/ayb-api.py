# ayb-api.py

The official AYB api wrapper

## Classes

### Client

###### Methods

- fetch_stats()

  - Fetch overall site statistics for ayblisting.com
  - Example:

  ```py
  import aybapi

  client = aybapi.Client()
  stats = client.fetch_stats()
  print(stats)

  # {
  #   bots: 158,
  #   pending_approval: 2,
  #   unread_reports: 0
  # }

  ```

- fetch_bot(String: id)

  - Fetch a bot from the site using its id
  - Example

  ```py
  import aybapi

  client = aybapi.Client()
  bot = client.fetch_bot("389604896606781440")
  print(bot)

  # Liam
  ```

- fetch_category(String: id)

  - Fetch a category by id
  - Example

  ```py
  import aybapi

  client = aybapi.Client()
  category = client.fetch_category("12")
  print(category.name)

  # Music
  ```

---

### Bot

###### Methods

- fetch_category()

  - Fetch the category of that bot
  - Example

  ```py
  import aybapi

  client = aybapi.Client()
  bot = client.fetch_bot("389604896606781440")
  cat = bot.fetch_category()
  print(cat.name)

  # Bump
  ```

###### Properties

- **Client: client** `The client that fetched this bot`
- **String: note** `If success if False this will contain a note on why`
- **String: user_name** `The name of the bot`
- **String: id** `The id of the bot`
- **Boolean: success** `The success status of fetching the bot`
- **String: owner_id** `The id of the owner for this bot`
- **String: avatar_url** `The url for the avatar of this bot`
- **Number: votes** `The amount of votes the bot has on the website`
- **String: category_id** `The id of the category this bot is in`
- **Boolean: approved** `If the bot is approved on the website`
- **Boolean: premium** `The bot's premium status`
- **Boolean: certified** `If the bot has been certified on the website`
- **String: prefix** `The prefix of this bot`
- **String: permissions** `The permissions this bot asks for`
- **String: library** `The library this bot was made with`
- **String: brief_desc** `This bot's short description`
- **String: long_desc** `This bot's long description`
- **String: website_url** `This bot's website url, if any`
- **String: github_url** `The url to this bot's GitHub reposiory, if any`
- **String: support_server_invite** `An invite to the support server`

---

### Category

###### Properties

- **Boolean: success** `The success status of fetching the category`
- **String: id** `The id of this category`
- **String: name** `The name of this category`
- **String: slug** `The slug of this category`
- **String: note** `If success if False this will contain a note on why`
