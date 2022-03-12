from collections import defaultdict


# Custom tag
CITED_BY_TAG = 'CB'
CITED_BY_TEXT = 'Cited By'

NOTE_TAG = 'N1'
TYPE_TAG = 'TY'
END_REFERENCE_TAG = 'ER'

CSV_DELIMITER = '\t'
SUB_DELIMITER = ' | '

# https://en.wikipedia.org/wiki/RIS_(file_format)
TAG_KEY_MAPPING = defaultdict(
    lambda: 'unknown_tag',
    {
        'TY': 'type_of_reference',
        'A1': 'first_authors',
        'A2': 'secondary_authors',
        'A3': 'tertiary_authors',
        'A4': 'subsidiary_authors',
        'AB': 'abstract',
        'AD': 'author_address',
        'AN': 'accession_number',
        'AU': 'authors',
        'AV': 'location_in_archives',
        'BT': 'secondary_title_references',
        'C1': 'custom1',
        'C2': 'custom2',
        'C3': 'custom3',
        'C4': 'custom4',
        'C5': 'custom5',
        'C6': 'custom6',
        'C7': 'custom7',
        'C8': 'custom8',
        'CA': 'caption',
        'CB': 'cited_by',
        'CN': 'call_number',
        'CP': 'cp_field',
        'CT': 'title_of_unpublished_reference',
        'CY': 'place_published',
        'DA': 'date',
        'DB': 'name_of_database',
        'DO': 'doi',
        'DP': 'database_provider',
        'ED': 'editor',
        'EP': 'end_page',
        'ET': 'edition',
        'ID': 'id',
        'IS': 'number',
        'J1': 'periodical_name',
        'J2': 'alternate_title1',
        'JA': 'alternate_title2',
        'JF': 'alternate_title3',
        'JO': 'journal_name',
        'KW': 'keywords',
        'L1': 'file_attachments1',
        'L2': 'file_attachments2',
        'L3': 'related_records',
        'L4': 'figure',
        'LA': 'language',
        'LB': 'label',
        'LK': 'website_link',
        'M1': 'note',
        'M2': 'miscellaneous_2',
        'M3': 'type_of_work',
        'N1': 'notes',
        'N2': 'abstract',
        'NV': 'number_of_Volumes',
        'OP': 'original_publication',
        'PB': 'publisher',
        'PP': 'publishing_place ',
        'PY': 'year',
        'RI': 'reviewed_item',
        'RN': 'research_notes',
        'RP': 'reprint_edition',
        'SE': 'version',
        'SN': 'issn',
        'SP': 'start_page',
        'ST': 'short_title',
        'T1': 'primary_title',
        'T2': 'secondary_title',
        'T3': 'tertiary_title',
        'TA': 'translated_author',
        'TI': 'title',
        'TT': 'translated_title',
        'U1': 'user_definable_1',
        'U2': 'user_definable_2',
        'U3': 'user_definable_3',
        'U4': 'user_definable_4',
        'U5': 'user_definable_5',
        'UR': 'url',
        'VL': 'volume',
        'VO': 'published_standard_number',
        'Y1': 'publication_year',
        'Y2': 'access_date',
        'ER': 'end_of_reference',
        'UK': 'unknown_tag',
    }
)

TYPE_REFERENCE_MAPPING = defaultdict(
    lambda: 'unknown_type_reference',
    {
        'ABST': 'abstract',
        'ADVS': 'audiovisual_material',
        'AGGR': 'aggregated_database',
        'ANCIENT': 'ancient_text',
        'ART': 'art_work',
        'BILL': 'bill',
        'BLOG': 'blog',
        'BOOK': 'whole_book',
        'CASE': 'case',
        'CHAP': 'book_chapter',
        'CHART': 'chart',
        'CLSWK': 'classical_work',
        'COMP': 'computer_program',
        'CONF': 'conference_proceeding',
        'CPAPER': 'conference_paper',
        'CTLG': 'catalog',
        'DATA': 'data_file',
        'DBASE': 'online_database',
        'DICT': 'dictionary',
        'EBOOK': 'electronic_book',
        'ECHAP': 'electronic_book_section',
        'EDBOOK': 'edited_book',
        'EJOUR': 'electronic_article',
        'WEB': 'web_page',
        'ENCYC': 'encyclopedia',
        'EQUA': 'equation',
        'FIGURE': 'figure',
        'GEN': 'generic',
        'GOVDOC': 'government_document',
        'GRANT': 'grant',
        'HEAR': 'hearing',
        'ICOMM': 'internet_communication',
        'INPR': 'in_press',
        'JFULL': 'journal_(full)',
        'JOUR': 'journal',
        'LEGAL': 'legal_rule_or_regulation',
        'MANSCPT': 'manuscript',
        'MAP': 'map',
        'MGZN': 'magazine_article',
        'MPCT': 'motion_picture',
        'MULTI': 'online_multimedia',
        'MUSIC': 'music_score',
        'NEWS': 'newspaper',
        'PAMP': 'pamphlet',
        'PAT': 'patent',
        'PCOMM': 'personal_communication',
        'RPRT': 'report',
        'SER': 'serial_publication',
        'SLIDE': 'slide',
        'SOUND': 'sound_recording',
        'STAND': 'standard',
        'STAT': 'statute',
        'THES': 'thesis/dissertation',
        'UNBILL': 'unenacted_bill',
        'UNPB': 'unpublished_work',
        'VIDEO': 'video_recording'
    }
)
