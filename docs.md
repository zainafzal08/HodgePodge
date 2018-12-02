# Hodge Podge API

The memory banks of our dear sweet boy.

## Application Endpoints

### User

`GET /user/:discordId` Gets the information for a user

```
{
  id: String,
  nickname: String,
  discord_id: String,
  oauth_token: String
}
```

`POST /user/:discordId` Make a new user!


`PUT /user/:discordId` update a user!

```
{
  oauth_token: String,
  nickname: String
}
```

### Server

`PUT /server/:serverId/memes` add a new meme to a server

```
{
  trigger: String,
  response: String
}
```

### Shop - requires users to have money / xp / other details!

`POST /server/:serverId/shop/:shop` add a new shop

`PUT /server/:serverId/shop/:shop` add a new item to a shop

`GET /server/:serverId/shop/:shop` get list of items in the shop

`DELETE /server/:serverId/shop/:shop` buy item from shop
