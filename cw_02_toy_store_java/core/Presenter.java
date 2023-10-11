package cw_02_toy_store_java.core;

import cw_02_toy_store_java.exceptions.NullInput;
import cw_02_toy_store_java.exceptions.WrongSimbolInput;

/**
 * Подготовка и ввод данных в программу
 */
public class Presenter {
    private ParametersSetting ps = new ParametersSetting();

    public Presenter() {
        super();
    }

    public Toy createToy(int index) {
        boolean flag = true;
        int id = index + 1;
        String name = "";
        Integer frequency = 0;

        while (flag) {
            try {
                System.out.println("В наименование игрушки, допускается только ввод русского алфавита");
                name = ps.createName("Введите наименование игрушки: ");
                flag = false;
            } catch (NullInput e) {
                System.out.println(e.getMessage());
            } catch (WrongSimbolInput e) {
                System.out.println(e.getMessage());
            }
        }

        while (!flag) {
            try {
                System.out.println("Частота выпадения игрушки указывается целым числом от 1 до 9");
                frequency = Integer.parseInt(ps.createFrequency("Укажите частоту выпадения игрушки: "));
                flag = true;
            } catch (NullInput e) {
                System.out.println(e.getMessage());
            } catch (WrongSimbolInput e) {
                System.out.println(e.getMessage());
            }
        }

        Toy toy = new Toy(id, name, frequency);
        toy.printToy();
        return toy;

    }
}
