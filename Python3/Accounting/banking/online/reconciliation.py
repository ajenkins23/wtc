import requests

print(f'[Module] online.Reconciliation loaded.')

def do_reconciliation():
    print(f'Doing Online Bank reconciliation.')
    response = requests.get('https://www.wethinkcode.co.za')
    print(response.status_code)