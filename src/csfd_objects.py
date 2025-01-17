from enum import Enum
from typing import List, Dict, Optional
from src.csfd_utils import tojson

class PrintableObject:
    args: dict = None

    def to_dict(self):
        return self.args

    def __str__(self):
        return tojson(self.to_dict())

class CzechEnum(Enum):
    @classmethod
    def get_by_czech_name(cls, name: str):
        """Vrátí enum podle českého názvu"""
        for k, v in cls.__members__.items():
            if name in v.value[1:]:
                return v
        return None

    @classmethod
    def get_by_value(cls, value: int):
        """Vrátí enum podle hodnoty"""
        for k, v in cls.__members__.items():
            if value == v.value[0]:
                return v
        return None

    @classmethod
    def search_by_czech_name(cls, search: str):
        """Vrátí enum podle českého názvu"""
        found = []
        for k, v in cls.__members__.items():
            if search.lower() in [x.lower() for x in v.value[1:]]:
                found.append(v)
        return found

# <editor-fold desc="GLOBAL TYPES">

class Continents(CzechEnum):
    """Kontinenty (původy) filmů pro vyhledávání v žebříčcích"""

    EUROPE                = "continent-1", "Evropa"
    AMERICA               = "continent-2", "Amerika"
    ASIA                  = "continent-3", "Asie"
    AFRICA                = "continent-4", "Afrika"
    AUSTRALIA_AND_OCEANIA = "continent-5", "Austrálie a Oceánie"

class Origins(CzechEnum):
    """Původy filmů/místa narození tvůrců pro vyhledávání"""

    AFGHANISTAN                         = 3,   "Afghánistán"
    ALBANIA                             = 4,   "Albánie"
    ALGERIA                             = 5,   "Alžírsko"
    ANDORRA                             = 6,   "Andorra"
    ANGOLA                              = 7,   "Angola"
    ANTIQUA                             = 8,   "Antigua a Barbuda"
    ARGENTINA                           = 9,   "Argentina"
    ARMENIA                             = 10,  "Arménie"
    ARUBA                               = 205, "Aruba"
    AUSTRALIA                           = 11,  "Austrálie"
    AZERBAIJAN                          = 185, "Ázerbájdžán"
    BAHAMAS                             = 12,  "Bahamy"
    BAHRAIN                             = 13,  "Bahrajn"
    BANGLADESH                          = 14,  "Bangladéš"
    BARBADOS                            = 15,  "Barbados"
    BELGIUM                             = 16,  "Belgie"
    BELIZE                              = 17,  "Belize"
    BELARUS                             = 28,  "Bělorusko"
    BENIN                               = 18,  "Benin"
    BHUTAN                              = 19,  "Bhútán"
    BOLIVIA                             = 20,  "Bolívie"
    BOSNIA                              = 21,  "Bosna a Hercegovina"
    BOTSWANA                            = 22,  "Botswana"
    BRAZIL                              = 23,  "Brazílie"
    BRUNEI                              = 24,  "Brunej"
    BULGARIA                            = 25,  "Bulharsko"
    BURKINA_FASO                        = 26,  "Burkina Faso"
    BURUNDI                             = 27,  "Burundi"
    CURACAO                             = 229, "Curaçao"
    CHAD                                = 187, "Čad"
    MONTENEGRO                          = 190, "Černá Hora"
    CZECHIA                             = 1,   "Česko"
    CZECHOSLOVAKIA                      = 197, "Československo"
    CHINA                               = 195, "Čína"
    DENMARK                             = 34,  "Dánsko"
    KONGO                               = 31,  "Demokratická republika Kongo"
    DOMINICA                            = 32,  "Dominika"
    DOMINICAN_REPUBLIC                  = 33,  "Dominikánská republika"
    DJIBOUTI                            = 35,  "Džibutsko"
    EGYPT                               = 36,  "Egypt"
    EQUADOR                             = 37,  "Ekvádor"
    ERITREA                             = 38,  "Eritrea"
    ESTONIA                             = 39,  "Estonsko"
    ETHIOPIA                            = 40,  "Etiopie"
    FAROE_ISLANDS                       = 211, "Faerské ostrovy"
    MICRONESIA                          = 108, "Federativní státy Mikronésie"
    YUGOSLAVIA_FEDERAL                  = 200, "Fed. rep. Jugoslávie"
    FIJI                                = 41,  "Fidži"
    PHILIPPINES                         = 42,  "Filipíny"
    FINLAND                             = 43,  "Finsko"
    FRANCE                              = 44,  "Francie"
    POLYNESIA                           = 213, "Francouzská Polynésie"
    GABON                               = 45,  "Gabon"
    GAMBIA                              = 46,  "Gambie"
    GHANA                               = 47,  "Ghana"
    GRENADA                             = 48,  "Grenada"
    GREENLAND                           = 206, "Grónsko"
    GEORGIA                             = 49,  "Gruzie"
    GUADELOUPE                          = 214, "Guadeloupe"
    GUATEMALA                           = 50,  "Guatemala"
    GUINEA                              = 51,  "Guinea"
    GUINEA_BISSAU                       = 52,  "Guinea-Bissau"
    GUYANA                              = 53,  "Guyana"
    HAITI                               = 54,  "Haiti"
    HONDURAS                            = 55,  "Honduras"
    HONG_KONG                           = 196, "Hongkong"
    CHILE                               = 29,  "Chile"
    CROATIA                             = 30,  "Chorvatsko"
    INDIA                               = 56,  "Indie"
    INDONESIA                           = 57,  "Indonésie"
    IRAQ                                = 59,  "Irák"
    IRAN                                = 186, "Írán"
    IRELAND                             = 58,  "Irsko"
    ICELAND                             = 60,  "Island"
    ITALY                               = 61,  "Itálie"
    ISRAEL                              = 62,  "Izrael"
    JAMAICA                             = 63,  "Jamajka"
    JAPAN                               = 64,  "Japonsko"
    YEMEN                               = 65,  "Jemen"
    SOUTH_AFRICAN_REPUBLIC              = 66,  "Jihoafrická republika"
    SOUTH_KOREA                         = 67,  "Jižní Korea"
    JORDAN                              = 68,  "Jordánsko"
    YUGOSLAVIA                          = 201, "Jugoslávie"
    CAMBODIA                            = 69,  "Kambodža"
    CAMEROON                            = 70,  "Kamerun"
    CANADA                              = 71,  "Kanada"
    CAPE_VERDE                          = 72,  "Kapverdy"
    QATAR                               = 73,  "Katar"
    KAZAKHSTAN                          = 74,  "Kazachstán"
    KENYA                               = 75,  "Keňa"
    KIRIBATI                            = 76,  "Kiribati"
    COLOMBIA                            = 77,  "Kolumbie"
    COMOROS                             = 78,  "Komory"
    CONGO                               = 79,  "Kongo"
    KOREA                               = 208, "Korea"
    KOSOVO                              = 80,  "Kosovo"
    COSTA_RICA                          = 81,  "Kostarika"
    YUGOSLAVIA_KINGDOM                  = 231, "Království Srbů, Chorvatů a Slovinců"
    CRETE                               = 210, "Kréta"
    CUBA                                = 82,  "Kuba"
    KUWAIT                              = 83,  "Kuvajt"
    CYPRUS                              = 84,  "Kypr"
    KYRGYZSTAN                          = 85,  "Kyrgyzstán"
    LAOS                                = 86,  "Laos"
    LESOTHO                             = 87,  "Lesotho"
    LIBANON                             = 88,  "Libanon"
    LIBERIA                             = 90,  "Libérie"
    LIBYA                               = 89,  "Libye"
    LIECHTENSTEIN                       = 91,  "Lichtenštejnsko"
    LITHUANIA                           = 92,  "Litva"
    LATVIA                              = 93,  "Lotyšsko"
    LUXEMBOURG                          = 94,  "Lucembursko"
    MACAO                               = 221, "Macao"
    MADAGASKAR                          = 95,  "Madagaskar"
    HUNGARY_KINGDOM                     = 230, "Maďarské království"
    HUNGARY                             = 106, "Maďarsko"
    MACEDONIA                           = 96,  "Makedonie"
    MALAYSIA                            = 97,  "Malajsie"
    MALAWI                              = 98,  "Malawi"
    MALDIVES                            = 99,  "Maledivy"
    MALI                                = 100, "Mali"
    MALTA                               = 101, "Malta"
    MOROCCO                             = 102, "Maroko"
    MARSHALL_ISLANDS                    = 103, "Marshallovy ostrovy"
    MARTINIQUE                          = 215, "Martinik"
    MAURITIUS                           = 104, "Mauricius"
    MAURITANIA                          = 105, "Mauritánie"
    MAYOTTE                             = 216, "Mayotte"
    MEXICO                              = 107, "Mexiko"
    MOLDAVIA                            = 109, "Moldavsko"
    MONACO                              = 110, "Monako"
    MONGOLIA                            = 111, "Mongolsko"
    MOZAMBIQUE                          = 112, "Mosambik"
    MYANMAR                             = 113, "Myanmar"
    NAMIBIA                             = 114, "Namibie"
    NAURU                               = 115, "Nauru"
    GERMAN_EMPIRE                       = 226, "Německá říše"
    GERMANY                             = 123, "Německo"
    NEPAL                               = 116, "Nepál"
    NIGER                               = 117, "Niger"
    NIGERIA                             = 118, "Nigérie"
    NICARAGUA                           = 119, "Nikaragua"
    NETHERLANDS                         = 120, "Nizozemsko"
    NORWAY                              = 121, "Norsko"
    NEW_CALEDONIA                       = 217, "Nová Kaledonie"
    NEW_ZEALAND                         = 122, "Nový Zéland"
    OMAN                                = 124, "Omán"
    OTTOMAN_EMPIRE                      = 228, "Osmanská říše"
    PAKISTAN                            = 133, "Pákistán"
    PALAU                               = 125, "Palau"
    PALESTINE                           = 202, "Palestina"
    PANAMA                              = 126, "Panama"
    PAPUA_NEW_GUINEA                    = 127, "Papua-Nová Guinea"
    PARAGUAY                            = 128, "Paraguay"
    PERU                                = 129, "Peru"
    IVORY_COAST                         = 130, "Pobřeží slonoviny"
    POLAND                              = 131, "Polsko"
    PUERTO_RICO                         = 203, "Portoriko"
    PORTUGAL                            = 132, "Portugalsko"
    PROTECTORATE_OF_BOHEMIA_AND_MORAVIA = 224, "Protektorát Čechy a Morava"
    AUSTRIAN_EMPIRE                     = 222, "Rakouská říše"
    AUSTRIA                             = 134, "Rakousko"
    AUSTRIA_HUNGARY                     = 204, "Rakousko-Uhersko"
    EQUATORIAL_GUINEA                   = 135, "Rovníková Guinea"
    ROMANIA                             = 136, "Rumunsko"
    RUSSIAN_EMPIRE                      = 220, "Ruské impérium"
    RUSSIA                              = 137, "Rusko"
    RWANDA                              = 138, "Rwanda"
    GREECE                              = 189, "Řecko"
    SAINT_PIERRE_AND_MIQUELON           = 218, "Saint-Pierre a Miquelon"
    SALVADOR                            = 139, "Salvador"
    SAMOA                               = 140, "Samoa"
    SAN_MARINO                          = 141, "San Marino"
    SAUDI_ARABIA                        = 142, "Saúdská Arábie"
    SENEGAL                             = 143, "Senegal"
    NORTH_KOREA                         = 144, "Severní Korea"
    NORTH_MACEDONIA                     = 233, "Severní Makedonie"
    SEYCHELLES                          = 145, "Seychely"
    SIERRA_LEONE                        = 146, "Sierra Leone"
    SINGAPORE                           = 147, "Singapur"
    SLOVAKIA                            = 2,   "Slovensko"
    SLOVAKIA_STATE                      = 225, "Slovenský stát"
    SLOVENIA                            = 148, "Slovinsko"
    SOMALIA                             = 149, "Somálsko"
    SOVIET_UNION                        = 199, "Sovětský svaz"
    UNITED_ARAB_EMIRATES                = 150, "Spojené arabské emiráty"
    SERBIA                              = 151, "Srbsko"
    SERBIA_AND_MONTENEGRO               = 209, "Srbsko a Černá Hora"
    SUDAN                               = 159, "Súdán"
    SURINAME                            = 153, "Surinam"
    SAINT_LUCIA                         = 154, "Svatá Lucie"
    SAINT_KITTS_AND_NEVIS               = 155, "Svatý Kryštof a Nevis"
    SAINT_THOMAS_AND_PRINCES_ISLAND     = 156, "Svatý Tomáš a Princův ostrov"
    SAINT_VINCENT_AND_THE_GRENADINES    = 157, "Svatý Vincenc a Grenadiny"
    SWAZILAND                           = 158, "Svazijsko"
    SYRIA                               = 160, "Sýrie"
    SOLOMON_ISLANDS                     = 188, "Šalamounovy ostrovy"
    SPAIN                               = 191, "Španělsko"
    SRI_LANKA                           = 192, "Šrí Lanka"
    SWEDEN                              = 193, "Švédsko"
    SWEDISH_NORWEGIAN_UNION             = 223, "Švédsko-norská unie"
    SWITZERLAND                         = 194, "Švýcarsko"
    TAJIKISTAN                          = 171, "Tádžikistán"
    TANZANIA                            = 161, "Tanzanie"
    THAILAND                            = 163, "Thajsko"
    TAIWAN                              = 162, "Tchaj-wan"
    TIBET                               = 212, "Tibet"
    TOGO                                = 164, "Togo"
    TONGA                               = 165, "Tonga"
    TRINIDAD_AND_TOBAGO                 = 166, "Trinidad a Tobago"
    TUNISIA                             = 167, "Tunisko"
    TURKEY                              = 168, "Turecko"
    TURKMENISTAN                        = 169, "Turkmenistán"
    TUVALU                              = 170, "Tuvalu"
    UGANDA                              = 173, "Uganda"
    KINGDOM_OF_HUNGARY                  = 227, "Uherské království"
    UKRAINE                             = 174, "Ukrajina"
    URUGUAY                             = 175, "Uruguay"
    USA                                 = 172, "USA"
    UZBEKISTAN                          = 176, "Uzbekistán"
    VANUATU                             = 177, "Vanuatu"
    VATICAN_CITY                        = 178, "Vatikán"
    GREAT_BRITAIN                       = 179, "Velká Británie"
    VENEZUELA                           = 180, "Venezuela"
    VIETNAM                             = 181, "Vietnam"
    EAST_GERMANY                        = 198, "Východní Německo"
    EAST_TIMOR                          = 182, "Východní Timor"
    WALLIS_AND_FUTUNA                   = 219, "Wallis a Futuna"
    ZAMBIA                              = 183, "Zambie"
    WEST_GERMANY                        = 207, "Západní Německo"
    ZIMBABWE                            = 184, "Zimbabwe"

class Months(CzechEnum):
    """Měsíce v roce"""

    JANUARY   = 1, "Leden"
    FEBRUARY  = 2, "Únor"
    MARCH     = 3, "Březen"
    APRIL     = 4, "Duben"
    MAY       = 5, "Květen"
    JUNE      = 6, "Červen"
    JULY      = 7, "Červenec"
    AUGUST    = 8, "Srpen"
    SEPTEMBER = 9, "Září"
    OCTOBER   = 10, "Říjen"
    NOVEMBER  = 11, "Listopad"
    DECEMBER  = 12, "Prosinec"

# </editor-fold>

# <editor-fold desc="MOVIE SEARCH TYPES">

class MovieSorts(Enum):
    """Možnosti řazení filmů pro vyhledávání"""

    BY_RATING_COUNT = "rating_count"
    """podle počtu hodnocení"""

    BY_BEST_RATING  = "rating_average"
    """od nejlepšího"""

    BY_WORST_RATING = "rating_average_asc"
    """od nejhoršího"""

    BY_FAN_COUNT    = "fanclub_count"
    """podle počtu fanoušků"""

    BY_NEWEST       = "year"
    """od nejnovějšího"""

    BY_OLDEST       = "year_asc"
    """od nejstaršího"""

class MovieTypes(Enum):
    """Typy filmů pro vyhledávání"""

    MOVIE             = 0
    """Film"""

    SERIAL            = 3
    """Seriál"""

    SERIES            = 10
    """Série - doesn't apply to Advanced Search"""

    TV_MOVIE          = 2
    """TV film"""

    TV_SHOW           = 4
    """Pořad"""

    STUDENT_MOVIE     = 7
    """Studentský film"""

    AMATER_MOVIE      = 8
    """Amaterský film"""

    THEATER_REC       = 5
    """Divadelní záznam"""

    MUSIC_VIDEO       = 9
    """Hudební videoklip"""

    CONCERT           = 6
    """Koncert"""

    VIDEO_COMPILATION = 14
    """Video kompilace"""

class MovieGenres(CzechEnum):
    """Žánry filmů pro vyhledávání"""

    ACTION        = 1,  "Akční"
    ANIMATED      = 3,  "Animovaný"
    ADVENTURE     = 11, "Dobrodružný"
    DOCUMENTARY   = 13, "Dokumentární"
    DRAMA         = 2,  "Drama"
    EROTIC        = 45, "Erotický"
    EXPERIMENTAL  = 26, "Experimentální"
    FANTASY       = 4,  "Fantasy"
    FILMNOIR      = 20, "Film-noir"
    HISTORICAL    = 21, "Historický"
    HORROR        = 5,  "Horor"
    MUSIC         = 22, "Hudební"
    IMAX          = 28, "IMAX"
    DISASTER      = 39, "Katastrofický"
    COMEDY        = 9,  "Komedie"
    CRIME         = 18, "Krimi"
    SHORT         = 14, "Krátkometrážní"
    PUPPET        = 23, "Loutkový"
    MUSICAL       = 12, "Muzikál"
    MYSTERY       = 16, "Mysteriózní"
    EDUCATIONAL   = 44, "Naučný"
    FABLE         = 25, "Podobenství"
    POETIC        = 27, "Poetický"
    FAIRYTALE     = 30, "Pohádka"
    PORNOGRAPHIC  = 10, "Pornografický"
    SHORTSTORY    = 29, "Povídkový"
    PSYCHOLOGICAL = 31, "Psychologický"
    PUBLICISTICAL = 33, "Publicistický"
    REALITYTV     = 35, "Reality-TV"
    ROADMOVIE     = 40, "Road movie"
    FAMILY        = 6,  "Rodinný"
    ROMANTIC      = 15, "Romantický"
    SCIFI         = 7,  "Sci-fi"
    COMPETITION   = 36, "Soutěžní"
    SPORT         = 32, "Sportovní"
    STANDUP       = 43, "Stand-up"
    TALKSHOW      = 34, "Talk-show"
    DANCE         = 41, "Taneční"
    TELENOVELA    = 38, "Telenovela"
    THRILLER      = 8,  "Thriller"
    VRMOVIE       = 46, "VR film"
    WAR           = 17, "Válečný"
    WESTERN       = 19, "Western"
    FUN           = 42, "Zábavný"
    BIOGRAPHICAL  = 37, "Životopisný"

class MovieFilters(Enum):
    """Doplňující filtry pro vyhledávání filmů"""

    IN_CINEMAS      = "in_cinemas"
    """běží v kinech"""

    ON_TV           = "on_tv"
    """poběží na TV"""

    ON_VOD          = "on_vod"
    """k přehrání na VOD"""

    WITH_COLLECTION = "with_collection"
    """ve filmotéce"""

    WITH_BAZAAR     = "with_bazaar"
    """ve filmotéce prodej/sháňka"""

    ON_BLURAY       = "on_bluray"
    """ke koupi na Blu-ray"""

    ON_DVD          = "on_dvd"
    """ke koupi na DVD"""

    WITH_COMMENTS   = "with_comments"
    """s recenzemi"""

    WITH_PHOTOS     = "with_photos"
    """s galerií"""

    WITH_VIDEOS     = "with_videos"
    """s videi"""

    WITH_AWARDS     = "with_awards"
    """s oceněními"""

    WITH_TRIVIA     = "with_trivia"
    """se zajímavostmi"""

class MovieOriginFilters(Enum):
    """Filtry pro vyhledávání filmů podle původu"""

    AT_LEAST_ALL_SELECTED        = 2
    """minimálně všechny zvolené"""

    EXACTLY_AND_ONLY_SELECTED    = 1
    """přesně a pouze zvolené"""

    AT_LEAST_ONE_OF_THE_SELECTED = 3
    """alespoň jeden z zvolených"""

class MovieOriginOptions(Enum):
    """Specifikace původu pro vyhledávání"""

    ORIGINS = 0
    """Původy, které se mají vyhledávat"""

    EXCLUDE = 1
    """
        Původy, které se mají vynechat.
        Platí pouze pokud je nastavený FILTER na:
            AT_LEAST_ONE_OF_THE_SELECTED nebo AT_LEAST_ALL_SELECTED
    """

    FILTER  = 2
    """Nastavení filtru pro vyhledávání původu"""

class MovieGenreFilters(Enum):
    """Filtry pro vyhledávání filmů podle žánrů"""

    AT_LEAST_ALL_SELECTED        = 2
    """minimálně všechny zvolené"""

    EXACTLY_AND_ONLY_SELECTED    = 1
    """přesně a pouze zvolené"""

    AT_LEAST_ONE_OF_THE_SELECTED = 3
    """alespoň jeden z zvolených"""

class MovieGenreOptions(Enum):
    """Specifikace žánrů pro vyhledávání"""

    GENRES  = 0
    """Žánry, které se mají vyhledávat"""

    EXCLUDE = 1
    """
        Žánry, které se mají vynechat.
        Platí pouze pokud je nastavený FILTER na:
            AT_LEAST_ONE_OF_THE_SELECTED nebo AT_LEAST_ALL_SELECTED
    """

    FILTER  = 2
    """Nastavení filtru pro vyhledávání žánrů"""

class MovieOptions(Enum):
    """Možnosti pro vyhledávání filmů"""

    TYPES              = 0
    """Typy filmů, podle kterých se má vyhledávat"""

    GENRES             = 1
    """Žánry, podle kterých se má vyhledávat"""

    ORIGINS            = 2
    """Původy, podle kterých se má vyhledávat"""

    YEAR_FROM          = 3
    """Rok od kterého se mají vyhledávat filmy"""

    YEAR_TO            = 4
    """Rok do kterého se mají vyhledávat filmy"""

    RATING_FROM        = 5
    """Hodnocení od kterého se mají vyhledávat filmy"""

    RATING_TO          = 6
    """Hodnocení do kterého se mají vyhledávat filmy"""

    TAGS               = 7
    """Tagy, podle kterých se má vyhledávat"""

    ACTORS             = 8
    """ID herců, podle kterých se má vyhledávat"""

    DIRECTORS          = 9
    """ID režisérů, podle kterých se má vyhledávat"""

    COMPOSERS          = 10
    """ID skladatelů, podle kterých se má vyhledávat"""

    SCREENWRITERS      = 11
    """ID scénáristů, podle kterých se má vyhledávat"""

    AUTHORS            = 12
    """ID autorů předlohy, podle kterých se má vyhledávat"""

    CINEMATOGRAPHERS   = 13
    """ID kameramanů, podle kterých se má vyhledávat"""

    PRODUCERS          = 14
    """ID producentů, podle kterých se má vyhledávat"""

    EDITORS            = 15
    """ID střihačů, podle kterých se má vyhledávat"""

    SOUND_ENGINEERS    = 16
    """ID zvukařů, podle kterých se má vyhledávat"""

    SCENOGRAPHERS      = 17
    """ID scenografů, podle kterých se má vyhledávat"""

    MASK_DESIGNERS     = 18
    """ID maskérů, podle kterých se má vyhledávat"""

    COSTUME_DESIGNERS  = 19
    """ID kostymérů, podle kterých se má vyhledávat"""

    ADDITIONAL_FILTERS = 20
    """Doplňující filtry pro vyhledávání filmů"""

class MovieParams(Enum):
    TYPES              = "type",            []
    GENRES             = "genre",           {}
    ORIGINS            = "origin",          {}
    YEAR_FROM          = "year_from",       None
    YEAR_TO            = "year_to",         None
    RATING_FROM        = "rating_from",     None
    RATING_TO          = "rating_to",       None
    TAGS               = "tag",             []
    ACTORS             = "actor",           []
    DIRECTORS          = "director",        []
    COMPOSERS          = "composer",        []
    SCREENWRITERS      = "screenwriter",    []
    AUTHORS            = "author",          []
    CINEMATOGRAPHERS   = "cinematographer", []
    PRODUCERS          = "production",      []
    EDITORS            = "edit",            []
    SOUND_ENGINEERS    = "sound",           []
    SCENOGRAPHERS      = "scenography",     []
    MASK_DESIGNERS     = "mask",            []
    COSTUME_DESIGNERS  = "costumes",        []
    ADDITIONAL_FILTERS = "conditions",      []

# </editor-fold>

# <editor-fold desc="CREATOR SEARCH TYPES">

class CreatorGenders(Enum):
    MALE = 1
    """Muž"""

    FEMALE = 2
    """Žena"""

class CreatorSorts(Enum):
    """Možnosti řazení tvůrců pro vyhledávání"""

    BY_FAN_COUNT = "fanclub_count"
    """podle počtu fanoušků"""

    BY_YOUNGEST  = "birth_date"
    """od nejmladšího"""

    BY_OLDEST    = "birth_date_asc"
    """od nejstaršího"""

class CreatorTypes(CzechEnum):
    """Typy tvůrců pro vyhledávání"""

    COMPOSER         = 3,  "skladatel",  "skladatelka"
    CINEMATOGRAPHER  = 6,  "kameraman",  "kameramanka"
    SOUND_ENGINEER   = 9,  "zvukař",     "zvukařka"
    COSTUME_DESIGNER = 12, "kostymér",   "kostymérka"
    ACTOR            = 1,  "herec",      "herečka"
    SCREENWRITER     = 4,  "scenárista", "scenáristka"
    PRODUCER         = 7,  "producent",  "producentka"
    SCENOGRAPHER     = 10, "scénograf",  "scénografka"
    AUTHOR           = 13, "tvůrce",     "tvůrce"
    DIRECTOR         = 2,  "režisér",    "režisérka"
    WRITER           = 5,  "spisovatel", "spisovatelka"
    EDITOR           = 8,  "střihač",    "střihačka"
    MASK_DESIGNER    = 11, "maskér",     "maskérka"
    PERFORMER        = 14, "účinkující", "účinkující"

class CreatorFilters(Enum):
    """Doplňující filtry pro vyhledávání tvůrců"""

    WITH_BIOGRAPHY   = "with_biography"
    """s biografií"""

    WITH_PHOTOS      = "with_photos"
    """s galerií"""

    WITH_CONTACT     = "with_contact"
    """s kontakty"""

    WITH_AWARDS      = "with_awards"
    """s oceněními"""

    WITH_FORUM_POSTS = "with_forum_posts"
    """s diskuzí"""

    WITH_TRIVIA      = "with_trivia"
    """se zajímavostmi"""

class CreatorOptions(Enum):
    """Možnosti pro vyhledávání tvůrců"""

    TYPES              = 0
    """Typy tvůrců, podle kterých se má vyhledávat"""

    BIRTH_FROM         = 1
    """Datum narození od kterého se má vyhledávat (DD.MM.RRRR)"""

    BIRTH_TO           = 2
    """Datum narození do kterého se má vyhledávat (DD.MM.RRRR)"""

    BIRTH_COUNTRY      = 3
    """ID země narození, podle kterého se má vyhledávat"""

    DEATH_FROM         = 4
    """Datum úmrtí od kterého se má vyhledávat (DD.MM.RRRR)"""

    DEATH_TO           = 5
    """Datum úmrtí do kterého se má vyhledávat (DD.MM.RRRR)"""

    DEATH_COUNTRY      = 6
    """ID země úmrtí, podle kterého se má vyhledávat"""

    ADDITIONAL_FILTERS = 7
    """Doplňující filtry pro vyhledávání tvůrců"""

    GENDER             = 8
    """Pohlaví tvůrce podle kterého se má vyhledávat"""

class CreatorParams(Enum):
    TYPES              = "type",             []
    BIRTH_FROM         = "birth_from",       None
    BIRTH_TO           = "birth_to",         None
    BIRTH_COUNTRY      = "birth_country_id", None
    DEATH_FROM         = "death_from",       None
    DEATH_TO           = "death_to",         None
    DEATH_COUNTRY      = "death_country_id", None
    ADDITIONAL_FILTERS = "conditions",       []
    GENDER             = "gender",           None

class CreatorFilmographySorts(Enum):
    """Možnosti řazení filmografie"""

    BY_NEWEST       = "year"
    """od nejnovějšího"""

    BY_BEST_RATING  = "sort_average"
    """od nejlepšího"""

    BY_RATING_COUNT = "rating_count"
    """podle počtu hodnocení"""

# </editor-fold>

# <editor-fold desc="MOST ACTIVE USERS TYPES">

class ActiveUsersSorts(Enum):
    """Možnosti řazení nejaktivnějších uživatelů"""

    ALL_TIME   = 2
    """celkově"""

    LAST_MONTH = 1
    """za poslední měsíc"""

# </editor-fold>

# <editor-fold desc="TEXT SEARCH TYPES">

class TextSearchedMovie(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", None)
        self.name: Optional[str] = args.get("name", None)
        self.genres: List[str] = args.get("genres", [])
        self.origins: List[str] = args.get("origins", [])
        self.directors: List[dict] = args.get("directors", [])
        self.actors: List[dict] = args.get("actors", [])
        self.performes: List[dict] = args.get("performes", [])
        self.image: Optional[str] = args.get("image", None)

class TextSearchedCreator(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.name: Optional[str] = args.get("name", None)
        self.types: List[str] = args.get("types", [])
        self.image: Optional[str] = args.get("image", None)

class TextSearchedSeries(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.name: Optional[str] = args.get("name", None)
        self.genres: List[str] = args.get("genres", [])
        self.origins: List[str] = args.get("origins", [])
        self.directors: List[dict] = args.get("directors", [])
        self.actors: List[dict] = args.get("actors", [])
        self.performes: List[dict] = args.get("performes", [])
        self.image: Optional[str] = args.get("image", None)

class TextSearchedUser(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.name: Optional[str] = args.get("name", None)
        self.real_name: Optional[str] = args.get("real_name", None)
        self.points: int = args.get("points", -1)
        self.image: Optional[str] = args.get("image", None)

class TextSearchResult(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.movies: List[TextSearchedMovie] = args.get("movies", [])
        self.creators: List[TextSearchedCreator] = args.get("creators", [])
        self.series: List[TextSearchedSeries] = args.get("series", [])
        self.users: List[TextSearchedUser] = args.get("users", [])

# </editor-fold>

# <editor-fold desc="AUTOCOMPLETE SEARCH TYPES">

class AutoCompleteSearchJsonWrapper:
    __JSON_OBJECT = None

    def __init__(self, json_object: dict):
        self.__JSON_OBJECT = json_object
        for k, v in json_object.items():
            setattr(self, k, v)

    def to_dict(self):
        return self.__JSON_OBJECT

    def __str__(self):
        return tojson(self.to_dict())

class FilmCreator(AutoCompleteSearchJsonWrapper):
    def __init__(self, *args):
        super().__init__(*args)
        self.id: int = getattr(self, "id", -1)
        self.text: Optional[str] = getattr(self, "text", None)
        self.image: Optional[str] = getattr(self, "image", None)
        self.info: Optional[str] = getattr(self, "info", None)

class Tag(AutoCompleteSearchJsonWrapper):
    def __init__(self, *args):
        super().__init__(*args)
        self.id: int = getattr(self, "id", -1)
        self.text: Optional[str] = getattr(self, "text", None)
        self.info: Optional[str] = getattr(self, "info", None)
        self.hide_image: bool = getattr(self, "hide_image", False)

# </editor-fold>

# <editor-fold desc="ADVANCED SEARCH TYPES">

class SearchedMovie(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.title: Optional[str] = args.get("title", None)
        self.year: int = args.get("year", -1)
        self.origins: List[str] = args.get("origins", [])
        self.genres: List[str] = args.get("genres", [])

    def get_genres(self):
        return [MovieGenres.get_by_czech_name(g) for g in self.genres]

    def get_origins(self):
        return [Origins.get_by_czech_name(o) for o in self.origins]

class SearchMoviesResult(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.page: int = args.get("page", -1)
        self.movies: List[SearchedMovie] = args.get("movies", [])
        self.has_prev_page: bool = args.get("has_prev_page", False)
        self.has_next_page: bool = args.get("has_next_page", False)

class SearchedCreator(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.name: Optional[str] = args.get("name", None)
        self.birth_year: int = args.get("birth_year", -1)
        self.types: List[str] = args.get("types", [])

    def get_types(self):
        return [CreatorTypes.get_by_czech_name(g) for g in self.types]

class SearchCreatorsResult(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.page: int = args.get("page", -1)
        self.creators: List[SearchedCreator] = args.get("creators", [])
        self.has_prev_page: bool = args.get("has_prev_page", False)
        self.has_next_page: bool = args.get("has_next_page", False)

# </editor-fold>

# <editor-fold desc="OTHER TYPES">

class Movie(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.url: Optional[str] = args.get("url", None)
        self.type: Optional[str] = args.get("type", None)
        self.title: Optional[str] = args.get("title", None)
        self.year: int = args.get("year", -1)
        self.duration: Optional[str] = args.get("duration", None)
        self.genres: List[str] = args.get("genres", None)
        self.origins: List[str] = args.get("origins", None)
        self.rating: dict = args.get("rating", {})
        self.ranks: dict = args.get("ranks", {})
        self.other_names: dict = args.get("other_names", {})
        self.creators: dict = args.get("creators", {})
        self.vods: dict = args.get("vods", {})
        self.tags: dict = args.get("tags", {})
        self.reviews: dict = args.get("reviews", {})
        self.gallery: dict = args.get("gallery", {})
        self.trivia: dict = args.get("trivia", {})
        self.premieres: List[dict] = args.get("premieres", [])
        self.plot: Optional[str] = args.get("plot", None)
        self.cover: Optional[str] = args.get("cover", None)

class Creator(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.url: Optional[str] = args.get("url", None)
        self.type: Optional[str] = args.get("type", None)
        self.name: Optional[str] = args.get("name", None)
        self.age: int = args.get("age", -1)
        self.birth_date: Optional[str] = args.get("birth_date", None)
        self.birth_place: Optional[str] = args.get("birth_place", None)
        self.bio: Optional[str] = args.get("bio", None)
        self.ranks: dict = args.get("ranks", {})
        self.trivia: dict = args.get("trivia", {})
        self.gallery: dict = args.get("gallery", {})
        self.filmography: dict = args.get("filmography", {})
        self.image: Optional[str] = args.get("image", None)

class User(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.url: Optional[str] = args.get("url", None)
        self.name: Optional[str] = args.get("name", None)
        self.real_name: Optional[str] = args.get("real_name", None)
        self.origin: Optional[str] = args.get("origin", None)
        self.about: Optional[str] = args.get("about", None)
        self.registered: Optional[str] = args.get("registered", None)
        self.last_login: Optional[str] = args.get("last_login", None)
        self.points: int = args.get("points", -1)
        self.fans: int = args.get("fans", -1)
        self.awards: dict = args.get("awards", {})
        self.most_watched_genres: dict = args.get("most_watched_genres", {})
        self.most_watched_types: dict = args.get("most_watched_types", {})
        self.most_watched_origins: dict = args.get("most_watched_origins", {})
        self.reviews: dict = args.get("reviews", {})
        self.ratings: dict = args.get("ratings", {})
        self.is_currently_online: bool = args.get("is_currently_online", False)
        self.image: Optional[str] = args.get("image", None)

# </editor-fold>

# <editor-fold desc="NEWS TYPES">

class News(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.title: Optional[str] = args.get("title", None)
        self.text: Optional[str] = args.get("text", None)
        self.date: Optional[str] = args.get("date", None)
        self.author_id: int = args.get("author_id", -1)
        self.author_name: Optional[str] = args.get("author_name", None)
        self.most_read_news: List[dict] = args.get("most_read_news", [])
        self.most_latest_news: List[dict] = args.get("most_latest_news", [])
        self.related_news: List[dict] = args.get("related_news", [])
        self.image: Optional[str] = args.get("image", None)
        self.prev_news_id: int = args.get("prev_news_id", -1)
        self.next_news_id: int = args.get("next_news_id", -1)

class NewsList(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.page: int = args.get("page", -1)
        self.main_news: dict = args.get("main_news", {})
        self.news: List[dict] = args.get("news", [])
        self.most_read_news: List[dict] = args.get("most_read_news", [])
        self.most_latest_news: List[dict] = args.get("most_latest_news", [])
        self.has_prev_page: bool = args.get("has_prev_page", False)
        self.has_next_page: bool = args.get("has_next_page", False)

# </editor-fold>

# <editor-fold desc="USERS TYPES">

class FavoriteUser(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.position: int = args.get("position", -1)
        self.id: int = args.get("id", -1)
        self.name: Optional[str] = args.get("name", None)
        self.real_name: Optional[str] = args.get("real_name", None)
        self.about: Optional[str] = args.get("about", None)
        self.points: int = args.get("points", -1)
        self.ratings: int = args.get("ratings", -1)
        self.reviews: int = args.get("reviews", -1)
        self.image: Optional[str] = args.get("image", None)

class OtherFavoriteUser(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.name: Optional[str] = args.get("name", None)
        self.real_name: Optional[str] = args.get("real_name", None)
        self.points: int = args.get("points", -1)
        self.image: Optional[str] = args.get("image", None)

class FavoriteUsers(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.most_favorite_users: List[FavoriteUser] = args.get("most_favorite_users", [])
        self.by_regions: Dict[str, List[OtherFavoriteUser]] = args.get("by_regions", {})
        self.by_country: Dict[Origins, List[OtherFavoriteUser]] = args.get("by_country", {})

class ActiveUser(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.name: Optional[str] = args.get("name", None)
        self.image: Optional[str] = args.get("image", None)

class ActiveUserByReviews(ActiveUser):
    def __init__(self, args: dict):
        super().__init__(args)
        self.reviews: int = args.get("reviews", -1)

class ActiveUserByDiaries(ActiveUser):
    def __init__(self, args: dict):
        super().__init__(args)
        self.diaries: int = args.get("diaries", -1)

class ActiveUserByContent(ActiveUser):
    def __init__(self, args: dict):
        super().__init__(args)
        self.content: int = args.get("content", -1)

class ActiveUserByTrivia(ActiveUser):
    def __init__(self, args: dict):
        super().__init__(args)
        self.trivia: int = args.get("trivia", -1)

class ActiveUserByBiography(ActiveUser):
    def __init__(self, args: dict):
        super().__init__(args)
        self.biography: int = args.get("biography", -1)

class ActiveUsers(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.by_reviews: List[ActiveUserByReviews] = args.get("by_reviews", [])
        self.by_diaries: List[ActiveUserByDiaries] = args.get("by_diaries", [])
        self.by_content: List[ActiveUserByContent] = args.get("by_content", [])
        self.by_trivia: List[ActiveUserByTrivia] = args.get("by_trivia", [])
        self.by_biography: List[ActiveUserByBiography] = args.get("by_biography", [])

# </editor-fold>

# <editor-fold desc="DVDS TYPES">

class DVDMonthly(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.name: Optional[str] = args.get("name", None)
        self.year: int = args.get("year", -1)
        self.genres: List[str] = args.get("genres", [])
        self.origins: List[str] = args.get("origins", [])
        self.directors: List[dict] = args.get("directors", [])
        self.actors: List[dict] = args.get("actors", [])
        self.distributor: Optional[str] = args.get("distributor", None)
        self.image: Optional[str] = args.get("image", None)

class DVDSMonthlyByReleaseDate(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.dvds: Dict[str, List[DVDMonthly]] = args.get("dvds", {})
        self.has_prev_page: bool = args.get("has_prev_page", False)
        self.has_next_page: bool = args.get("has_next_page", False)

class DVDSMonthlyByRating(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.dvds: List[DVDMonthly] = args.get("dvds", [])
        self.has_prev_page: bool = args.get("has_prev_page", False)
        self.has_next_page: bool = args.get("has_next_page", False)

class DVDYearly(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.name: Optional[str] = args.get("name", None)
        self.year: int = args.get("year", -1)
        self.date: Optional[str] = args.get("date", None)

class DVDSYearlyByReleaseDate(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.dvds: Dict[Months, List[DVDYearly]] = args.get("dvds", {})

class DVDSYearlyByRating(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.dvds: List[DVDYearly] = args.get("dvds", [])

# </editor-fold>

# <editor-fold desc="DVDS TYPES">

class BlurayMonthly(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.name: Optional[str] = args.get("name", None)
        self.year: int = args.get("year", -1)
        self.genres: List[str] = args.get("genres", [])
        self.origins: List[str] = args.get("origins", [])
        self.directors: List[dict] = args.get("directors", [])
        self.actors: List[dict] = args.get("actors", [])
        self.distributor: dict = args.get("distributor", {})
        self.image: Optional[str] = args.get("image", None)

class BluraysMonthlyByReleaseDate(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.blurays: Dict[str, List[BlurayMonthly]] = args.get("blurays", {})
        self.has_prev_page: bool = args.get("has_prev_page", False)
        self.has_next_page: bool = args.get("has_next_page", False)

class BluraysMonthlyByRating(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.blurays: List[BlurayMonthly] = args.get("blurays", [])
        self.has_prev_page: bool = args.get("has_prev_page", False)
        self.has_next_page: bool = args.get("has_next_page", False)

class BlurayYearly(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.name: Optional[str] = args.get("name", None)
        self.year: int = args.get("year", -1)
        self.types: List[str] = args.get("types", [])
        self.date: Optional[str] = args.get("date", None)

class BluraysYearlyByReleaseDate(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.blurays: Dict[Months, List[BlurayYearly]] = args.get("blurays", {})

class BluraysYearlyByRating(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.blurays: List[BlurayYearly] = args.get("blurays", [])

# </editor-fold>

# <editor-fold desc="USER RATINGS TYPES">

class UserRatingsSorts(Enum):
    """Možnosti řazení uživatelských hodnocení"""

    BY_NEWLY_ADDED = "inserted_datetime"
    """seřadit od nově přidaných"""

    BY_NAME = "film_name"
    """seřadit abecedně"""

    BY_YEAR = "film_year"
    """seřadit podle roku vzniku filmu"""

    BY_RATING = "rating"
    """seřadit dle hodnocení"""

class UserRating(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.name: Optional[str] = args.get("name", None)
        self.year: int = args.get("year", None)
        self.rating: int = args.get("rating", -1)
        self.date: Optional[str] = args.get("date", None)

class UserRatings(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.total: int = args.get("total", -1)
        self.ratings: List[UserRating] = args.get("ratings", [])
        self.has_prev_page: bool = args.get("has_prev_page", False)
        self.has_next_page: bool = args.get("has_next_page", False)

# </editor-fold>

# <editor-fold desc="USER REVIEWS TYPES">

class UserReviewsSorts(Enum):
    """Možnosti řazení uživatelských recenzí"""

    BY_NEWLY_ADDED = "inserted_datetime"
    """seřadit od nově přidaných"""

    BY_NAME = "film_name"
    """seřadit abecedně"""

    BY_YEAR = "film_year"
    """seřadit podle roku vzniku filmu"""

    BY_RATING = "rating"
    """seřadit dle hodnocení"""

class UserReview(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.name: Optional[str] = args.get("name", None)
        self.year: int = args.get("year", None)
        self.rating: float = args.get("rating", None)
        self.date: Optional[str] = args.get("date", None)
        self.text: Optional[str] = args.get("text", None)
        self.image: Optional[str] = args.get("image", None)

class UserReviews(PrintableObject):
    def __init__(self, args: dict):
        self.args: dict = args
        self.total: int = args.get("total", -1)
        self.reviews: List[UserReview] = args.get("reviews", [])
        self.has_prev_page: bool = args.get("has_prev_page", False)
        self.has_next_page: bool = args.get("has_next_page", False)

# </editor-fold>

# <editor-fold desc="LEADERBOARDS TYPES">

class LeaderboardMovie(PrintableObject):
    def __init__(self, args: dict) -> None:
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.position: int = args.get("position", -1)
        self.title: Optional[str] = args.get("title", None)
        self.year: int = args.get("year", -1)
        self.origins: List[str] = args.get("origins", [])
        self.genres: List[str] = args.get("genres", [])
        self.directors: List[dict] = args.get("directors", [])
        self.actors: List[dict] = args.get("actors", [])
        self.rating: dict = args.get("rating", {})
        self.image: Optional[str] = args.get("image", None)

    def get_genres(self):
        return [MovieGenres.get_by_czech_name(g) for g in self.genres]

    def get_origins(self):
        return [Origins.get_by_czech_name(o) for o in self.origins]
    
class LeaderboardSerial(PrintableObject):
    def __init__(self, args: dict) -> None:
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.position: int = args.get("position", -1)
        self.title: Optional[str] = args.get("title", None)
        self.year: int = args.get("year", -1)
        self.origins: List[str] = args.get("origins", [])
        self.genres: List[str] = args.get("genres", [])
        self.directors: List[dict] = args.get("directors", [])
        self.actors: List[dict] = args.get("actors", [])
        self.rating: dict = args.get("rating", {})
        self.image: Optional[str] = args.get("image", None)

    def get_genres(self):
        return [MovieGenres.get_by_czech_name(g) for g in self.genres]

    def get_origins(self):
        return [Origins.get_by_czech_name(o) for o in self.origins]
    
class LeaderboardPerson(PrintableObject):
    def __init__(self, args: dict) -> None:
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.position: int = args.get("position", -1)
        self.name: Optional[str] = args.get("name", None)
        self.origin: Optional[str] = args.get("origin", None)
        self.fan_count: int = args.get("fan_count", -1)
        self.image: Optional[str] = args.get("image", None)

    def get_origin(self):
        return Origins.get_by_czech_name(self.origin)
    
class LeaderboardActors(PrintableObject):
    def __init__(self, args: dict) -> None:
        self.args: dict = args
        self.actors: List[LeaderboardPerson] = args.get("actors", [])
        self.actresses: List[LeaderboardPerson] = args.get("actresses", [])

class LeaderboardPersonBestMovie(PrintableObject):
    def __init__(self, args: dict) -> None:
        self.args: dict = args
        self.id: int = args.get("id", -1)
        self.position: int = args.get("position", -1)
        self.name: Optional[str] = args.get("name", None)
        self.origin: Optional[str] = args.get("origin", None)
        self.movie_count: int = args.get("movie_count", -1)
        self.avg_rating: float = args.get("avg_rating", -1)
        self.image: Optional[str] = args.get("image", None)

    def get_origin(self):
        return Origins.get_by_czech_name(self.origin)

class LeaderboardDirectors(PrintableObject):
    def __init__(self, args: dict) -> None:
        self.args: dict = args
        self.directors: List[LeaderboardPerson] = args.get("directors", [])
        self.with_best_movie: List[LeaderboardPersonBestMovie] = args.get("with_best_movie", [])

class LeaderboardOthers(PrintableObject):
    def __init__(self, args: dict) -> None:
        self.args: dict = args
        self.screenwriters: List[LeaderboardPerson] = args.get("screenwriters", [])
        self.cinematographers: List[LeaderboardPerson] = args.get("cinematographers", [])
        self.composers: List[LeaderboardPerson] = args.get("composers", [])

class LeaderboardCustom(PrintableObject):
    def __init__(self, args: dict) -> None:
        self.args: dict = args
        self.page: int = args.get("page", -1)
        self.records: List[LeaderboardMovie] = args.get("records", [])
        self.has_prev_page: bool = args.get("has_prev_page", False)
        self.has_next_page: bool = args.get("has_next_page", False)

class LeaderboardCustomOptions(Enum):
    """Možnosti pro vyhledávání filmů"""

    TYPE      = 0
    """Typ filmu, podle kterých se má vyhledávat"""

    GENRES    = 1
    """Žánry, podle kterých se má vyhledávat"""

    ORIGIN    = 2
    """Původ, podle kterých se má vyhledávat"""

    YEAR_FROM = 3
    """Rok od kterého se má vyhledávat"""

    YEAR_TO   = 4
    """Rok do kterého se má vyhledávat"""

    ACTORS    = 5
    """ID herců, podle kterých se má vyhledávat"""

    DIRECTORS = 6
    """ID režisérů, podle kterých se má vyhledávat"""

class LeaderboardCustomParams(Enum):
    TYPE      = "type",      None
    GENRES    = "genre",     []
    ORIGIN    = "origin",    None
    YEAR_FROM = "year_from", None
    YEAR_TO   = "year_to",   None
    ACTORS    = "actor",     []
    DIRECTORS = "director",  []
    
# </editor-fold>

# <editor-fold desc="EXCEPTIONS">

class CsfdScraperInvalidRequest(Exception):
    """Exception for invalid request"""
    pass

# </editor-fold>
