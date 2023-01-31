# CSFD.cz Scraper

This is a simple scraper for [CSFD.cz](https://www.csfd.cz/), a Czech movie database.

#### This scraper is not meant to be used for any illegal purposes.
#### I am *NOT* responsible for any misuse of this scraper.

## Usage

### Imports
```python
from src.csfd_scraper import CsfdScraper
from src.csfd_objects import *

scraper = CsfdScraper()
```

### Get movie by ID
```python
movie = scraper.movie(31881)
```

### Get creator by ID
```python
creator = scraper.creator(84039)
```

### Get user by ID
```python
user = scraper.user(447317)
```

### News list
```python
news_list = scraper.news_list()
news_list_2 = scraper.news_list(page=2)
```

### Get News by ID
```python
news = scraper.news(8360)
```

### Search movies/creators/series/users by text
```python
result = scraper.text_search("spielberg")
```

### Search movies by text
```python
result = scraper.text_search_movies("spielberg")
```

### Search creators by text
```python
result = scraper.text_search_creators("spielberg")
```

### Search series by text
```python
result = scraper.text_search_series("spielberg")
```

### Search users by text
```python
result = scraper.text_search_users("spielberg")
```

### Search movies by Advanced Search
```python
result = scraper.search_movies({
    MovieParams.TYPES: [MovieTypes.MOVIE],
    MovieParams.ORIGINS: {
        MovieOriginOptions.FILTER: MovieOriginFilters.AT_LEAST_ALL_SELECTED,
        MovieOriginOptions.ORIGINS: [Origins.USA],
    },
    MovieParams.GENRES: {
        MovieGenreOptions.FILTER: MovieGenreFilters.AT_LEAST_ALL_SELECTED,
        MovieGenreOptions.GENRES: [
            MovieGenres.ACTION,
            MovieGenres.ADVENTURE,
            MovieGenres.FANTASY,
            MovieGenres.HORROR,
            MovieGenres.COMEDY,
        ],
        MovieGenreOptions.EXCLUDE: [MovieGenres.DRAMA, MovieGenres.EROTIC]
    }
})
```
- #### Should return [The Monster Squad](https://www.csfd.cz/film/31881-zahrobni-komando/prehled/)

### Search creators by Advanced Search
```python
result = scraper.search_creators({
    CreatorParams.TYPES: [
        CreatorTypes.COMPOSER,
        CreatorTypes.DIRECTOR,
        CreatorTypes.CINEMATOGRAPHER
    ],
    CreatorParams.BIRTH_COUNTRY: Origins.USA,
    CreatorParams.ADDITIONAL_FILTERS: [
        CreatorFilters.WITH_BIOGRAPHY,
        CreatorFilters.WITH_AWARDS,
        CreatorFilters.WITH_TRIVIA
    ],
    CreatorParams.GENDER: CreatorGenders.FEMALE
})
```
- #### Should return [Lana Del Rey](https://www.csfd.cz/tvurce/84039-lana-del-rey/prehled/)