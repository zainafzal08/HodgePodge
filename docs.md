# Hodge Podge API

The memory banks of our dear sweet boy.

## Application Endpoints

### User

`GET /user/:discord_id` Gets the information for a user

```
{
  id: String,
  nickname: String,
  discord_id: String,
  oauth_token: String
}
```

`POST /user/:discord_id` Make a new user! params are optional


`PUT /user/:discord_id` update a user!

```
{
  oauth_token: String,
  nickname: String
}
```

### Server

`PUT /server/:server_id/memes` add a new meme to a server

```
{
  trigger: String,
  response: String
}
```
