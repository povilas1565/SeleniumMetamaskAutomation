
## MetamaskAutomation
 Автоматизации действий расширения метамаски на сайтах криптосвапалок(криптообменников) с помощью веб-драйвера selenium.

#### Для установки:

```sh
pip install ./metamask_automation
```
или
```sh
pip install -i https://test.pypi.org/simple/ metamask-automation
```
Проверить, существует ли:
```sh
pip list
```

## Функции

#### 1. Скачать расширение:

```sh
metamask_automation.downloadMetamaskExtension()
```
Эта функция должна быть запущена один раз перед всеми функциями для загрузки расширения метамаски. Если вы измените каталог или создадите файл python в другом месте, его необходимо запустить первым, иначе будет выдано следующее исключение:

«Путь к расширению не существует».

#### 2. Запуск расширения:
```sh
metamask_automation.launchMetamaskExtension(args)
```
args: путь к веб-драйверу Chrome.

Эта функция возвращает значение, содержащее драйвер. Вы можете получить его как:
```sh
driver = launchSeleniumWebdriver(r‘C:\Drivers\chromedriver_win32\chromedriver.exe’)
```
Теперь при использовании можно вызывать любой метод selenium.

```sh
driver.get("https://google.com")
```
#### 3. Импорт кошелька:
```sh
metamask_automation.metamaskSetup(arg1, arg2)
```
arg1 : начальная фраза для кошелька
arg2: пароль от кошелька


#### 4. Смена сети метамаски:
```sh
metamask_automation.changeMetamaskNetwork(arg)
```
arg: название сети

Имена сетей указаны ниже. При выборе любой другой сети выдает ошибку.

- Ethereum Mainnet
- Ropsten Test Network
- Kovan Test Network
- Rinkeby Test Network
- Goerli Test Network

#### 5. Соединение с любым сайтом:
```sh
metamask_automation.connectToWebsite()
```

Чтобы воспользоваться этой функцией, вы должны сначала зайти на веб-сайт.
```sh
driver.get("https://google.com")
metamask_automation.connectToWebsite()
```

#### 6. Проведенение различных одобренных транзакций:

Подтверждение: 
```sh 
metamask_automation.confirmApprovalFromMetamask()
```

Отклонение: 
```sh 
metamask_automation.rejectApprovalFromMetamask()
```

#### 7. Проведение любых транзакций, кроме одобренных:

Подтверждение: 
```sh
metamask_automation.confirmTransactionFromMetamask()
```

Отклонение: 
```sh
metamask_automation.rejectTransactionFromMetamask()
```

#### 8. Добавление токена в свой кошелек:

```sh
metamask_automation.addToken(arg)
```
arg: контрактный адрес токена

#### 9. Знак:

Подтверждение знака: 
```sh
metamask_automation.signConfirm()
```
Отклонение знака: 
```sh
metamask_automation.signReject()
```

#### 10. Авторизация:

Подтверждение авторизации:
```sh
metamask_automation.signInConfirm()
```
Отклонение авторизации:
```sh
metamask_automation.signInReject()
```

#### 11. Регистрация:

Подтверждение регистрации:
```sh
metamask_automation.signOutConfirm()
```
Отклонение регистрации:
```sh
metamask_automation.signOutReject()
```


### Ошибки:

список pip показывает пакет, “metamask_automation”но ваша среда IDE не обнаруживает пакет

##### Решение:

Перейдите в настройки IDE -> Интерпретатор Python.

Измените путь на C://ProgramFiles//Python//python.exe или, в вашем случае, добавьте путь, по которому установлен python.exe.
