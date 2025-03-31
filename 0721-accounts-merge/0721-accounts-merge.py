class UF:
    def __init__(self, n):
        self.repr = [i for i in range(n)]
        self.sizes = [1 for _ in range(n)]
    
    def union(self, x, y):
        repr_x = self.find(x)
        repr_y = self.find(y)

        if repr_x == repr_y:
            return

        if self.sizes[repr_x] >= self.sizes[repr_y]:
            self.sizes[repr_x] += self.sizes[repr_y]
            self.repr[repr_y] = repr_x
        else:
            self.sizes[repr_y] += self.sizes[repr_x]
            self.repr[repr_x] = repr_y

    
    def find(self, x):
        if self.repr[x] == x:
            return x
        
        self.repr[x] = self.find(self.repr[x])
        return self.repr[x]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        email_to_group_map = {}
        merged_accounts = []

        for idx, account in enumerate(accounts):
            name = account[0]
            emails = account[1:]
            for email in emails:
                if email not in email_to_group_map:
                    email_to_group_map[email] = idx
                else:
                    uf.union(idx, email_to_group_map[email])
        
        components = {}
        for email, group in email_to_group_map.items():
            parent_group = uf.find(group)
            if parent_group not in components:
                components[parent_group] = []
            components[parent_group].append(email)

        for group, emails in components.items():
            account_name = accounts[group][0]
            account_emails = sorted(emails)

            merged_account = [account_name] + account_emails
            merged_accounts.append(merged_account)
        
        return merged_accounts

        
