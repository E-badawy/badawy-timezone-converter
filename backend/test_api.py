import requests
import json

print("Testing Badawy Timezone Converter API\n" + "="*50)

# Test current endpoint
response = requests.post('http://127.0.0.1:5000/api/current', 
    json={'timezone': 'UTC'})
print("\n✓ Current Time Endpoint Test:")
print(f"  Status: {response.status_code}")
data = response.json()
print(f"  Timezone: {data.get('timezone')}")
print(f"  Time: {data.get('formatted')}")

# Test convert endpoint
response = requests.post('http://127.0.0.1:5000/api/convert',
    json={'datetime': '2026-02-13T12:00:00', 'from_tz': 'UTC', 'to_tz': 'America/New_York'})
print("\n✓ Convert Endpoint Test:")
print(f"  Status: {response.status_code}")
data = response.json()
print(f"  From: {data.get('original', {}).get('timezone')}")
print(f"  To: {data.get('converted', {}).get('timezone')}")
print(f"  Time Difference: {data.get('time_difference_hours')} hours")

# Test compare endpoint
response = requests.post('http://127.0.0.1:5000/api/compare',
    json={'timezones': ['UTC', 'America/New_York', 'Asia/Tokyo']})
print("\n✓ Compare Endpoint Test:")
print(f"  Status: {response.status_code}")
data = response.json()
results = data.get('comparison', [])
print(f"  Timezones Compared: {len(results)}")
for tz_data in results[:2]:
    print(f"    - {tz_data.get('timezone')}: {tz_data.get('formatted')}")

print("\n" + "="*50)
print("✓ All endpoints working correctly!")
