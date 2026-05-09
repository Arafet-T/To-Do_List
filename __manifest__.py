{
    'name': 'To-Do List',
    'author': 'Arafet Tekaya',
    'category': 'Productivity',
    'version': '19.0.0.1.0',
    'depends': ['base', 'mail'],
    'data': [
        'views/base_menu.xml',
        'views/todo_task_view.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
            'web.assets_backend' : ['todo_management/static/src/css/todo_task.css']
        },
    'application': True,
}