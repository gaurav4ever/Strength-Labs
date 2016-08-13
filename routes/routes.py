
from controllers import *
route = [
		(
			r"/",
			home.homeHandler
		),
		(
			r"/auth/register",
			auth.registerHandler
		),
		(
			r"/auth/login",
			auth.loginHandler
		),
		(
			r"/auth/logout",
			auth.logoutHandler
		),
		(
			r"/profile",
			profile.profileHandler
		),
		(
			r"/shop",
			shop.shopHandler
		),
		(
			r"/readmore",
			readmore.readMore
		),
		(
			r"/addtocart",
			cart.addcartHandler
		),
		(
			r"/cart",
			cart.cartHandler
		),
		(
			r"/cart/coupon_code",
			cart.coupon_codeHandler
		),
		(
			r"/team",
			team.teamHandler
		),
		(
			r"/change_pass",
			change_password.change_passwordHandler
		),
		(
			r"/change_pass/changepassword",
			change_password.changepasswordHandler
		),
		(
			r"/profile_address",
			profile_address.profile_addressHandler
		),
		(
			r"/profile_settings",
			profile_settings.profile_settingsHandler
		),
		(
			r"/profile_settings/changesettings",
			profile_settings.changesettingsHandler
		),
		(
			r"/account_settings",
			account_settings.account_settingsHandler
		),
		(
			r"/account_settings/deactivate_account",
			account_settings.deactivate_accountHandler
		),
		(
			r"/recent_orders",
			recent_orders.recent_ordersHandler
		),
		(
			r"/cod",
			cod.codHandler
		),
		(
			r"/custom_plans",
			custom_plans.custom_plansHandler
		),
		(
			r"/chat_with_dietitian",
			chat_with_dietitian.chat_with_dietitianHandler
		),
		(
			r"/regular_plan/view",
			regular_plan.regular_planHandler
		),
		(
			r"/monthly_pan/view",
			monthly_plan.monthly_planHandler
		),
		(
			r"/monthly_plan_shredding",
			plans.monthly_plan_shreddingHandler
		),
		(
			r"/monthly_plan_shredding_veg_egg",
			plans.monthly_plan_shredding_veg_eggHandler
		),
		(
			r"/monthly_plan_shredding_non_veg",
			plans.monthly_plan_non_vegshreddingHandler
		),
		(
			r"/monthly_plan_bulking",
			plans.monthly_plan_bulkingHandler
		),
		(
			r"/monthly_plan_bulking_veg_egg",
			plans.monthly_plan_bulking_veg_eggHandler
		),
		(
			r"/monthly_plan_bulking_non_veg",
			plans.monthly_plan_bulking_non_vegHandler
		),
		(
			r"/monthly_plan_fat_loss",
			plans.monthly_plan_fat_lossHandler
		),
		(
			r"/monthly_plan_fat_loss_veg_egg",
			plans.monthly_plan_fat_loss_veg_eggHandler	
		),
		(
			r"/monthly_plan_fat_loss_non_veg",
			plans.monthly_plan_fat_loss_non_vegHandler
		),
		(
			r"/monthly_plan_custom",
			plans.monthly_plan_customHandler
		),
		(
			r"/macro_cal",
			home.macro_calHandler
		),
		(
			r"/plan_form",
			home.plan_formHandler

		),
		(
			r"/faq",
			home.faqHandler
		),
		(
			r"/viewOrders",
			viewOrders.viewOrdersHandler
		),
		(
			r"/orders",
			orders.ordersHandler
		),
		(
			r"/req_msg",
			home.req_msgHandler
		),
		(
			r"/chicken_breast",
			temp.chicken_breastHandler
		),
		(
			r"/chilli_paneer",
			temp.chilli_paneerHandler
		),
		(
			r"/boiled_eggs",
			temp.boiled_eggsHandler
		),
		(
			r"/terms_privacy",
			home.terms_privacyHandler

		)
]
					
