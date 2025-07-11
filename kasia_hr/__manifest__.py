{
    'name': 'KS HR', # Nom affiché dans Odoo (Applications)
    'version': '0.1', # Version du module
    'category': 'Human Resources', # Catégorie (où trouver le module)
    'summary': 'Module for extending HR Employee functionalities for Kasia', # Résumé court
    'description': """
        A little test of module about hr for learning step by step about Odoo development for more accuracy heritage
    """, # Description détaillée
    'author': 'kasia',
    'website': 'https://www.yourcompany.com',  # mettre le lien su site web sur lequel sera placé tout le code si vous en avez (champs facultatif)

    # Modules Odoo dont ce module dépend.
    'depends': ['base', 'hr'],# 'base' est presque toujours nécessaire puis 'hr' pour les employés (hr.employee) et 'product' pour les articles (product.template, product.category)
    'data': ['security/ir.model.access.csv',
             'views/hr_employee_inherit_view.xml',
    ],
    'installable': True, # pour qu il soit installable en tant que nouveau module
    'application': True, # toujours en FALSE de base pour eviter son installation des le démarrage du serveur
    'license': 'LGPL-3', # licence permettant la création et modification du code et de le distribuer, même dans des applications propriétaires, en respectant les règles
}