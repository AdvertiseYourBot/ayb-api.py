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
            self.support_server_invite = "https://discord.gg/" + \
                info['supportservercode']
        else:
            self.note = info['note']

    def __str__(self):
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("owner_id", self.owner_id),
            ("user_name", self.user_name),
            ("avatar_url", self.avatar_url),
            ("votes", self.votes),
            ("category_id", self.category_id),
            ("approved", self.approved),
            ("premium", self.premium),
            ("certified", self.certified),
            ("prefix", self.prefix),
            ("permissions", self.permissions),
            ("library", self.library),
            ("brief_desc", self.brief_desc),
            ("website_url", self.website_url),
            ("github_url", self.github_url),
            ("support_server_invite", self.support_server_invite)
        ]
        return "%s<%s>" % (
            self.__class__.__name__,
            " ".join(f"{i[0]}={i[1]}," for i in attrs if i[1] != None),
        )

    def fetch_category(self):
        return self.client.fetch_category(self.category_id)
