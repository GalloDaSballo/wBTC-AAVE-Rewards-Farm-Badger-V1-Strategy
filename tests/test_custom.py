import brownie
from brownie import *
from helpers.constants import MaxUint256
import pytest

"""
  TODO: Put your tests here to prove the strat is good!
  See test_harvest_flow, for the basic tests
  See test_strategy_permissions, for tests at the permissions level
"""

@pytest.fixture
def aavePool():
  return Contract.from_explorer("0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9")

@pytest.fixture
def aaveRewards():
  return Contract.from_explorer("0xd784927Ff2f95ba542BfC824c8a8a98F3495f6b5")


def test_my_custom_test(want, deployer, vault, strategy, aavePool, aaveRewards):
  balance = want.balanceOf(deployer)
  want.approve(vault, balance, {"from": deployer})
  vault.deposit(balance, {"from": deployer})
  vault.earn({"from": deployer})

  chain.sleep(15)
  chain.mine(500)

  aToken = Contract.from_explorer(strategy.aToken())

  assert strategy.balanceOfPool() == aToken.balanceOf(strategy)

  ## If we deposited, then we must have some rewards

  assert aaveRewards.getRewardsBalance([aToken], strategy) > 0