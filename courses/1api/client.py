import requests

# requests.get("http://127.0.0.1:8080")

requests.post("http://127.0.0.1:7777/games", json={
    "name": "spiderman",
    "studio": "sony",
    "total_hours": 20,
    "hours_played": 10,
})

# requests.delete("http://127.0.0.1:7777/games/spiderman")

# requests.put("http://127.0.0.1:7777/games/spiderman", json={"hours_played": 5})
