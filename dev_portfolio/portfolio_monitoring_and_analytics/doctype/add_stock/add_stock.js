// Copyright (c) 2023, Panigrahis.com and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Add Stock", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Add Stock', {
	quantity: function(frm) {
	    var investment;
		investment=frm.doc.quantity*frm.doc.price_of_buying;
		frm.set_value('investment',investment);
		frm.set_df_property('investment', 'read_only', 1);
	},
	price_of_buying: function(frm) {
	    var investment;
		var price_of_buying_in_paisa;
		investment=frm.doc.quantity*frm.doc.price_of_buying;
		frm.set_value('investment',investment);
		frm.set_df_property('investment', 'read_only', 1);

		price_of_buying_in_paisa = Math.round(100*frm.doc.price_of_buying);
		frm.set_value('price_of_buying_in_paisa',price_of_buying_in_paisa);
	},
	refresh: function(frm){
		document.getElementsByClassName('layout-side-section')[0].style.display = 'none';  
				
		}
	
	
});
