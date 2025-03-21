{
    "name": "Student Management",
    "summary": "Module quản lý thông tin sinh viên",
    "author": "Lê Bá Dũng",
    "category": "Education",
    'depends': ['base', 'contacts'],
    'description': """
    Quản lý Sinh Viên
    """,
    "sequence": -900,
    "data": [
        "security/student_management_groups.xml",
        "security/ir.model.access.csv",
        "views/book_views.xml",
        "views/student_views.xml",
        "views/sequence.xml",
        'data/library_book_sequence.xml'
    ],
    "installable": True,
    "application": True,
}
