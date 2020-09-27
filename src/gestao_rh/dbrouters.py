'''
Este caso nao sera usado devido uma limitacao de relacionamentos
ao lidar com multiplas databases

Limitations of multiple databases¶
Cross-database relations¶
Django doesn’t currently provide any support for foreign key or
many-to-many relationships spanning multiple databases.
If you have used a router to partition models to different databases,
any foreign key and many-to-many relationships defined by those models
must be internal to a single database.

https://docs.djangoproject.com/en/3.1/topics/db/multi-db/
'''


class EmployeesDBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'employees':
            return 'employeesdb'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'employees':
            return 'employeesdb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'employees' or obj2._meta.app_label == 'employees':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'employees':
            return db == 'employeesdb'
        return None
