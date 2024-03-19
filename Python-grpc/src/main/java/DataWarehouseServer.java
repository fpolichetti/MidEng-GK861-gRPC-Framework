import io.grpc.Server;
import io.grpc.ServerBuilder;

import java.io.IOException;

public class DataWarehouseServer {

    private static final int PORT = 50051;
    private Server server;

    public void start() throws IOException {
        server = ServerBuilder.forPort(PORT)
                .addService(new DataWarehouseServiceImpl())
                .build()
                .start();
    }

    public void blockUntilShutdown() throws InterruptedException {
        if (server == null) {
            return;
        }
        server.awaitTermination();
    }

    public static void main (String[] args) throws InterruptedException, IOException {
        DataWarehouseServer server = new DataWarehouseServer();
        System.out.println( "DataWarehouse is available!");
        server.start();
        server.blockUntilShutdown();
    }

}
