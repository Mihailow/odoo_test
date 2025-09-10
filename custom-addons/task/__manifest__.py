{
    'name': 'Task',
    'version': '1.0',
    'author': 'Михаил Брамник',
    'category': 'Custom',
    'depends': ['base'],
    'data': [
        'security/task_groups.xml',
        'security/ir.model.access.csv',
        'security/task_rules.xml',
        'views/task_view.xml',
    ],
    'installable': True,
    'application': True,
}
