### Тестовое задание отдел бэкенд Сарафан

#### 1. Напишите программу:
Которая выводит n первых элементов последовательности 122333444455555… (число повторяется столько раз, чему оно равно).

#### 2. Реализовать Django проект магазина продуктов со следующим функционалом:

- [x] Должна быть реализована возможность создания, редактирования, удаления категорий и подкатегорий товаров в админке.
- [x] Категории и подкатегории обязательно должны иметь наименование, slug-имя, изображение
- [x] Подкатегории должны быть связаны с родительской категорией
- [ ] Должен быть реализован эндпоинт для просмотра всех категорий с подкатегориями. Должны быть предусмотрена пагинация.
- [x] Должна быть реализована возможность добавления, изменения, удаления продуктов в админке.
- [ ] Продукты должны:
  - [x] относится к определенной подкатегории
  - [x] соответственно категории, 
  - [x] должны иметь наименование, 
  - [x] slug-имя, 
  - [ ] изображение в 3-х размерах, 
  - [x] цену
- [ ] Должен быть реализован эндпоинт вывода продуктов с пагинацией. Каждый продукт в выводе должен иметь поля: наименование, slug, категория, подкатегория, цена, список изображений
- [ ] Реализовать эндпоинт добавления, изменения (изменение количества), удаления продукта в корзине.
- [ ] Реализовать эндпоинт вывода состава корзины с подсчетом количества товаров и суммы стоимости товаров в корзине.
- [ ] Реализовать возможность полной очистки корзины
- [ ] Операции по эндпоинтам категорий и продуктов может осуществлять любой пользователь
- [ ] Операции по эндпоинтам корзины может осуществлять только авторизированный пользователь и только со своей корзиной
- [ ] Реализовать авторизацию по токену

Тестовое задание сдается ссылкой на свой репозиторий.
