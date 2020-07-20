class Bot:
  def __init__(self, client, info):
    self.success = info['success']
    self.client = client

    if (self.success):
      self.id = info['clientid']
      self.owner_id = info['ownerid']
      self.user_name = info['botname']
      self.avatar_url = info['botavatar']
      self.votes = info['score']
      self.category_id = info['category']
      self.approved = info['approved']
      self.premium = info['premium']
      self.certified = info['certified']
      self.prefix = info['prefix']
      self.permissions = info['permissions']
      self.library = info['library']
      self.brief_desc = info['brief']
      self.long_desc = info['description']
      self.website_url = info['websiteurl']
      self.github_url = info['github']
      self.support_server_invite = "https://discord.gg/" + info['supportServerCode']
    else:
      self.note = info['note']

  def fetch_category(self):
    return self.client.fetch_category(self.category_id)
