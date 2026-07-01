class Solution(object):
    def accountsMerge(self, accounts):
        graph = {}
        email_to_name = {}
        
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if first_email not in graph:
                    graph[first_email] = set()
                if email not in graph:
                    graph[email] = set()
                
                graph[first_email].add(email)
                graph[email].add(first_email)
                email_to_name[email] = name
                
        visited = set()
        merged_accounts = []
        
        for email in email_to_name:
            if email not in visited:
                visited.add(email)
                queue = [email]
                component = []
                
                while queue:
                    curr = queue.pop(0)
                    component.append(curr)
                    
                    if curr in graph:
                        for neighbor in graph[curr]:
                            if neighbor not in visited:
                                visited.add(neighbor)
                                queue.append(neighbor)
                            
                merged_accounts.append([email_to_name[email]] + sorted(component))
                
        return merged_accounts
