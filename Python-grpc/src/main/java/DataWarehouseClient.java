import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

public class DataWarehouseClient {

    public static void main(String[] args) {

        ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost", 50051)
                .usePlaintext()
                .build();

        DataWarehouseServiceGrpc.DataWarehouseServiceBlockingStub stub = DataWarehouseServiceGrpc.newBlockingStub(channel);

        DataWarehouse.WarehouseRequest dataRequest = DataWarehouse.WarehouseRequest.newBuilder()
                .setId(1).setAuth("IloveSYT".hashCode())
                .build();

        System.out.println("Request erfolgreich geschickt mit id: "+ dataRequest.getId());


        try {
            DataWarehouse.WarehouseResponse response = stub.warehousing(dataRequest);

            System.out.println("Response erhalten");
            System.out.println("Warehouse ID: " + response.getWarehouseID());
            System.out.println("Warehouse Name: " + response.getWarehouseName());
            System.out.println("Warehouse Storage: " + response.getWarehouseStorage());
            System.out.println("Warehouse Location: " + response.getWarehouseLocation());
            System.out.println("Warehouse Avaibility: " + response.getWarehouseAvailability());
            System.out.println("Warehouse Parkinslots: " + response.getWarehouseParkingSlots());
            response.getProductDataList().forEach(product -> {
                System.out.println("Product ID: " + product.getProductID() +
                        ", Name: " + product.getProductName() +
                        ", Category: " + product.getProductCategory() +
                        ", Price: " + product.getProductPrice() +
                        ", Stock: " + product.getProductStock() +
                        ", Expiry Date: " + product.getProductExpiryDate() +
                        ", Availability: " + product.getProductAvailability());
            });
        } catch (Exception e) {
            System.err.println("Fehler bei der Anfrage: " + e.getMessage());
        } finally {
            channel.shutdown();
        }
    }
}
