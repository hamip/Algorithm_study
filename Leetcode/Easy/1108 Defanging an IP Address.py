# https://leetcode.com/problems/defanging-an-ip-address/

# 1108. Defanging an IP Address

class Solution:
    def defangIPaddr(self, address: str) -> str:        
        return "[.]".join(address.split("."))
