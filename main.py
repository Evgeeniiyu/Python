from sqlalchemy.orm import sessionmaker
from models import create_database, Author, Category, Games

# Создание сессии
engine = create_database()
Session = sessionmaker(bind=engine)
session = Session()

# Функции работы с данными
def insert_author(name):
    author = Author(name=name)
    session.add(author)
    session.commit()
    return author

def insert_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()
    return category

def insert_games(title, author_id, category_id):
    book = Games(title=title, author_id=author_id, category_id=category_id)
    session.add(book)
    session.commit()
    return book

def get_author_by_id(author_id):
    return session.query(Author).filter_by(id=author_id).first()

def get_all_games():
    return session.query(Games).all()

def update_games(games_id, title=None, author_id=None, category_id=None):
    book = session.query(Games).filter_by(id=games_id).first()
    if not games:
        return None
    if title:
        games.title = title
    if author_id:
        games.author_id = author_id
    if category_id:
        games.category_id = category_id
    session.commit()
    return games

def delete_author(author_id):
    author = session.query(Author).filter_by(id=author_id).first()
    if author:
        session.delete(author)
        session.commit()

def delete_book(games_id):
    games = session.query(Games).filter_by(id=games_id).first()
    if games:
        session.delete(games)
        session.commit()

# Примеры использования
if __name__ == '__main__':
    # Добавление данных
    author1 = insert_author("Alexey Pajitnov")
    category1 = insert_category("Puzzle")
    games1 = insert_book("1984", author1.id, category1.id)

    # Получение данных
    print(f"Author by ID: {get_author_by_id(author1.id).name}")
    print("All games:")
    for games in get_all_games():
        print(f"{games.title} by {games.author.name}")

    # Обновление книги
    updated_games = update_games(games1.id, title="Tetris")
    print(f"Updated games: {updated_games.title}")

    # Удаление данных
    delete_book(games1.id)
    delete_author(author1.id)
