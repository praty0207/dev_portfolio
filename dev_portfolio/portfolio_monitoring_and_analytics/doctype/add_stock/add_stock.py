# Copyright (c) 2023, Panigrahis.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AddStock(Document):
	def portfolio_stock_recalc(company):
		

	def after_submit(self):
		company = self.company_code
		portfolio_stock_recalc(company)
		frappe.log("log part-1" + company)
		companies_frm_db = frappe.db.get_list("Add Stock", filters={"company_code": company}, fields=["company_code", "quantity", 'investment'])
		#frappe.msgprint(companies_frm_db)
		frappe.log(companies_frm_db)
		count_transactions = len(companies_frm_db)
		frappe.msgprint(str(count_transactions))

		total_stock_investment = 0
		count_stocks = 0

		for item in range(count_transactions):
			total_stock_investment = total_stock_investment + companies_frm_db[item]['investment']
			count_stocks = count_stocks + companies_frm_db[item]['quantity']
  
		cumulative_quantity = count_stocks
		total_invested = total_stock_investment
		average_price_of_buying = round(total_invested / cumulative_quantity, 2)
		number_of_transactions = count_transactions


		if(frappe.db.exists({"doctype":"Stocks", "company_code":company})):

			exist_doc = frappe.get_doc('Stocks', company)
			exist_doc.cumulative_quantity = cumulative_quantity
			exist_doc.total_invested = total_invested
			exist_doc.average_price_of_buying = average_price_of_buying
			exist_doc.number_of_transactions = number_of_transactions
			exist_doc.save()
		else:
			new_stock = frappe.get_doc({
				"doctype":"Stocks",
				"company_code":company,
				"cumulative_quantity":cumulative_quantity,
				"total_invested":total_invested,
				"average_price_of_buying":average_price_of_buying,
				"number_of_transactions":number_of_transactions
				})
			new_stock.insert()

