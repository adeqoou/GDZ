from gdz import GDZ
import re


gdz = GDZ()


def parse_int(data: str):
    result = re.findall(r'\d+', data)
    if not result:
        return False

    return result[0]


def get_subject(subject_id: int):
    subjects = list(filter(lambda subject: subject.id == subject_id, gdz.subjects))
    if not subjects:
        return None

    return subjects[0]


def parse_data(models):
    books = gdz.books[0:100]

    for book in books:
        try:
            book_subject = get_subject(book.subject_id)
            if not book_subject:
                continue

            subject = models.Subject.objects.get_or_create(title=book_subject.title)[0]
            cover = models.Cover.objects.get_or_create(url=book.cover_url)[0]

            book_model, is_created = models.Book.objects.get_or_create(
                title=book.title,
                classes=book.classes,
                authors=book.authors,
                year=2016,
                description=book.description,
                publisher=book.publisher,
                subject=subject,
                search_keywords=book.search_keywords,
                subtype=book.subtype,
                cover=cover
            )

            if not is_created:
                part = book_model.parts.create(
                    title=1
                )

                book_structure = gdz.book_structure(book)
                for structure in book_structure:
                    for task in structure.tasks:
                        integer_title = parse_int(task.title)

                        if not integer_title:
                            continue

                        task_extended = gdz.task_extended(task)

                        images = list(image for edition in task_extended.editions for image in edition.images)

                        task = part.tasks.create(
                            title=task.title,
                            description=task.description
                        )

                        for image in images:
                            task.images.create(
                                url=image.url
                            )

            book_model.save()

        except (Exception, BaseException):
            continue



