import datetime
from math import radians
import random

print("\n")

weekend_text = "70% week-end"
week_text = "50% semaine"

# date = input("day/month/year : ")
# price = input("price : ")
# start_loaction = input("start location : ")
# end_location = input("end location : ")
# start_time = input("departure time : ")
# end_time = input("arrival time : ")

date = "30/06/21"
price = "21.3"
start_loaction = "Paris Est"
end_location = "Chaumont"
start_time = "11h42"
end_time = "14h12"

buy_hour = int(start_time.split("h")[0])
buy_min = int(start_time.split("h")[1]) - random.randint(0, 5)
buy_sec = random.randint(0, 59)

# --- date things ---
day = int(date.split("/")[0])
month = int(date.split("/")[1])
year = date.split("/")[2]

if len(year) != 4:
    year = "20" + year

year = int(year)

date = datetime.datetime(year, month, day)
day_num = date.weekday()

day_names = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
day_name = day_names[day_num]

month_names = [
    "Janvier",
    "Février",
    "Mars",
    "Avril",
    "Mai",
    "Juin",
    "Juillet",
    "Août",
    "Septembre",
    "Octobre",
    "Novembre",
    "Décembre",
]
month_name = month_names[month - 1]

if day_num == 5 or day_num == 6:
    promo = weekend_text
else:
    promo = week_text
# -------------------

# --- price things ---
if price.count(","):
    price.replace(",", ".")
euro = price.split(".")[0]
centime = price.split(".")[1]
if len(centime) == 1:
    centime += "0"
# --------------------

print(f"prix : {euro}€{centime}")
print(f"{day_name} {day} {month_name} {year}")
print(f"{buy_hour}:{buy_min}:{buy_sec}")

template = f"""
<table id="bodyTable" border="0" width="100%" cellspacing="0" cellpadding="2">
    <tbody>
        <tr>
            <td style="vertical-align: top;" align="center">
                <table id="emailContainer" style="background-color: #ffffff; --darkreader-inline-bgcolor: #181a1b;"
                    border="0" width="550" cellspacing="0" cellpadding="10" data-darkreader-inline-bgcolor="">
                    <tbody>
                        <tr>
                            <td style="background-color: #ffffff; padding: 10px; vertical-align: top; height: 75px; --darkreader-inline-bgcolor: #181a1b;"
                                align="center" data-darkreader-inline-bgcolor="">
                                <table id="emailSNCF"
                                    style="padding-left: 20px; padding-top: 20px; padding-bottom: 20px; background-color: #ffffff; --darkreader-inline-bgcolor: #181a1b;"
                                    role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0"
                                    data-darkreader-inline-bgcolor="">
                                    <tbody>
                                        <tr>
                                            <td style="vertical-align: middle;" align="left">
                                                <img src="http://medias.cdn.vsct.fr/mpd/prod/emails/logo_sncf.jpg"
                                                    alt="SNCF" width="59" height="33" border="0">
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td style="vertical-align: top; background-color: #ffffff; padding: 10px; --darkreader-inline-bgcolor: #181a1b;"
                                data-darkreader-inline-bgcolor="">
                                <table id="emailHeader"
                                    style="background-color: #ffffff; --darkreader-inline-bgcolor: #181a1b;"
                                    role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0"
                                    data-darkreader-inline-bgcolor="">
                                    <tbody>
                                        <tr>
                                            <td style="padding: 20px 0px 20px 20px; vertical-align: top; background-color: #ffffff; color: #3d3d3f; --darkreader-inline-bgcolor: #181a1b; --darkreader-inline-color: #c1bbb3;"
                                                align="left" data-darkreader-inline-bgcolor=""
                                                data-darkreader-inline-color="">
                                                <h1 style="font-family: Arial, sans-serif; font-size: 25px; font-weight: 500; color: #000000; text-transform: uppercase; --darkreader-inline-color: #e8e6e3;"
                                                    data-darkreader-inline-color="">Confirmation de
                                                    <br>
                                                    <span style="color: #0f6e9a; --darkreader-inline-color: #65c4f0;"
                                                        data-darkreader-inline-color="">votre voyage</span>
                                                </h1>
                                                <p
                                                    style="font-family: Arial, sans-serif; font-size: 12px; margin-top: 1em; margin-bottom: 1em;">
                                                    {day_name} {day} {month_name}</p>
                                            </td>
                                            <td style="text-align: center; padding: 20px 0;">
                                                <img src="http://medias.cdn.vsct.fr/mpd/prod/emails/icn_kepi.jpg" alt=""
                                                    width="149" height="91" border="0">
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td style="background-color: #ffffff; vertical-align: top; padding: 0px; --darkreader-inline-bgcolor: #181a1b;"
                                data-darkreader-inline-bgcolor="">
                                <table id="emailMessage"
                                    style="background-color: #ffffff; --darkreader-inline-bgcolor: #181a1b;" border="0"
                                    width="100%" cellspacing="0" cellpadding="0" data-darkreader-inline-bgcolor="">
                                    <tbody>
                                        <tr>
                                            <td style="font-family: Arial, sans-serif; font-size: 12px; color: #3d3d3f; vertical-align: top; padding: 30px; --darkreader-inline-color: #c1bbb3;"
                                                align="left" data-darkreader-inline-color="">
                                                <p style="margin-top: 1em; margin-bottom: 1em;">Bonjour,</p>
                                                <p style="margin-top: 1em; margin-bottom: 1em;">Vous avez effectué une
                                                    commande. Vous trouverez ci-dessous le détail de votre commande.</p>
                                                <p style="margin-top: 1em; margin-bottom: 1em;">Nous vous souhaitons un
                                                    excellent voyage.</p>
                                                <p style="margin-top: 1em; margin-bottom: 1em;">Votre équipe SNCF TER
                                                </p>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td style="background-color: #ffffff; padding: 10px; vertical-align: top; border-top: 4px solid #ecf0f1; --darkreader-inline-bgcolor: #181a1b; --darkreader-inline-border-top: #35393b;"
                                align="center" data-darkreader-inline-bgcolor="" data-darkreader-inline-border-top="">
                                <table
                                    style="background-color: #ffffff; border-bottom: 1px solid #ecf0f1; --darkreader-inline-bgcolor: #181a1b; --darkreader-inline-border-bottom: #35393b;"
                                    border="0" width="100%" cellspacing="0" cellpadding="0"
                                    data-darkreader-inline-bgcolor="" data-darkreader-inline-border-bottom="">
                                    <tbody>
                                        <tr>
                                            <td style="width: 20px;" width="20">&nbsp;</td>
                                            <td style="text-align: left;" colspan="2" align="left">
                                                <p style="margin: 0; padding: 0; line-height: 0; height: 5px;">&nbsp;
                                                </p>
                                                <h2 style="font-family: Arial, sans-serif; font-size: 18px; font-weight: 500; color: #000000; text-transform: uppercase; line-height: 20px; --darkreader-inline-color: #e8e6e3;"
                                                    data-darkreader-inline-color="">Rappel
                                                    <span style="color: #0f6e9a; --darkreader-inline-color: #65c4f0;"
                                                        data-darkreader-inline-color="">de votre commande</span>
                                                </h2>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="width: 20px;" width="20">&nbsp;</td>
                                            <td style="vertical-align: top;" align="left">
                                                <h2 style="padding: 0px 0px 5px; font-family: Arial, sans-serif; font-size: 13px; font-weight: 500; color: #3d3d3f; margin-top: 0.4em; margin-bottom: 0.4em; --darkreader-inline-color: #c1bbb3;"
                                                    data-darkreader-inline-color="">
                                                    <strong
                                                        style="color: #0f6e9a; font-weight: normal; --darkreader-inline-color: #65c4f0;"
                                                        data-darkreader-inline-color="">Aller simple</strong> 30/06/2021
                                                </h2>
                                                <p style="font-family: Arial, sans-serif; font-size: 13px; color: #3d3d3f; margin-top: 0.4em; margin-bottom: 1em; --darkreader-inline-color: #c1bbb3;"
                                                    data-darkreader-inline-color=""> {start_loaction}
                                                    <strong style="font-weight: normal;">
                                                        <img style="margin-left: 10px; margin-right: 10px;"
                                                            src="http://medias.cdn.vsct.fr/mpd/prod/emails/icn_arrow.jpg"
                                                            alt="icone fleche" width="10" height="11">
                                                    </strong> {end_location}
                                                </p>
                                            </td>
                                            <td style="vertical-align: top;" align="left">
                                                <p style="padding: 0px 0px 0px 20px; font-family: Arial, sans-serif; font-size: 17px; font-weight: 500; color: #0f6e9a; margin-top: 0.4em; margin-bottom: 0.4em; --darkreader-inline-color: #65c4f0;"
                                                    data-darkreader-inline-color="">{euro},
                                                    <span style="font-size: 14px;">{centime} €</span>
                                                </p>
                                                <p style="padding: 0px 0px 0px 20px; font-family: Arial, sans-serif; font-size: 11px; color: #767676; margin-top: 0.4em; margin-bottom: 1em; --darkreader-inline-color: #9d9588;"
                                                    data-darkreader-inline-color="">pour 1 personne</p>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td style="background-color: #ffffff; padding-left: 10px; --darkreader-inline-bgcolor: #181a1b;"
                                align="center" data-darkreader-inline-bgcolor="">
                                <table id="emailTrajetPassager6"
                                    style="background-color: #ffffff; padding: 10px; --darkreader-inline-bgcolor: #181a1b;"
                                    border="0" width="100%" cellspacing="0" cellpadding="0"
                                    data-darkreader-inline-bgcolor="">
                                    <tbody>
                                        <tr>
                                            <td align="center" valign="top">
                                                <table id="emailTrajet" border="0" width="100%" cellspacing="0"
                                                    cellpadding="0">
                                                    <tbody>
                                                        <tr>
                                                            <td style="padding: 0 10px;" colspan="3" align="left"
                                                                valign="top">
                                                                <h2 style="font-family: Arial, sans-serif; font-size: 13px; font-weight: 500; color: #0f6e9a; margin-top: 0.83em; margin-bottom: 0.83em; --darkreader-inline-color: #65c4f0;"
                                                                    data-darkreader-inline-color="">Aller {day_name} {day}
                                                                    Month year</h2>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td style="padding: 0 10px 10px; width: 210px;" align="left"
                                                                valign="middle">
                                                                <p style="font-family: Arial, sans-serif; font-size: 12px; color: #3d3d3f; margin-bottom: 1em; margin-top: 0px; --darkreader-inline-color: #c1bbb3;"
                                                                    data-darkreader-inline-color="">Start location</p>
                                                                <p style="font-family: Arial, sans-serif; font-size: 12px; margin-top: -10px; color: #767676; --darkreader-inline-color: #9d9588;"
                                                                    data-darkreader-inline-color="">Départ {start_time}
                                                                </p>
                                                            </td>
                                                            <td style="width: 40px; padding: 0 10px 10px;" align="left"
                                                                valign="top">
                                                                <img src="http://medias.cdn.vsct.fr/mpd/prod/emails/icn_arrow.jpg"
                                                                    alt="flèche" width="10px" height="11px">
                                                            </td>
                                                            <td style="padding: 0 10px 10px 0;" align="left"
                                                                valign="middle">
                                                                <p style="font-family: Arial, sans-serif; font-size: 12px; color: #3d3d3f; margin-bottom: 1em; margin-top: 0px; --darkreader-inline-color: #c1bbb3;"
                                                                    data-darkreader-inline-color="">End destination</p>
                                                                <p style="font-family: Arial, sans-serif; font-size: 12px; margin-top: -10px; color: #767676; --darkreader-inline-color: #9d9588;"
                                                                    data-darkreader-inline-color="">Arrivée {end_time}</p>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td align="left" valign="top">
                                                <table
                                                    style="padding: 0px 10px; border-left: 1px solid #0f6e9a; --darkreader-inline-border-left: #1285ba;"
                                                    border="0" width="100%" cellspacing="0" cellpadding="0"
                                                    data-darkreader-inline-border-left="">
                                                    <tbody>
                                                        <tr>
                                                            <td style="font-family: Arial, sans-serif; font-size: 12px; color: #3d3d3f; padding: 10px; overflow-wrap: break-word; --darkreader-inline-color: #c1bbb3;"
                                                                data-darkreader-inline-color="">Robin P.</td>
                                                            <td style="font-family: Arial, sans-serif; font-size: 12px; color: #3d3d3f; width: 140px; max-width: 140px; padding: 10px 10px 10px 0px; overflow-wrap: break-word; --darkreader-inline-color: #c1bbb3;"
                                                                data-darkreader-inline-color="">PRIMO Grand Est {promo}</td>
                                                            <td style="font-family: Arial, sans-serif; font-size: 16px; color: #0f6e9a; padding: 10px 10px 10px 0px; overflow-wrap: break-word; --darkreader-inline-color: #65c4f0;"
                                                                data-darkreader-inline-color="">{euro},
                                                                <span style="font-size: 12px;">{centime} €</span>
                                                            </td>
                                                            <td style="padding: 10px 10px 10px 0;" align="center"
                                                                valign="middle">
                                                                <table>
                                                                    <tbody>
                                                                        <tr>
                                                                            <td style="color: #ffffff; font-family: Arial, sans-serif; font-size: 12px; font-weight: bold; letter-spacing: -0.5px; padding: 10px 15px; background-color: #0f6e9a; border-radius: 5px; text-decoration: none; text-transform: uppercase; display: block; border-bottom: 2px solid #0d5d83 !important; --darkreader-inline-color: #e8e6e3; --darkreader-inline-bgcolor: #0c587b; --darkreader-inline-border-bottom: #1389c1;"
                                                                                data-darkreader-inline-color=""
                                                                                data-darkreader-inline-bgcolor=""
                                                                                data-darkreader-inline-border-bottom="">
                                                                                <a href="https://a4099669-13aa-4aee-837f-81d87ef9b31c"
                                                                                    style="color: white; text-decoration: none; --darkreader-inline-color: #e8e6e3;"
                                                                                    target="_blank"
                                                                                    data-darkreader-inline-color=""
                                                                                    rel="noopener">imprimer ce
                                                                                    billet</a>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <!-- Vos références de commande-->
                        <tr>
                            <td style="background-color: #ffffff; border-top: 4px solid #ecf0f1; padding: 10px 10px 20px; --darkreader-inline-bgcolor: #181a1b; --darkreader-inline-border-top: #35393b;"
                                align="center" data-darkreader-inline-bgcolor="" data-darkreader-inline-border-top="">
                                <table role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
                                    <tbody>
                                        <tr>
                                            <td style="vertical-align: middle; text-align: left;" align="left">
                                                <table
                                                    style="background-color: #ffffff; --darkreader-inline-bgcolor: #181a1b;"
                                                    role="presentation" border="0" width="100%" cellspacing="0"
                                                    cellpadding="0" data-darkreader-inline-bgcolor="">
                                                    <tbody>
                                                        <tr>
                                                            <td style="width: 20px;" width="20">&nbsp;</td>
                                                            <td>
                                                                <p
                                                                    style="margin: 0; padding: 0; line-height: 0; height: 10px;">
                                                                    &nbsp;</p>
                                                                <h2 style="font-family: Arial, sans-serif; font-size: 18px; font-weight: 500; color: #000000; text-transform: uppercase; line-height: 20px; margin: 0px; padding: 0px; --darkreader-inline-color: #e8e6e3;"
                                                                    data-darkreader-inline-color="">Vos références
                                                                    <span
                                                                        style="color: #0f6e9a; --darkreader-inline-color: #65c4f0;"
                                                                        data-darkreader-inline-color="">de
                                                                        commande</span>
                                                                </h2>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <br>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="background-color: #ffffff; padding: 10px; vertical-align: top; --darkreader-inline-bgcolor: #181a1b;"
                                                align="center" data-darkreader-inline-bgcolor="">
                                                <table
                                                    style="width: 314px; background-color: #ffffff; margin-left: auto; margin-right: auto; --darkreader-inline-bgcolor: #181a1b;"
                                                    role="presentation" border="0" cellspacing="0" cellpadding="0"
                                                    align="center" data-darkreader-inline-bgcolor="">
                                                    <tbody>
                                                        <!--<tr>
                                                            <th style="border-top: 1px solid #8c8c8c; border-left: 1px solid #8c8c8c; border-bottom: 1px solid #8c8c8c; vertical-align: middle; text-align: left; background-color: #ffffff; --darkreader-inline-border-top: #50575b; --darkreader-inline-border-left: #50575b; --darkreader-inline-border-bottom: #50575b; --darkreader-inline-bgcolor: #181a1b;"
                                                                scope="row" width="55" height="38"
                                                                data-darkreader-inline-border-top=""
                                                                data-darkreader-inline-border-left=""
                                                                data-darkreader-inline-border-bottom=""
                                                                data-darkreader-inline-bgcolor="">
                                                                <img title="La référence de votre commande"
                                                                    src="http://medias.cdn.vsct.fr/mpd/prod/emails/picto_id.jpg"
                                                                    alt="Référence de votre commande (8 chiffres)"
                                                                    width="42" height="38">
                                                            </th>
                                                            <td id="referenceContainer"
                                                                style="font-family: Arial, sans-serif; border-top: 1px solid #8c8c8c; border-right: 1px solid #8c8c8c; border-bottom: 1px solid #8c8c8c; text-align: left; letter-spacing: 2px; vertical-align: middle; background-color: #ffffff; --darkreader-inline-border-top: #50575b; --darkreader-inline-border-right: #50575b; --darkreader-inline-border-bottom: #50575b; --darkreader-inline-bgcolor: #181a1b;"
                                                                height="38" data-darkreader-inline-border-top=""
                                                                data-darkreader-inline-border-right=""
                                                                data-darkreader-inline-border-bottom=""
                                                                data-darkreader-inline-bgcolor=""> None </td>
                                                        </tr>-->
                                                        <tr style="height: 10px;" aria-hidden="true">
                                                            <th>&nbsp;</th>
                                                            <td>&nbsp;</td>
                                                        </tr>
                                                        <tr>
                                                            <th style="height: 38px; border-top: 1px solid #8c8c8c; border-left: 1px solid #8c8c8c; border-bottom: 1px solid #8c8c8c; vertical-align: middle; text-align: left; background-color: #ffffff; --darkreader-inline-border-top: #50575b; --darkreader-inline-border-left: #50575b; --darkreader-inline-border-bottom: #50575b; --darkreader-inline-bgcolor: #181a1b;"
                                                                scope="row" width="55" height="38"
                                                                data-darkreader-inline-border-top=""
                                                                data-darkreader-inline-border-left=""
                                                                data-darkreader-inline-border-bottom=""
                                                                data-darkreader-inline-bgcolor="">
                                                                <img title="Le nom d’un des passagers"
                                                                    src="http://medias.cdn.vsct.fr/mpd/prod/emails/picto_name.jpg"
                                                                    alt="Nom d’un des passagers" width="42" height="38">
                                                            </th>
                                                            <td id="nomReferenceContainer"
                                                                style="font-family: Arial, sans-serif; height: 38px; border-top: 1px solid #8c8c8c; border-right: 1px solid #8c8c8c; border-bottom: 1px solid #8c8c8c; text-align: left; text-transform: uppercase; vertical-align: middle; background-color: #ffffff; --darkreader-inline-border-top: #50575b; --darkreader-inline-border-right: #50575b; --darkreader-inline-border-bottom: #50575b; --darkreader-inline-bgcolor: #181a1b;"
                                                                height="38" data-darkreader-inline-border-top=""
                                                                data-darkreader-inline-border-right=""
                                                                data-darkreader-inline-border-bottom=""
                                                                data-darkreader-inline-bgcolor="">PERRET</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <br>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                                <table
                                    style="width: 100%; background-color: #ffffff; margin-left: auto; margin-right: auto; --darkreader-inline-bgcolor: #181a1b;"
                                    role="presentation" border="0" cellspacing="0" cellpadding="0" align="center"
                                    data-darkreader-inline-bgcolor="">
                                    <tbody>
                                        <tr>
                                            <td style="padding: 10px 20px 10px 15px;" valign="top" width="234">
                                                <p style="font-size: 12px; color: #0c0c0c; margin: 0px; --darkreader-inline-color: #e0deda;"
                                                    data-darkreader-inline-color="">
                                                    <strong>Télécharger vos billets sur l’Appli SNCF</strong>
                                                </p>
                                                <table>
                                                    <tbody>
                                                        <tr>
                                                            <td>
                                                                <img src="http://medias.cdn.vsct.fr/mpd/prod/emails/appli_sncf.jpg"
                                                                    alt="" width="115" height="131">
                                                            </td>
                                                            <td>
                                                                <p>
                                                                    <a href="https://itunes.apple.com/fr/app/sncf/id945434433?mt=8"
                                                                        target="_blank"
                                                                        style="text-decoration: none; border: 0px; --darkreader-inline-border-top: initial; --darkreader-inline-border-right: initial; --darkreader-inline-border-bottom: initial; --darkreader-inline-border-left: initial;"
                                                                        data-darkreader-inline-border-top=""
                                                                        data-darkreader-inline-border-right=""
                                                                        data-darkreader-inline-border-bottom=""
                                                                        data-darkreader-inline-border-left=""
                                                                        rel="noopener">
                                                                        <img style="border: 0px; --darkreader-inline-border-top: initial; --darkreader-inline-border-right: initial; --darkreader-inline-border-bottom: initial; --darkreader-inline-border-left: initial;"
                                                                            src="http://medias.cdn.vsct.fr/mpd/prod/emails/appstore.jpg"
                                                                            alt="Disponible sur l’App Store" width="110"
                                                                            height="32"
                                                                            data-darkreader-inline-border-top=""
                                                                            data-darkreader-inline-border-right=""
                                                                            data-darkreader-inline-border-bottom=""
                                                                            data-darkreader-inline-border-left="">
                                                                    </a>
                                                                </p>
                                                                <p>
                                                                    <a href="https://play.google.com/store/apps/details?id=com.sncf.fusion&amp;hl=fr"
                                                                        target="_blank"
                                                                        style="text-decoration: none; border: 0px; --darkreader-inline-border-top: initial; --darkreader-inline-border-right: initial; --darkreader-inline-border-bottom: initial; --darkreader-inline-border-left: initial;"
                                                                        data-darkreader-inline-border-top=""
                                                                        data-darkreader-inline-border-right=""
                                                                        data-darkreader-inline-border-bottom=""
                                                                        data-darkreader-inline-border-left=""
                                                                        rel="noopener">
                                                                        <img style="border: 0px; --darkreader-inline-border-top: initial; --darkreader-inline-border-right: initial; --darkreader-inline-border-bottom: initial; --darkreader-inline-border-left: initial;"
                                                                            src="http://medias.cdn.vsct.fr/mpd/prod/emails/googleplay.jpg"
                                                                            alt="Disponible sur Google Play" width="110"
                                                                            height="32"
                                                                            data-darkreader-inline-border-top=""
                                                                            data-darkreader-inline-border-right=""
                                                                            data-darkreader-inline-border-bottom=""
                                                                            data-darkreader-inline-border-left="">
                                                                    </a>
                                                                </p>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                            <td style="--darkreader-inline-bgcolor: #2b2f31;" bgcolor="#ddd" width="2"
                                                data-darkreader-inline-bgcolor="">&nbsp;</td>
                                            <td style="padding: 10px 15px 10px 20px;" valign="top" width="234">
                                                <p style="font-size: 12px; color: #0c0c0c; margin: 0px; --darkreader-inline-color: #e0deda;"
                                                    data-darkreader-inline-color="">
                                                    <strong>Accéder à vos billets sur le site TER</strong>
                                                </p>
                                                <p style="margin: 0; padding-right: 10px;">
                                                    <a href="http://www.ter.sncf.com/lorraine/compte/profil">
                                                        <img style="display: block; margin: auto; border: none; --darkreader-inline-border-top: initial; --darkreader-inline-border-right: initial; --darkreader-inline-border-bottom: initial; --darkreader-inline-border-left: initial;"
                                                            src="http://medias.cdn.vsct.fr/mpd/prod/emails/site_ter.jpg"
                                                            alt="" width="130" height="91"
                                                            data-darkreader-inline-border-top=""
                                                            data-darkreader-inline-border-right=""
                                                            data-darkreader-inline-border-bottom=""
                                                            data-darkreader-inline-border-left="">
                                                    </a>
                                                </p>
                                                <p style="font-family: Arial, sans-serif; font-size: 11px; line-height: 1.5; color: #3d3d3f; margin-top: 0px; margin-bottom: 0px; --darkreader-inline-color: #c1bbb3;"
                                                    data-darkreader-inline-color="">Consulter, imprimer vos billets,
                                                    imprimer vos justificatifs ou annuler vos billets depuis le
                                                    <a href="http://www.ter.sncf.com/lorraine/compte/profil"
                                                        style="color: #0f6e9a; font-weight: bold; --darkreader-inline-color: #65c4f0;"
                                                        data-darkreader-inline-color="">Site TER</a>.
                                                </p>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td style="background-color: #ffffff; padding: 0px 20px 0px 10px; vertical-align: top; border-top: 4px solid #ecf0f1; --darkreader-inline-bgcolor: #181a1b; --darkreader-inline-border-top: #35393b;"
                                align="center" data-darkreader-inline-bgcolor="" data-darkreader-inline-border-top="">
                                <table style="background-color: #ffffff; --darkreader-inline-bgcolor: #181a1b;"
                                    border="0" width="100%" cellspacing="0" cellpadding="0"
                                    data-darkreader-inline-bgcolor="">
                                    <tbody>
                                        <tr>
                                            <td style="padding-left: 20px; text-align: left;" colspan="5">
                                                <p style="font-family: Arial, sans-serif; font-size: 12px; color: #3d3d3f; margin-top: 2em; margin-bottom: 2em; text-transform: uppercase; border-bottom: 1px solid #dedede; width: 120px; padding-bottom: 0.5em; --darkreader-inline-color: #c1bbb3; --darkreader-inline-border-bottom: #393e40;"
                                                    data-darkreader-inline-color=""
                                                    data-darkreader-inline-border-bottom="">Votre billet est :</p>
                                            </td>
                                        </tr>
                                        <tr style="vertical-align: top;" align="center">
                                            <td style="width: 173px;">
                                                <p style="font-family: Arial, sans-serif; font-size: 11px; color: #3d3d3f; margin-top: 0px; margin-bottom: 1em; line-height: 1.5; font-weight: bold; --darkreader-inline-color: #c1bbb3;"
                                                    data-darkreader-inline-color="">
                                                    <img style="margin-bottom: 10px;"
                                                        src="http://medias.cdn.vsct.fr/mpd/prod/emails/icn_ter_30.png"
                                                        alt="icone ter" width="34" height="28">
                                                    <br>Utilisable uniquement
                                                    <br>sur TER
                                                </p>
                                            </td>
                                            <td style="width: 173px;">
                                                <p style="font-family: Arial, sans-serif; font-size: 11px; color: #3d3d3f; margin-top: 0px; margin-bottom: 1em; line-height: 1.5; font-weight: bold; --darkreader-inline-color: #c1bbb3;"
                                                    data-darkreader-inline-color="">
                                                    <img style="margin-bottom: 10px;"
                                                        src="http://medias.cdn.vsct.fr/mpd/prod/emails/icn_carte2.png"
                                                        alt="icone sign" width="30" height="30">
                                                    <br>Billet nominatif
                                                </p>
                                            </td>
                                            <td style="width: 173px;">
                                                <p style="font-family: Arial, sans-serif; font-size: 11px; color: #3d3d3f; margin-top: 0px; margin-bottom: 1em; line-height: 1.5; font-weight: bold; --darkreader-inline-color: #c1bbb3;"
                                                    data-darkreader-inline-color="">
                                                    <img style="margin-bottom: 10px;"
                                                        src="http://medias.cdn.vsct.fr/mpd/prod/emails/icn_code_30.png"
                                                        alt="icone code Barre" width="27" height="27">
                                                    <br>À imprimer ou à
                                                    <br>charger sur l’appli SNCF
                                                </p>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td style="background: #ffffff; padding: 10px; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b;"
                                data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">
                                <table id="footer-cgu" style="padding: 0 10px 0 10px;" border="0" width="100%"
                                    cellspacing="0" cellpadding="0">
                                    <tbody>
                                        <tr style="padding: 10px 10px 16px 10px; vertical-align: top;">
                                            <td style="width: 5px;" align="left">
                                                <img src="http://medias.cdn.vsct.fr/mpd/prod/emails/icn_date.png"
                                                    alt="icone calendrier" width="16" height="16">
                                            </td>
                                            <td style="height: 20px;" align="left">
                                                <p style="font-family: Arial, sans-serif; text-align: justify; font-size: 11px; color: #3d3d3f; line-height: 16px; margin-top: 0px; margin-bottom: 2em; --darkreader-inline-color: #c1bbb3;"
                                                    data-darkreader-inline-color="">Votre titre est valable sur les
                                                    trains et cars TER. Envie de changer d’horaire ? Vous pouvez prendre
                                                    dans la même journée un autre train/car TER avant ou après celui
                                                    initialement choisi en respectant la date, le parcours et les
                                                    conditions du tarif acheté.</p>
                                            </td>
                                        </tr>
                                        <tr style="padding: 10px 10px 16px 10px; vertical-align: top;">
                                            <td style="width: 5px;" align="left">
                                                <img src="http://medias.cdn.vsct.fr/mpd/prod/emails/icn_carte.png"
                                                    alt="icone carte" width="16" height="16">
                                            </td>
                                            <td style="height: 20px;" align="left">
                                                <p style="font-family: Arial, sans-serif; text-align: justify; font-size: 11px; color: #3d3d3f; line-height: 16px; margin-top: 0px; margin-bottom: 2em; --darkreader-inline-color: #c1bbb3;"
                                                    data-darkreader-inline-color="">Votre titre est nominatif et ne peut
                                                    être cédé à un autre passager.</p>
                                            </td>
                                        </tr>
                                        <tr style="padding: 10px 10px 16px 10px; vertical-align: top;">
                                            <td style="width: 5px;" align="left">
                                                <img src="http://medias.cdn.vsct.fr/mpd/prod/emails/icn_remboursement.png"
                                                    alt="icone remboursement" width="16" height="16">
                                            </td>
                                            <td style="height: 20px;" align="left">
                                                <p style="font-family: Arial, sans-serif; text-align: left; font-size: 11px; color: #3d3d3f; line-height: 16px; margin-top: 0px; margin-bottom: 2em; --darkreader-inline-color: #c1bbb3;"
                                                    data-darkreader-inline-color="">Si votre tarif le permet, vous
                                                    pouvez annuler votre billet jusqu’à la veille du départ sur le site
                                                    TER ou l’application SNCF (pas de remboursement en gare).</p>
                                            </td>
                                        </tr>
                                        <tr style="padding: 10px 10px 16px 10px; vertical-align: top;">
                                            <td style="width: 5px;" align="left">
                                                <img src="http://medias.cdn.vsct.fr/mpd/prod/emails/icn_code.jpg"
                                                    alt="icone code" width="16" height="16">
                                            </td>
                                            <td style="height: 20px;" align="left">
                                                <p style="font-family: Arial, sans-serif; text-align: justify; font-size: 11px; color: #3d3d3f; line-height: 16px; margin-top: 0px; margin-bottom: 2em; --darkreader-inline-color: #c1bbb3;"
                                                    data-darkreader-inline-color="">Pas besoin de composter.
                                                    Présentez-vous à bord muni de votre titre (billet non imprimable en
                                                    gare), d’une pièce d’identité et des éventuels justificatifs de
                                                    réduction.</p>
                                            </td>
                                        </tr>
                                        <tr style="padding-top: 0; padding-bottom: 0;">
                                            <td style="width: 5px; padding: 0 10px 16px 10px; vertical-align: top;">
                                                &nbsp;</td>
                                            <td style="height: 20px; padding: 0 10px 16px 10px; vertical-align: top;">
                                                <p
                                                    style="font-family: Arial, sans-serif; font-size: 10px; margin-top: 1em; font-weight: bold;">
                                                    Pour plus de détails, merci de vous reporter aux
                                                    <a href="http://www.ter.sncf.com/lorraine/conditions-de-vente"
                                                        style="color: #0f6e9a; text-decoration: none; font-weight: bold; --darkreader-inline-color: #65c4f0;"
                                                        title="conditions de vente
                                  [Nouvelle Fenêtre]" target="_blank" data-darkreader-inline-color=""
                                                        rel="noopener">conditions de vente.</a>
                                                </p>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td style="background: #ffffff; padding: 20px; vertical-align: top; border-top: 4px solid #ecf0f1; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b; --darkreader-inline-border-top: #35393b;"
                                align="center" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor=""
                                data-darkreader-inline-border-top="">
                                <table id="emailCGV"
                                    style="font-size: 10px; background: #ffffff; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b;"
                                    role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0"
                                    data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">
                                    <tbody>
                                        <tr>
                                            <td style="padding: 10px; vertical-align: top;" align="left">
                                                <h2
                                                    style="font-family: Arial, sans-serif; font-size: 12px; text-transform: uppercase; margin-top: 0; margin-bottom: 0;">
                                                    DONNÉES DE TRANSACTION</h2>
                                                <p style="font-family: Arial, sans-serif; font-size: 11px; line-height: 16px; color: #3d3d3f; margin-top: 1em; margin-bottom: 1em; list-style: none; margin-left: 0px; padding-left: 0px; --darkreader-inline-color: #c1bbb3;"
                                                    data-darkreader-inline-color="">&nbsp;</p>
                                                <div style="font-family: Arial, sans-serif; font-size: 11px; line-height: 1.5; color: #3d3d3f; margin-top: 1em; margin-bottom: 1em; padding-left: 0px; --darkreader-inline-color: #c1bbb3;"
                                                    data-darkreader-inline-color="">
                                                    <span style="font-weight: bold; text-transform: uppercase;">USAGE :
                                                        DEBIT</span>
                                                    <br>CARTE BANCAIRE - CB
                                                    <br>Date et heure de transaction : le {day}/{month}/{year} à
                                                    {buy_hour}:{buy_min}:{buy_sec}
                                                    <br>N° carte : #######8628
                                                    <br>TRANSACTION DE PAIEMENT
                                                    <br>DÉBIT VENTE A DISTANCE SÉCURISÉE
                                                    <br>N° de transaction : 633881
                                                    <br>ID de transaction: HP1181809948
                                                    <br>N° d’autorisation : 686141
                                                    <br>Montant de transaction : {euro},{centime}€
                                                    <br>Identifiant du commerçant : 201519037580031
                                                    <br>Enseigne, code département, commune : SNCF TER LOR MOB, 75,
                                                    PARIS
                                                    <br>
                                                    <a href="https://www.ter.sncf.com"
                                                        style="color: #0f6e9a; --darkreader-inline-color: #65c4f0;"
                                                        data-darkreader-inline-color="">www.ter.sncf.com</a>
                                                </div>
                                                <p style="font-family: Arial, sans-serif; font-size: 11px; line-height: 1.5; color: #3d3d3f; margin-top: 1em; margin-bottom: 1em; --darkreader-inline-color: #c1bbb3;"
                                                    data-darkreader-inline-color="">En cas de réclamation, merci de
                                                    fournir à notre
                                                    <a href="http://www.ter.sncf.com/lorraine/contacts"
                                                        style="color: #0f6e9a; --darkreader-inline-color: #65c4f0;"
                                                        data-darkreader-inline-color="">Centre de relation Clients</a>
                                                    les éléments suivants : code UNI point de vente 691923, numéro de
                                                    recette 001, numéro de séance comptable Non connu, dossier voyage
                                                    AJVRCK
                                                </p>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td style="background-color: #d3d3d3; padding: 10px; --darkreader-inline-bgcolor: #313537;"
                                align="center" valign="top" data-darkreader-inline-bgcolor="">
                                <table id="emailFooter" border="0" width="100%" cellspacing="0" cellpadding="20">
                                    <tbody>
                                        <tr>
                                            <td style="font-family: Arial, sans-serif; font-size: 11px; line-height: 1.5; color: #3d3d3f; --darkreader-inline-color: #c1bbb3;"
                                                align="left" valign="top" data-darkreader-inline-color="">
                                                <p style="margin-top: 1em; margin-bottom: 1em;">Vous pouvez consulter
                                                    les
                                                    <a href="http://www.ter.sncf.com/lorraine/conditions-de-vente"
                                                        title="Centre de Relation Clients [Nouvelle Fenêtre]"
                                                        target="_blank" rel="noopener">Conditions Générales de Vente</a>
                                                    sur le
                                                    <a href="http://www.ter.sncf.com/lorraine" target="_blank"
                                                        rel="noopener">site régional</a>.
                                                </p>
                                                <p style="margin-top: 1em; margin-bottom: 1em;">SNCF.COM - SNCF,
                                                    Etablissement Public à caractère Industriel et Commercial au capital
                                                    de 4.270.897.305,31 € enregistré au RCS sous le numéro 552 049 447,
                                                    dont le siège est 2 place aux Étoiles, CS 7000, 93633 La
                                                    Plaine-Saint-Denis Cedex</p>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>
""".encode(
    "utf-8"
)

with open("SNCF\\final.html", "wb") as f:
    f.write(template)
