import os
from os.path import exists, join, splitext
from os import scandir, rename
from shutil import move

# OPERATIONAL PATHS
source = r"C:\Users\rwik\Downloads"
dest_book = r"C:\Users\rwik\Downloads\Book"
dest_image = r"C:\Users\rwik\Downloads\IMAGE"
dest_comics = r"C:\Users\rwik\Downloads\Book\Comics"
ext_book = [".doc", ".docx", ".odt", ".pdf", ".kfx", ".mobi", ".epub"]
ext_comics = [".cbz", ".cbr"]
ext_image = [".jpg", ".jpeg", ".jpe", ".png", ".gif", ".webp", ".bmp", ".svg", ".ico"]


def make_unique(dest, name):
    n, e = splitext(name)
    counter = 1
    while exists(f"{dest}'\'{name}"):
        name = f"{n}{'_'}({str(counter)}){e}"
        counter += 1
    return name


def move_file(dest, e, name):
    if exists(f"{dest}'\'{name}"):
        u_name = make_unique(dest,name)
        old = join(dest,name)
        n_name = join(dest,u_name)
        rename(old,n_name)
    move(e, os.path.join(dest, name))


class MoveHandler():

    @staticmethod
    def check_book(e, name):
        for ext in ext_book:
            if name.endswith(ext) or name.endswith(ext.upper()):
                move_file(dest_book, e, name)
                print(f"Moved Book : {name}")

    @staticmethod
    def start_here(source_folder):
        with scandir(source_folder) as entries:
            for e in entries:
                name = e.name
                #print(name)
                MoveHandler.check_book(e, name)
                MoveHandler.check_comics(e, name)
                MoveHandler.check_image(e, name)

    @staticmethod
    def check_comics(e, name):
        for ext in ext_comics:
            if name.endswith(ext) or name.endswith(ext.upper()):
                move_file(dest_book, e, name)
                print(f"Moved Comics : {name}")

    @staticmethod
    def check_image(e, name):
        for ext in ext_image:
            if name.endswith(ext) or name.endswith(ext.upper()):
                move_file(dest_book, e, name)
                print(f"Moved Image : {name}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #move(r"C:\Users\rwik\Downloads\River Out Of Eden_ A Darwinian View Of Life -- Richard Dawkins [Dawkins, Richard] -- 2008 -- c236da49e53075312efcb934b876357f -- Anna’s Archive.epub", dest_book)
    MoveHandler.start_here(source)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
