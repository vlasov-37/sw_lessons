# Установка git и коммиты в репозиторий

# Регистрируем аккаунт на github.com. У вас теперь есть email, логин и пароль от него.

1. `sudo apt-get install git` # Установили клиент git на своем linux.
В удобной для вас дирректории
1. `git clone https://github.com/g10k/sw_lessons.git` # Создастся папка sw_lessons
1. `cd sw_lessons/homeworks # Перешли в папку sw_lessons/homeworks`
1.  `mkdir glok-sw; cd glok-sw; mkdir lesson_1; cd lesson_1` # Создаем свою папку и файл приветствия g10k-sw - заменить на название вашей папки
1. `touch hello_world`
1. `echo 'Hello from user' > hello_world` # Записали текст "Hello from user"

Для дальнейших действий вы должны быть добавлены в "Соавторы" в проекте github (для этого ставите звездочку и я вас добавляю)

1. `git branch <ваш ник>` # создаем ветку для себя
1. `git checkout <ваш ник>` # переходим в ветку, из которой будем теперь работать  
1. `git add hello_world` # взяли под контроль версий.
1. `git commit hello_world -m 'comment from user'` # добавили в индекс с комментарием для вашего коммита
1. `git config --global user.email "ваш email_при регистрации на github"` # для авторизации
1. `git push origin <ваш ник>` # Отправляем изменения на сервер, нужно будет ввести ник и пароль, в конце должно быть `Ok`

Чтобы не вводить каждый раз ник и пароль их можно [добавить в конфиг git](https://git-scm.com/book/ru/v1/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%9F%D0%B5%D1%80%D0%B2%D0%BE%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-Git)
Правильным способом авторизации является [авторизация через ssh-ключ](https://help.github.com/articles/generating-an-ssh-key/)
