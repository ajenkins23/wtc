from user.authentication import authenticate_user
from transactions.journal import receive_income, pay_expense
# from banking import reconciliation
from banking.fvb import reconciliation as fvb_recon
# from banking.ubsa import reconciliation as ubsa_recon
# from banking.online import reconciliation as online_recon
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
            for _ in sys.argv:
                if _ != sys.argv[0]:
                    print(_)
    # help("modules")
    authenticate_user()
    # reconciliation.do_reconciliation()
    # ubsa_recon.do_reconciliation()
    # online_recon.do_reconciliation()
    receive_income(100)
    pay_expense(100)
    fvb_recon.do_reconciliation()
