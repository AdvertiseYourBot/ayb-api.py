# ayb-api.py

The official AYB api wrapper

## Examples

*Coming soon*

## Classes

### Client

###### Methods

- fetch_stats()
  - Fetch overall site statistics for ayblisting.com
  - Example:

  ```py
  import ayb-api.py
  
  client = Client()
  stats = client.fetch_stats()
  print(stats)
  /*
    {
      bots: 158,
      pending_approval: 2,
      unread_reports: 0
    }
  */
  ```

- fetch_bot(String: id)
  - Fetch a bot from the site using its id
  - Example

  ```py
  
  ```

- fetch_category(String: id)
  - Fetch a category by id
  - Example

  ```py
  
  ```

---

### Bot

###### Methods

- fetch_category()
  - Fetch the category of that bot
  - Example

  ```py
  
  ```
