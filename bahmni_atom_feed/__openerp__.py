{
    "name": "Bahmni  Event Publisher",
    "version": "1.0",
    "depends": ["base","product","sale","account"],
    "author": "ThoughtWorks Technologies Pvt. Ltd.",
    "category": "Product",
	"summary": "Event Publisher",
    "description": """
    """,
    'data': [
        "security/ir.model.access.csv",
        "atom_event_sequence.xml",
        "sale_order_group_filter.xml",
        "order_type_shop_map_view.xml"
    ],
    'demo': [],
    'css' : [
        ],

    'auto_install': False,
    'application': True,
    'installable': True,
#    'certificate': 'certificate',
}
