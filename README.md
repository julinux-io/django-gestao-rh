# Django Gestao RH


![CI](https://github.com/vespene/django-gestao-rh/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/juliosaraiva/django-gestao-rh/branch/master/graph/badge.svg)](https://codecov.io/gh/juliosaraiva/django-gestao-rh)
[![Updates](https://pyup.io/repos/github/juliosaraiva/django-gestao-rh/shield.svg)](https://pyup.io/repos/github/juliosaraiva/django-gestao-rh/)


# Setup
The script `compose.sh` there is everything that needs to run successfully this project. It accept a parameter `down` if you would like to destroy all services.

Up all services
```sh
$ ./compose.sh
```

Down all services
```sh
$ ./compose down
```


Run collectstatic

```
$ docker-compose exec app_gestao pipenv run python manage.py collectstatic
```
