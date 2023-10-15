I used pipenv for this project. If you have trouble running project use pipenv shell, pipenv install django and pipenv install mysqlclient commands.



admin/
api/
api-auth/
restaurant/booking/tables
auth/ ^users/$ [name='user-list']
auth/ ^users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
auth/ ^users/activation/$ [name='user-activation']
auth/ ^users/activation\.(?P<format>[a-z0-9]+)/?$ [name='user-activation']
auth/ ^users/me/$ [name='user-me']
auth/ ^users/me\.(?P<format>[a-z0-9]+)/?$ [name='user-me']
auth/ ^users/resend_activation/$ [name='user-resend-activation']
auth/ ^users/resend_activation\.(?P<format>[a-z0-9]+)/?$ [name='user-resend-activation']
auth/ ^users/reset_password/$ [name='user-reset-password']
auth/ ^users/reset_password\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password']
auth/ ^users/reset_password_confirm/$ [name='user-reset-password-confirm']
auth/ ^users/reset_password_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password-confirm']
auth/ ^users/reset_username/$ [name='user-reset-username']
auth/ ^users/reset_username\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username']
auth/ ^users/reset_username_confirm/$ [name='user-reset-username-confirm']
auth/ ^users/reset_username_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username-confirm']
auth/ ^users/set_password/$ [name='user-set-password']
auth/ ^users/set_password\.(?P<format>[a-z0-9]+)/?$ [name='user-set-password']
auth/ ^users/set_username/$ [name='user-set-username']
auth/ ^users/set_username\.(?P<format>[a-z0-9]+)/?$ [name='user-set-username']
auth/ ^users/(?P<username>[^/.]+)/$ [name='user-detail']
auth/ ^users/(?P<username>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']
auth/ ^$ [name='api-root']
auth/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
auth/ ^token/login/?$ [name='login']
auth/ ^token/logout/?$ [name='logout']
api/ booking/
api/ users/
api/ menu-items/
api/ menu-items/<int:pk>
api/ animegirls
api/ api-token-auth/
