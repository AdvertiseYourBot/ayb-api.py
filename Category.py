class Category:
  def __init__(self, info):
    self.success = info['success']
    
    if (self.success):
      self.id = info['id']
      self.name = info['name']
      self.slug = info['slug']
    else:
      self.note = info['note']