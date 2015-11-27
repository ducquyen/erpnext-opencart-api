from __future__ import unicode_literals
from frappe import _, msgprint, throw
from frappe.utils import cint, cstr, flt
from erpnext.accounts.party import get_party_account, get_due_date

from frappe.model.mapper import get_mapped_doc
import frappe


@frappe.whitelist()
def get_sales_statistic(sales_order):
    back_order_no = frappe.db.get_values('Back Order', {'docstatus': '0', 'customer': frappe.db.get_value('Sales Order', sales_order, 'customer')}, 'name')
    delivery_note_no = frappe.db.get_values('Delivery Note', {'sales_order': sales_order}, 'name')
    sales_invoice_no = frappe.db.get_values('Sales Invoice', {'sales_order': sales_order}, 'name')
    packing_slip_no = frappe.db.get_values('Packing Slip', {'sales_order': sales_order}, 'name')
    return {
        'back_order': back_order_no,
        'delivery_note': delivery_note_no,
        'sales_invoice': sales_invoice_no,
        'packing_slip': packing_slip_no
    }
