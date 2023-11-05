package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements VendingMachine {

    private static VendingMachineImpl instance;

    private Map<String, Drink> drinks;
    private int quarters;

    private VendingMachineImpl() {
        drinks = new HashMap<>();
        drinks.put("Coca-Cola", new FizzyDrinkImpl("Coca-Cola"));
        drinks.put("Pepsi", new FizzyDrinkImpl("Pepsi"));
        drinks.put("Agua", new NonFizzyDrinkImpl("Agua"));
    }

    public static VendingMachineImpl getInstance() {
        if (instance == null) {
            synchronized (VendingMachineImpl.class) {
                if (instance == null) {
                    instance = new VendingMachineImpl();
                }
            }
        }
        return instance;
    }

    @Override
    public void insertQuarter() {
        quarters++;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        if (quarters < 50) {
            throw new NotEnoughMoneyException();
        }

        Drink drink = drinks.get(name);
        if (drink == null) {
            throw new UnknownDrinkException();
        }

        quarters -= 50;
        return drink;
    }
}
