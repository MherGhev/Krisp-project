from flask import Flask, request, jsonify
import requests
import redis
from cachetools import TTLCache
from concurrent.futures import ThreadPoolExecutor
import json

app = Flask(__name__)

GENERATOR_SERVICE_URL = "http://generator-service:8080/generate"

local_cache = TTLCache(maxsize=3, ttl=10)
redis_client = redis.Redis(host='redis', port=6379, db=0)


def runcascade(viewerid):
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(requests.post, GENERATOR_SERVICE_URL, json={"modelname": f"Model-{i+1}", "viewerid": viewerid})
            for i in range(5)
        ]
        results = [f.result().json() for f in futures]
    
    merged_result = { "viewerid": viewerid, "recommendations": results }
    return merged_result

@app.route('/recommend', methods=['POST'])
def recommend():
    viewerid = request.json.get("viewerid")
    cache_result = get_from_cache(viewerid)

    if cache_result:
        return cache_result
    
    recommendations = runcascade(viewerid)

    set_cache(viewerid, recommendations)

    return jsonify(recommendations), 200


def get_from_cache(viewerid):
    local_cache_result = local_cache.get(viewerid)
    redis_cache_result = redis_client.get(viewerid)

    if local_cache_result:
        return local_cache_result
    
    if redis_cache_result:
        return json.loads(redis_cache_result)
    

def set_cache(viewerid, recommendations):
    local_cache[viewerid] = recommendations
    redis_client.setex(viewerid, 30, json.dumps(recommendations))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)