# SPDX-FileCopyrightText: 2023 James R. Barlow
# SPDX-License-Identifier: MPL-2.0

"""Language codes and names from ISO 639.

Derived from
https://www.loc.gov/standards/iso639-2/ascii_8bits.html
"""


from typing import NamedTuple


class ISOCodeData(NamedTuple):
    """Data for a single ISO 639 code."""
    alt: str
    alpha_2: str
    english: str
    french: str


ISO_639_3 = {
    'aar': ISOCodeData('', 'aa', 'Afar', 'afar'),
    'abk': ISOCodeData('', 'ab', 'Abkhazian', 'abkhaze'),
    'ace': ISOCodeData('', '', 'Achinese', 'aceh'),
    'ach': ISOCodeData('', '', 'Acoli', 'acoli'),
    'ada': ISOCodeData('', '', 'Adangme', 'adangme'),
    'ady': ISOCodeData('', '', 'Adyghe; Adygei', 'adyghé'),
    'afa': ISOCodeData(
        '',
        '',
        'Afro-Asiatic languages',
        'afro-asiatiques, langues',
    ),
    'afh': ISOCodeData('', '', 'Afrihili', 'afrihili'),
    'afr': ISOCodeData('', 'af', 'Afrikaans', 'afrikaans'),
    'ain': ISOCodeData('', '', 'Ainu', 'aïnou'),
    'aka': ISOCodeData('', 'ak', 'Akan', 'akan'),
    'akk': ISOCodeData('', '', 'Akkadian', 'akkadien'),
    'alb': ISOCodeData('sqi', 'sq', 'Albanian', 'albanais'),
    'ale': ISOCodeData('', '', 'Aleut', 'aléoute'),
    'alg': ISOCodeData(
        '',
        '',
        'Algonquian languages',
        'algonquines, langues',
    ),
    'alt': ISOCodeData('', '', 'Southern Altai', 'altai du Sud'),
    'amh': ISOCodeData('', 'am', 'Amharic', 'amharique'),
    'ang': ISOCodeData(
        '',
        '',
        'English, Old (ca.450-1100)',
        'anglo-saxon (ca.450-1100)',
    ),
    'anp': ISOCodeData('', '', 'Angika', 'angika'),
    'apa': ISOCodeData('', '', 'Apache languages', 'apaches, langues'),
    'ara': ISOCodeData('', 'ar', 'Arabic', 'arabe'),
    'arc': ISOCodeData(
        '',
        '',
        'Official Aramaic (700-300 BCE); Imperial Aramaic (700-300 BCE)',
        "araméen d'empire (700-300 BCE)",
    ),
    'arg': ISOCodeData('', 'an', 'Aragonese', 'aragonais'),
    'arm': ISOCodeData('hye', 'hy', 'Armenian', 'arménien'),
    'arn': ISOCodeData(
        '',
        '',
        'Mapudungun; Mapuche',
        'mapudungun; mapuche; mapuce',
    ),
    'arp': ISOCodeData('', '', 'Arapaho', 'arapaho'),
    'art': ISOCodeData(
        '',
        '',
        'Artificial languages',
        'artificielles, langues',
    ),
    'arw': ISOCodeData('', '', 'Arawak', 'arawak'),
    'asm': ISOCodeData('', 'as', 'Assamese', 'assamais'),
    'ast': ISOCodeData(
        '',
        '',
        'Asturian; Bable; Leonese; Asturleonese',
        'asturien; bable; léonais; asturoléonais',
    ),
    'ath': ISOCodeData(
        '',
        '',
        'Athapascan languages',
        'athapascanes, langues',
    ),
    'aus': ISOCodeData(
        '',
        '',
        'Australian languages',
        'australiennes, langues',
    ),
    'ava': ISOCodeData('', 'av', 'Avaric', 'avar'),
    'ave': ISOCodeData('', 'ae', 'Avestan', 'avestique'),
    'awa': ISOCodeData('', '', 'Awadhi', 'awadhi'),
    'aym': ISOCodeData('', 'ay', 'Aymara', 'aymara'),
    'aze': ISOCodeData('', 'az', 'Azerbaijani', 'azéri'),
    'bad': ISOCodeData('', '', 'Banda languages', 'banda, langues'),
    'bai': ISOCodeData('', '', 'Bamileke languages', 'bamiléké, langues'),
    'bak': ISOCodeData('', 'ba', 'Bashkir', 'bachkir'),
    'bal': ISOCodeData('', '', 'Baluchi', 'baloutchi'),
    'bam': ISOCodeData('', 'bm', 'Bambara', 'bambara'),
    'ban': ISOCodeData('', '', 'Balinese', 'balinais'),
    'baq': ISOCodeData('eus', 'eu', 'Basque', 'basque'),
    'bas': ISOCodeData('', '', 'Basa', 'basa'),
    'bat': ISOCodeData('', '', 'Baltic languages', 'baltes, langues'),
    'bej': ISOCodeData('', '', 'Beja; Bedawiyet', 'bedja'),
    'bel': ISOCodeData('', 'be', 'Belarusian', 'biélorusse'),
    'bem': ISOCodeData('', '', 'Bemba', 'bemba'),
    'ben': ISOCodeData('', 'bn', 'Bengali', 'bengali'),
    'ber': ISOCodeData('', '', 'Berber languages', 'berbères, langues'),
    'bho': ISOCodeData('', '', 'Bhojpuri', 'bhojpuri'),
    'bih': ISOCodeData('', 'bh', 'Bihari languages', 'langues biharis'),
    'bik': ISOCodeData('', '', 'Bikol', 'bikol'),
    'bin': ISOCodeData('', '', 'Bini; Edo', 'bini; edo'),
    'bis': ISOCodeData('', 'bi', 'Bislama', 'bichlamar'),
    'bla': ISOCodeData('', '', 'Siksika', 'blackfoot'),
    'bnt': ISOCodeData('', '', 'Bantu languages', 'bantou, langues'),
    'bos': ISOCodeData('', 'bs', 'Bosnian', 'bosniaque'),
    'bra': ISOCodeData('', '', 'Braj', 'braj'),
    'bre': ISOCodeData('', 'br', 'Breton', 'breton'),
    'btk': ISOCodeData('', '', 'Batak languages', 'batak, langues'),
    'bua': ISOCodeData('', '', 'Buriat', 'bouriate'),
    'bug': ISOCodeData('', '', 'Buginese', 'bugi'),
    'bul': ISOCodeData('', 'bg', 'Bulgarian', 'bulgare'),
    'bur': ISOCodeData('mya', 'my', 'Burmese', 'birman'),
    'byn': ISOCodeData('', '', 'Blin; Bilin', 'blin; bilen'),
    'cad': ISOCodeData('', '', 'Caddo', 'caddo'),
    'cai': ISOCodeData(
        '',
        '',
        'Central American Indian languages',
        "amérindiennes de L'Amérique centrale, langues",
    ),
    'car': ISOCodeData('', '', 'Galibi Carib', 'karib; galibi; carib'),
    'cat': ISOCodeData('', 'ca', 'Catalan; Valencian', 'catalan; valencien'),
    'cau': ISOCodeData(
        '',
        '',
        'Caucasian languages',
        'caucasiennes, langues',
    ),
    'ceb': ISOCodeData('', '', 'Cebuano', 'cebuano'),
    'cel': ISOCodeData(
        '',
        '',
        'Celtic languages',
        'celtiques, langues; celtes, langues',
    ),
    'cha': ISOCodeData('', 'ch', 'Chamorro', 'chamorro'),
    'chb': ISOCodeData('', '', 'Chibcha', 'chibcha'),
    'che': ISOCodeData('', 'ce', 'Chechen', 'tchétchène'),
    'chg': ISOCodeData('', '', 'Chagatai', 'djaghataï'),
    'chi': ISOCodeData('zho', 'zh', 'Chinese', 'chinois'),
    'chk': ISOCodeData('', '', 'Chuukese', 'chuuk'),
    'chm': ISOCodeData('', '', 'Mari', 'mari'),
    'chn': ISOCodeData('', '', 'Chinook jargon', 'chinook, jargon'),
    'cho': ISOCodeData('', '', 'Choctaw', 'choctaw'),
    'chp': ISOCodeData('', '', 'Chipewyan; Dene Suline', 'chipewyan'),
    'chr': ISOCodeData('', '', 'Cherokee', 'cherokee'),
    'chu': ISOCodeData(
        '',
        'cu',
        ('Church Slavic; Old Slavonic; Church Slavonic;'
         ' Old Bulgarian; Old Church Slavonic'),
        "slavon d'église; vieux slave; slavon liturgique; vieux bulgare",
    ),
    'chv': ISOCodeData('', 'cv', 'Chuvash', 'tchouvache'),
    'chy': ISOCodeData('', '', 'Cheyenne', 'cheyenne'),
    'cmc': ISOCodeData('', '', 'Chamic languages', 'chames, langues'),
    'cnr': ISOCodeData('', '', 'Montenegrin', 'monténégrin'),
    'cop': ISOCodeData('', '', 'Coptic', 'copte'),
    'cor': ISOCodeData('', 'kw', 'Cornish', 'cornique'),
    'cos': ISOCodeData('', 'co', 'Corsican', 'corse'),
    'cpe': ISOCodeData(
        '',
        '',
        'Creoles and pidgins, English based',
        "créoles et pidgins basés sur l'anglais",
    ),
    'cpf': ISOCodeData(
        '',
        '',
        'Creoles and pidgins, French-based',
        'créoles et pidgins basés sur le français',
    ),
    'cpp': ISOCodeData(
        '',
        '',
        'Creoles and pidgins, Portuguese-based',
        'créoles et pidgins basés sur le portugais',
    ),
    'cre': ISOCodeData('', 'cr', 'Cree', 'cree'),
    'crh': ISOCodeData(
        '',
        '',
        'Crimean Tatar; Crimean Turkish',
        'tatar de Crimé',
    ),
    'crp': ISOCodeData('', '', 'Creoles and pidgins', 'créoles et pidgins'),
    'csb': ISOCodeData('', '', 'Kashubian', 'kachoube'),
    'cus': ISOCodeData('', '', 'Cushitic languages', 'couchitiques, langues'),
    'cze': ISOCodeData('ces', 'cs', 'Czech', 'tchèque'),
    'dak': ISOCodeData('', '', 'Dakota', 'dakota'),
    'dan': ISOCodeData('', 'da', 'Danish', 'danois'),
    'dar': ISOCodeData('', '', 'Dargwa', 'dargwa'),
    'day': ISOCodeData('', '', 'Land Dayak languages', 'dayak, langues'),
    'del': ISOCodeData('', '', 'Delaware', 'delaware'),
    'den': ISOCodeData('', '', 'Slave (Athapascan)', 'esclave (athapascan)'),
    'dgr': ISOCodeData('', '', 'Dogrib', 'dogrib'),
    'din': ISOCodeData('', '', 'Dinka', 'dinka'),
    'div': ISOCodeData('', 'dv', 'Divehi; Dhivehi; Maldivian', 'maldivien'),
    'doi': ISOCodeData('', '', 'Dogri', 'dogri'),
    'dra': ISOCodeData(
        '',
        '',
        'Dravidian languages',
        'dravidiennes, langues',
    ),
    'dsb': ISOCodeData('', '', 'Lower Sorbian', 'bas-sorabe'),
    'dua': ISOCodeData('', '', 'Duala', 'douala'),
    'dum': ISOCodeData(
        '',
        '',
        'Dutch, Middle (ca.1050-1350)',
        'néerlandais moyen (ca. 1050-1350)',
    ),
    'dut': ISOCodeData('nld', 'nl', 'Dutch; Flemish', 'néerlandais; flamand'),
    'dyu': ISOCodeData('', '', 'Dyula', 'dioula'),
    'dzo': ISOCodeData('', 'dz', 'Dzongkha', 'dzongkha'),
    'efi': ISOCodeData('', '', 'Efik', 'efik'),
    'egy': ISOCodeData('', '', 'Egyptian (Ancient)', 'égyptien'),
    'eka': ISOCodeData('', '', 'Ekajuk', 'ekajuk'),
    'elx': ISOCodeData('', '', 'Elamite', 'élamite'),
    'eng': ISOCodeData('', 'en', 'English', 'anglais'),
    'enm': ISOCodeData(
        '',
        '',
        'English, Middle (1100-1500)',
        'anglais moyen (1100-1500)',
    ),
    'epo': ISOCodeData('', 'eo', 'Esperanto', 'espéranto'),
    'est': ISOCodeData('', 'et', 'Estonian', 'estonien'),
    'ewe': ISOCodeData('', 'ee', 'Ewe', 'éwé'),
    'ewo': ISOCodeData('', '', 'Ewondo', 'éwondo'),
    'fan': ISOCodeData('', '', 'Fang', 'fang'),
    'fao': ISOCodeData('', 'fo', 'Faroese', 'féroïen'),
    'fat': ISOCodeData('', '', 'Fanti', 'fanti'),
    'fij': ISOCodeData('', 'fj', 'Fijian', 'fidjien'),
    'fil': ISOCodeData('', '', 'Filipino; Pilipino', 'filipino; pilipino'),
    'fin': ISOCodeData('', 'fi', 'Finnish', 'finnois'),
    'fiu': ISOCodeData(
        '',
        '',
        'Finno-Ugrian languages',
        'finno-ougriennes, langues',
    ),
    'fon': ISOCodeData('', '', 'Fon', 'fon'),
    'fre': ISOCodeData('fra', 'fr', 'French', 'français'),
    'frm': ISOCodeData(
        '',
        '',
        'French, Middle (ca.1400-1600)',
        'français moyen (1400-1600)',
    ),
    'fro': ISOCodeData(
        '',
        '',
        'French, Old (842-ca.1400)',
        'français ancien (842-ca.1400)',
    ),
    'frr': ISOCodeData('', '', 'Northern Frisian', 'frison septentrional'),
    'frs': ISOCodeData('', '', 'Eastern Frisian', 'frison oriental'),
    'fry': ISOCodeData('', 'fy', 'Western Frisian', 'frison occidental'),
    'ful': ISOCodeData('', 'ff', 'Fulah', 'peul'),
    'fur': ISOCodeData('', '', 'Friulian', 'frioulan'),
    'gaa': ISOCodeData('', '', 'Ga', 'ga'),
    'gay': ISOCodeData('', '', 'Gayo', 'gayo'),
    'gba': ISOCodeData('', '', 'Gbaya', 'gbaya'),
    'gem': ISOCodeData('', '', 'Germanic languages', 'germaniques, langues'),
    'geo': ISOCodeData('kat', 'ka', 'Georgian', 'géorgien'),
    'ger': ISOCodeData('deu', 'de', 'German', 'allemand'),
    'gez': ISOCodeData('', '', 'Geez', 'guèze'),
    'gil': ISOCodeData('', '', 'Gilbertese', 'kiribati'),
    'gla': ISOCodeData(
        '',
        'gd',
        'Gaelic; Scottish Gaelic',
        'gaélique; gaélique écossais',
    ),
    'gle': ISOCodeData('', 'ga', 'Irish', 'irlandais'),
    'glg': ISOCodeData('', 'gl', 'Galician', 'galicien'),
    'glv': ISOCodeData('', 'gv', 'Manx', 'manx; mannois'),
    'gmh': ISOCodeData(
        '',
        '',
        'German, Middle High (ca.1050-1500)',
        'allemand, moyen haut (ca. 1050-1500)',
    ),
    'goh': ISOCodeData(
        '',
        '',
        'German, Old High (ca.750-1050)',
        'allemand, vieux haut (ca. 750-1050)',
    ),
    'gon': ISOCodeData('', '', 'Gondi', 'gond'),
    'gor': ISOCodeData('', '', 'Gorontalo', 'gorontalo'),
    'got': ISOCodeData('', '', 'Gothic', 'gothique'),
    'grb': ISOCodeData('', '', 'Grebo', 'grebo'),
    'grc': ISOCodeData(
        '',
        '',
        'Greek, Ancient (to 1453)',
        "grec ancien (jusqu'à 1453)",
    ),
    'gre': ISOCodeData(
        'ell',
        'el',
        'Greek, Modern (1453-)',
        'grec moderne (après 1453)',
    ),
    'grn': ISOCodeData('', 'gn', 'Guarani', 'guarani'),
    'gsw': ISOCodeData(
        '',
        '',
        'Swiss German; Alemannic; Alsatian',
        'suisse alémanique; alémanique; alsacien',
    ),
    'guj': ISOCodeData('', 'gu', 'Gujarati', 'goudjrati'),
    'gwi': ISOCodeData('', '', "Gwich'in", "gwich'in"),
    'hai': ISOCodeData('', '', 'Haida', 'haida'),
    'hat': ISOCodeData(
        '',
        'ht',
        'Haitian; Haitian Creole',
        'haïtien; créole haïtien',
    ),
    'hau': ISOCodeData('', 'ha', 'Hausa', 'haoussa'),
    'haw': ISOCodeData('', '', 'Hawaiian', 'hawaïen'),
    'heb': ISOCodeData('', 'he', 'Hebrew', 'hébreu'),
    'her': ISOCodeData('', 'hz', 'Herero', 'herero'),
    'hil': ISOCodeData('', '', 'Hiligaynon', 'hiligaynon'),
    'him': ISOCodeData(
        '',
        '',
        'Himachali languages; Western Pahari languages',
        'langues himachalis; langues paharis occidentales',
    ),
    'hin': ISOCodeData('', 'hi', 'Hindi', 'hindi'),
    'hit': ISOCodeData('', '', 'Hittite', 'hittite'),
    'hmn': ISOCodeData('', '', 'Hmong; Mong', 'hmong'),
    'hmo': ISOCodeData('', 'ho', 'Hiri Motu', 'hiri motu'),
    'hrv': ISOCodeData('', 'hr', 'Croatian', 'croate'),
    'hsb': ISOCodeData('', '', 'Upper Sorbian', 'haut-sorabe'),
    'hun': ISOCodeData('', 'hu', 'Hungarian', 'hongrois'),
    'hup': ISOCodeData('', '', 'Hupa', 'hupa'),
    'iba': ISOCodeData('', '', 'Iban', 'iban'),
    'ibo': ISOCodeData('', 'ig', 'Igbo', 'igbo'),
    'ice': ISOCodeData('isl', 'is', 'Icelandic', 'islandais'),
    'ido': ISOCodeData('', 'io', 'Ido', 'ido'),
    'iii': ISOCodeData('', 'ii', 'Sichuan Yi; Nuosu', 'yi de Sichuan'),
    'ijo': ISOCodeData('', '', 'Ijo languages', 'ijo, langues'),
    'iku': ISOCodeData('', 'iu', 'Inuktitut', 'inuktitut'),
    'ile': ISOCodeData('', 'ie', 'Interlingue; Occidental', 'interlingue'),
    'ilo': ISOCodeData('', '', 'Iloko', 'ilocano'),
    'ina': ISOCodeData(
        '',
        'ia',
        'Interlingua (International Auxiliary Language Association)',
        'interlingua (langue auxiliaire internationale)',
    ),
    'inc': ISOCodeData('', '', 'Indic languages', 'indo-aryennes, langues'),
    'ind': ISOCodeData('', 'id', 'Indonesian', 'indonésien'),
    'ine': ISOCodeData(
        '',
        '',
        'Indo-European languages',
        'indo-européennes, langues',
    ),
    'inh': ISOCodeData('', '', 'Ingush', 'ingouche'),
    'ipk': ISOCodeData('', 'ik', 'Inupiaq', 'inupiaq'),
    'ira': ISOCodeData('', '', 'Iranian languages', 'iraniennes, langues'),
    'iro': ISOCodeData('', '', 'Iroquoian languages', 'iroquoises, langues'),
    'ita': ISOCodeData('', 'it', 'Italian', 'italien'),
    'jav': ISOCodeData('', 'jv', 'Javanese', 'javanais'),
    'jbo': ISOCodeData('', '', 'Lojban', 'lojban'),
    'jpn': ISOCodeData('', 'ja', 'Japanese', 'japonais'),
    'jpr': ISOCodeData('', '', 'Judeo-Persian', 'judéo-persan'),
    'jrb': ISOCodeData('', '', 'Judeo-Arabic', 'judéo-arabe'),
    'kaa': ISOCodeData('', '', 'Kara-Kalpak', 'karakalpak'),
    'kab': ISOCodeData('', '', 'Kabyle', 'kabyle'),
    'kac': ISOCodeData('', '', 'Kachin; Jingpho', 'kachin; jingpho'),
    'kal': ISOCodeData('', 'kl', 'Kalaallisut; Greenlandic', 'groenlandais'),
    'kam': ISOCodeData('', '', 'Kamba', 'kamba'),
    'kan': ISOCodeData('', 'kn', 'Kannada', 'kannada'),
    'kar': ISOCodeData('', '', 'Karen languages', 'karen, langues'),
    'kas': ISOCodeData('', 'ks', 'Kashmiri', 'kashmiri'),
    'kau': ISOCodeData('', 'kr', 'Kanuri', 'kanouri'),
    'kaw': ISOCodeData('', '', 'Kawi', 'kawi'),
    'kaz': ISOCodeData('', 'kk', 'Kazakh', 'kazakh'),
    'kbd': ISOCodeData('', '', 'Kabardian', 'kabardien'),
    'kha': ISOCodeData('', '', 'Khasi', 'khasi'),
    'khi': ISOCodeData('', '', 'Khoisan languages', 'khoïsan, langues'),
    'khm': ISOCodeData('', 'km', 'Central Khmer', 'khmer central'),
    'kho': ISOCodeData('', '', 'Khotanese; Sakan', 'khotanais; sakan'),
    'kik': ISOCodeData('', 'ki', 'Kikuyu; Gikuyu', 'kikuyu'),
    'kin': ISOCodeData('', 'rw', 'Kinyarwanda', 'rwanda'),
    'kir': ISOCodeData('', 'ky', 'Kirghiz; Kyrgyz', 'kirghiz'),
    'kmb': ISOCodeData('', '', 'Kimbundu', 'kimbundu'),
    'kok': ISOCodeData('', '', 'Konkani', 'konkani'),
    'kom': ISOCodeData('', 'kv', 'Komi', 'kom'),
    'kon': ISOCodeData('', 'kg', 'Kongo', 'kongo'),
    'kor': ISOCodeData('', 'ko', 'Korean', 'coréen'),
    'kos': ISOCodeData('', '', 'Kosraean', 'kosrae'),
    'kpe': ISOCodeData('', '', 'Kpelle', 'kpellé'),
    'krc': ISOCodeData('', '', 'Karachay-Balkar', 'karatchai balkar'),
    'krl': ISOCodeData('', '', 'Karelian', 'carélien'),
    'kro': ISOCodeData('', '', 'Kru languages', 'krou, langues'),
    'kru': ISOCodeData('', '', 'Kurukh', 'kurukh'),
    'kua': ISOCodeData('', 'kj', 'Kuanyama; Kwanyama', 'kuanyama; kwanyama'),
    'kum': ISOCodeData('', '', 'Kumyk', 'koumyk'),
    'kur': ISOCodeData('', 'ku', 'Kurdish', 'kurde'),
    'kut': ISOCodeData('', '', 'Kutenai', 'kutenai'),
    'lad': ISOCodeData('', '', 'Ladino', 'judéo-espagnol'),
    'lah': ISOCodeData('', '', 'Lahnda', 'lahnda'),
    'lam': ISOCodeData('', '', 'Lamba', 'lamba'),
    'lao': ISOCodeData('', 'lo', 'Lao', 'lao'),
    'lat': ISOCodeData('', 'la', 'Latin', 'latin'),
    'lav': ISOCodeData('', 'lv', 'Latvian', 'letton'),
    'lez': ISOCodeData('', '', 'Lezghian', 'lezghien'),
    'lim': ISOCodeData(
        '',
        'li',
        'Limburgan; Limburger; Limburgish',
        'limbourgeois',
    ),
    'lin': ISOCodeData('', 'ln', 'Lingala', 'lingala'),
    'lit': ISOCodeData('', 'lt', 'Lithuanian', 'lituanien'),
    'lol': ISOCodeData('', '', 'Mongo', 'mongo'),
    'loz': ISOCodeData('', '', 'Lozi', 'lozi'),
    'ltz': ISOCodeData(
        '',
        'lb',
        'Luxembourgish; Letzeburgesch',
        'luxembourgeois',
    ),
    'lua': ISOCodeData('', '', 'Luba-Lulua', 'luba-lulua'),
    'lub': ISOCodeData('', 'lu', 'Luba-Katanga', 'luba-katanga'),
    'lug': ISOCodeData('', 'lg', 'Ganda', 'ganda'),
    'lui': ISOCodeData('', '', 'Luiseno', 'luiseno'),
    'lun': ISOCodeData('', '', 'Lunda', 'lunda'),
    'luo': ISOCodeData(
        '',
        '',
        'Luo (Kenya and Tanzania)',
        'luo (Kenya et Tanzanie)',
    ),
    'lus': ISOCodeData('', '', 'Lushai', 'lushai'),
    'mac': ISOCodeData('mkd', 'mk', 'Macedonian', 'macédonien'),
    'mad': ISOCodeData('', '', 'Madurese', 'madourais'),
    'mag': ISOCodeData('', '', 'Magahi', 'magahi'),
    'mah': ISOCodeData('', 'mh', 'Marshallese', 'marshall'),
    'mai': ISOCodeData('', '', 'Maithili', 'maithili'),
    'mak': ISOCodeData('', '', 'Makasar', 'makassar'),
    'mal': ISOCodeData('', 'ml', 'Malayalam', 'malayalam'),
    'man': ISOCodeData('', '', 'Mandingo', 'mandingue'),
    'mao': ISOCodeData('mri', 'mi', 'Maori', 'maori'),
    'map': ISOCodeData(
        '',
        '',
        'Austronesian languages',
        'austronésiennes, langues',
    ),
    'mar': ISOCodeData('', 'mr', 'Marathi', 'marathe'),
    'mas': ISOCodeData('', '', 'Masai', 'massaï'),
    'may': ISOCodeData('msa', 'ms', 'Malay', 'malais'),
    'mdf': ISOCodeData('', '', 'Moksha', 'moksa'),
    'mdr': ISOCodeData('', '', 'Mandar', 'mandar'),
    'men': ISOCodeData('', '', 'Mende', 'mendé'),
    'mga': ISOCodeData(
        '',
        '',
        'Irish, Middle (900-1200)',
        'irlandais moyen (900-1200)',
    ),
    'mic': ISOCodeData('', '', "Mi'kmaq; Micmac", "mi'kmaq; micmac"),
    'min': ISOCodeData('', '', 'Minangkabau', 'minangkabau'),
    'mis': ISOCodeData('', '', 'Uncoded languages', 'langues non codées'),
    'mkh': ISOCodeData('', '', 'Mon-Khmer languages', 'môn-khmer, langues'),
    'mlg': ISOCodeData('', 'mg', 'Malagasy', 'malgache'),
    'mlt': ISOCodeData('', 'mt', 'Maltese', 'maltais'),
    'mnc': ISOCodeData('', '', 'Manchu', 'mandchou'),
    'mni': ISOCodeData('', '', 'Manipuri', 'manipuri'),
    'mno': ISOCodeData('', '', 'Manobo languages', 'manobo, langues'),
    'moh': ISOCodeData('', '', 'Mohawk', 'mohawk'),
    'mon': ISOCodeData('', 'mn', 'Mongolian', 'mongol'),
    'mos': ISOCodeData('', '', 'Mossi', 'moré'),
    'mul': ISOCodeData('', '', 'Multiple languages', 'multilingue'),
    'mun': ISOCodeData('', '', 'Munda languages', 'mounda, langues'),
    'mus': ISOCodeData('', '', 'Creek', 'muskogee'),
    'mwl': ISOCodeData('', '', 'Mirandese', 'mirandais'),
    'mwr': ISOCodeData('', '', 'Marwari', 'marvari'),
    'myn': ISOCodeData('', '', 'Mayan languages', 'maya, langues'),
    'myv': ISOCodeData('', '', 'Erzya', 'erza'),
    'nah': ISOCodeData('', '', 'Nahuatl languages', 'nahuatl, langues'),
    'nai': ISOCodeData(
        '',
        '',
        'North American Indian languages',
        'nord-amérindiennes, langues',
    ),
    'nap': ISOCodeData('', '', 'Neapolitan', 'napolitain'),
    'nau': ISOCodeData('', 'na', 'Nauru', 'nauruan'),
    'nav': ISOCodeData('', 'nv', 'Navajo; Navaho', 'navaho'),
    'nbl': ISOCodeData(
        '',
        'nr',
        'Ndebele, South; South Ndebele',
        'ndébélé du Sud',
    ),
    'nde': ISOCodeData(
        '',
        'nd',
        'Ndebele, North; North Ndebele',
        'ndébélé du Nord',
    ),
    'ndo': ISOCodeData('', 'ng', 'Ndonga', 'ndonga'),
    'nds': ISOCodeData(
        '',
        '',
        'Low German; Low Saxon; German, Low; Saxon, Low',
        'bas allemand; bas saxon; allemand, bas; saxon, bas',
    ),
    'nep': ISOCodeData('', 'ne', 'Nepali', 'népalais'),
    'new': ISOCodeData('', '', 'Nepal Bhasa; Newari', 'nepal bhasa; newari'),
    'nia': ISOCodeData('', '', 'Nias', 'nias'),
    'nic': ISOCodeData(
        '',
        '',
        'Niger-Kordofanian languages',
        'nigéro-kordofaniennes, langues',
    ),
    'niu': ISOCodeData('', '', 'Niuean', 'niué'),
    'nno': ISOCodeData(
        '',
        'nn',
        'Norwegian Nynorsk; Nynorsk, Norwegian',
        'norvégien nynorsk; nynorsk, norvégien',
    ),
    'nob': ISOCodeData(
        '',
        'nb',
        'Bokmål, Norwegian; Norwegian Bokmål',
        'norvégien bokmål',
    ),
    'nog': ISOCodeData('', '', 'Nogai', 'nogaï; nogay'),
    'non': ISOCodeData('', '', 'Norse, Old', 'norrois, vieux'),
    'nor': ISOCodeData('', 'no', 'Norwegian', 'norvégien'),
    'nqo': ISOCodeData('', '', "N'Ko", "n'ko"),
    'nso': ISOCodeData(
        '',
        '',
        'Pedi; Sepedi; Northern Sotho',
        'pedi; sepedi; sotho du Nord',
    ),
    'nub': ISOCodeData('', '', 'Nubian languages', 'nubiennes, langues'),
    'nwc': ISOCodeData(
        '',
        '',
        'Classical Newari; Old Newari; Classical Nepal Bhasa',
        'newari classique',
    ),
    'nya': ISOCodeData(
        '',
        'ny',
        'Chichewa; Chewa; Nyanja',
        'chichewa; chewa; nyanja',
    ),
    'nym': ISOCodeData('', '', 'Nyamwezi', 'nyamwezi'),
    'nyn': ISOCodeData('', '', 'Nyankole', 'nyankolé'),
    'nyo': ISOCodeData('', '', 'Nyoro', 'nyoro'),
    'nzi': ISOCodeData('', '', 'Nzima', 'nzema'),
    'oci': ISOCodeData(
        '',
        'oc',
        'Occitan (post 1500)',
        'occitan (après 1500)',
    ),
    'oji': ISOCodeData('', 'oj', 'Ojibwa', 'ojibwa'),
    'ori': ISOCodeData('', 'or', 'Oriya', 'oriya'),
    'orm': ISOCodeData('', 'om', 'Oromo', 'galla'),
    'osa': ISOCodeData('', '', 'Osage', 'osage'),
    'oss': ISOCodeData('', 'os', 'Ossetian; Ossetic', 'ossète'),
    'ota': ISOCodeData(
        '',
        '',
        'Turkish, Ottoman (1500-1928)',
        'turc ottoman (1500-1928)',
    ),
    'oto': ISOCodeData('', '', 'Otomian languages', 'otomi, langues'),
    'paa': ISOCodeData('', '', 'Papuan languages', 'papoues, langues'),
    'pag': ISOCodeData('', '', 'Pangasinan', 'pangasinan'),
    'pal': ISOCodeData('', '', 'Pahlavi', 'pahlavi'),
    'pam': ISOCodeData('', '', 'Pampanga; Kapampangan', 'pampangan'),
    'pan': ISOCodeData('', 'pa', 'Panjabi; Punjabi', 'pendjabi'),
    'pap': ISOCodeData('', '', 'Papiamento', 'papiamento'),
    'pau': ISOCodeData('', '', 'Palauan', 'palau'),
    'peo': ISOCodeData(
        '',
        '',
        'Persian, Old (ca.600-400 B.C.)',
        'perse, vieux (ca. 600-400 av. J.-C.)',
    ),
    'per': ISOCodeData('fas', 'fa', 'Persian', 'persan'),
    'phi': ISOCodeData(
        '',
        '',
        'Philippine languages',
        'philippines, langues',
    ),
    'phn': ISOCodeData('', '', 'Phoenician', 'phénicien'),
    'pli': ISOCodeData('', 'pi', 'Pali', 'pali'),
    'pol': ISOCodeData('', 'pl', 'Polish', 'polonais'),
    'pon': ISOCodeData('', '', 'Pohnpeian', 'pohnpei'),
    'por': ISOCodeData('', 'pt', 'Portuguese', 'portugais'),
    'pra': ISOCodeData('', '', 'Prakrit languages', 'prâkrit, langues'),
    'pro': ISOCodeData(
        '',
        '',
        'Provençal, Old (to 1500); Occitan, Old (to 1500)',
        "provençal ancien (jusqu'à 1500); occitan ancien (jusqu'à 1500)",
    ),
    'pus': ISOCodeData('', 'ps', 'Pushto; Pashto', 'pachto'),
    'qaa': ISOCodeData(
        '',
        '',
        'Reserved for local use',
        "réservée à l'usage local",
    ),
    'que': ISOCodeData('', 'qu', 'Quechua', 'quechua'),
    'raj': ISOCodeData('', '', 'Rajasthani', 'rajasthani'),
    'rap': ISOCodeData('', '', 'Rapanui', 'rapanui'),
    'rar': ISOCodeData(
        '',
        '',
        'Rarotongan; Cook Islands Maori',
        'rarotonga; maori des îles Cook',
    ),
    'roa': ISOCodeData('', '', 'Romance languages', 'romanes, langues'),
    'roh': ISOCodeData('', 'rm', 'Romansh', 'romanche'),
    'rom': ISOCodeData('', '', 'Romany', 'tsigane'),
    'rum': ISOCodeData(
        'ron',
        'ro',
        'Romanian; Moldavian; Moldovan',
        'roumain; moldave',
    ),
    'run': ISOCodeData('', 'rn', 'Rundi', 'rundi'),
    'rup': ISOCodeData(
        '',
        '',
        'Aromanian; Arumanian; Macedo-Romanian',
        'aroumain; macédo-roumain',
    ),
    'rus': ISOCodeData('', 'ru', 'Russian', 'russe'),
    'sad': ISOCodeData('', '', 'Sandawe', 'sandawe'),
    'sag': ISOCodeData('', 'sg', 'Sango', 'sango'),
    'sah': ISOCodeData('', '', 'Yakut', 'iakoute'),
    'sai': ISOCodeData(
        '',
        '',
        'South American Indian languages',
        'sud-amérindiennes, langues',
    ),
    'sal': ISOCodeData('', '', 'Salishan languages', 'salishennes, langues'),
    'sam': ISOCodeData('', '', 'Samaritan Aramaic', 'samaritain'),
    'san': ISOCodeData('', 'sa', 'Sanskrit', 'sanskrit'),
    'sas': ISOCodeData('', '', 'Sasak', 'sasak'),
    'sat': ISOCodeData('', '', 'Santali', 'santal'),
    'scn': ISOCodeData('', '', 'Sicilian', 'sicilien'),
    'sco': ISOCodeData('', '', 'Scots', 'écossais'),
    'sel': ISOCodeData('', '', 'Selkup', 'selkoupe'),
    'sem': ISOCodeData('', '', 'Semitic languages', 'sémitiques, langues'),
    'sga': ISOCodeData(
        '',
        '',
        'Irish, Old (to 900)',
        "irlandais ancien (jusqu'à 900)",
    ),
    'sgn': ISOCodeData('', '', 'Sign Languages', 'langues des signes'),
    'shn': ISOCodeData('', '', 'Shan', 'chan'),
    'sid': ISOCodeData('', '', 'Sidamo', 'sidamo'),
    'sin': ISOCodeData('', 'si', 'Sinhala; Sinhalese', 'singhalais'),
    'sio': ISOCodeData('', '', 'Siouan languages', 'sioux, langues'),
    'sit': ISOCodeData(
        '',
        '',
        'Sino-Tibetan languages',
        'sino-tibétaines, langues',
    ),
    'sla': ISOCodeData('', '', 'Slavic languages', 'slaves, langues'),
    'slo': ISOCodeData('slk', 'sk', 'Slovak', 'slovaque'),
    'slv': ISOCodeData('', 'sl', 'Slovenian', 'slovène'),
    'sma': ISOCodeData('', '', 'Southern Sami', 'sami du Sud'),
    'sme': ISOCodeData('', 'se', 'Northern Sami', 'sami du Nord'),
    'smi': ISOCodeData('', '', 'Sami languages', 'sames, langues'),
    'smj': ISOCodeData('', '', 'Lule Sami', 'sami de Lule'),
    'smn': ISOCodeData('', '', 'Inari Sami', "sami d'Inari"),
    'smo': ISOCodeData('', 'sm', 'Samoan', 'samoan'),
    'sms': ISOCodeData('', '', 'Skolt Sami', 'sami skolt'),
    'sna': ISOCodeData('', 'sn', 'Shona', 'shona'),
    'snd': ISOCodeData('', 'sd', 'Sindhi', 'sindhi'),
    'snk': ISOCodeData('', '', 'Soninke', 'soninké'),
    'sog': ISOCodeData('', '', 'Sogdian', 'sogdien'),
    'som': ISOCodeData('', 'so', 'Somali', 'somali'),
    'son': ISOCodeData('', '', 'Songhai languages', 'songhai, langues'),
    'sot': ISOCodeData('', 'st', 'Sotho, Southern', 'sotho du Sud'),
    'spa': ISOCodeData('', 'es', 'Spanish; Castilian', 'espagnol; castillan'),
    'srd': ISOCodeData('', 'sc', 'Sardinian', 'sarde'),
    'srn': ISOCodeData('', '', 'Sranan Tongo', 'sranan tongo'),
    'srp': ISOCodeData('', 'sr', 'Serbian', 'serbe'),
    'srr': ISOCodeData('', '', 'Serer', 'sérère'),
    'ssa': ISOCodeData(
        '',
        '',
        'Nilo-Saharan languages',
        'nilo-sahariennes, langues',
    ),
    'ssw': ISOCodeData('', 'ss', 'Swati', 'swati'),
    'suk': ISOCodeData('', '', 'Sukuma', 'sukuma'),
    'sun': ISOCodeData('', 'su', 'Sundanese', 'soundanais'),
    'sus': ISOCodeData('', '', 'Susu', 'soussou'),
    'sux': ISOCodeData('', '', 'Sumerian', 'sumérien'),
    'swa': ISOCodeData('', 'sw', 'Swahili', 'swahili'),
    'swe': ISOCodeData('', 'sv', 'Swedish', 'suédois'),
    'syc': ISOCodeData('', '', 'Classical Syriac', 'syriaque classique'),
    'syr': ISOCodeData('', '', 'Syriac', 'syriaque'),
    'tah': ISOCodeData('', 'ty', 'Tahitian', 'tahitien'),
    'tai': ISOCodeData('', '', 'Tai languages', 'tai, langues'),
    'tam': ISOCodeData('', 'ta', 'Tamil', 'tamoul'),
    'tat': ISOCodeData('', 'tt', 'Tatar', 'tatar'),
    'tel': ISOCodeData('', 'te', 'Telugu', 'télougou'),
    'tem': ISOCodeData('', '', 'Timne', 'temne'),
    'ter': ISOCodeData('', '', 'Tereno', 'tereno'),
    'tet': ISOCodeData('', '', 'Tetum', 'tetum'),
    'tgk': ISOCodeData('', 'tg', 'Tajik', 'tadjik'),
    'tgl': ISOCodeData('', 'tl', 'Tagalog', 'tagalog'),
    'tha': ISOCodeData('', 'th', 'Thai', 'thaï'),
    'tib': ISOCodeData('bod', 'bo', 'Tibetan', 'tibétain'),
    'tig': ISOCodeData('', '', 'Tigre', 'tigré'),
    'tir': ISOCodeData('', 'ti', 'Tigrinya', 'tigrigna'),
    'tiv': ISOCodeData('', '', 'Tiv', 'tiv'),
    'tkl': ISOCodeData('', '', 'Tokelau', 'tokelau'),
    'tlh': ISOCodeData('', '', 'Klingon; tlhIngan-Hol', 'klingon'),
    'tli': ISOCodeData('', '', 'Tlingit', 'tlingit'),
    'tmh': ISOCodeData('', '', 'Tamashek', 'tamacheq'),
    'tog': ISOCodeData('', '', 'Tonga (Nyasa)', 'tonga (Nyasa)'),
    'ton': ISOCodeData(
        '',
        'to',
        'Tonga (Tonga Islands)',
        'tongan (Îles Tonga)',
    ),
    'tpi': ISOCodeData('', '', 'Tok Pisin', 'tok pisin'),
    'tsi': ISOCodeData('', '', 'Tsimshian', 'tsimshian'),
    'tsn': ISOCodeData('', 'tn', 'Tswana', 'tswana'),
    'tso': ISOCodeData('', 'ts', 'Tsonga', 'tsonga'),
    'tuk': ISOCodeData('', 'tk', 'Turkmen', 'turkmène'),
    'tum': ISOCodeData('', '', 'Tumbuka', 'tumbuka'),
    'tup': ISOCodeData('', '', 'Tupi languages', 'tupi, langues'),
    'tur': ISOCodeData('', 'tr', 'Turkish', 'turc'),
    'tut': ISOCodeData('', '', 'Altaic languages', 'altaïques, langues'),
    'tvl': ISOCodeData('', '', 'Tuvalu', 'tuvalu'),
    'twi': ISOCodeData('', 'tw', 'Twi', 'twi'),
    'tyv': ISOCodeData('', '', 'Tuvinian', 'touva'),
    'udm': ISOCodeData('', '', 'Udmurt', 'oudmourte'),
    'uga': ISOCodeData('', '', 'Ugaritic', 'ougaritique'),
    'uig': ISOCodeData('', 'ug', 'Uighur; Uyghur', 'ouïgour'),
    'ukr': ISOCodeData('', 'uk', 'Ukrainian', 'ukrainien'),
    'umb': ISOCodeData('', '', 'Umbundu', 'umbundu'),
    'und': ISOCodeData('', '', 'Undetermined', 'indéterminée'),
    'urd': ISOCodeData('', 'ur', 'Urdu', 'ourdou'),
    'uzb': ISOCodeData('', 'uz', 'Uzbek', 'ouszbek'),
    'vai': ISOCodeData('', '', 'Vai', 'vaï'),
    'ven': ISOCodeData('', 've', 'Venda', 'venda'),
    'vie': ISOCodeData('', 'vi', 'Vietnamese', 'vietnamien'),
    'vol': ISOCodeData('', 'vo', 'Volapük', 'volapük'),
    'vot': ISOCodeData('', '', 'Votic', 'vote'),
    'wak': ISOCodeData('', '', 'Wakashan languages', 'wakashanes, langues'),
    'wal': ISOCodeData('', '', 'Wolaitta; Wolaytta', 'wolaitta; wolaytta'),
    'war': ISOCodeData('', '', 'Waray', 'waray'),
    'was': ISOCodeData('', '', 'Washo', 'washo'),
    'wel': ISOCodeData('cym', 'cy', 'Welsh', 'gallois'),
    'wen': ISOCodeData('', '', 'Sorbian languages', 'sorabes, langues'),
    'wln': ISOCodeData('', 'wa', 'Walloon', 'wallon'),
    'wol': ISOCodeData('', 'wo', 'Wolof', 'wolof'),
    'xal': ISOCodeData('', '', 'Kalmyk; Oirat', 'kalmouk; oïrat'),
    'xho': ISOCodeData('', 'xh', 'Xhosa', 'xhosa'),
    'yao': ISOCodeData('', '', 'Yao', 'yao'),
    'yap': ISOCodeData('', '', 'Yapese', 'yapois'),
    'yid': ISOCodeData('', 'yi', 'Yiddish', 'yiddish'),
    'yor': ISOCodeData('', 'yo', 'Yoruba', 'yoruba'),
    'ypk': ISOCodeData('', '', 'Yupik languages', 'yupik, langues'),
    'zap': ISOCodeData('', '', 'Zapotec', 'zapotèque'),
    'zbl': ISOCodeData(
        '',
        '',
        'Blissymbols; Blissymbolics; Bliss',
        'symboles Bliss; Bliss',
    ),
    'zen': ISOCodeData('', '', 'Zenaga', 'zenaga'),
    'zgh': ISOCodeData(
        '',
        '',
        'Standard Moroccan Tamazight',
        'amazighe standard marocain',
    ),
    'zha': ISOCodeData('', 'za', 'Zhuang; Chuang', 'zhuang; chuang'),
    'znd': ISOCodeData('', '', 'Zande languages', 'zandé, langues'),
    'zul': ISOCodeData('', 'zu', 'Zulu', 'zoulou'),
    'zun': ISOCodeData('', '', 'Zuni', 'zuni'),
    'zxx': ISOCodeData(
        '',
        '',
        'No linguistic content; Not applicable',
        'pas de contenu linguistique; non applicable',
    ),
    'zza': ISOCodeData(
        '',
        '',
        'Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki',
        'zaza; dimili; dimli; kirdki; kirmanjki; zazaki',
    ),
}


def iso_639_2_from_3(iso3: str) -> str:
    """Convert ISO 639-3 code to ISO 639-2 code."""
    if iso3 in ISO_639_3:
        return ISO_639_3[iso3].alpha_2
    else:
        return ""
