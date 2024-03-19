
import datawarehouse.*;
import io.grpc.stub.StreamObserver;
import model.ProductData;
import model.WarehouseData;
import product.ProductSimulation;
import warehouse.WarehouseSimulation;

import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;

public class DataWarehouseServiceImpl extends DataWarehouseServiceGrpc.DataWarehouseServiceImplBase {

    static ConcurrentMap<String, Long> activeClients = new ConcurrentHashMap<>();

    @Override
    public void warehousing(DataWarehouse.WarehouseRequest request, StreamObserver<DataWarehouse.WarehouseResponse> responseObserver) {
        int id = request.getId();
        int auth = request.getAuth();
        String clientId = String.valueOf(request.getId());
        activeClients.put(clientId, System.currentTimeMillis());
        System.out.println("Connected ID: " + id);
        if(auth == -1267811949) {
            WarehouseSimulation wsim = new WarehouseSimulation();
            WarehouseData wdata = wsim.generateData(id);
            ProductSimulation psim = new ProductSimulation();
            ProductData randomData = psim.generateData(id);
            DataWarehouse.ProductData product1 = DataWarehouse.ProductData.newBuilder()
                    .setProductID(1)
                    .setProductName(randomData.getProductName())
                    .setProductCategory(randomData.getProductCategory())
                    .setProductPrice(randomData.getProductPrice())
                    .setProductStock(randomData.getProductStock())
                    .setProductExpiryDate(String.valueOf(randomData.getProductExpiryDate()))
                    .setProductAvailability(randomData.isProductAvailability())
                    .build();


            DataWarehouse.WarehouseResponse response = DataWarehouse.WarehouseResponse.newBuilder()
                    .setWarehouseID(id)
                    .setWarehouseName(wdata.getWarehouseName())
                    .setWarehouseLocation(wdata.getWarehouseLocation())
                    .setWarehouseStorage(wdata.getWarehouseStorage())
                    .setWarehouseParkingSlots(wdata.getWarehouseParkingSlots())
                    .setWarehouseAvailability(wdata.isWarehouseAvaibility())
                    .addProductData(product1)
                    .build();

            responseObserver.onNext(DataWarehouse.WarehouseResponse.newBuilder().build());
            responseObserver.onCompleted();
        } else {
            responseObserver.onError(new io.grpc.StatusRuntimeException(io.grpc.Status.UNAUTHENTICATED));
        }
    }

    @Override
    public void ping(DataWarehouse.PingRequest request, StreamObserver<DataWarehouse.PingResponse> responseObserver) {
        String clientId = request.getClientID();
        if (activeClients.containsKey(clientId)) {
            activeClients.put(clientId, System.currentTimeMillis());
            responseObserver.onNext(DataWarehouse.PingResponse.newBuilder().setMessage("Healthy").build());
        } else {
            responseObserver.onNext(DataWarehouse.PingResponse.newBuilder().setMessage("Unknown client").build());
        }
        responseObserver.onCompleted();
    }
}
