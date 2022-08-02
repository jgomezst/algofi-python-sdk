from .staking_config import STAKING_CONFIGS, rewards_manager_app_id
from .staking import Staking
from .staking_user import StakingUser

class StakingClient: 

    def __init__(self, algofi_client):
        self.algofi_client = algofi_client
        self.algod = self.algofi_client.algod
        self.network = self.algofi_client.network
        self.staking_configs = STAKING_CONFIGS[self.network]
        self.staking_contracts = {}

    def load_state(self):
        for staking_config in self.staking_configs:
            self.staking_contracts[staking_config.app_id] = Staking(self.algod, self, rewards_manager_app_id[self.network], staking_config)
            self.staking_contracts[staking_config.app_id].load_state()

    def get_user(address):
        return StakingUser(self, address)