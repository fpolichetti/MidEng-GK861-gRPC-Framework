import grpc
from DataWarehouse_pb2_grpc import DataWarehouseServiceStub
from DataWarehouse_pb2 import WarehouseRequest

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = DataWarehouseServiceStub(channel)

        data_request = WarehouseRequest(
            id=1,
            auth=-1267811949
        )


        print(f"Request erfolgreich geschickt mit id: {data_request.id}")

        try:
            response = stub.warehousing(data_request)

            print("Response erhalten")
            print(f"Warehouse ID: {response.warehouseID}")
            print(f"Warehouse Name: {response.warehouseName}")
            print(f"Warehouse Storage: {response.warehouseStorage}")
            print(f"Warehouse Location: {response.warehouseLocation}")
            print(f"Warehouse Avaibility: {response.warehouseAvailability}")
            print(f"Warehouse Parkinslots: {response.warehouseParkingSlots}")

            for product in response.productData:
                print(f"Product ID: {product.productID}, "
                    f"Name: {product.productName}, "
                    f"Category: {product.productCategory}, "
                    f"Price: {product.productPrice}, "
                    f"Stock: {product.productStock}, "
                    f"Expiry Date: {product.productExpiryDate}, "
                    f"Availability: {product.productAvailability}")

        except grpc.RpcError as e:
            print(f"Fehler bei der Anfrage: {e.details()}")

if __name__ == '__main__':
    run()