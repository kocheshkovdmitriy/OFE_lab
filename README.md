# OFE_lab
лаборатория Лицей 40


def download_file_view(request, id):
    object = get_object_or_404(MyModel, id)
    # Создаём FileResponse
    return FileResponse(object.file.open(), as_attachment=True, filename=object.file.name)
``` [1](https://stackoverflow.com/questions/9462999/how-to-download-a-filefield-file-in-django-view)

