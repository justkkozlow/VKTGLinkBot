START_MESSAGE = """❤️Приветствую! Начнём с регистрации.\n
У вас есть ВИП код?\n
Для приобретения ВИП статуса, чтобы не выполнять задания, вы можете написать @xxxxx"""

AUTH_USER = """Воспользуйтесь меню"""

LINK_ENTER = ("➡️Пришлите адрес вашей личной страницы VK, с которой будете работать. \n"
              "Мы будем проверять выполнение вами заданий по этой странице.")

VIP_CODE_ENTER = "💎Введите ВИП код"
VIP_CODE_SUCESS = """✅Есть контакт! Срок действия кода - до {vip_code_end_date}\n
Теперь ваши ссылки будут сразу попадать в очередь к другим участникам. 
Вам не нужно самостоятельно выполнять задания."""

VK_PAGE_SUCESS = "✅Отлично! Теперь вы можете отправлять ссылки в чат"
VK_PAGE_ERROR = "⛔️Упс! Что-то пошло не так (Проверьте правильность ссылки)"

LINK_ERROR = """⛔️Упс! Что-то пошло не так(\n
Проверьте правильность ссылки"""

WRONG_FORMAT = "Не верный формат запроса"

WRONG_COMMAND = "Неизвестная комманда"

NO_VK_PAGE_IN_PROFILE = "Вы не привязали рабочую VK страницу"

VK_PAGE_ALREADY_EXSIST = "Страница {vk_page_url} уже привязана к Вашему профилю"

WRONG_URL_FORMAT = "Некорректный формат ссылки"

ONLY_ONE_LINK_TO_SEND = "Можно отправить только одну ссылку за раз"

WRONG_VIP_CODE = "Неверный ВИП код"

VIP_CODE_EXSISTS = "У Вас уже есть Вип код"

NO_CURRENT_TASK = "Нет заданий"
TASK_ACCEPTED_MANUALLY = "Задание принято!"

USER_TASK_NUMBER = "Задание № "

MEMBER_STATUS = """Страница VK: {url}
Статус: {status}
Telegram ID: {tg_id}"""

LINK_ADDED_FOR_NUMBER = """Ваша ссылка: {link} добавлена в очередь под № {number}"""
TASK_IS_NOT_COMPLETE = """Вы не завершили задание № {current_task}:\n{links}"""
LINK_COUNT_ERROR = """😢Не могу принять ссылку: {link}.\n
                     От вашей предыдущей должно пройти {count} чужих ссылок.\n
                     Осталось: {allow_links}"""
NO_TASKS_NOW = """Сейчас нет заданий\n\nВаша ссылка добавлена в очередь под № {number}"""

COMMENT_MISSING = "Отсутствует комментарий или его длина менее 5 слов"
LIKE_MISSING = "Отсутствует лайк"
SUBSCRIBE_MISSING = "Отсутсвтует подписка"
RESULT_MESSAGE = """
{value}
"""
