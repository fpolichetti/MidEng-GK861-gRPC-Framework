
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.util.Map;

public class HealthCheckManager extends Thread {

    @Override
    public void run() {
        while (!Thread.interrupted()) {
            for (Map.Entry<String, Long> entry : DataWarehouseServiceImpl.activeClients.entrySet()) {
                long lastSeen = System.currentTimeMillis() - entry.getValue();
                String status = lastSeen < 2000 ? "healthy" : "no response";
                try (FileWriter fw = new FileWriter("/home/f/Java-grpc/logs.txt", true)) {
                    fw.write(entry.getKey() +", " +LocalTime.now() + ", "+status+"\n");
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }
}