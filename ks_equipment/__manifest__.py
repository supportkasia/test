{
    'name': 'KS Equipment', # Nom affiché dans Odoo (Applications)
    'version': '0.1', # Version du module
    'category': 'Manufacturing/Equipment', # Catégorie (où trouver le module)
    'summary': 'Module of equipment managing for the employees', # Résumé court
    'description': """
        A little test of module about equipment for learning step by step about Odoo development
    """, # Description détaillée
    'author': 'kasia',
    'website': 'https://www.yourcompany.com',  # mettre le lien su site web sur lequel sera placé tout le code si vous en avez (champs facultatif)

    # Modules Odoo dont ce module dépend.
    'depends': ['base', 'hr', 'product'],# 'base' est presque toujours nécessaire puis 'hr' pour les employés (hr.employee) et 'product' pour les articles (product.template, product.category)
    'data': [
        'security/ir.model.access.csv',
        'report/product_attribution_report_attestation_restitution.xml',
        'report/product_attribution_report.xml',
        # 'report/product_attribution_template.xml',
        'views/product_attribution_views.xml',
    ],
    'installable': True, # pour qu il soit installable en tant que nouveau module
    'application': True, # toujours en FALSE de base pour eviter son installation des le démarrage du serveur
    'license': 'LGPL-3', # licence permettant la création et modification du code et de le distribuer, même dans des applications propriétaires, en respectant les règles
}