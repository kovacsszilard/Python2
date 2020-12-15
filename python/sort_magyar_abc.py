def sort_magyar_abc(lista):
    abc = "-_aAáÁbBcCdDeEéÉfFgGhHiIíÍjJkKlLmMnNoOóÓöÖőŐpPqQrRsStTuUúÚüÜűŰvVwWxXyYzZ"
    rendezve = sorted(lista, key = lambda word: [abc.index(c) for c in word])
    return rendezve