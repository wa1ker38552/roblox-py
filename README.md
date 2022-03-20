# Roblox PY

A module made for fetching player data and statistics over multiple sources used for finding Roblox player data.

**Features:**
<br/>
Below is a quick list of all functions currently in Roblox PY.
<br/><br/>
```foo = roblox.player('bar')```<br/><br/>
```foo.API_links```<br/>
```foo.username```<br/>
```foo.id```<br/>
```foo.terminated```<br/>
```foo.private```<br/>
```foo.previous_usernames```<br/>
```foo.is_online```<br/>
```foo.last_online```<br/>
```foo.inventory```<br/>
```foo.value```<br/>
```foo.rap```<br/>
```foo.collectibles```<br/>
```foo.friends```<br/>
```foo.followers```<br/>
```foo.following```<br/>
```foo.displayname```<br/>
```foo.description```<br/>
```foo.chat_disabled```<br/>
```foo.display_enabled```<br/>
```foo.message_disabled```<br/>
<br/>
**API_links:**
<br/>
```foo.API_links``` returns API links used by Roblox such as message and friends. ```foo.API_links``` returns a dictionary for keys and values of API links. <br/>
- ```foo.API_links['profileicon']``` returns the link of the profile picture icon of the user
- ```foo.API_links['friends']``` returns the friends link of the user
- ```foo.API_links['message']``` returns the message linik of the user
<br/><br/>
**Returns List:**
<br/>
The following functions returns lists when called:
<br/>
- ```foo.previous_usernames```
- ```foo.inventory```
<br/>
The username and inventory functions return ```[]``` if nothing is returned. If the inventory is private, there might be an index error.
<br/><br/>
**Returns True/False:**
<br/>
The following funtions return a bool when called:
- ```foo.terminated``` checks termination
- ```foo.private``` checks for private inventory
- ```foo.is_online``` checks if online
- ```foo.chat_disabled``` checks for enabled chat
- ```foo.display_enabled``` checks for enabled display name
- ```foo.message_disabled``` checks for messaging enabled
<br/><br/>
**Returns String:**
The following functions return string when called:
- ```foo.username``` returns player username
- ```foo.id``` returns player ID
- ```foo.last_online``` returns time in date time format
- ```foo.value``` returns player value (Rolimons)
- ```foo.rap``` returns player RAP
- ```foo.collectibles``` returns number of limiteds owned
- ```foo.friends``` returns amount of friends
- ```foo.followers``` returns amount of followers
- ```foo.following``` returns amount of players following
- ```foo.display_name``` returns player displayname (if enabled)
- ```foo.description``` returns player description
<br/><br/>
**Information:**
  <br/>
  Information parsed by Roblox PY is from the following sources:
  - rblxTrade (https://rblx.trade/docs/index.html)
  - rolimons (https://rolimons.com)
  - roblox (https://roblox.com)
  <br/>
 
