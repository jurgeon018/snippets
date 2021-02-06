git init
git log
touch app.py
git status
git add filename
git show
git show 2008566b8834a201286221e874348626d3bf6796
git log -p
git restore app.py # восстанавливает содержание файла до последнего коммита, Отменяет изменения которые были внесены в файл который еще не попал в индекс
git restore --stages app.py # восстанавливает содержание файла до последнего коммита, Отменяет изменения которые были внесены в файл который уже попал в индекс
git diff # показывает какие изменения были внесены в файл с момента последнего коммита, но еще не попали в индекс
git diff --stage # выведет изменения которые находятся в индексе
git commit -am 'message' # выполняет git add . под капоток
git mv app.py application.py
git rm app.py # удаляет из индекса и из файловой системы
git rm --cached app.py # удаляет из индекса 





untracked <- touch app.py
staged <- git add app.oy
commited <- git commit -m 'm'
modified <- change something in file app.py
staged <- git add app.py
commited <- git commit -m 'm'


Указатели.
У каждой ветки есть свой указатель, а также есть указатель-метка HEAD.git 
Каждый следующий коммит ссылается на предыдущий.
В качестве ссылки выступает хэш-сумма коммита.
Зная какой коммит был последний, можно отследить все предыдущие коммиты до самого первого.
Как быстро узнать какой коммит последний, без просчета всех ссылок?
Для этого в гите есть метка HEAD, которая указывает на какой-то коммит.
После каждого комита эта метка перемещается со старого коммита на новый.



git branch -d branch_name - удалить ветку
git merge master branch_name - слить ветку в мастер.
fast-forward commit - если branch_name является прямым продолжением коммита, на котором стоит HEAD, и в который нужно сделать мерж.

git merge master branch_name - слить ветку в мастер. 
merge commit - Если нельзя просто так передвинуть указатель ветки мастер, то единственный способ - создать третий коммит,
который будет ссылаться на два других коммита, на который указывали ветки master и branch_name

git fetch origin - обновляет укаатели веток слежения, но локальные указатели веток не изменятся
git merge origin master

git pull origin master == git fetch origin + git merge origin master

Если сервер, получив ваши правки, может просто передвинуть указатель ветки вперед, на ваш новый коммит,
то он примет их, и сделает при этом fast-forward.
Если требуется mrege - сервер отклонит ваши правки.


git push origin master 
git push --set-upstream origin master
git push
