base = """
<!DOCTYPE html>

<style>
    body {
        font-family: Calibri;
        font-size: large;
        font-weight: 400;
    }

    ul {
        padding: 0;
        margin: 0;
        list-style: none;
        display: flex;
    }
</style>
"""

transactions = [
    -200.0,
    512.1,
    6.9,
    -100.0,
    -2.74,
    -10.63,
    15.1,
    -23.0,
    100.0,
    -320.0,
    120.0,
    200.0,
    -13.7,
    -7.3,
    -5.6,
    -7.37,
    8.7,
    -10.9,
    -2.0,
    -12.0,
    -9.6,
    100.0,
    -320.0,
    120.0,
    -5.6,
    -5.6,
    -10.0,
    -9.9,
    -7.55,
    8.7,
    -10.9,
    -5.6,
    -5.6,
    -3.5,
    -9.9,
    100.0,
    -320.0,
    -5.6,
    100.0,
    -100.0,
    120.0,
    150.0,
    -8.01,
    8.7,
    -10.9,
]

transactions_name = [
    "VIR SEPA M PERRET ROBIN",
    "VIR SEPA DDFIP DE LA MARNE",
    "VIR SEPA PRO BTP PRESTATIONS FR",
    "CB GROUPEMENT PARI FACT",
    "CB INTERMARCHE",
    "CB PAYPAL",
    "VIR SEPA C.P.A.M. CHAUMONT",
    "CB CBT G BONNAY",
    "VIR SEPA MR PERRET LUDOVIC OU",
    "VIR SEPA LOYER COLLOC ROBIN",
    "VIR SEPA MLLE DE PAUW AURORE",
    "VIR SEPA M PERRET ROBIN",
    "CB MC DONALD'S",
    "CB ECRANS CHAUMONT",
    "CB SNCF INTERNET",
    "CB INTERMARCHE",
    "* REMISE SERVICES BOUQUET LIBE",
    "* COTISATION BOUQUET LIBERTE",
    "CB MC DONALD'S",
    "CB DEL ARTE CHMT",
    "CB BURGER KING",
    "VIR SEPA MR PERRET LUDOVIC OU",
    "VIR SEPA LOYER COLLOC ROBIN",
    "VIR SEPA MLLE DE PAUW AURORE",
    "CB SNCF INTERNET",
    "CB SNCF INTERNET",
    "VIREMENT VERS COMPTE N26",
    "CB MC DONALD'S",
    "CB INTERMARCHE",
    "* REMISE SERVICES BOUQUET LIBE",
    "* COTISATION BOUQUET LIBERTE",
    "CB SNCF INTERNET",
    "CB SNCF INTERNET",
    "CB MC DONALD'S",
    "CB MC DONALD'S",
    "VIR SEPA MR PERRET LUDOVIC OU",
    "VIR SEPA LOYER COLLOC ROBIN",
    "CB SNCF INTERNET",
    "VIR SEPA WINAMAX",
    "CB WINAMAX FR",
    "VIR SEPA MLLE DE PAUW AURORE",
    "VIR SEPA MLLE DE PAUW AURORE",
    "CB GEANT CG804",
    "* REMISE SERVICES BOUQUET LIBE",
    "* COTISATION BOUQUET LIBERTE",
]


total_spent = 0
total_gained = 0
for transaction in transactions:
    if transaction < 0:
        total_spent += abs(transaction)
    else:
        total_gained += transaction


both = {}
for i in range(0, len(transactions)):
    if transactions_name[i] in both.keys():
        both[transactions_name[i]] += transactions[i]
    else:
        both[transactions_name[i]] = transactions[i]

conclusion_str = "<body>"
for key in both.keys():
    if both[key] < 0:
        conclusion_str += (
            f"""{key} : <a style="color: red;font-weight: 600;">{both[key]}</a><br>"""
        )
    elif both[key] > 0:
        conclusion_str += f"""{key} : <a style="color: green;font-weight: 600;">+{both[key]}</a><br>"""
    else:
        conclusion_str += (
            f"""{key} : <a style="color: black;font-weight: 600;">{both[key]}</a><br>"""
        )

total_str = f"""<br>total spent : -{total_spent}<br>total gained : {total_gained}<br>"""
if sum(transactions) < 0:
    total_str += f"""total : <a style="color: red;font-weight: 700;">{sum(transactions)}</a><br>"""
elif sum(transactions) > 0:
    total_str += f"""total : <a style="color: green;font-weight: 700;">+{sum(transactions)}</a><br>"""
else:
    total_str += f"""total : <a style="color: black;font-weight: 700;">{sum(transactions)}</a><br>"""

final_str = base + conclusion_str + total_str + "</body>"

print(final_str)
