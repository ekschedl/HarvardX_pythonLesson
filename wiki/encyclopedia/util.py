import os
import markdown

def list_entries():
    entries = []
    entries_dir = "entries"  # Папка с записями

    # Получаем список файлов в папке entries
    for filename in os.listdir(entries_dir):
        if filename.endswith(".md"):  # Убедись, что только markdown файлы
            entries.append(filename[:-3])  # Убираем .md

    return entries





def get_entry(title):
    """Возвращает содержимое записи с заданным заголовком, если она существует."""
    # Определяем путь к файлам записей
    entries_path = os.path.join('entries', f"{title}.md")

    if os.path.isfile(entries_path):
        with open(entries_path, 'r') as file:
            return markdown.markdown(file.read())
    else:
        return None  # Если файл не найден, возвращаем None



def save_entry(title, content):
    # Создайте директорию, если она не существует
    if not os.path.exists('entries'):
        os.makedirs('entries')
    # Сохраните контент в файл
    with open(f"entries/{title}.md", "w") as f:
        f.write(content)
