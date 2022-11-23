# dict_add_nondup -- Menambahkan elemen baru ke dalam dict<str->list> jika elemen belum ada di dalam dict tersebut
def dict_add_nondup(d:dict, key:str, val:list) -> None:
    if key not in d.keys():
        d[key] = []
    if val not in d[key]:
        d[key].append(val)
