from psnawp_api import PSNAWP

psnawp = PSNAWP('xyz0GtvCr6Javg9MOdxDDa6rilcxvfAQYjMkBDdeboefJ00IP8AslSiKMi2w5Xnk')

# This is you
client = psnawp.me()
print(client.online_id)
print("\n")
print(client.get_profile_legacy()['profile']['trophySummary']['level'])
print("\n")
