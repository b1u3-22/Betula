![Betula](assets/readme_banner.png)

:czech_republic: Českou verzi popisu naleznete [zde](README.cz.md)

**Open source, modern and accesible system for housing associations**

[Overview](#overview--) • [Features](#features--) • [Installation](#installation--) • [Demo](#demo--) • [Screenshots](#screenshots--)

## Overview :book:
Betula is a system for housing associations, creating a place to share information with it's members and display basic information about the particular association.

## Features :dizzy:
### Main page
You can display contacts and short description of your house. It also allows you to include small 3-image scrolling gallery

### Gallery
The full-blown gallery displaying all your pictures with information about it

### Dashboard
The heart of the system and also the first page where only the members of the assosiaction can get to. It shows them the financial status, info about current debts and of course post the admin has shared

### Settings
You can change practicaly anything from here:
* Main page
    * Emails
    * Phones
    * Background image
    * Description 
    * Gallery images
* Gallery 
    * Images
    * Info about images
* Dashboard
    * Current state of bank account
    * Add or remove debts
    * Manage users
        * Add or remove user
        * Their password 
        * Email
        * Permissions

## Installation :cd:
Betula can be installed using **Docker** :whale2: using one of the automatically built images
*(Please note that if you choose image with the **latest** tag, it includes breaking changes. Therefore it is recommended to use images with **stable** tag)*

### Installation using `docker-compsose`
```
version: "3.4"
services:
  betula:
    image: ghcr.io/b1u3-22/betula:stable
    container_name: betula
    ports:
      - 80:80
    volumes:
      betula_config:/config
      betula_images:/images
    restart: unless-stopped
```

## Demo :house:
*TO BE ADDED*

## Screenshots :framed_picture:
*TO BE ADDED*