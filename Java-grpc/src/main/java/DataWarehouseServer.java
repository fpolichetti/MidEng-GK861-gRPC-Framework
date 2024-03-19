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
        System.out.println("Server started, listening on " + PORT);

        new HealthCheckManager().start();
    }

    public void blockUntilShutdown() throws InterruptedException {
        if (server != null) {
            server.awaitTermination();
        }
    }

    public static void main(String[] args) throws IOException, InterruptedException {
        final DataWarehouseServer server = new DataWarehouseServer();
        server.start();
        server.blockUntilShutdown();
    }
}
