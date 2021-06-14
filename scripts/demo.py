from brownie import *
from config import (
  BADGER_DEV_MULTISIG,
  WANT,
  LP_COMPONENT,
  REWARD_TOKEN,
  PROTECTED_TOKENS,
  FEES
)
from dotmap import DotMap
from scripts.deploy import deploy

def main():
  return demo()

def demo():
  """
    Deploys, vault, controller and strats and wires them up for you to test
    Also makes a deposit
    Used in the brownie console to save time
  """
  deployed = deploy()

  toDep = deployed.want.balanceOf(deployed.deployer)

  deployed.want.approve(deployed.sett, toDep, {"from": deployed.deployer})
  deployed.sett.deposit(toDep, {"from": deployed.deployer})
  deployed.sett.earn({"from": deployed.deployer})

  chain.sleep(50) ## So we accrue interest

  return deployed