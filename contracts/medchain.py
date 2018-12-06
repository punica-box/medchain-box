from boa.interop.System.Runtime import Notify
from boa.interop.System.Storage import GetContext, Get, Put, Delete
from boa.interop.System.Runtime import Deserialize,Serialize

def Main(operation, args):
    if operation == 'Save_Manufacture_Data':
        manufacture_date = args[0]
        manufacture_time = args[1]
        manufacture_origin = args[2]
        manufacture_company = args[3]
        manufacture_people = args[4]
        manufacture_medicine_name = args[5]
        manufacture_expiry_date = args[6]
        manufacture_ingredient1 = args[7]
        manufacture_amount1 = args[8]
        manufacture_ingredient2 = args[9]
        manufacture_amount2 = args[10]
        manufacture_ingredient3 = args[11]
        manufacture_amount3 = args[12]
        manufacture_ingredient4 = args[13]
        manufacture_amount4 = args[14]
        manufacture_ingredient5 = args[15]
        manufacture_amount5 = args[16]
        manufacture_ingredient6 = args[17]
        manufacture_amount6 = args[18]
        manufacture_ingredient7 = args[19]
        manufacture_amount7 = args[20]
        manufacture_ingredient8 = args[21]
        manufacture_amount8 = args[22]
        return Save_Manufacture_Data(manufacture_date,
                                    manufacture_time,
                                    manufacture_origin,
                                    manufacture_company,
                                    manufacture_people,
                                    manufacture_medicine_name,
                                    manufacture_expiry_date,
                                    manufacture_ingredient1,
                                    manufacture_amount1,
                                    manufacture_ingredient2,
                                    manufacture_amount2,
                                    manufacture_ingredient3,
                                    manufacture_amount3,
                                    manufacture_ingredient4,
                                    manufacture_amount4,
                                    manufacture_ingredient5,
                                    manufacture_amount5,
                                    manufacture_ingredient6,
                                    manufacture_amount6,
                                    manufacture_ingredient7,
                                    manufacture_amount7,
                                    manufacture_ingredient8,
                                    manufacture_amount8)

    if operation == 'Get_Manufacture_Data':
        return Get_Manufacture_Data()

    if operation == 'Save_Storage_Data':
        storage_location = args[0]
        storage_condition = args[1]
        storage_temperature = args[2]
        storage_humidity = args[3]
        storage_warehouse = args[4]
        storage_start_date = args[5]
        storage_end_date = args[6]
        return Save_Storage_Data(storage_location,
                                storage_condition,
                                storage_temperature,
                                storage_humidity,
                                storage_warehouse,
                                storage_start_date,
                                storage_end_date)

    if operation == 'Get_Storage_Data':
        return Get_Storage_Data()

    if operation == 'Save_Logistics_Data':
        logistics_ship_company = args[0]
        logistics_ship_model = args[1]
        logistics_ship_date = args[2]
        logistics_arrive_date = args[3]
        logistics_origin = args[4]
        logistics_destination = args[5]
        return Save_Logistics_Data(logistics_ship_company,
                                    logistics_ship_model,
                                    logistics_ship_date,
                                    logistics_arrive_date,
                                    logistics_origin,
                                    logistics_destination)

    if operation == 'Get_Logistics_Data':
        return Get_Logistics_Data()

    if operation == 'Save_Distribution_Data':
        distribution_date = args[0]
        distribution_time = args[1]
        distribution_company = args[2]
        distribution_people = args[3]
        distribution_buyer = args[4]
        distribution_amount = args[5]
        return Save_Distribution_Data(distribution_date,
                                        distribution_time,
                                        distribution_company,
                                        distribution_people,
                                        distribution_buyer,
                                        distribution_amount)

    if operation == 'Get_Distribution_Data':
        return Get_Distribution_Data()

    return False

def Save_Manufacture_Data(manufacture_date,manufacture_time,manufacture_origin,manufacture_company,manufacture_people,manufacture_medicine_name,manufacture_expiry_date,manufacture_ingredient1,manufacture_amount1,manufacture_ingredient2,manufacture_amount2,manufacture_ingredient3,manufacture_amount3,manufacture_ingredient4,manufacture_amount4,manufacture_ingredient5,manufacture_amount5,manufacture_ingredient6,manufacture_amount6,manufacture_ingredient7,manufacture_amount7,manufacture_ingredient8,manufacture_amount8):
    context = GetContext()
    manufacture_data = {
        'manufacture_date':manufacture_date,
        'manufacture_time':manufacture_time,
        'manufacture_origin':manufacture_origin,
        'manufacture_company':manufacture_company,
        'manufacture_people':manufacture_people,
        'manufacture_medicine_name':manufacture_medicine_name,
        'manufacture_expiry_date':manufacture_expiry_date,
        'manufacture_ingredient1':manufacture_ingredient1,
        'manufacture_amount1':manufacture_amount1,
        'manufacture_ingredient2':manufacture_ingredient2,
        'manufacture_amount2':manufacture_amount2,
        'manufacture_ingredient3':manufacture_ingredient3,
        'manufacture_amount3':manufacture_amount3,
        'manufacture_ingredient4':manufacture_ingredient4,
        'manufacture_amount4':manufacture_amount4,
        'manufacture_ingredient5':manufacture_ingredient5,
        'manufacture_amount5':manufacture_amount5,
        'manufacture_ingredient6':manufacture_ingredient6,
        'manufacture_amount6':manufacture_amount6,
        'manufacture_ingredient7':manufacture_ingredient7,
        'manufacture_amount7':manufacture_amount7,
        'manufacture_ingredient8':manufacture_ingredient8,
        'manufacture_amount8':manufacture_amount8
    }
    manufacture_data2 = Serialize(manufacture_data)
    Put(context, "manufacture_data", manufacture_data2)
    return True

def Get_Manufacture_Data():
    context = GetContext()
    data = Get(context,"manufacture_data")
    if not data:
        return False
    p = Deserialize(data)
    Notify(p["manufacture_date"],p["manufacture_time"],p["manufacture_origin"],p["manufacture_company"],p["manufacture_people"],p["manufacture_medicine_name"],p["manufacture_expiry_date"],p["manufacture_ingredient1"],p["manufacture_amount1"],p["manufacture_ingredient2"],p["manufacture_amount2"],p["manufacture_ingredient3"],p["manufacture_amount3"],p["manufacture_ingredient4"],p["manufacture_amount4"],p["manufacture_ingredient5"],p["manufacture_amount5"],p["manufacture_ingredient6"],p["manufacture_amount6"],p["manufacture_ingredient7"],p["manufacture_amount7"],p["manufacture_ingredient8"],p["manufacture_amount8"])
    return True

def Save_Storage_Data(storage_location,storage_condition,storage_temperature,storage_humidity,storage_warehouse,storage_start_date,storage_end_date):
    context = GetContext()
    storage_data = {
        'storage_location':storage_location,
        'storage_condition':storage_condition,
        'storage_temperature':storage_temperature,
        'storage_humidity':storage_humidity,
        'storage_warehouse':storage_warehouse,
        'storage_start_date':storage_start_date,
        'storage_end_date':storage_end_date
    }
    storage_data2 = Serialize(storage_data)
    Put(context, "storage_data", storage_data2)
    return True

def Get_Storage_Data():
    context = GetContext()
    data = Get(context,"storage_data")
    if not data:
        return False
    p = Deserialize(data)
    Notify(p["storage_location"],p["storage_condition"],p["storage_temperature"],p["storage_humidity"],p["storage_warehouse"],p["storage_start_date"],p["storage_end_date"])
    return True

def Save_Logistics_Data(logistics_ship_company,logistics_ship_model,logistics_ship_date,logistics_arrive_date,logistics_origin,logistics_destination):
    context = GetContext()
    logistics_data = {
        'logistics_ship_company':logistics_ship_company,
        'logistics_ship_model':logistics_ship_model,
        'logistics_ship_date':logistics_ship_date,
        'logistics_arrive_date':logistics_arrive_date,
        'logistics_origin':logistics_origin,
        'logistics_destination':logistics_destination
    }
    logistics_data2 = Serialize(logistics_data)
    Put(context, "logistics_data", logistics_data2)
    return True

def Get_Logistics_Data():
    context = GetContext()
    data = Get(context,"logistics_data")
    if not data:
        return False
    p = Deserialize(data)
    Notify(p["logistics_ship_company"],p["logistics_ship_model"],p["logistics_ship_date"],p["logistics_arrive_date"],p["logistics_origin"],p["logistics_destination"])
    return True

def Save_Distribution_Data(distribution_date,distribution_time,distribution_company,distribution_people,distribution_buyer,distribution_amount):
    context = GetContext()
    distribution_data = {
        'distribution_date':distribution_date,
        'distribution_time':distribution_time,
        'distribution_company':distribution_company,
        'distribution_people':distribution_people,
        'distribution_buyer':distribution_buyer,
        'distribution_amount':distribution_amount
    }
    distribution_data2 = Serialize(distribution_data)
    Put(context, "distribution_data", distribution_data2)
    return True

def Get_Distribution_Data():
    context = GetContext()
    data = Get(context,"distribution_data")
    if not data:
        return False
    p = Deserialize(data)
    Notify(p["distribution_date"],p["distribution_time"],p["distribution_company"],p["distribution_people"],p["distribution_buyer"],p["distribution_amount"])
    return True