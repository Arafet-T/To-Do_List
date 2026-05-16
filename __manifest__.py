{
    'name': 'To-Do List',
    'author': 'Arafet Tekaya',
    'category': 'Productivity',
    'version': '19.0.0.1.0',
    'depends': ['base', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/base_menu.xml',
        'views/todo_task_view.xml',
        'wizards/bulk_task_assignment_wizard_view.xml',
        'reports/todo_task_report.xml'
    ],
    'assets': {
            'web.assets_backend' : ['todo_management/static/src/css/todo_task.css']
        },
    'application': True,
}