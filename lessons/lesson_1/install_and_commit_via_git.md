# Установка git и коммиты в репозиторий

### 1. Регистрируем аккаунт на github.com. У вас теперь есть email, логин и пароль от него.
  2.1 `sudo apt-get install git` # Установили клиент git на своем linux.
  # В удобной для вас дирректории
  2.2 `git clone https://github.com/g10k/sw_lessons.git` # Создастся папка sw_lessons
  2.3 `cd sw_lessons/homeworks # Перешли в папку sw_lessons/homeworks`
  2.4 # Создаем свою папку и файл приветствия
  2.5  `mkdir glok-sw; cd glok-sw; mkdir lesson_1; cd lesson_1`
  2.6 `touch hello_world`
  2.7 `echo 'Hello from user' > hello_world` # Записали текст "Hello from user"
  2.8 # Для дальнейших действий вы должны быть добавлены в "Соавторы" в проекте github (для этого ставите звездочку и я вас добавляю)
  2.9 `git add hello_world`
  2.10 `git commit hello_world -m 'comment from user'` # Комментарий для вашего коммита
  2.11 `git config --global user.email "ваш email_при регистрации на github"`
  2.20 `git push origin` # Отправляем изменения на сервер, нужно будет ввести ник и пароль, в конце должно быть `Ok`
  # Чтобы не вводить каждый раз ник и пароль их можно [добавить в конфиг git](https://git-scm.com/book/ru/v1/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%9F%D0%B5%D1%80%D0%B2%D0%BE%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-Git)
  # Правильным способом авторизации является [авторизация через ssh-ключ](https://help.github.com/articles/generating-an-ssh-key/)
