from telebot import types


menu_access_no = types.InlineKeyboardMarkup(row_width=3)
menu_access_no.add(
    types.InlineKeyboardButton(text='Acheter un accès', callback_data='buy_access'),                       # +
    types.InlineKeyboardButton(text='Profil', callback_data='profile'),                                # +
    types.InlineKeyboardButton(text='Information', callback_data='access_no_info'),                       # +
    types.InlineKeyboardButton(text='Тех. Soutien', callback_data='support_no')                       # +
)

menu_access_yes = types.InlineKeyboardMarkup(row_width=2)
menu_access_yes.add(
    types.InlineKeyboardButton(text='Profil', callback_data='profile'),                                # +
    types.InlineKeyboardButton(text='Information', callback_data='access_yes_info'),                     # +
    types.InlineKeyboardButton(text='Demander un paiement', callback_data='order_payout'),                 # +
    types.InlineKeyboardButton(text='Тех. Soutien', callback_data='support_yes')                      # -
)

menu_admin = types.InlineKeyboardMarkup(row_width=2)
menu_admin.add(
    types.InlineKeyboardButton(text='Information', callback_data='admin_info'),                          # +
    types.InlineKeyboardButton(text='Demandes de retrait', callback_data='admin_list_order_payment'),      # +
    types.InlineKeyboardButton(text='Profit', callback_data='admin_profit'),                           # +
    types.InlineKeyboardButton(text="Déconnectez-vous de l'administrateur", callback_data='go_main_menu')                   # +
)

btn_close = types.InlineKeyboardMarkup(row_width=3)
btn_close.add(
    types.InlineKeyboardButton(text='❌', callback_data='close')
)

menu_buy_access = types.InlineKeyboardMarkup(row_width=3)
menu_buy_access.add(
    types.InlineKeyboardButton(text='🔄 Paiement par chèque', callback_data='check_payment'),
    types.InlineKeyboardButton(text='Annuler l'achat', callback_data='cancel_payment')
)

btn_back_to_admin_menu = types.InlineKeyboardMarkup(row_width=3)
btn_back_to_admin_menu.add(
    types.InlineKeyboardButton(text="Retour au menu d'administration", callback_data='back_to_admin_menu')
)

admin_order_info = types.InlineKeyboardMarkup(row_width=3)
admin_order_info.add(
    types.InlineKeyboardButton(text='Retirer de la liste', callback_data='del_order'),
    types.InlineKeyboardButton(text='Se déconnecter', callback_data='back_to_admin_menu')
)   types.InlineKeyboardButton(text='Удалить из списка', callback_data='del_order'),
    types.InlineKeyboardButton(text='Выйти', callback_data='back_to_admin_menu')
)