import requests


day = input("What day are you requesting input for?")
r = requests.get(f"https://adventofcode.com/2024/day/{day}/input", cookies={'session': '53616c7465645f5f4e835b286f5ffee1684a6fd7ba6f55e8f0fd617d79923eba5532634c4c01c1e55337b4dadd739d63eae957446e8cad7e80c54b265f39ff74'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'})

with open(f"day{day}input.txt", 'w') as f:
    f.write(r.text)