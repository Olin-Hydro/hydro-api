from flask_restx import Namespace, Resource
from flask import jsonify
import os
from web3 import Web3

from .resources.schemas import BlockSchema


api = Namespace("block", description="Blockchain data")

block_schema = BlockSchema()


@api.route("/")
class block_data(Resource):
    """
    Class for retrieving blockchain data
    """

    def get(self):
        """
        Get latest nutrient data from our nutrient smart contract
        """
        infura_url = os.environ.get("INFURA_URL")
        abi = os.environ.get("NUTRIENT_CONTRACT_ABI")
        address = os.environ.get("NUTRIENT_CONTRACT_ADDRESS")
        web3 = Web3(Web3.HTTPProvider(infura_url))
        nutrient_contract = web3.eth.contract(address=address, abi=abi)
        data = nutrient_contract.functions.getNutrients().call()
        return jsonify(block_schema.dump({"data":data}))

