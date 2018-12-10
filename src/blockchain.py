#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import binascii
from ontology.smart_contract.neo_contract.abi.abi_info import AbiInfo
from ontology.ont_sdk import OntologySdk
from ontology.wallet.wallet_manager import WalletManager
from ontology.account.account import Account

dict_abi = {"contractHash": "8bc0f46814f436cfb2ffe7bf95ad61e6db0db213", "abi": {"functions": [
    {"name": "Main", "parameters": [{"name": "operation", "type": ""}, {"name": "args", "type": ""}], "returntype": ""},
    {"name": "Save_Manufacture_Data",
     "parameters": [{"name": "manufacture_date", "type": ""}, {"name": "manufacture_time", "type": ""},
                    {"name": "manufacture_origin", "type": ""}, {"name": "manufacture_company", "type": ""},
                    {"name": "manufacture_people", "type": ""}, {"name": "manufacture_medicine_name", "type": ""},
                    {"name": "manufacture_expiry_date", "type": ""}, {"name": "manufacture_ingredient1", "type": ""},
                    {"name": "manufacture_amount1", "type": ""}, {"name": "manufacture_ingredient2", "type": ""},
                    {"name": "manufacture_amount2", "type": ""}, {"name": "manufacture_ingredient3", "type": ""},
                    {"name": "manufacture_amount3", "type": ""}, {"name": "manufacture_ingredient4", "type": ""},
                    {"name": "manufacture_amount4", "type": ""}, {"name": "manufacture_ingredient5", "type": ""},
                    {"name": "manufacture_amount5", "type": ""}, {"name": "manufacture_ingredient6", "type": ""},
                    {"name": "manufacture_amount6", "type": ""}, {"name": "manufacture_ingredient7", "type": ""},
                    {"name": "manufacture_amount7", "type": ""}, {"name": "manufacture_ingredient8", "type": ""},
                    {"name": "manufacture_amount8", "type": ""}], "returntype": ""},
    {"name": "Get_Manufacture_Data", "parameters": [{"name": "", "type": ""}], "returntype": ""},
    {"name": "Save_Storage_Data",
     "parameters": [{"name": "storage_location", "type": ""}, {"name": "storage_condition", "type": ""},
                    {"name": "storage_temperature", "type": ""}, {"name": "storage_humidity", "type": ""},
                    {"name": "storage_warehouse", "type": ""}, {"name": "storage_start_date", "type": ""},
                    {"name": "storage_end_date", "type": ""}], "returntype": ""},
    {"name": "Get_Storage_Data", "parameters": [{"name": "", "type": ""}], "returntype": ""},
    {"name": "Save_Logistics_Data",
     "parameters": [{"name": "logistics_ship_company", "type": ""}, {"name": "logistics_ship_model", "type": ""},
                    {"name": "logistics_ship_date", "type": ""}, {"name": "logistics_arrive_date", "type": ""},
                    {"name": "logistics_origin", "type": ""}, {"name": "logistics_destination", "type": ""}],
     "returntype": ""}, {"name": "Get_Logistics_Data", "parameters": [{"name": "", "type": ""}], "returntype": ""},
    {"name": "Save_Distribution_Data",
     "parameters": [{"name": "distribution_date", "type": ""}, {"name": "distribution_time", "type": ""},
                    {"name": "distribution_company", "type": ""}, {"name": "distribution_people", "type": ""},
                    {"name": "distribution_buyer", "type": ""}, {"name": "distribution_amount", "type": ""}],
     "returntype": ""}, {"name": "Get_Distribution_Data", "parameters": [{"name": "", "type": ""}], "returntype": ""}]}}
abi_info = AbiInfo(dict_abi['contractHash'], dict_abi.get('entrypoint', ''), dict_abi['abi']['functions'],
                   dict_abi.get('events', ''))

manufacture_date = '3 Aug 2017'
manufacture_time = '11:03 A.M.'
manufacture_origin = 'India'
manufacture_company = 'Getwell Oncology'
manufacture_people = 'Machon Christ'
manufacture_medicine_name = 'Gefitinib Tablets IP'
manufacture_expiry_date = '20 Nov 2025'
manufacture_ingredient1 = 'Gardasil'
manufacture_amount1 = '0.225mg'
manufacture_ingredient2 = 'Thiomersal'
manufacture_amount2 = '0.103mg'
manufacture_ingredient3 = 'Human Serum Albumin'
manufacture_amount3 = '0.097mg'
manufacture_ingredient4 = 'Recombinant human serum albumin'
manufacture_amount4 = '0.093mg'
manufacture_ingredient5 = 'Gelatine'
manufacture_amount5 = '0.076mg'
manufacture_ingredient6 = 'Monosodium glutamate'
manufacture_amount6 = '0.054mg'
manufacture_ingredient7 = 'Ovalbumin'
manufacture_amount7 = '0.023mg'
manufacture_ingredient8 = 'Sorbitol and other stabilisers'
manufacture_amount8 = '0.009mg'

storage_location = 'Caloni District, India'
storage_condition = 'Good'
storage_temperature = '23 degree celsius'
storage_humidity = '65%'
storage_warehouse = 'Onergy Max. Ltd.'
storage_start_date = '4 Aug 2017'
storage_end_date = '17 Oct 2017'

logistics_ship_company = 'Seagull Shipping Ltd.'
logistics_ship_model = 'KX438'
logistics_ship_date = '17 Oct 2017'
logistics_arrive_date = '28 Dec 2017'
logistics_origin = 'Varoni Harbor, India'
logistics_destination = 'Shen Zhen Harbor, China'

distribution_date = '18 Nov 2018'
distribution_time = '14:23 P.M.'
distribution_company = 'Tai Sin Medicine Ltd.'
distribution_people = 'Chan Tai Fung'
distribution_buyer = 'Mr. Piglet'
distribution_amount = 'RMB $5400.00'

save_manufacture_func = abi_info.get_function('Save_Manufacture_Data')
save_manufacture_func.set_params_value((manufacture_date, manufacture_time, manufacture_origin, manufacture_company,
                                        manufacture_people, manufacture_medicine_name, manufacture_expiry_date,
                                        manufacture_ingredient1, manufacture_amount1, manufacture_ingredient2,
                                        manufacture_amount2, manufacture_ingredient3, manufacture_amount3,
                                        manufacture_ingredient4, manufacture_amount4, manufacture_ingredient5,
                                        manufacture_amount5, manufacture_ingredient6, manufacture_amount6,
                                        manufacture_ingredient7, manufacture_amount7, manufacture_ingredient8,
                                        manufacture_amount8))

save_storage_func = abi_info.get_function('Save_Storage_Data')
save_storage_func.set_params_value((storage_location, storage_condition, storage_temperature, storage_humidity,
                                    storage_warehouse, storage_start_date, storage_end_date))

save_logistics_func = abi_info.get_function('Save_Logistics_Data')
save_logistics_func.set_params_value((logistics_ship_company, logistics_ship_model, logistics_ship_date,
                                      logistics_arrive_date, logistics_origin, logistics_destination))

save_distribution_func = abi_info.get_function('Save_Distribution_Data')
save_distribution_func.set_params_value(
    (distribution_date, distribution_time, distribution_company, distribution_people,
     distribution_buyer, distribution_amount))
acct = Account('f7bfe8f8ed0cf33a2321bbbdd0c621ef2826d22d16d087a950a2a8f57a128239')
rpc_address = 'http://polaris3.ont.io:20336'
sdk = OntologySdk()
sdk.rpc.set_address(rpc_address)
contract_address_hex = b'8bc0f46814f436cfb2ffe7bf95ad61e6db0db213'
contract_address_bytearray = bytearray(binascii.a2b_hex(contract_address_hex))
contract_address_bytearray.reverse()
gas_limit = 20000000
gas_price = 500
manufacture_tx_hash = sdk.neo_vm().send_transaction(contract_address_bytearray, acct, acct, gas_limit, gas_price,
                                                    save_manufacture_func, False)
print(manufacture_tx_hash)
sdk.rpc.get_smart_contract_event_by_tx_hash(manufacture_tx_hash)
storage_tx_hash = sdk.neo_vm().send_transaction(contract_address_bytearray, acct, acct, gas_limit, gas_price,
                                                save_storage_func, False)
print(storage_tx_hash)
sdk.rpc.get_smart_contract_event_by_tx_hash(storage_tx_hash)
logistics_tx_hash = sdk.neo_vm().send_transaction(contract_address_bytearray, acct, acct, gas_limit, gas_price,
                                                  save_logistics_func, False)
print(logistics_tx_hash)
sdk.rpc.get_smart_contract_event_by_tx_hash(logistics_tx_hash)
distribution_tx_hash = sdk.neo_vm().send_transaction(contract_address_bytearray, acct, acct, gas_limit, gas_price,
                                                     save_distribution_func, False)
print(distribution_tx_hash)
sdk.rpc.get_smart_contract_event_by_tx_hash(distribution_tx_hash)
