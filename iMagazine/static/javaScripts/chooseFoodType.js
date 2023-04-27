(function () {
    // Получаем все кнопки типов продуктов
    const typeBtns = document.querySelectorAll('.food-type');


    // Получаем все карточки продуктов
    const productCards = document.querySelectorAll('.product-card');

    // Назначаем обработчик события для каждой кнопки
    typeBtns.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            // Получаем тип продукта, который соответствует нажатой кнопке
            const typeId = e.target.dataset.type;
        

            // Перебираем все карточки продуктов
            productCards.forEach((card) => {
                // Получаем тип продукта, которому соответствует текущая карточка
                const cardTypeId = card.dataset.type;
          

                // Если типы продуктов совпадают, то отображаем карточку, иначе скрываем
                if (typeId === cardTypeId) {
                    card.style.display = 'flex'
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
})();
