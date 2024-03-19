package warehouse;

import model.ProductData;
import model.WarehouseData;
import product.ProductSimulation;

public class WarehouseService {
    public WarehouseData getWarehouseData( int inID ) {

    	WarehouseSimulation simulation = new WarehouseSimulation();
        return simulation.generateData( inID );

    }

    public ProductData getProductData(int inID) {

        ProductSimulation simulation = new ProductSimulation();
        return simulation.generateData(inID);

    }
}