from fastapi import FastAPI, HTTPException
from web3 import Web3

app = FastAPI()

INFURA_URL = "https://mainnet.infura.io/v3/70763a11c51244d88635ae348c24e973"
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

@app.get("/balance/{address}")
async def get_balance(address: str):
    if not w3.is_address(address):
        raise HTTPException(status_code=400, detail="Invalid Ethereum address")
    
    balance = w3.eth.get_balance(address)
    balance_in_eth = w3.from_wei(balance, 'ether')
    
    return { "the address you're looking for": address, "balance": str(balance_in_eth)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
