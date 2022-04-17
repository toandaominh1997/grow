from uuid import uuid4
from blockchain import BlockChain

from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


node_identifier = str(uuid4()).replace('-', '')
blockchain = BlockChain()

@app.get("/")
async def hello():
    return "Hello"

@app.get("/mine")
def mine():

    # first we need to run the proof of work algorithm to calculate the new proof..
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # we must recieve reward for finding the proof in form of receiving 1 Coin
    blockchain.new_transaction(
        sender=0,
        recipient=node_identifier,
        amount=1,
    )

    # forge the new block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "Forged new block.",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return response


@app.get('/transaction/new')
def new_transaction():

    values = request.get_json()
    required = ['sender', 'recipient', 'amont']

    if not all(k in values for k in required):
        return 'Missing values.', 400

    # create a new transaction
    index = blockchain.new_transaction(
        sender = values['sender'],
        recipient = values['recipient'],
        amount = values['amount']
    )

    response = {
        'message': f'Transaction will be added to the Block {index}',
    }
    return response

@app.get("/chain")
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return response

@app.get('/nodes/register')
def register_nodes():
    values = request.get_json()

    print('values',values)
    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    # register each newly added node
    for node in nodes: blockchain.register_node(node)

    response = {
        'message': "New nodes have been added",
        'all_nodes': list(blockchain.nodes),
    }

    return response

