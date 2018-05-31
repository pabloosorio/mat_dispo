{
    'name': 'Bibo',
    'version': '10.0.0',
    'summary': 'Personalizacion de bibo',
    'description': 'Modificacion de la orden de compra, factura,pedido de venta',
    'category': 'Personalizaicion',
    'author': 'Raul Ovalle, Nayeli Valencia Díaz',
    'website': 'www.xmarts.com',
    'depends': [
        'purchase',
        'purchase_discount',
                ],
    'data': [
        'reports/purchase_order_report.xml',
        'reports/invoice_report.xml',
        'reports/report.xml',
        'reports/report_sale.xml',
        'views/product_template_view.xml',

    ],
    'installable': True,
    'auto_install': False,
}
