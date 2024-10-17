from django.shortcuts import render, redirect, get_object_or_404
import os  # Убедитесь, что этот импорт добавлен
from . import util
from .models import Entry


def index(request):
    entries = util.list_entries()
    entries.sort()  # Сортируем записи по алфавиту

    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })


def entry(request, title):
    entry_content = util.get_entry(title)
    if entry_content is None:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": entry_content
    })


def create_entry(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        # Сохраните статью, например, в файле или базе данных
        util.save_entry(title, content)  # вам нужно реализовать эту функцию в util.py
        return redirect("index")
    return render(request, "encyclopedia/create_entry.html")


def delete_entry(request, title):
    # Проверяем, существует ли запись
    entry_path = os.path.join('entries', f"{title}.md")

    if request.method == 'POST':
        # Удаляем файл, если он существует
        if os.path.exists(entry_path):
            os.remove(entry_path)
            return redirect("index")  # Перенаправляем на главную страницу после удаления
        else:
            return render(request, 'encyclopedia/error.html', {
                "title": title,
                "message": "Запись не найдена."
            })

    # Если метод не POST, просто отображаем страницу удаления
    return render(request, 'encyclopedia/delete.html', {'title': title})
