function updateCart() {
    fetch('/mycart/')
        .then(response => response.text())
        .then(html => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            const cartContainer = doc.querySelector('.cart-container');
            const mainCartContainer = document.querySelector('.cart-container');

            // Извлечение новых кнопок и удаление старых
            const oldButtons = mainCartContainer.querySelectorAll('.add-to-cart');
            oldButtons.forEach(button => {
                button.removeEventListener('click', updateCart);
            });

            mainCartContainer.innerHTML = ''; // очищаем контейнер
            mainCartContainer.innerHTML = cartContainer.innerHTML ; // добавляем новый контент

            // настройка обработчика событий на кнопке
            setupButton();
        });
}

function setupButton() {
    const buttons = document.querySelectorAll('.add-to-cart');
    buttons.forEach(button => {
        button.addEventListener('click', event => {
            const productId = button.getAttribute('data-product-id');
            const csrfToken = button.getAttribute('data-csrf-token');

            fetch(`/add-to-cart/${productId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({})
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        updateCart();
                    }
                });
        });
    });
}

// настройка обработчика событий при загрузке страницы
document.addEventListener('DOMContentLoaded', () => {
    setupButton();
});
