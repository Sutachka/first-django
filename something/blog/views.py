from django.shortcuts import render


def home(request):
    posts = [
        {
            'id': 1,
            'title': 'Мой первый пост о космосе',
            'description': 'Небольшая статья о космосе и создании анимации.'
        },
        {
            'id': 2,
            'title': 'Как я изучаю Django',
            'description': 'Первые шаги в создании веб-приложения.'
        }
    ]

    return render(request, 'blog/home.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html')


def post_detail(request, post_id):
    return render(
        request,
        'blog/post_detail.html',
        {'post_id': post_id}
    )