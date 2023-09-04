# class MyRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'app':
#             return 'second_db'
#         return 'default'

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'dev':
#             return 'dusnei_dev'
#         return 'default'
