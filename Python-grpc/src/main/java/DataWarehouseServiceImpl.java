import io.grpc.stub.StreamObserver;
import model.ProductData;
import model.WarehouseData;
import product.ProductSimulation;
import warehouse.WarehouseSimulation;

public class DataWarehouseServiceImpl extends DataWarehouseServiceGrpc.DataWarehouseServiceImplBase {
    @Override
    public void warehousing(DataWarehouse.WarehouseRequest request, StreamObserver<DataWarehouse.WarehouseResponse> responseObserver) {
        int id = request.getId();
        int auth = request.getAuth();

        if(auth == "IloveSYT".hashCode()) {
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
                    .setProductExpiryDate(randomData.getProductExpiryDate())
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

            responseObserver.onNext(response);
            responseObserver.onCompleted();
        } else {
            responseObserver.onError(new io.grpc.StatusRuntimeException(io.grpc.Status.UNAUTHENTICATED));
        }
    }
}
