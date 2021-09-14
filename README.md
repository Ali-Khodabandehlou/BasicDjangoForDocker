# BasicDjangoForDocker

This repo is a simple config to install and run django alongside nginx, postgresql, and gunicorn on Development and Production stages for your project.

Since I used a profilemanager app in all my projects, I've also added the simples version of that app for your use.

I have follwed this tutorial to setup my containers:
[https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)

I also suggest you follow their other tutorial on improving your security on production.

## Installation

This repo contains images for both **Development** and **Production** stages.

### Development
The deveopment stage is more simple and the size of the image is if no importance. To run the containers do the following:
```
cd BasicDjangoForDocker/
docker-compose up -d --build
```

After successful build, you can use this command to create a superuser with it's profile:
```
docker-compose exec web python manage.py initiate_admin
```

### Production

The production stage has a more complicated structure. You have to configure settings for **Nginx**, **postgresql**, and **userprofile** in order to enhance your security.

To run the containers:
```
cd BasicDjangoForDocker/
docker-compose -f docker-compose.prod.yml up -d --build
```

After successful build, you can use this command to create a superuser with it's profile:
```
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
docker-compose -f docker-compose.prod.yml exec web python manage.py collect static
docker-compose -f docker-compose.prod.yml exec web python manage.py initiate_admin
```

You can also do *makemigrations* command if you didn't made them in development or you've mistakenly deleted them.

## Change the defaults

I have created a simple environment for both **Dev** and **Prod** stages. I recommend you research for better configurations for both your users' and your own secrity and safety.

To change the default username and password, check the file: **./app/applications/profilemanager/management/commands/initiate_admin.py**

To change the defaults for postgresql config check **.env files** and also the **docker-compose files**

You should also check for directories if you're intended to change the project name. An important file would be: **./nginx/nginx.conf**

##

I hope ypu enjoy using the docker image.

I'd be happy to hear bug reports and your suggestions.

*Live long and prosper*
