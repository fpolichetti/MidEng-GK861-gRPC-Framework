
import grpc
import time
import threading
from DataWarehouse_pb2_grpc import DataWarehouseServiceStub
from DataWarehouse_pb2 import WarehouseRequest, PingRequest

def ping_server(stub):
    while True:
        try:
            ping_response = stub.ping(PingRequest(clientID="2"))
            print(f"Ping Response: {ping_response.message}")
        except grpc.RpcError as e:
            print(f"Fehler beim Pingen: {e.details()}")
        time.sleep(1)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = DataWarehouseServiceStub(channel)

        data_request = WarehouseRequest(id=2, auth=-1267811949)

        try:
            response = stub.warehousing(data_request)

            print("Request erfolgreich geschickt mit id:", data_request.id)
            print("Response erhalten")
            print("Warehouse ID:", response.warehouseID)
            print("Warehouse Name:", response.warehouseName)
            print("Warehouse Storage:", response.warehouseStorage)
            print("Warehouse Location:", response.warehouseLocation)
            print("Warehouse Availability:", response.warehouseAvailability)
            print("Warehouse Parking Slots:", response.warehouseParkingSlots)

            for product in response.productData:
                print("Product ID:", product.productID,
                      "Name:", product.productName,
                      "Category:", product.productCategory,
                      "Price:", product.productPrice,
                      "Stock:", product.productStock,
                      "Expiry Date:", product.productExpiryDate,
                      "Availability:", product.productAvailability)

        except grpc.RpcError as e:
            print("Fehler bei der Anfrage:", e.details())

        ping_thread = threading.Thread(target=ping_server, args=(stub,))
        ping_thread.daemon = True 
        ping_thread.start()

        try:
            while True:
                time.sleep(60) 
        except KeyboardInterrupt:
            print("Programm durch Benutzer beendet")

if __name__ == '__main__':
    run()
