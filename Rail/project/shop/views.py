from django.shortcuts import render

products = [
    {'id': 1, 'title': 'Худи', 'size': 'L', 'price': 1200, },
    {'id': 2, 'title': 'Майка', 'size': 'XL', 'price': 2222},
    {'id': 3, 'title': 'Футболка', 'size': 'XXL', 'price': 0},
    {'id': 4, 'title': 'Одежда', 'size': 'S', 'price': 666},
    {'id': 5, 'title': 'Кепарик', 'size': 'M', 'price': 500},
]


def productsView(request):
    return render(request, 'shop/products.html', context={'products': products})


def product(request, id):
    product = products[id-1]
    return render(request, 'shop/product.html', context={'product': product})


def index(request):
    header = 'Данные пользователя'
    langs = ['python', 'js', 'css', 'html', 'инопланетянский']
    user = {'name': 'Крутой', 'surname': 'Человек'}
    address = ('Groove Street', 3, 54)
    text = '<h4>текст</h4>'

    data = {'header': header, 'langs': langs, 'user': user, 'address': address, 'text': text}
    return render(request, 'shop/index.html', context=data)


def about(request):
    data = {'name': 'Me', 'interests': 'Sublime Text'}
    return render(request, 'shop/about.html', context=data)


def contacts(request):
    return render(request, 'shop/contacts.html')