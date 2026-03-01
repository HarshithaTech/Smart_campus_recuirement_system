from fastapi import Request, HTTPException
import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, requests_per_minute: int = 60):
        self.requests_per_minute = requests_per_minute
        self.visits = defaultdict(list)

    async def __call__(self, request: Request):
        client_ip = request.client.host
        current_time = time.time()
        
        # Filter visits in the last 60 seconds
        self.visits[client_ip] = [v for v in self.visits[client_ip] if current_time - v < 60]
        
        if len(self.visits[client_ip]) >= self.requests_per_minute:
            raise HTTPException(status_code=429, detail="Too many requests")
            
        self.visits[client_ip].append(current_time)

rate_limiter = RateLimiter()
