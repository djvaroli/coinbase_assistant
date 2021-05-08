from app.utils import account_utils


class Portfolio:
    def __init__(
        self
    ):
        self.__accounts = account_utils.fetch_accounts(return_active=True)
        self.__net_input = None
        self.__value = None

    @property
    def accounts(self):
        return self.__accounts
    
    @accounts.setter
    def accounts(self, *args):
        raise Exception("Use the add_account method to add a portfolio account.")
    
    def add_account(self, account):
        assert isinstance(account, account_utils.ExtendedCoinbaseAccount), "Account must be a Coinbase Account instance"
        self.accounts.append(account)

    def breakdown(self, format_for_sms: bool = False) -> dict:
        portfolio_breakdown = {"net_input": 0.0, "net_value": 0.0, "accounts": {}}

        for account in self.accounts:
            name = account.name
            account_input = account.net_input()
            account_value = float(account.native_balance.amount)
            portfolio_breakdown["accounts"][name] = {"net_input": account_input, "net_value": account_value}
            portfolio_breakdown["net_input"] += account_input
            portfolio_breakdown["net_value"] += account_value
        
        portfolio_breakdown["diff"] = round(portfolio_breakdown["net_value"] - portfolio_breakdown["net_input"],4)

        if format_for_sms:
            portfolio_breakdown = self.__format_portfolio_breakdown(portfolio_breakdown, "sms")
        return portfolio_breakdown

    @staticmethod
    def __format_portfolio_breakdown(breakdown: dict, format: str = "sms"):
        net_value = breakdown['net_value']
        net_input = breakdown['net_input']
        diff = breakdown['diff']
        account_blobs = breakdown['accounts']

        sms_text = f"Net portfolio value: {net_value: .3f}$\n"
        sms_text += f"Net portfolio input: {net_input: .3f}$\n"
        sms_text += f"Difference: {diff:.3f}$\n\n"
        sms_text += f"Account info breakdown\n\n"

        for account_name, account_details in account_blobs.items():
            account_input = account_details['net_input']
            account_value = account_details['net_value']
            sms_text += f"Name: {account_name}\n"
            sms_text += f"Value: {account_value}$\n"
            sms_text += f"Input: {account_input}$\n\n"
        
        return sms_text

