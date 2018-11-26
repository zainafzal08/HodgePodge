# Hodge Podge API

### The Problem

Ok so Hodge podge is a discord bot, why does he need a web facing api? Long story short when i tried to set up a persistant user state so hodge podge could remember who you are and what permissions you had, i realised that i would need a couple things.

1. A way to manage user state easily
2. A way for server admins to manage their members permissions
3. A way to seperate the database logic from the text processing and feature logic

The solution was to build an api that acted as hodge podges memory banks. This allows the actual main code to focus on reacting to user input in a meaningul way and all annoying user state management can be handled by the API. In addition the API allows for manipulation of the database by admins and super admins through a website.

Note this is a interesting digretion from the original idea to make hodge podges core computation a api and allow him to talk anywhere. The issue with this is not all text messaging platforms support all features and each one has such different API's that the amount of work it takes to usher each app into a uniform API is equivalent to just building up the whole text processing again.

The API has a definite user state you can't meddle with. Only you can link multiple instances of yourself on multiple apps. (this comes much later and isn't a issue but nice to know we have flexibility)

### API
