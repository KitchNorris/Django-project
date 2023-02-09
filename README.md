Данный проект представляет собой сайт для блога и включает в себя следующую реализацию backend части:
1. Регистрация новых пользователей и вход существующих.
2. Возможность авторизованным пользователям создавать темы и посты. Пост имеет заголовок и текст поста.
3. Просматривать список пользователей с возможностью сортировки по количеству постов.
4. Просматривать список постов других пользователей, отсортированный по дате
создания, сначала свежие.
5. Авторизованным пользователям подписываться и отписываться на посты других
пользователей.
6. Авторизованным пользователям формировать ленту из постов пользователей, на
которые была осуществлена подписка. В ленту попадают новые посты
пользователей после выполнения подписки. Сортировка по дате создания поста,
сначала свежие. Список постов отдается страницами по 5 шт.
7. Авторизованным пользователям помечать посты в ленте как прочитанные и
выполнять фильтрацию постов по данному признаку.
8. Администратору управлять пользователями и контентом средствами Django admin.

Также на базе проекта сформировано REST API, позволяющее получить список пользователей и постов, 
и покрытие unit-тестами представлений, форм и моделей.
