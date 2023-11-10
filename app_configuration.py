# app_configuration = {
#     'database_host': 'localhost',
#     'database_port': 3306,
#     'database_user': 'user',
#     'database_password': 'pass',
#     'database+name': 'sqlDB'
# }
#
# for key, value in app_configuration.items():
#     print('Key:', key)
#     print('Value', value)
#     print()
#
# Key: database_host
# Value localhost
#
# Key: database_port
# Value 3306
#
# Key: database_user
# Value user
#
# Key: database_password
# Value pass
#
# Key: database+name
# Value sqlDB

app_configuration = {
    'database_host': 'localhost',
    'database_port': 3306,
    'database_user': 'user',
    'database_password': 'pass',
    'database+name': 'sqlDB'
}

for key in app_configuration.values():
    print('Key:', key)

# Key: localhost
# Key: 3306
# Key: user
# Key: pass
# Key: sqlDB
