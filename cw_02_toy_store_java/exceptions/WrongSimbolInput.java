package cw_02_toy_store_java.exceptions;

public class WrongSimbolInput extends RuntimeException{
    public WrongSimbolInput() {
        super("Введены некорректные символы.");
    }
}
