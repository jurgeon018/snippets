cd /home/jurgeon/dev/margo/src

python3 manage.py shell -c "from django.contrib.auth import get_user_model; User=get_user_model(); User.objects.create_superuser('admin1', 'admin@gmail.com', 'admin')"



cd /home/jurgeon/dev/snippets/vps/
