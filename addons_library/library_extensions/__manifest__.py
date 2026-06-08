{
    "name": "Library Extension",
    "depends": ['library'],
    "summary": "Extension for the library module",
    'data':[
        'security/ir.model.access.csv', 
        'views/library_book_views.xml',
        'views/menu.xml'
    ],
    'installable': True,
    'application':False,

}