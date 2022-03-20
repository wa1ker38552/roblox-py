import requests

def format_response(response):
  data = response[1:response.index('inventory')]
  data = data.split(',')
  value = data[3].split(':')[1]
  rap = data[4].split(':')[1]
  response = response[:-1][response.index('inventory')+9:][3:]
  item_data = []
  items = []
  for i in range(len(response)):
    if response[i] == '{': charset = i
    if response[i] == '}': item_data.append(response[charset:i+1])
  for i in range(len(item_data)): 
    item_data[i] = item_data[i].split(',')
    for j in range(len(item_data[i])):
      item_data[i][j] = item_data[i][j].replace('"','').replace('{','')
  for asset in item_data: items.append(asset[3].split(':')[1])
  return [items, value, rap]

def time_format(time):
  time = time.split('T')
  time[1] = time[1].split('.')
  return time[0]+' '+''.join(time[1][0])

def parse(response, start, pointer):
  x = response.index(start)+len(start)
  while response[x] != pointer: x += 1
  return response[response.index(start)+len(start):x]

def inverse_parse(response, start, pointer):
  x = response.index(start)
  while response[x] != pointer: x -= 1
  return response[x+1:response.index(start)]

class roblox():
  class player():
    def __init__(self, username):
      self.API_links = {}
      self.username = username
      response_object = requests.get('https://rblx.trade/u/'+self.username).text # rbxtrade parse
      self.id = parse(response_object, 'https://www.roblox.com/users/', '/')
      self.terminated = bool(parse(response_object, 'isDeleted":', ',') in ['true'])
      self.private = bool(parse(response_object, 'isPrivate":', ',') in ['true'])
  
      response_object = requests.get('https://rblx.trade/api/v2/users/'+self.id+'/profile/header').text # rblxtrade API (playerinfo)
      self.previous_usernames = list(parse(response_object, '"previousUsernames":[', ']'))
      response_object = requests.get('https://rblx.trade/api/v2/users/'+self.id+'/last-online').text # rblxtrade API (lastonline)
      self.is_online = bool(parse(response_object, '"isOnline":', ',') in ['true'])
      self.last_online = time_format(parse(response_object, '"lastOnline":"', '"'))
      response_object = requests.get('https://rblx.trade/api/v2/users/'+self.id+'/inventory?allowRefresh=false').text # rblxtrade API (inventory)
      formatted = format_response(response_object)
      self.inventory = formatted[0]
      self.value = formatted[1]
      
      response_object = requests.get('https://rolimons.com/player/'+self.id).text # rolimons parse
      self.collectibles = inverse_parse(response_object,'],"terminated":',',')
      self.rap = inverse_parse(response_object, '],"num_limiteds":', ',')
      
      response_object = requests.get('https://www.roblox.com/users/'+self.id).text # roblox parse
      self.friends = parse(response_object, 'data-friendscount="', '"')
      self.followers = parse(response_object, 'data-followerscount="', '"')
      self.following = parse(response_object, 'data-followingscount="', '"')
      self.displayname = parse(response_object, 'class="profile-name text-overflow">', '<').replace(' ', '').replace('\n', '')
      self.description  = parse(response_object, 'Join pokemongo2537 on Roblox and explore together!', '"')
      
      self.chat_disabled = bool(parse(response_object, 'data-ischatdisabledbyprivacysetting="', '"') in ['true'])
      self.display_enabled = bool(parse(response_object, '"roblox-display-names" data-enabled="', '"') in ['true'])
      self.message_disabled = bool(parse(response_object, 'data-messagesdisabled="', '"') in ['true'])
  
      self.API_links['profileicon'] = parse(response_object, 'name=twitter:image1 content="', '"')
      self.API_links['friends'] = parse(response_object, 'data-friendurl="', '"')
      self.API_links['message'] = parse(response_object, 'data-messageurl="', '"')
