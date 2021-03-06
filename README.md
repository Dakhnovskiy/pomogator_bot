# pomogator_bot
Personal assistant for telegramm

Найти бота можно так: @pomogator_personal_assistant_bot

## Возможности:
* **[/погода|/weather] [населенный пункт] [количество дней]**
            
    Получить информацию о погоде в конкретном населённом пункте за период до пяти дней
    
    Если не указан параметр количество дней, то информация предоставляется за 1 день
    
    Если указан параметр количество дней, то информация предоставляется за каждый день в разрезе трёх часов 
    
    Если не указан параметр населенный пункт, то информация предоставляется по населённым пункту из последнего запроса, если запроса с указанием населенного пункта не было, то предоставляется информация о погоде в городе Москва

    Для получения данных о прогнозе погоды использует [этот](https://github.com/Dakhnovskiy/weather_forecast_service) сервис


* **[/вики|/wiki] [строка поиска]**

    Ищет по параметру строка поиска данные в [википедии](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0) и возвращает первый результат и ссылку на статью

    Для поиска использует [MediaWiki action API](https://www.mediawiki.org/wiki/API:Main_page/ru)


* **[/заметки|/notes]**
            
    Управление заметками(Создание, удаление, просмотр). 
    
    Возвращает InlineKeyboard интерфейс для управления заметками   

    Для управления зяметками использует [этот](https://github.com/Dakhnovskiy/notes_service) сервис


* **[/перевод|/translate]**
            
    Перевод текстов 
    
    Возвращает InlineKeyboard интерфейс для конфигурации перевода

    Для перевода использует [API переводчика](https://tech.yandex.ru/translate/) от yandex



## Задачи:

* Напоминалки
* Сводка новостей(общие/по тематике)
* Курсы валют
* Список покупок:
    * Добавить, вычеркунуть, групповой список
* Отложенные посты в соцсети
* Интеграция с почтой

