from django.core.management.base import BaseCommand
from menu.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Удаляем старые данные
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаём категории
        pizza = Category.objects.create(name="Пицца")
        drinks = Category.objects.create(name="Напитки")
        desserts = Category.objects.create(name="Десерты")

        # Пиццы
        Product.objects.create(
            category=pizza,
            name="Маргарита",
            description="Классическая пицца с томатным соусом, сыром моцарелла и базиликом.",
            price=350,
            diameter=30,
            weight=520,
            calories=890,
            image="products/margarita.webp"
        )
        Product.objects.create(
            category=pizza,
            name="Пепперони",
            description="Пикантная пепперони, сыр моцарелла и томатный соус.",
            price=380,
            diameter=30,
            weight=560,
            calories=1020,
            image="products/pepperoni.webp"
        )
        Product.objects.create(
            category=pizza,
            name="Гавайская",
            description="Ветчина, ананас, сыр моцарелла и томатный соус.",
            price=370,
            diameter=30,
            weight=550,
            calories=960,
            image="products/hawaiian.webp"
        )
        Product.objects.create(
            category=pizza,
            name="Четыре сыра",
            description="Пицца с моцареллой, горгонзолой, пармезаном и чеддером.",
            price=380,
            diameter=30,
            weight=590,
            calories=1100,
            image="products/4cheese.webp"
        )
        Product.objects.create(
            category=pizza,
            name="Барбекю",
            description="Курица BBQ, бекон, лук, соус BBQ и сыр моцарелла.",
            price=420,
            diameter=30,
            weight=610,
            calories=1000,
            image="products/bbq.webp"
        )
        Product.objects.create(
            category=pizza,
            name="Вегетарианская",
            description="Томаты, шампиньоны, болгарский перец, маслины и моцарелла.",
            price=380,
            diameter=30,
            weight=500,
            calories=800,
            image="products/vege.webp"
        )
        Product.objects.create(
            category=pizza,
            name="Пикантэ",
            description="Горчичный соус, сыр моцарелла, бекон, копченое куриное филе, сыр дорблю.",
            price=320,
            diameter=30,
            weight=450,
            calories=700,
            image="products/pikante.webp"
        )
        Product.objects.create(
            category=pizza,
            name="Американо",
            description="Соус барбекю, сыр моцарелла, помидоры, охотничьи колбаски, пепперони, картофель фри, петрушка.",
            price=350,
            diameter=30,
            weight=580,
            calories=1000,
            image="products/amerikano.webp"
        )

        # Напитки
        Product.objects.create(
            category=drinks,
            name="Кола",
            description="Газированный напиток Coca-Cola.",
            price=50,
            weight=500,
            calories=250,
            image="products/cola.jfif"
        )
        Product.objects.create(
            category=drinks,
            name="Апельсиновый сок",
            description="Свежевыжатый апельсиновый сок.",
            price=120,
            weight=950,
            calories=150,
            image="products/orange_juice.webp"
        )
        Product.objects.create(
            category=drinks,
            name="Яблочный сок",
            description="Свежевыжатый яблочный сок.",
            price=120,
            weight=950,
            calories=150,
            image="products/apple_juice.webp"
        )
        Product.objects.create(
            category=drinks,
            name="Томатный сок",
            description="Томатный сок.",
            price=120,
            weight=950,
            calories=150,
            image="products/tomato_juice.webp"
        )
        Product.objects.create(
            category=drinks,
            name="Вода без газа",
            description="Чистая питьевая вода без газа.",
            price=40,
            weight=520,
            calories=10,
            image="products/water.webp"
        )
        Product.objects.create(
            category=drinks,
            name="Лимонад",
            description="Мята, сироп, содовая, лимон.",
            price=180,
            weight=520,
            calories=100,
            image="products/limonade.webp"
        )

        # Десерты
        Product.objects.create(
            category=desserts,
            name="Шоколадный маффин",
            description="Маффин с шоколадным вкусом, приготовленный на основе какао-порошка, с насыщенным ароматом и нежной текстурой.",
            price=50,
            weight=80,
            calories=200,
            image="products/muffin.webp"
        )
        Product.objects.create(
            category=desserts,
            name="Шоколадный пончик",
            description="Пончик с шоколадной начинкой, покрыт какао-глазурью и посыпкой. Внутри — нежная сладкая какао-начинка.",
            price=50,
            weight=70,
            calories=250,
            image="products/chocolate_donut.webp"
        )
        Product.objects.create(
            category=desserts,
            name="Малиновый пончик",
            description="Пончик с малиновой начинкой (малина + сыр Philadelphia, 18%), покрыт розовой глазурью и украшен лиофилизированной малиной. Лёгкое и воздушное тесто по специальному рецепту.",
            price=50,
            weight=70,
            calories=250,
            image="products/raspberry_donut.webp"
        )

        self.stdout.write(self.style.SUCCESS("База успешно наполнена тестовыми данными!"))
