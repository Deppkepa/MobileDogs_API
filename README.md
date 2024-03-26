# MobileDogs_API
Цели проекта:
1. Цифровизовать наблюдение и заботу за бездомными собаками посредством разработки ошейника.
2. Помочь неравнодушным людям следить и заботиться за бездомными собаками. В качестве напоминалок сообщать пользователям, что нужно сделать с той или иной собакой. Также по картам отслеживать, где эти собаки находятся.

Прежде чем пользователь сможет пользоваться приложением ему нужно будет зарегистрироваться. После можно прикрепить конкретных собак, за которыми человек будет ухаживать. После пользователю будут приходить текстовые уведомления о состоянии собаки и что нужно сделать с ней (например, что её нужно покормить и т.д.). Также у пользователя будет система оценки пользователей (чтобы пользователи действительно следили за собаками, потому что в противном случае волонтёра снимут с программмы). Также будут профили собаки и пользователя. Обязательно должно присутствовать фото собаки, чтобы её можно было узнать.
Профиль ошейника собаки:
- статус ошейника (заряд ошейника, на месте ли ошейник, корректность работы ошейника)
- фото собаки
- id ошейника
- Кличка собаки
- Имя прикреплённого волонтёра
- Заметки по собаке(может, стоит быть осторожным при каких-то действиях, описание внешности, характера, особые опознавательные признаки, состояние здоровья (например после осмотра ветеринаром), вакцинация )
- статус собаки (время последнего приёма пищи, подвижность собаки, уровень кислорода в крови)
- задания для заботы о собаке
- местоположение собаки (точка на карте, если ошейник надет, иначе последнее известное местоположение)
Профиль пользователя:
- id пользователя
- фото пользователя
- от какой организации
- какие собаки закреплены
- когда был в последний раз в онлайне
- список задач для пользователя
- роль пользователя
- электронная почта
- имя
- пароль
  У пользователей будут роли по которым можно будет работать. Например, если волонтерская организация захотела поработать с этой системой, они могут зарагистрироваться и организовать группу с админами, которые будут назначать другим пользователем задания по тем или иным собакам. Пример: за группой можно закрепить список собак и админ будет отслеживать состояние этих собак, чтобы не осталась ни одна собака без присмотра.


Запросы: 

1. Регистрация пользователей:
- POST запрос на '/users/register' с данными пользователя (имя, электронная почта, пароль)
возвращает ID пользователя

2. Регистрация ошейников:
- POST запрос на '/collars/register' с данными ошейника (регистрационный номер, фото собаки, кличка собаки)
возвращает объект ошейника с уникальным ID

3. Привязка ошейников и пользователей:
- POST запрос на '/users/{user_id}/collars/{collar_id}/link' для привязки ошейника к пользователю с данными пользователя и ошейника (ID пользователя, ID ошейника)
возвращает ответ об успехе или неудаче

4. 
