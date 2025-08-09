from fastapi import FastAPI, HTTPException 
from schemas import GenreURLChoices, Band, Album

app = FastAPI()



BANDS = [
    {
        "id": 1,
        'name': 'The Kinks',
        'genre': 'Rock',
        'albums': [
            {'title': 'Kinks', 'relesase_date': '1964-10-02'},
            {'title': 'Face to Face', 'relesase_date': '1966-10-28'},
            {'title': 'Arthur', 'relesase_date': '1969-10-10'}
        ]
    },
    {
        "id": 2,
        'name': 'Pink Floyd',
        'genre': 'electronic',
        'albums': [
        ]
    },
    {
        "id": 3,
        'name': 'The Beatles',
        'genre': 'Metal',
        'albums': [
        ]
    },
    {
        "id": 4,
        'name': 'Led Zeppelin',
        'genre': 'Hip-hop',
        'albums': [
            {'title': 'Led Zeppelin', 'relesase_date': '1969-01-12'},
            {'title': 'Led Zeppelin II', 'relesase_date': '1969-10-22'},
            {'title': 'Led Zeppelin IV', 'relesase_date': '1971-11-08'}
        ]
    },
    {
        "id": 5,
        'name': 'Queen',
        'genre': 'Rock',
        'albums': [
            {'title': 'Queen', 'relesase_date': '1973-07-13'},
            {'title': 'A Night at the Opera', 'relesase_date': '1975-11-21'},
            {'title': 'The Game', 'relesase_date': '1980-06-30'}
        ]
    }
]

@app.get("/bands")
async def bands(
    genre: GenreURLChoices | None = None,
    has_albums: bool = False
    ) -> list[Band]:

    band_list = [Band(**b) for b in BANDS]

    if genre:
        band_list = [
            b for b in band_list if b.genre.lower() ==  genre.value
        ]

    if has_albums:
        band_list = [
            a for a in band_list if len(a.albums) > 0
        ]
    return band_list


@app.get("/band/{band_id}")
async def band(band_id: int) -> Band:
    band = next((Band(**b) for b in BANDS if b['id'] == band_id), None)
    if not band:
        raise HTTPException(status_code=404, detail='Band not found')
    return band 

 
