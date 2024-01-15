Scenario: Проверка чек-бокса Word File
    Given Открыта стартовая страница сайта
    When Нажали на кнопку Element
    And В раскрытом справа меню кликнули ЛКМ на Check Box
    And Расскрыли директорию Home
    And Расскрыли директорию Downloads
    And Выбрали чекбос Word File.doc
    Then Появилось сообщение 'You have selected: wordFile'
