import settings


buy_access = "❕ Accès d'achat\n\n' \
              '🥝 Paiement usdt:\n\n' \
             f'❕ Numéro:     {settings.USDT_ADRESS}\n' \
             f'❕ Somme:     {settings.ACCESS_COST} usdt\n' \
             '❕ Commenter:    {code}'


start_menu = 'Bonjour, {name}\n' \
        'Ton id - {id}\n' \
        'Vous êtes au menu:'


admin_menu = 'Bonjour, {name}\n' \
             'Vous êtes dans le menu admin: '


profile = '📰 Profil\n\n' \
          'votre nom - {name}\n' \
          'Ton id - {id}\n' \
          'Accéder - {access}'


access_no_info = '❕ Informations sur la pyramide\n\n' \
                 '💥 La pyramide a un système à 3 niveaux\n' \
                 '💥 En payant pour accès, vous obtenez un lien personnel pour inviter des utilisateurs\n' \
                 f'💥 За chaque invitation.  utilisateur qui a payé pour accès que vous obtenez {settings.PERCENT_1 * 100} % du paiement\n' \
                 f'💥 За chaque invitation.  nom utilisateur que vous obtenez {settings.PERCENT_2 * 100} % du paiement\n' \
                 f'💥 Plus loin {settings.PERCENT_3 * 100} % du paiement\n' \
                 f'💥En invitant un seul utilisateur actif, vous pouvez obtenir plus de 10 usdt !!'


access_yes_info = '⚠️ Information\n\n' \
                  '❕ Votre référence.  le code - {ref_code}\n' \
                  '❕ Votre référence. lien - {ref_url}\n\n' \
                  '💰 Vos revenus - {profit} usdt\n' \
                  '👥Nombre de personnes invitées - {amount_invite_users}'


support = 'Si vous avez une question/un problème, écrivez:\n\n' \
          '@login'


admin_profit = '💰 Arrive pour tous les temps - {} usdt'


admin_info = 'informations générales\n\n' \
             'Unique au total utilisateurs - {users}\n' \
             "Nombre de personnes ayant payé pour l'accès - {deposit}\n'


order_payment = 'demande de retrait\n\n' \
                'ID demande - {}\n' \
                'User_id - {}\n' \
                'Nom - {}\n' \
                'Somme - {}\n' \
                'la date - {}\n' \
                'usdt - {}'


withdraw = '⚠️ Demande de paiement\n\n' \
            '❕ Votre solde - {} usdt\n' \
           f'❕ Min.  montant du paiement - {settings.MIN_PAYOUT} BTC\n\n' \
           '❕ Saisissez le montant que vous souhaitez retirer: \n\n' \
           f'❗️ par exemple: 5000 ou alors 7064.34'


людей оплативших доступ - {deposit}\n'


order_payment = 'Запрос на вывод\n\n' \
                'ID запроса - {}\n' \
                'User_id - {}\n' \
                'Имя - {}\n' \
                'Сумма - {}\n' \
                'Дата - {}\n' \
                'QIWI - {}'


withdraw = '⚠️ Запрос выплаты\n\n' \
           '❕ Ваш баланс - {} руб\n' \
           f'❕ Мин. сумма выплаты - {settings.MIN_PAYOUT} руб\n\n' \
           '❕ Введите сумму которую хотите вывести: \n\n' \
           f'❗️ Например: 500 или 764.34'

